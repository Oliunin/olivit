from django.urls import path
from map import views
from map.views import gethouses, getcompanies

urlpatterns = [
    #path('',views.map,name='map'),
    path(r'API/gethouses/', gethouses.as_view(),name='gethouses'),
    path(r'API/getcompanies/',getcompanies.as_view(),name='getcompanies'),
]
