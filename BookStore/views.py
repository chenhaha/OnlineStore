#coding:utf-8
from django.shortcuts import render,render_to_response
from django import forms
from BookStore.models import *
from django.contrib import auth
from OnlineStore import settings
from django.template import RequestContext

# Create your views here.


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名:')
    password = forms.CharField(label='密  码:')


def global_settings(request):
    image_url = settings.IMAGE_URL
    return locals()


def index(request):
    #验证登录
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
    #取出书籍信息
    bookname = Book.objects.values()
    #bookimage = Book.objects.get(name='firstjavacode')['picture'][1:]
    print settings.IMAGE_URL, bookname[2]['picture']
    return render_to_response('index.html', locals(), context_instance=RequestContext(request) )


def about(request):
    form = LoginForm()
    return render_to_response('about.htm', {'form': form})


def cart(request):
    form = LoginForm()
    return render_to_response('cart.htm', {'form': form})


def category(request):
    form = LoginForm()
    return render_to_response('category.htm', {'form': form})


def contact(request):
    form = LoginForm()
    return render_to_response('contact.htm', {'form': form})


def myaccount(request):
    form = LoginForm()
    return render_to_response('myaccount.htm', {'form': form})


def register(request):
    form = LoginForm()
    return render_to_response('register.htm', {'form': form})


def specials(request):
    form = LoginForm()
    return render_to_response('specials.htm', {'form': form})


def details(request):
    form = LoginForm()
    return render_to_response('details.htm', {'form': form})


