from django.contrib import admin
from .models import MovieInfo, SourceType, CyberUser, AppInfo, Report

@admin.register(MovieInfo)
class MovieInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "release_date", "source_type", "upload_source_code", "file_id", "upload_by", "is_web" ,"season")

@admin.register(SourceType)
class SourceTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(CyberUser)
class CyberUserAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "account_id", "is_active", "is_web_account", "source_type", "cyber_access_token")


@admin.register(AppInfo)
class AppInfoAdmin(admin.ModelAdmin):
    list_display = ("device", "version", "url", "total_download", "force_update")


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("device_id","device_name","first_login_date", "last_login_date",)
