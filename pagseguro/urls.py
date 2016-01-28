# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url
from pagseguro import views

urlpatterns = [
     url(r'^$', views.receive_notification, name='pagseguro_receive_notification'),
]
