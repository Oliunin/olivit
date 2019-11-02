from django.urls import path
from map import views
from map.views import gethouses, getcompanies

urlpatterns = [
    path(r'',views.map,name='map'),
    path('gethouses/', gethouses.as_view()),
    path('getcompanies/',getcompanies.as_view()),
]
