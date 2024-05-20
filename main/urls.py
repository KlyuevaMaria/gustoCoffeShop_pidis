from django.urls import path
from . import views
from django.urls import re_path


urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),

    path('menu', views.menu, name='menu'),

    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('basket', views.basket, name='basket'),
    path('register', views.register, name='register'),
    # path('login', LoginUser.as_view(), name='login'),
    path('login', views.LoginUser.as_view(), name='login'),

    # path('item', views.item, name='item'),
    # re_path(r'^(?P<name>[-\w]+)$',
    #         views.item,
    #         name='item'),
path('<str:menu>/<str:name>/', views.item, name='item')


]
