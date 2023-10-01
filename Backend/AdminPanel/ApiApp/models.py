from django.db import models
from django.utils import timezone


# Create your models here.

class SourceType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class MovieInfo(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)
    release_date = models.DateField(default=timezone.now,null=True, blank=True)
    trailer_url = models.CharField(max_length=900)
    download_url = models.CharField(max_length=900)
    thumbnail_url = models.CharField(max_length=900, null=True, blank=True)
    source_url = models.CharField(max_length=900, null=True, blank=True)
    screenshots = models.JSONField(null=True, blank=True)
    source_type = models.CharField(max_length=200, null=True, blank=True)
    source_type = models.ForeignKey(SourceType, on_delete=models.CASCADE)
    duration = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=200, null=True, blank=True)
    genres = models.CharField(max_length=200, null=True, blank=True)
    cast = models.CharField(max_length=200, null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    upload_source_code= models.CharField(max_length=200)

    def __str__(self):
        return self.name


