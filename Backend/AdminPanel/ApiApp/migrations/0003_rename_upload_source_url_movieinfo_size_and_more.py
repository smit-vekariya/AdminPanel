# Generated by Django 4.2.5 on 2023-10-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0002_movieinfo_upload_source_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieinfo',
            old_name='upload_source_url',
            new_name='size',
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='upload_source_code',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='download_url',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='trailer_url',
            field=models.CharField(max_length=900),
        ),
    ]
