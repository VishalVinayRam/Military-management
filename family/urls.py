from django.urls import path

from ammon.views import *
from .views import *
from django.conf.urls import include

urlpatterns = [
    path('login/',regiement_logins,name="reg-login"),
    path('data/',dashboard,name="dashboard"),
    path('datas',dashboards,name="dashboards")

]