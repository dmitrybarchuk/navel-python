# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from models import Conditioner


def index(request):
    conditioners = Conditioner.objects.all()
    context = {
        'conditioners': conditioners,
    }
    return render(request, 'catalogue/index.html', context)
