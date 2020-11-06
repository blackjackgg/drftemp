# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Ask(models.Model):
    q = models.CharField('q', max_length=30,default="222")
    a = models.CharField('a', max_length=30,default="222")
    link = models.CharField('link', max_length=30,default="222")
    date = models.CharField('date', max_length=30,default="000")


    def __str__(self):
        return self.q


# Create your models here.
