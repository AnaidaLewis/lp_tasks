from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name = "index"),
    path("home", views.home, name = "home"),
    path("<int:id>", views.id, name = "id"),
    path("items", views.items, name = "addItem"),
]