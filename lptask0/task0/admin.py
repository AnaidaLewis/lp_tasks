from django.contrib import admin
from .models import ToDoList, Item
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('todolist','text','complete')
    list_filter = ('todolist','complete')
    search_fields = ['todolist__name']

admin.site.register(ToDoList)
admin.site.register(Item, ItemAdmin)