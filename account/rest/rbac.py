# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from operator import itemgetter

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response

from account.models import  Role, Permission
from account.rest.serializers import  RoleListSerializer,PermissionListSerializer





class RoleViewSet(ModelViewSet):
    '''
    角色管理：增删改查
    '''
    perms_map = (
        ('*', 'role_all', '角色管理'),
        ('list', 'role_list', '角色列表'),
        ('create', 'role_create', '角色创建'),
        ('update', 'role_edit', '角色编辑'),
        ('destroy', 'role_delete', '角色删除'),
    )
    queryset = Role.objects.all()
    serializer_class = RoleListSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', )
    ordering = ('id', )
    # permission_classes = (RbacPermission, )




class PermissionViewSet(ModelViewSet):
    '''
    权限：增删改查
    '''

    perms_map = (
        ('*', 'permission_all', '权限管理'),
        ('list', 'permission_list', '权限列表'),
        ('create', 'permission_create', '权限创建'),
        ('update', 'permission_edit', '权限编辑'),
        ('destroy', 'permission_delete', '权限删除'),
    )
    queryset = Permission.objects.all()
    serializer_class = PermissionListSerializer
    search_fields = ('name', )
    ordering = ('id', )
    # permission_classes = (RbacPermission, )


