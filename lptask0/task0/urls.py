from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("<int:id>", views.id, name = "id"),
    path("delete/", views.delete_td, name = "delete_td"),
    path('user-page/', views.userPage, name = "user-page")
]