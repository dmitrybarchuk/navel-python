# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Conditioner(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Название модели')
    slug = models.SlugField(max_length=255, db_index=True, blank=True, unique=True)
    inverter = models.BooleanField(default=False, verbose_name=u'Инвертор')
    brand = models.ForeignKey('Brand', related_name='conditioner', verbose_name=u'Бренд', to_field='title')
    type = models.ForeignKey('Type', related_name='conditioner', verbose_name=u'Тип')
    block_type = models.ForeignKey('BlockType', related_name='conditioner', verbose_name=u'Тип внутреннего блока')
    image = models.ImageField(upload_to='conditioners', blank=True, verbose_name=u'Изображение')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата добавления')

    class Meta:
        verbose_name = u'Кондиционер'
        verbose_name_plural = u'Кондиционеры'

    def __unicode__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Название', unique=True)
    description = models.TextField(verbose_name=u'Описание', blank=True)

    class Meta:
        verbose_name = u'Бренд'
        verbose_name_plural = u'Бренды'

    def __unicode__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'Название')

    class Meta:
        verbose_name = u'Тип'
        verbose_name_plural = u'Типы'

    def __unicode__(self):
        return self.title


class BlockType(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'Название')

    class Meta:
        verbose_name = u'Тип внутреннего блока'
        verbose_name_plural = u'Типы внутреннего блока'

    def __unicode__(self):
        return self.title
