# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):
    currentUser = User.objects.get(id = request.session['user_id'])
    exId = currentUser.favorites.values_list('id', flat = True)
    dope = Item.objects.exclude(id__in=exId)
    data = {
        'items': dope,
        'user': User.objects.get(id = request.session['user_id'])
    }
    print data
    return render(request, 'items/index.html', data)

def newItem(request):
    res = Item.objects.itemVal(request.POST)
    print request.session['user_id']
    if res['status']:
         print "Adding item"
         Item.objects.newItem(request.POST, request.session['user_id'])
    else:
        for error in res['itemErrors']:
            messages.error(request, error)  
            # error is a tag. Tags can be error, success, etc. Can be manipulated further like changing colors          
        print res['itemErrors']
    return redirect('/items')
def create(request):
    return render(request, 'items/newItem.html')

def addFav(request, item_id):
    Item.objects.addFav(item_id, request.session['user_id'])
    return redirect('/items')

def removeFav(request, item_id):
    Item.objects.removeFav(item_id, request.session['user_id'])
    return redirect('/items')

def displayUser(request, item_id):
    errors = Item.objects.validateNew(request.POST)
    item = Item.objects.filter(id = item_id)
    usersWhoFav = User.objects.filter(favorites = item)
    data = {
        'users': usersWhoFav
    }
    print data
    return render(request, 'items/profile.html', data)

def delete(request, item_id):
    user = Item.objects.get(id = user_id)
    Item.objects.deleteItem(item_id, request.session['user_id'])
    return redirect ('/items')

    
    


# Create your views here.

