from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('form/', views.form, name='form'),
    path('example/', views.example, name='example'),

]