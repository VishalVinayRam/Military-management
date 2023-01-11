from django.urls import path
from .views import *
from django.conf.urls import include

urlpatterns = [
    path('login/',login ,name="login"),
    path('/', index, name='index'),
    path('register/', register_solider, name='sol-register'),
    path('datas/',sol_data),
    path('holiday/',leave_letter)
    ]