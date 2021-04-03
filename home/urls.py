from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, reverse


urlpatterns = [
    path('', views.home, name='home'),
]