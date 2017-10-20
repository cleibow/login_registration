# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    return render(request, 'login_app/index.html')

def login(request):
    email = request.POST['email'].lower()
    password = request.POST['password']
    users = User.objects.filter(email = email)
    if len(users):
        user = users[0]
        if user.password == password:
            request.session['user_id'] = user.id
            return redirect('/')

def registration(request):
    res = User.objects.userIsValid(request.POST)
    if res['status']:
        user = User.objects.createUser(request.POST)
        request.session['user_id'] = user_id
        return redirect('/home')
        print 'valid user'
    else:
        for error in res['errors']:
            messages.error(request, error)            
        print res['errors']
    return redirect ('/home')

def home(request):
    if 'user_id' not in request.session:
        user = User.objects.newUser(request.POST)
        request.session['user_id'] = user_id

    return render(request, 'login_app/home.html')




# Create your views here.
