from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('create/',views.create,name = 'create'),
    path('vote/<str:pk>',views.view_poll,name = 'vote'),
    path('result/<str:pk>',views.result,name = 'result'),
    path('delete/<str:pk>/',views.delete_poll,name = 'delete_poll'),
]