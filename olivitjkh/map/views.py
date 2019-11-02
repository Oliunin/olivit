from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#Импорты для API
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from rest_framework.response import Response
from rest_framework import generics
from map.models import Company,House
from map.serializers import HouseSerializer, CompanySerializer
# Create your views here.

def map(request):
    return render(request,'map/map.html')

class gethouses(generics.ListAPIView):
    """
    Returns a list of all houses
    """
    def get(self, request):
        Houses = House.objects.all()
        # Companies = Company.objects.all()
        HSerializer = HouseSerializer(Houses, many=True)
        # CSerializer = CompanySerializer(Companies, many=True)
        return Response({"Houses": HSerializer.data})

class getcompanies(generics.ListAPIView):
    """
    Returns a list of all companies
    """
     # model = Company
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    def get(self, request):
        Companies = Company.objects.all()
        # Companies = Company.objects.all()
        CSerializer = CompanySerializer(Companies, many=True)
        # CSerializer = CompanySerializer(Companies, many=True)
        return Response({"Companies": CSerializer.data})
