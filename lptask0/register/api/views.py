from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import Group
from task0.models import ToDoList

from .serializer import RegistrationSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
@permission_classes(())
def reqistration_view(request):
    serializer = RegistrationSerializer(data = request.data)
    data = {}
    if serializer.is_valid():
        my_user = serializer.save()
        data['response'] = "successfully registered a new user"
        data['username'] = my_user.username
        data['email'] = my_user.email
        token = Token.objects.get(user = my_user).key
        data['token'] = token

        group = Group.objects.get(name = 'ToDoUsers')
        my_user.groups.add(group)
        ToDoList.objects.create(user = my_user, name = my_user.username)
    
    else:
        data = serializer.errors
    return Response(data)
 
     