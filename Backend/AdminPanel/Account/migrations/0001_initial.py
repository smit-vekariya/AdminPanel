# Generated by Django 4.2.5 on 2023-10-02 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(blank=True, db_index=True, max_length=128, null=True, verbose_name='type')),
                ('level', models.PositiveIntegerField(blank=True, choices=[(20, 'info'), (30, 'warning'), (10, 'debug'), (40, 'error'), (50, 'fatal')], db_index=True, default=40)),
                ('message', models.TextField()),
                ('traceback', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
