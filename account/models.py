# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import  ListModelMixin, CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ViewSetMixin
from rest_framework.viewsets import ModelViewSet

from datetime import date
# from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import smart_unicode
from django.db.models import Model
#常用导入头部
from rest_framework.response import Response




###自定义的用户类 跟权限类
class MyUser(AbstractUser):
    VIP = '1'
    NORMAL = '2'

    TYPES = (
        (NORMAL, '普通'),
        (VIP, '会员'),
    )

    type = models.CharField(u'账号类型', choices=TYPES, default='8', max_length=2)
    roles = models.ManyToManyField("Role", verbose_name="角色", blank=True)

    class Meta:
        verbose_name = u'账号'
        verbose_name_plural = u'账号'

    def __str__(self):
        return self.username


class Role(models.Model):
    """
    角色
    """
    name = models.CharField(max_length=32, unique=True, verbose_name="角色")
    permissions = models.ManyToManyField("Permission", blank=True, verbose_name="权限")
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name="描述")

    def __str__(self):
        return self.name




class Permission(models.Model):
    """
    权限
    """
    name = models.CharField(max_length=30, unique=True, verbose_name="权限名")
    method = models.CharField(max_length=250, unique=True, null=True, blank=True, verbose_name="方法")
    pid = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父权限")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name
        ordering = ['id']