from register.api import serializer
from task0.models import ToDoList, Item
from register.models import MyUser

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializer import ItemSerializer, MyUserSerializer
# Create your views here.

@api_view(['GET'])
@permission_classes(())
def apiOverview(request):
    api_urls = {
        'Users': '/api/users/',
        'Items': '/api/items/',
        'Item-detail': '/api/item-detail/<int:pk>/',
        'Item-create': '/api/item-create/',
        'Item-update': '/api/item-update/<int:pk>/',
        'Item-delete': '/api/item-delete/<int:pk>/',

    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes(())
def MyUsers(request):
    MyUsers = MyUser.objects.all()
    serializer = MyUserSerializer(MyUsers, many = True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes(())
def Items(request):
    Items = Item.objects.all()
    serializer = ItemSerializer(Items, many = True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def ItemDetail(request, pk):
    try:
	    Items = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ItemSerializer(Items, many=False)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def ItemCreate(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def ItemUpdate(request, pk):
    try:
	    Item_update = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

     #request.user is token ka user
    ls = ToDoList.objects.get(user = request.user)
    items = Item.objects.filter(todolist = ls.id)
    print(items)
 
    if Item_update not in items:
        return Response({'response': 'You are do not have permission to update item'})

    if request.method == 'PUT':
        serializer = ItemSerializer(instance=Item_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['DELETE'])
@permission_classes(())
@permission_classes((IsAuthenticated,))
def ItemDelete(request, pk):
    try:
	    Item_delete = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    ls = ToDoList.objects.get(user = request.user)
    items = Item.objects.filter(todolist = ls.id)
    print(items)
 
    if Item_delete not in items:
        return Response({'response': 'You are do not have permission to delete item'})

    if request.method == 'DELETE':
        Item_delete.delete()
        return Response('Item succsesfully delete!')
        
         

