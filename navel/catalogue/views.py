# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from catalogue.forms import CatalogueFilterForm
from models import Conditioner, Brand, Type, BlockType


def index(request, brand_title=None):
    conditioners = Conditioner.objects.all()
    filter_form = CatalogueFilterForm(request.GET)

    if brand_title:
        conditioners = conditioners.filter(brand__title=brand_title)
        brand = get_object_or_404(Brand, title=brand_title)
        filter_form.data = {'brand__in': [brand.pk]}

    if filter_form.is_valid():
        conditioners = conditioners.filter(**filter_form.cleaned_data)

    context = {
        'conditioners': conditioners,
        'filter_form': filter_form,
    }
    return render(request, 'catalogue/index.html', context)


def brand(request, brand_id):
    return index(request, brand_title=brand_id)


def model(request, brand_id, slug):
    conditioner = get_object_or_404(Conditioner, brand_id=brand_id, slug=slug)
    return render(request, 'catalogue/model.html', context={'conditioner': conditioner})
