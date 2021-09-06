from django.contrib import admin
from .models import MyUser
# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username','email','Created')
    list_filter = ('Created',)
    search_fields = ['username']

admin.site.register(MyUser, MyUserAdmin)
