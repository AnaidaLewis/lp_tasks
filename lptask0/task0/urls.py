from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("<int:id>", views.id, name = "id"),
    # path("delete/<int:id/>", views.delete_item, name = "delete_item"),
]