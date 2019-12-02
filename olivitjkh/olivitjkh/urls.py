"""olivitjkh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from map import urls, views
from django.conf import settings
from django.http import HttpResponseRedirect
from auth0login import urls

# Rest API
from rest_framework import routers
from mtasks.serializers import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('admin/', admin.site.urls,name='taskpanel'),
    path(r'',include('map.urls'),name='map'),
    path(r'^tasks/',include('mtasks.urls')),
    #path(r'^$', lambda r: HttpResponseRedirect('admin/')),   # Remove this redirect if you add custom views
    path(r'advanced_filters/', include('advanced_filters.urls')),
    path(r'api/v1/', include(router.urls),name='taskapi'),
    path(r'',include('auth0login.urls')),
]

admin.site.site_header = settings.SITE_HEADER
