from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, reverse


urlpatterns = [
    path('', views.home, name='home'),
    path('login_register/<str:log_or_reg>', views.login_register, name='login_register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/home.html'), name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]