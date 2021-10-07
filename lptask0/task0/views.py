from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import List, Account
from register.decorators import  allowed_users, admin_only

# Create your views here.


@login_required(login_url = 'login')
@admin_only
def home(request):
    ls = ToDoList.objects.all() 
    if request.method == 'POST':
        form = List(request.POST)
        if form.is_valid():
            form.save()      
    else:
        form = List()
    context = {'form':form, 'submit':"Add ToDoList", 'ls':ls}
    return render(request, "task0/create.html",context)


@login_required(login_url = 'login')
def id(response,id):
    ls = ToDoList.objects.get(id = id)
    it = Item.objects.filter(todolist=ls)

    if response.method == "POST":
        print(response.POST) #self reference
        if response.POST.get("update"):
            for item in it:
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2 : 
                Item.objects.create(todolist = ls, text = txt, complete = False)
            else:
                print("Invalid")

        elif response.POST.get("delete"):
            for item in it:
                if response.POST.get("c"+str(item.id)) == "clicked":
                    del_item = Item.objects.get(id = item.id)
                    del_item.delete()
            it = Item.objects.filter(todolist=ls)
    context = {'it':it, 'ls':ls}
    return render(response, 'task0/items.html',context)


@login_required(login_url = 'login')
@allowed_users(allowed_roles =['Admin'])
def delete_td(request):
    ls = ToDoList.objects.all() 
    if request.method == 'POST':
        if request.POST.get("delete"):
            for td in ls:
                if request.POST.get("list"+str(td.id)) == "clicked":
                    del_td = ToDoList.objects.get(id = td.id)
                    del_td.delete()   
            ls = ToDoList.objects.all()
            return redirect("/")
    

@login_required(login_url = 'login')
@allowed_users(allowed_roles =['ToDoUsers'])
def userHome(request):
    get_user = ToDoList.objects.get(user = request.user)
    print(get_user)
    # return redirect(reverse('id', args = [get_user.id]))
    return redirect(get_user, permanent= True) #reverse does the same thing that u used with get absolute url
   

@login_required(login_url = 'login')
@allowed_users(allowed_roles =['ToDoUsers'])
def accountSettings(request):
    form = Account(instance = request.user)
    if request.method == 'POST':
       form = Account(request.POST, request.FILES, instance = request.user)
       if form.is_valid:
           form.save()
    context = {"form":form}
    return render(request, 'task0/user.html',context)


