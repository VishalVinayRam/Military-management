"""dbms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from soliders.views import *
from terror.views import *
from django.conf.urls import include
from django.conf import settings
from family import urls as familyurls
from regiment import urls as regimenturls
from ammon import urls as ammourls
from terror import urls as terrorurls
from missions import urls  as missionurls
from soliders.views import dashboard




urlpatterns = [
    path('admin/', admin.site.urls),
   path('sol/',include(familyurls)),
    path('reg/',include(regimenturls)),
    path('ammo/',include(ammourls)),
        path('mission/',include(missionurls)),
    path('ter/',include(terrorurls)),
    # path('login/',login,name="login"),
    path('',index,name="main_screen"),
    path('mains/',dashboard,name="dash_board"),
    path('register/',register_usere,name="register"),
    # patht
    # path('logout/',logouts,name="logout"),
    path('login/',LoginView.as_view(template_name='forms/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name ="forms/logout.html"), name='logout'),

    


]
