# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import  {a}View

#需要进行路由注册action才能生效
router = DefaultRouter()
router.register(r'', {a}View)


urlpatterns = router.urls




