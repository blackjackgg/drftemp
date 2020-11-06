# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import TaskView

#需要进行路由注册action才能生效
router = DefaultRouter()
router.register(r'', TaskView)
#
# urlpatterns = [
#     url(r'^', include(router.urls, namespace='ask')),
# ]

urlpatterns = router.urls


##简便的url配置  对应viewsetMixin

# urlpatterns = [
#     # url(r'^book$', BookView.as_view()),
#     # url(r'^book/(?P<id>\d+)$', BookEditView.as_view()),
#     url(r'^$', TaskView.as_view({"get": "list", "post": "create"})),
#     url(r'^(?P<pk>\d+)/$', TaskView.as_view({"get": "retrieve", "patch": "update", "delete": "destroy"})),
# ]



