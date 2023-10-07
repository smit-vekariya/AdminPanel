from django.contrib import admin
from .models import MovieInfo, SourceType, CyberUser

@admin.register(MovieInfo)
class MovieInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "release_date", "source_type", "upload_source_code", "file_id", "upload_by")

@admin.register(SourceType)
class SourceTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(CyberUser)
class CyberUserAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "account_id", "is_active", "source_type", "cyber_access_token")
