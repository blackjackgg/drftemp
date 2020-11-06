# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from account.rest.views import MyUserView, LoginView
from account.rest import  rbac

#
# router = DefaultRouter()
# router.register(r'ask', AskView.as_view(), base_name="ask")
#
# urlpatterns = [
#     url(r'^', include(router.urls, namespace='ask')),
# ]

##简便的url配置  对应viewsetMixin
router = DefaultRouter()
router.register(r'list', MyUserView)

router.register(r'permissions', rbac.PermissionViewSet)
router.register(r'roles', rbac.RoleViewSet)

#
urlpatterns = [
   url(r'login', LoginView.as_view()),
]

urlpatterns += router.urls
