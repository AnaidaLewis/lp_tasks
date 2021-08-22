from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import List
# Create your views here.
def id(response,id):
    ls = ToDoList.objects.get(id = id)
    it = Item.objects.filter(todolist=ls)

    if response.method == "POST":
        print(response.POST) #self reference
        if response.POST.get("save"):
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

        # elif response.POST.get("delete"):
        #     for item in it:
        #         if response.POST.get("a"+str(item.id)) == "clicked":
        #             item.complete = True
        #         else:
        #             item.complete = False
        #         del_item = item.objects.get(id = item.id)
        #         del_item.delete()
        

    return render(response, 'task0/items.html',{'it':it, 'ls':ls})

# def update(request,id):
#     select = ToDoList.objects.get(id = id)
#     u_form = Items(request.POST)
#     if u_form.is_valid():
#         u_form.save()
#     return render(request, "task0/create.html",{'form':u_form, 'submit':"Update Item"})

def home(request):
    if request.method == 'POST':
        form = List(request.POST)
        if form.is_valid():
           form.save()
        #    return redirect('/items')
    else:
        form = List()
    ls = ToDoList.objects.all()    
    return render(request, "task0/create.html",{'form':form, 'submit':"Add ToDoList", 'ls':ls})


# def items(request):
#     if request.method == 'POST':
#         form = Items(request.POST)
#         if form.is_valid():
#            form.save()
#            return redirect('/home')
#     else:
#         form = Items()
#         return render(request, "task0/create.html",{'form':form, 'submit':"Add Item"})

    
