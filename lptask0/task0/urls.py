from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("<int:id>/", views.id, name = "id"),
    path("delete/", views.delete_td, name = "delete_td"),

    path('user-home/', views.userHome, name = "user-page"),
    path('account/', views.accountSettings, name = "account"),
]