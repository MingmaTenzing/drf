from django.contrib.auth.models import Group, User
from .models import Cars
from rest_framework import serializers

class User_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields= ['url', 'username', 'email', 'groups', 
                ] 

class Group_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Group
        fields = ['url', 'name']
        
class car_serializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Cars
        fields = "__all__"
        

