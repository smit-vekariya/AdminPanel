# Generated by Django 4.2.5 on 2023-10-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0012_cyberuser_source_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
