# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render

from catalogue.forms import CatalogueFilterForm
from models import Conditioner, Brand, Type, BlockType


def index(request):
    conditioners = Conditioner.objects.all()
    filter_form = CatalogueFilterForm(request.GET)

    if filter_form.is_valid():
        conditioners = conditioners.filter(**filter_form.cleaned_data)

    context = {
        'conditioners': conditioners,
        'filter_form': filter_form,
    }
    return render(request, 'catalogue/index.html', context)
