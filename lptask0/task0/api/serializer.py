from rest_framework import serializers
from task0.models import Item
from register.models import MyUser
from rest_framework.authtoken.models import Token

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id','username','email','Created']