from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('svod/', views.svod, name='svod'),
    path('short_page/', views.short_page, name='short_page'),
    # path('main_page/', views.main_page, name='main_page'),
    # path('form_complete/', views.form_complete, name='form_complete'),
    path('final_form/<uuid:secret>/', views.final_form, name='final_form'),
]
