# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 05:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20170407_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='conditioner',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=255, unique=False),
            preserve_default=False,
        ),
    ]