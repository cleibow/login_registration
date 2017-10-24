from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'profile/(?P<item_id>\d+)$', views.displayUser),
    url(r'^removeFav/(?P<item_id>\d+)$', views.removeFav),
    url(r'^addFav/(?P<item_id>\d+)$', views.addFav),
    url(r'delete/(?P<item_id>\d+)$', views.delete),
    url(r'^create$', views.create),
    url(r'new$', views.newItem),
    url(r'^$', views.index)
]
