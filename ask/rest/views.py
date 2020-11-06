# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import  ListModelMixin, CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ViewSetMixin
from rest_framework.viewsets import ModelViewSet

#常用导入头部

from ask.models import Ask
from ask.serializers import AskSerializer
from rest_framework.response import Response


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



class AskView(ModelViewSet):
    queryset = Ask.objects.all()
    serializer_class = AskSerializer



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

