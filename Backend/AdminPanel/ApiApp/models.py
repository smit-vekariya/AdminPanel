from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db import models

class SourceType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name



class CyberUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cyber_access_token = models.TextField(null=True, blank=True)
    account_id = models.IntegerField(null=True,blank=True)
    source_type = models.ForeignKey(SourceType, on_delete=models.CASCADE,null=True,blank=True)
    is_active = models.BooleanField()
    is_web_account = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class MovieInfo(models.Model):
    name = models.CharField(max_length=100)
    static_id = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=250,null=True,blank=True)
    release_date = models.DateField(default=timezone.now,null=True, blank=True)
    trailer_url = models.CharField(max_length=900, null=True, blank=True)
    download_url = models.CharField(max_length=900)
    thumbnail_url = models.CharField(max_length=900, null=True, blank=True)
    source_url = models.CharField(max_length=900, null=True, blank=True)
    screenshots = models.JSONField(null=True, blank=True)
    source_type = models.ForeignKey(SourceType, null=True, blank=True, on_delete=models.CASCADE)
    duration = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=10000, null=True, blank=True)
    language = models.CharField(max_length=200, null=True, blank=True, default="Hindi")
    genres = models.CharField(max_length=200, null=True, blank=True)
    cast = models.CharField(max_length=200, null=True, blank=True)
    industry = models.CharField(max_length=200, null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    upload_source_code = models.CharField(max_length=200, null=True, blank=True)
    file_id = models.IntegerField(null=True,blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    account_id = models.IntegerField(null=True,blank=True)
    upload_by = models.ForeignKey(CyberUser,related_name='missions_assigned',on_delete=models.CASCADE, null=True,blank=True)
    imdb = models.CharField(max_length=200, null=True, blank=True)
    is_web = models.BooleanField(default=False)
    season = models.CharField(max_length=200, null=True, blank=True)
    episode = models.JSONField(null=True, blank=True)
    all_episode = models.JSONField(null=True, blank=True)


    def __str__(self):
        return self.name

class AppInfo(models.Model):
    device = models.CharField(max_length=200, null=True, blank=True)
    version = models.CharField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    total_download = models.CharField(max_length=200, null=True, blank=True)
    force_update = models.BooleanField(default=False)

    def __str__(self):
        return self.device

class Report(models.Model):
    device_id = models.CharField(max_length=200, null=True, blank=True)
    device_name = models.ForeignKey(AppInfo,on_delete=models.CASCADE, null=True, blank=True)
    first_login_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    last_login_date = models.DateTimeField(default=timezone.now, null=True, blank=True)



