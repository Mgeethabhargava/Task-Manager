from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.custom_login, name='login'),
    path('logout/', views.logout, name='logout'),
]
