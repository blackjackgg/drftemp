# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.admin import UserAdmin

from django.contrib import admin
from .models import  MyUser


admin.site.register(MyUser, UserAdmin)

# Register your models here.
