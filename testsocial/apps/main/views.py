import datetime

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, RegistrationForm, MessForm
from .models import Message

# Create your views here.
def index(request):
    return render(request, 'main/home.html', {'title':'Главная',})


def login_view(request):
    if request.method == 'GET':
        form = LoginForm(request.POST or None)
        context = {'form': form, 'title':'Войти'}
        return render(request, 'main/login.html', context=context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(index)
        context = {'form': form, 'title':'Войти',}
        return render(request, 'main/login.html', context=context)


def registration_view(request):
    if request.method == 'GET':
        form = RegistrationForm(request.POST or None)
        context = {'form': form,'title':'Регистрация'}
        return render(request, "main/reg.html", context)

    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)

            return redirect(index)

        context = {'form': form,'title':'Регистрация'}
        return render(request, "main/reg.html", context)


def chat_view(request):
    if request.method== "GET":
        mess = Message.objects.order_by('id')
        context = {'mess':mess, 'title':'Чат'}
        return render(request, 'main/chat.html',context=context)
    elif request.method=="POST":
        form = MessForm(request.POST)
        if form.is_valid():
            new_mess = form.save(commit=False)
            new_mess.message = request.user
            new_mess.text = form.cleaned_data['text']
            new_mess.pub_data = datetime.datetime.now()
            form.save()
            return redirect(chat_view)




