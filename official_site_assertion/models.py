# -*- coding: utf-8 -*-
from django.db import models

__author__ = 'Noots'
__version__ = '1.0'
__date__ = '2018/02/03'


class Assertion(models.Model):
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    url_pattern = models.CharField(max_length=255)
    created_time = models.DateTimeField('created time', auto_now_add=True, blank=True, null=True)
    updated_time = models.DateTimeField('updated time', auto_now=True, blank=True, null=True)


class Objective(models.Model):
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    url_pattern = models.CharField(max_length=255)
    created_time = models.DateTimeField('created time', auto_now_add=True, blank=True, null=True)
    updated_time = models.DateTimeField('updated time', auto_now=True, blank=True, null=True)
