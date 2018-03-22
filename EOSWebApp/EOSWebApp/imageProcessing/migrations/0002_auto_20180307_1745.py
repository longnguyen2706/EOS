# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-07 17:45
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageProcessing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempimage',
            name='gray_levels',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), default=[1], size=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempimage',
            name='k_labels',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), default=[1], size=20),
            preserve_default=False,
        ),
    ]