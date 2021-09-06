from django.shortcuts import render,redirect
from .forms import RegisterForm 

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from.decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group

from task0.models import ToDoList

from django.contrib import messages


# Create your views here.
@unauthenticated_user
def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'ToDoUsers')
            user.groups.add(group)

            ToDoList.objects.create(user = user, name = user.username)

            messages.success(request, 'Account created for ' + username)
            return redirect('/login')

    form = RegisterForm()
    return render(request,"register/register.html", {'form':form})


@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            messages.info(request, 'Incorrect Username or Password')

    context = {}
    return render(request,"register/login.html",context)


@login_required(login_url = 'login')
def logoutUser(request):

    logout(request)
    return redirect('/login')

