from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name = "api-overview"),
    path('users/',views.MyUsers, name = "Users"),
    path('items/',views.Items, name = "Items"),
    path('item-detail/<int:pk>/',views.ItemDetail, name = "Item-detail"),
    path('item-create/',views.ItemCreate, name = "Item-create"),
    path('item-update/<int:pk>/',views.ItemUpdate, name = "Item-update"),
    path('item-delete/<int:pk>/',views.ItemDelete, name = "Item-delete"),
]