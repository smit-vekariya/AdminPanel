from django.contrib import admin
from .models import MovieInfo, SourceType

@admin.register(MovieInfo)
class MovieInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "release_date", "source_type", "upload_source_code")


@admin.register(SourceType)
class SourceTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
