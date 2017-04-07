# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_conditioner_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditioner',
            name='block_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditioner', to='catalogue.BlockType', verbose_name='\u0422\u0438\u043f \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0435\u0433\u043e \u0431\u043b\u043e\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='conditioner',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditioner', to='catalogue.Brand', verbose_name='\u0411\u0440\u0435\u043d\u0434'),
        ),
        migrations.AlterField(
            model_name='conditioner',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='conditioner',
            name='inverter',
            field=models.BooleanField(default=False, verbose_name='\u0418\u043d\u0432\u0435\u0440\u0442\u043e\u0440'),
        ),
        migrations.AlterField(
            model_name='conditioner',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u043e\u0434\u0435\u043b\u0438'),
        ),
        migrations.AlterField(
            model_name='conditioner',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditioner', to='catalogue.Type', verbose_name='\u0422\u0438\u043f'),
        ),
    ]
