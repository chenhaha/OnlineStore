#coding:utf-8
from django.shortcuts import render,render_to_response
from django import forms
from BookStore.models import *
from django.contrib import auth
from OnlineStore import settings
from django.template import RequestContext
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse

# Create your views here.


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名:')
    password = forms.CharField(label='密  码:')


def global_settings(request):
    image_url = settings.IMAGE_URL
    return locals()


def index(request):
    #取出书籍信息
    bookname = Book.objects.values()
    print bookname
    #验证登录
    if request.user.is_authenticated():
        user = request.user
        return render_to_response('index.htm', locals())

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)

    #bookimage = Book.objects.get(name='firstjavacode')['picture'][1:]
    #print settings.IMAGE_URL, bookname[2]['picture']
    return render_to_response('index.htm', locals())#, context_instance=RequestContext(request)


def about(request):
    form = LoginForm()
    return render_to_response('about.htm', {'form': form})


def cart(request):
    #验证登录
    if request.user.is_authenticated():
        user = request.user
        return render_to_response('cart.htm', locals())
    return render_to_response('cart.htm')


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
    #取出书籍信息
    bookname = Book.objects.values()
    #验证登录
    if request.user.is_authenticated():
        user = request.user
        return render_to_response('details.htm', locals())
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)

    #print bookname[2]['desc']
    #bookimage = Book.objects.get(name='firstjavacode')['picture'][1:]
    return render_to_response('details.htm', locals())


