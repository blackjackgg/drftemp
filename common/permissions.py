# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny

from rest_framework.generics import ListAPIView

from account.models import MyUser

ALL_RBAC_VIEWS = []


class RbacPermission(BasePermission):
    # '''
    # 自定义权限
    # '''
    #
    def get_current_method(self, request, view):
        """
        获取当前请求的方法（当前请求的是post/get 还是 viewset 的 action）
        :param request:
        :param view:
        :return:
        """
        return hasattr(view, 'action') and getattr(view,'action') or request._request.method.lower()

    @classmethod  ##不需要实例化直接调用
    def get_permission_from_role(cls, request):
        try:

            perms = request.user.roles.values('permissions__name', ).distinct()  ##后面的权限方法都写在method中
            return [p['permissions__name'] for p in perms]   ##写入到权限方法中去
        except AttributeError:
            return []


    def get_current_perms(self, request, view):
        """
        获取当前需要验证的权限
        :return:
        """
        _method = self.get_current_method(request, view)
        perms_map = view.perms_map


        # name_or_perm_obj 可能是权限名称，也可能是基于BasePermission的权限扩展实例
        try:
            action, name_or_perm_obj, label = [(action, name_or_perm_obj, label)
                                               for action, name_or_perm_obj, label in perms_map
                                               if action == _method][0]
        except IndexError:
            return True

        print  name_or_perm_obj
        return name_or_perm_obj



    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if not hasattr(view, 'perms_map'):  ##搜集所需权限列表
            return True


        name_or_perm_obj = self.get_current_perms(request, view)
        if isinstance(name_or_perm_obj, BasePermission):
            return name_or_perm_obj.has_permission(request, view)  ##权限对象检查
        return self.has_name_in_perms(name_or_perm_obj, request)  ##字段检查


    def has_name_in_perms(self, perm_name, request):  ##检查用户有没有这个权限
        perms = self.get_permission_from_role(request)
        return perm_name == '*' or perm_name in perms


# class RbacLimitDoctorPermission(RbacPermission):
#     """
#     限制管理后台医生权限，但是又不限制普通用户
#     有些RBAC权限的viewset，会给到后台admin使用，同时又给到c端用户使用。
#     admin需要有权限控制，所以需要显示并做显示，但是c端只要登入就可以
#
#     如： 获取医生详情
#     """
#
#     def __init__(self, name):
#         """
#         :param name: 权限名称
#         """
#         self.name = name
#
#     def has_permission(self, request, view):
#         if request.user and request.user.is_authenticated:
#             return request.user.type == MyUser.ORDINARY_USER or self.has_name_in_perms(
#                 self.name, request)
#         return False
#
#
# class RbacAllowAny(RbacPermission):
#     """
#     不限制接口
#     """
#
#     def __init__(self, name):
#         self.name = name
#
#     def has_permission(self, request, view):
#         return True
#
#
# class ObjPermission(BasePermission):
#     '''
#     密码管理对象级权限控制
#     '''
#
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_superuser:
#             return True
#         elif request.user.id == obj.uid_id:
#             return True
#
#
# class TreeSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     label = serializers.CharField(max_length=20, source='name')
#     pid = serializers.PrimaryKeyRelatedField(read_only=True)
#
#
# class TreeAPIView(ListAPIView):
#     '''
#     自定义树结构View
#     '''
#     serializer_class = TreeSerializer
#     permission_classes = (IsAuthenticated, )
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         serializer = self.get_serializer(queryset, many=True)
#         tree_dict = {}
#         tree_data = []
#         try:
#             for item in serializer.data:
#                 tree_dict[item['id']] = item
#             for i in tree_dict:
#                 if tree_dict[i]['pid']:
#                     pid = tree_dict[i]['pid']
#                     parent = tree_dict[pid]
#                     parent.setdefault('children', []).append(tree_dict[i])
#                 else:
#                     tree_data.append(tree_dict[i])
#             results = tree_data
#         except KeyError:
#             results = serializer.data
#
#         if request.query_params.get(self.paginator.page_query_param):
#             return self.get_paginated_response(results)
#         return Response({'detail': results})


def rbac_handler(f):
    """
    这是修饰使用了RBAC权限的视图

    主要是收集所有的权限，方便执行python manage.py handler_perms 命令
    :param f:
    :return:
    """
    ALL_RBAC_VIEWS.append(f)
    return f
