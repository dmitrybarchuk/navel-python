# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Conditioner, Brand, Type, BlockType


class AdminConditioner(admin.ModelAdmin):
    list_display = ('title', 'brand', 'type', 'block_type', 'date_added')
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', 'brand', 'type', 'block_type',)
    list_filter = ('brand', 'type', 'block_type',)

admin.site.register(Conditioner, AdminConditioner)


class AdminBrand(admin.ModelAdmin):
    exclude = ()
    search_fields = ('title', )

admin.site.register(Brand, AdminBrand)


class AdminType(admin.ModelAdmin):
    exclude = ()
    search_fields = ('title', )

admin.site.register(Type, AdminType)


class AdminBlockType(admin.ModelAdmin):
    exclude = ()
    search_fields = ('title', )

admin.site.register(BlockType, AdminBlockType)
