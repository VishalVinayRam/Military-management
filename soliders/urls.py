from django.urls import path
from .views import *
from django.conf.urls import include

urlpatterns = [
    path('login/',login ,name="login"),
    path('', index, name='index'),
    path('register/', register_usere, name='register'),
    ]