# Generated by Django 4.2.5 on 2024-05-30 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0025_report_device_name_alter_movieinfo_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='first_login_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 30, 8, 7, 43, 259194), null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='last_login_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 30, 8, 7, 43, 259223), null=True),
        ),
    ]
