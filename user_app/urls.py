from django.urls import path
from . import views

app_name = 'user_app'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]
