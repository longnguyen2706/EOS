# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-05 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadImage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='dist_per_pixel',
            field=models.FloatField(null=True),
        ),
    ]
