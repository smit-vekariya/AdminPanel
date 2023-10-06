# Generated by Django 4.2.5 on 2023-10-05 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0009_cyberuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='cyberuser',
            name='account_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='account_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='upload_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='missions_assigned', to='ApiApp.cyberuser'),
        ),
    ]
