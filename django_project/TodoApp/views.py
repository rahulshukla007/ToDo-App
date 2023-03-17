from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.utils import timezone
from  . models import Todo

import logging
logging.basicConfig(filename='main.log', encoding='utf-8', level=logging.DEBUG)


def home(request):
    if request.method  == "GET":
        return render(request,'TodoApp/home.html')
    else:
        username = request.POST.get('uname')
        logging.debug(f'This is username {username}')
        print(username)
        password = request.POST.get('psw')
        logging.debug(f'This is username {password}')
        print(password)
        user = auth.authenticate(username = username, password = password)
        logging.debug(f'This is username {user}')
        print(user)
        try:
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                return redirect('/')
        except Exception as e:
            print(e)
            return redirect('/')

@login_required(login_url='Home')
def dashboard(request):
    obj = Todo.objects.all().order_by('-date')
    logging.debug(f'This is dashboard {obj}')
    print(obj)
    context = {'obj':obj}
    return render(request,'TodoApp/dashboard.html', context)

def addItem(request):
    if request.method == "POST":
        #print(request.POST)
        item = request.POST.get('item')
        print(item)
        date = timezone.now()
        print(date)
        data = Todo.objects.create(text=item, date=date)
        print(data.id)
        return redirect('/dashboard')


def delete(request, id):
    del_item = Todo.objects.get(id=id)
    del_item.delete()
    print(id)

    return redirect('/dashboard')

def signout(request):
    logout(request)
    return redirect('/')
        
   

