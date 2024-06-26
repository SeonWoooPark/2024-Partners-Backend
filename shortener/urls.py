from django.urls import path

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('url/create/', views.url_create, name='url_create'),
    path('<str:hash_value>/', views.url_redirect, name='url_redirect'),
    path('url/check/', views.url_check, name='url_check'),
    path('url/delete/<str:hash_value>/', views.url_delete, name='url_delete'),
]