
from django.shortcuts import render
from rest_framework import permissions, viewsets, request, response
from  django.contrib.auth.models import User,Group
from django.http import HttpRequest, HttpResponse

from .models import Cars

from .serializers import User_serializer, Group_Serializer, car_serializer

# Create your views here.

class User_view_set(viewsets.ModelViewSet, HttpRequest):
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes=[permissions.IsAuthenticated]
    print(HttpRequest.body)
    serializer_class = User_serializer
    # permission_classes = [permissions.IsAuthenticated]
    

class group_view_set( viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = Group_Serializer
    # permission_classes = [permissions.IsAuthenticated]

class car_view_set(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = car_serializer
   



    