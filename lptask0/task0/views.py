from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import List
# Create your views here.
def home(request):
    ls = ToDoList.objects.all() 
    if request.method == 'POST':
        form = List(request.POST)
        if form.is_valid():
            form.save()      
    else:
        form = List()
   
    return render(request, "task0/create.html",{'form':form, 'submit':"Add ToDoList", 'ls':ls})


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
    return render(response, 'task0/items.html',{'it':it, 'ls':ls})

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
    else:
            form = List()
    
    return render(request, "task0/create.html",{'form':form, 'submit':"Add ToDoList", 'ls':ls})
