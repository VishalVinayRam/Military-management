from django.urls import path
from .views import *
from django.conf.urls import include

urlpatterns = [
    path('login/',terror_login,name="ter-login")
]