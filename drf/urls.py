# -*- coding: utf-8 -*-
"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
import settings
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from ask.rest.views import AskView
import  ask.rest.urls

schema_view = get_schema_view(
   openapi.Info(
      title="swag接口文档",
      default_version='v1',
      description="描述描述",
      terms_of_service="https://www.blackjack.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ask/',include('ask.rest.urls', namespace='ask')),
    url(r'^task/',include('task.rest.urls', namespace='task')),
    url(r'^account/',include('account.rest.urls', namespace='account')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', views.obtain_auth_token),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
      name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework_docs')),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

