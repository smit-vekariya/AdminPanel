# Generated by Django 4.2.5 on 2023-11-08 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0020_report_appinfo_force_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='user_id',
            new_name='download_user',
        ),
    ]
