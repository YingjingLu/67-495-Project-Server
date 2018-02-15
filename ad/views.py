# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def index(request, data_list = [], anomaly_threshold = 0.9):
    title = 'test title'
    template = loader.get_template('ad/index.html')
    context = {'title': title, 'data_list': data_list, 'anomaly_threshold': anomaly_threshold}
    return HttpResponse(template.render(context, request))
