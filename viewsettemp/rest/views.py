# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import  ListModelMixin, CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ViewSetMixin
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
# from  rest_framework.filters import OrderingFilter
from django.db.models import Q
import django_filters
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

##认证类
#from myuser.auth import MyAuth
#常用导入头部

from .models import {a}
from .serializers import {a}Serializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
#from common.permissions import RbacPermission, rbac_handler




##token在header中携带 “Authorization”：“Token c4742d9de47d2cfec1dbe5819883ce6a3e4d99b”　　

# class MyFilter(django_filters.FilterSet):
#     class Meta:
#         model = {a}  # 模型名
#         sort = django_filters.OrderingFilter(fields=('q',))  ##排序
#         fields = '__all__'  #['exact','gte','lte']  year__gt  month__gt  day__gt


class {a}View(ModelViewSet):
    ''' ##markdown  使用说明'''
    ##使用perms_map进行留有权限管理 第一个是全新  最后一个是label
    perms_map = (('*', 'VIP', '会员'), ('list', '*', '普通用户'),   ##*表示能没有权限限制
                 ('create', 'VIP', '会员'), ('update', 'VIP', '会员'),
                 ('destroy', 'VIP','会员'))
    queryset = {a}.objects.all()  ##在此处修改查询集即可
    serializer_class ={a}Serializer
    # filter_class = MyFilter
    #ordering_fields = ('q', 'choice')                ##?ordering=price,name  查询 按照 price 排序后 在按 name 排序的结果 支持升序和降序 加-号即可
    #search_fields = ('q', 'a', 'link')  # 模糊搜索
    #authentication_classes = [TokenAuthentication, ]
    #permission_classes = [RbacPermission, ]

    # @swagger_auto_schema(method='get',operation_description='描述')
    # @action(methods=['get','post'],detail=False)   ##自定义方法
    # action是drf提供的路由和视图方法绑定关系的装饰器
    # 参数2: detail  当前是否方法是否属于详情页视图，False，系统不会自动增加pk在生成的路由地址中  True  则系统会自动增加pk在生成的路由地址
    # def query(self,request):  # 其接口 http://127.0.0.1:8000/task/query/
    #     # 获取阅读量最多的5条数据
    #     para= request.query_params          ## request.data post put 参数
    #     books = {a}.objects.filter(q__contains =para['q']) # 多条查询使用Q    #table.object.filter(Q(title__startswith='key1') | Q(title__startswith='key2'))
    #     serializer = {a}Serializer(instance=books,many=True)
    #     return Response(serializer.data)




