# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-05 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageProcessing', '0008_uploadedimage_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimage',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='uploadedimage',
            name='thumbnail_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
