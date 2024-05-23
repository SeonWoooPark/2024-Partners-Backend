from django.urls import path

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('url/create', views.url_create, name='url_create'),
]