#!/usr/bin/python
# -*- coding: utf-8 -*-

# libthumbor - python extension to thumbor
# http://github.com/rafaelcaricio/django-thumbor-url

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 Rafael Caricio rafael@caricio.com

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('libthumbor.django.views',
    url("^$", 'generate_url', name="generate_thumbor_url"),
)
