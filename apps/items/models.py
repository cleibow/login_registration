# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from ..login_app import views
from django.contrib import messages

from django.db import models
class itemManager(models.Manager):
    def itemVal(self,post):
        itemErrors = []
        name = post['name']
        print name
        if len(name) < 2: 
            itemErrors.append('Item name must be greater than 2 characters.')
        elif len(name) > 255 :
            itemErrors.append('Item name has too many characters')
        return {'status': len(itemErrors) == 0, 'itemErrors':itemErrors}


    def newItem(self, post, user_id):
        name = post['name']
        user = User.objects.get(id = user_id)
        return self.create(name = name, added_by = user)
    
    def addFav(self, item_id, user_id):
        user = User.objects.get(id = user_id)
        favI = self.get(id = item_id)
        user.favorites.add(favI)
        return user

    def removeFav(self, item_id, user_id):
        user = User.objects.get(id = user_id)
        favI = self.get(id = item_id)
        user.favorites.remove(favI)
        return user

    def deleteItem(self,item_id, user_id):
        itemToDelete = Item.objects.get(id = item_id)
        itemToDelete.delete()

    def validateNew(self,post):
        errors = {}
        if len(post['name']) < 3:
            errors['name'] = "Item name must be more than 3 characters long"
        return errors


    


class Item(models.Model):
    name = models.CharField(max_length = 255)
    added_by = models.ForeignKey(User, related_name = "items")
    wished_by = models.ManyToManyField(User, related_name = "favorites")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = itemManager()

    def __str__(self):
        return "Name: {}, added_by: {}, wished_by: {}".format(self.name, self.added_by, self.wished_by)
# Create your models here.
