# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import  ListModelMixin, CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ViewSetMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from  account.models  import MyUser
from serializers import  MyUserSerializer,LoginSerializer
import  django_filters
from rest_framework.decorators import action
from rest_framework import routers, serializers
from rest_framework.response import Response
from django.conf import settings

# class MyFilter(django_filters.FilterSet):
#     class Meta:
#         model = MyUser # 模型名
#         sort = django_filters.OrderingFilter(fields=('q',))  ##排序
#         fields = '__all__'   #['exact','gte','lte']  year__gt  month__gt  day__gt



class MyUserView(ModelViewSet):
    """
    用户管理 添加的视图
    """
    # perms_map = (
    #     ('*', 'user_all', '用户管理'),
    #     ('list', 'user_list', '用户列表'),
    #     ('create', 'user_create', '用户创建'),
    #     ('update', 'user_edit', '用户编辑'),
    #     ('destroy', 'destroy', '用户删除'),
    #     ('reset_password', 'reset_password', '重置用户密码'),
    # )
    queryset = MyUser.objects.filter()
    serializer_class = MyUserSerializer
    # filter_class = MyFilter
    # ordering = ('-date_joined',)
    search_fields = ('username', 'type')


    @action(methods=['get','post'], detail=True)
    def reset(self, request, *args, **kwargs):
        """重置用户密码"""
        instance = self.get_object()
        instance.set_password(settings.USER_INITIAL_PASSWORD)
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['get','post'], detail=True)
    def change_active(self, request, *args, **kwargs):
        """
        设置激活
        接受 **is_active** 参数
        :return:
        """
        is_active = request.data.get('is_active')

        instance = self.get_object()
        instance.is_active = is_active
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)



#
class LoginView(APIView):
    """ 登录视图 """

    serializer_class = LoginSerializer

    def post(self, request):
        """
        用户登录，获取 token
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
