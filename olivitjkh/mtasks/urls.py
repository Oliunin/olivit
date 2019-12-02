from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from map import urls, views
from django.conf import settings
from django.http import HttpResponseRedirect

# Rest API
from rest_framework import routers
from mtasks.serializers import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

APP_NAME='tasks'

urlpatterns = [
    # path('admin/', admin.site.urls,name='taskpanel'),
    # path(r'',include('map.urls'),name='map'),
    # #path(r'^$', lambda r: HttpResponseRedirect('admin/')),   # Remove this redirect if you add custom views
    # path(r'advanced_filters/', include('advanced_filters.urls')),
    # path(r'api/v1/', include(router.urls),name='taskapi'),
]
