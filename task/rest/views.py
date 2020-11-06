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

from ..models import Task
from ..serializers import TaskSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from common.permissions import RbacPermission, rbac_handler


# class AskView(APIView):
#     # 重写get方法 进行get访问时会进行的处理
#     def get(self, request):
#         if request.GET.get('add'):
#             data = Ask.objects.create(q=u"test", a="666",link="jack@163.com",date=u"排除")
#             return Response({"message":"ok"})        #Response(data_list.data)
#         else:
#             data = Ask.objects.all()[:10]
#             data_list = AskSerializer(data, many=True)
#             return Response(data_list.data)


# class BookView(ViewSetMixin, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer




# 如果我们再定义一个类
# class ModelViewSet(ViewSetMixin, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
#     pass

# class MyPermission(BasePermission):
#     message = "权限用户才能访问"
#     def has_permission(self, request, view):
#         """
#         自定义权限只有vip用户能访问，
#         注意我们初始化时候的顺序是认证在权限前面的，所以只要认证通过~
#         我们这里就可以通过request.user,拿到我们用户信息
#         request.auth就能拿到用户对象
#         """
#         print(request.auth)
#         return True


##token在header中携带 “Authorization”：“Token c4742d9de47d2cfec1dbe5819883ce6a3e4d99b”　　

class MyFilter(django_filters.FilterSet):
    class Meta:
        model = Task  # 模型名
        sort = django_filters.OrderingFilter(fields=('q',))  ##排序
        fields = {'q':['exact','icontains'], 'a':['exact','icontains'], 'choice':['exact','icontains']}   #['exact','gte','lte']  year__gt  month__gt  day__gt


class TaskView(ModelViewSet):
    ''' ##markdown  使用说明'''
    ##使用perms_map进行留有权限管理 第一个是全新  最后一个是label
    perms_map = (('*', '*', '会员'), ('list', '*', '普通用户'),   ##*表示能没有权限限制
                 ('create', 'VIP', '会员'), ('update', 'VIP', '会员'),
                 ('destroy', 'VIP','会员'),('query', "*", "查询"),)
    queryset = Task.objects.all()  ##在此处修改查询集即可
    serializer_class = TaskSerializer
    filter_class = MyFilter
    ordering_fields = ('q', 'choice')                ##?ordering=price,name  查询 按照 price 排序后 在按 name 排序的结果 支持升序和降序 加-号即可
    search_fields = ('q', 'a', 'link')  # 模糊搜索
    #authentication_classes = [TokenAuthentication, ]
    permission_classes = [RbacPermission, ]

    @swagger_auto_schema(method='get',operation_description='查询单个详细参数')
    @action(methods=['get','post'],detail=False)   ##自定义方法
    # action是drf提供的路由和视图方法绑定关系的装饰器
    # 参数2: detail  当前是否方法是否属于详情页视图，False，系统不会自动增加pk在生成的路由地址中  True  则系统会自动增加pk在生成的路由地址
    def query(self,request):  # 其接口 http://127.0.0.1:8000/task/query/
        # 获取阅读量最多的5条数据
        para= request.query_params          ## request.data post put 参数
        books = Task.objects.filter(q__contains =para['q']) # 多条查询使用Q    #table.object.filter(Q(title__startswith='key1') | Q(title__startswith='key2'))
        serializer = TaskSerializer(instance=books,many=True)
        return Response(serializer.data)




class TaskFilterView(ModelViewSet):
    queryset = Task.objects.all()  ##在此处修改查询集即可
    serializer_class = TaskSerializer



##filter内容
# Blog.objects.filter(title__contains ="django")
#.objects.filter(id__in = [3,6,9])
#.objects.filter(id__range =(30,45))
#.objects.exclude(id=3)
#.objects.filter(create_time__year = 2018)
#objects.filter(create_time__month=3)
#.objects.dates('create_time', 'year','DESC') 返回时间
##__gt gte lt lte startswith  endswith



##一般写法
# class ListCreateAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     pass
#
# class RetrieveUpdateDestroyAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     pass
#
#
# class AskView(ListCreateAPIView):
#     queryset = Ask.objects.all()
#     serializer_class =AskSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class AskEditView(RetrieveUpdateDestroyAPIView):
#     queryset = Ask.objects.all()
#     serializer_class = AskSerializer
#
#     def get(self, request, id, *args, **kwargs):
#         return self.retrieve(request, id, *args, **kwargs)
#
#     def patch(self, request, id, *args, **kwargs):
#         return self.update(request, id, *args, **kwargs)
#
#     def delete(self, request, id, *args, **kwargs):
#         return self.delete(request, id, *args, **kwargs)


##AIPVIEW的封装方法

# class BookView(APIView):
#
#     def get(self, request):
#         query_set = Book.objects.all()
#         book_ser = BookSerializer(query_set, many=True)
#         return Response(book_ser.data)
#
#     def post(self, request):
#         query_set = request.data
#         book_ser = BookSerializer(data=query_set)
#         if book_ser.is_valid():
#             book_ser.save()
#             return Response(book_ser.validated_data)
#         else:
#             return Response(book_ser.errors)
#
#
# class BookEditView(APIView):
#
#     def get(self, request, id):
#         query_set = Book.objects.filter(id=id).first()
#         book_ser = BookSerializer(query_set)
#         return Response(book_ser.data)
#
#     def patch(self, request, id):
#         query_set = Book.objects.filter(id=id).first()
#         book_ser = BookSerializer(query_set, data=request.data, partial=True)
#         if book_ser.is_valid():
#             book_ser.save()
#             return Response(book_ser.validated_data)
#         else:
#             return Response(book_ser.errors)
#
#     def delete(self, request, id):
#         query_set = Book.objects.filter(id=id).first()
#         if query_set:
#             query_set.delete()
#             return Response("")
#         else:
#             return Response("删除的书籍不存在")


#request.query_params 存放的是我们get请求的参数

#request.data 存放的是我们所有的数据，包括post请求的以及put，patch请求


##序列方法
##genericapiview的两个queryset = None   serializer_class = Non

