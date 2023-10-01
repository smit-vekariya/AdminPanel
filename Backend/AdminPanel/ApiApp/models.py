from django.db import models
from django.utils import timezone


# Create your models here.


class MovieInfo(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    release_date = models.DateField(default = timezone.now, null=True, blank=True)
    trailer_url = models.CharField(max_length=900, null=True, blank=True)
    download_url = models.CharField(max_length=900, null=True, blank=True)
    thumbnail_url = models.CharField(max_length=900, null=True, blank=True)
    source_url = models.CharField(max_length=900, null=True, blank=True)
    screenshots = models.JSONField(null=True, blank=True)
    source_type = models.CharField(max_length=200, null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=200, null=True, blank=True)
    genres = models.CharField(max_length=200, null=True, blank=True)
    cast = models.CharField(max_length=200, null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, null=True, blank=True)