# -*- coding: utf-8 -*-
# © 2018 QYT Technology
# Authored by: Zhao Xingtao (zxt50330@gmail.com)

from django.db import models


class ModelBase(models.Model):
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
