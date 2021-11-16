from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render
from home.RegistrationForm import RegistrationForm
from home.todoForm import TodoListForm
from home.models import TodoList
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    return render(request, "index.html")

# -----------------auth system::begin-----------------
def userRegister(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created')
            return redirect("/login")
    else:
        form = RegistrationForm()
    dataContext = {
        'form' : form
    }
    return render(request, 'pages/auth/register.html', dataContext)

def userLogin(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=user, password=password)
        if user is not None:
            try:
                login(request, user)
                messages.success(request, 'You have logged in successfully')
                return redirect("/todo_list")
            except:
                pass
        else:
            messages.warning(request, 'Login details did not match!!')
            return render(request, "pages/auth/login.html")
    return render(request, "pages/auth/login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")

# -----------------auth system::end-----------------

def todoList(request):
    if request.user.is_anonymous:
        return redirect('/login')
    count_task = TodoList.objects.all().count()
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Task Added To List")
                return redirect("/todo_list")
            except:
                pass
    else:
        form = TodoListForm()
    list_data = TodoList.objects.all()
    dataContext = {
        "name": request.user,
        "list_datas": list_data,
        "form":form,
        "count_task":count_task
    }
    return render(request, "pages/application/index.html", dataContext)

def updateList(request, id):
    if request.user.is_anonymous:
        return redirect('/login')
    count_task = TodoList.objects.all().count()
    dt = TodoList.objects.get(pk=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=dt)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Task Updated")
                return redirect("/todo_list")
            except:
                pass
    else:
        form = TodoListForm(instance=dt)
    list_data = TodoList.objects.all()
    dataContext = {
        "list_datas": list_data,
        "form":form,
        "count_task":count_task
    }
    return render(request, "pages/application/update.html", dataContext)

def deleteList(request, id):
    dt = TodoList.objects.get(pk=id)
    if request.method == "POST":
        # delete confirmation
        dt.delete()
        messages.warning(request, "Task Deleted!!")
        return redirect("/todo_list")
    return render(request, "pages/application/delete.html")