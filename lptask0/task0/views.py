from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import List,Items
# Create your views here.
def id(response,id):
    ls = ToDoList.objects.get(id = id)
    it = ls.item_set.get(id = id)
    return HttpResponse("<h1>%s</h1><br><p>%s</p>" %(ls.name, it.text))


def index(request):
    ls = ToDoList.objects.all()
    
    return render(request, 'task0/library.html',{'ls':ls})

def home(request):
    if request.method == 'POST':
        form = List(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/items')

    else:
        form = List()
        return render(request, "task0/create.html",{'form':form, 'submit':"Add ToDoList"})



def items(request):
    if request.method == 'POST':
        form = Items(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/')

    else:
        form = Items()
        return render(request, "task0/create.html",{'form':form, 'submit':"Add Item"})

    
