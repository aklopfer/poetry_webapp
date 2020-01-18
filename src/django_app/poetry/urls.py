# poetry/urls.py
from django.conf.urls import url
from django.urls import path
from poetry import views


urlpatterns = [
    path('', views.index, name='index'),
]
