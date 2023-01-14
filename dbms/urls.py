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
from django.contrib.auth.views import *
from soliders.views import *
from terror.views import *
from django.conf.urls import include
from django.conf import settings
from family import urls as familyurls
from regiment import urls as regimenturls
from ammon import urls as ammourls
from terror import urls as terrorurls
from missions import urls  as missionurls
from django.contrib.auth import views as auth_views
from soliders import urls as solidersurls





urlpatterns = [
    path('admin/', admin.site.urls),
   path('famlily/',include(familyurls)),
    path('reg/',include(regimenturls)),
    path('ammo/',include(ammourls)),
    path('sol/',include(solidersurls)),
        path('mission/',include(missionurls)),
    path('ter/',include(terrorurls)),
    path('login/',loginUser,name="login"),
    path('',index,name="main_screen"),
    path('mains/',dashboards,name="dash_board"),
    path('register/',register_usere,name="register"),
    path('hoilday/',leave_letter),
    # patht
    # path('logout/',logouts,name="logout"),
    # path('login/',LoginView.as_view(template_name='forms/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name ="forms/logout.html"), name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
   path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),      
    


]
