from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("<int:id>", views.id, name = "id"),
    # path("items", views.items, name = "addItem"),
    # path("home/<int:id>", views.update, name = "update"),
]