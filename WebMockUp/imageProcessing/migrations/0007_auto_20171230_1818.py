# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-30 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageProcessing', '0006_auto_20171230_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='document',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]