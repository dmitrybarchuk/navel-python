# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render
from models import Conditioner, Brand, Type, BlockType


def index(request):
    conditioners = Conditioner.objects.all()
    brands = Brand.objects.all()
    types = Type.objects.all()
    block_types = BlockType.objects.all()
    if request.GET.get('brand'):
        queries = [Q(brand=value) for value in request.GET.getlist('brand')]
        for query in queries:
            conditioners = conditioners.filter(query)
    if request.GET.get('type'):
        conditioners = conditioners.filter(type=request.GET.get('type'))
    if request.GET.get('block_type'):
        conditioners = conditioners.filter(block_type=request.GET.get('block_type'))
    if request.GET.get('inverter'):
        conditioners = conditioners.filter(inverter=request.GET.get('inverter'))
    context = {
        'conditioners': conditioners,
        'brands': brands,
        'types': types,
        'block_types': block_types,
    }
    return render(request, 'catalogue/index.html', context)
