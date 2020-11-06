# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from ask.rest.views import AskView

#
# router = DefaultRouter()
# router.register(r'ask', AskView.as_view(), base_name="ask")
#
# urlpatterns = [
#     url(r'^', include(router.urls, namespace='ask')),
# ]

##简便的url配置  对应viewsetMixin
urlpatterns = [
    # url(r'^book$', BookView.as_view()),
    # url(r'^book/(?P<id>\d+)$', BookEditView.as_view()),
    url(r'^$', AskView.as_view({"get": "list", "post": "create"})),
    url(r'^(?P<pk>\d+)/$', AskView.as_view({"get": "retrieve", "patch": "update", "delete": "destroy"})),
]
