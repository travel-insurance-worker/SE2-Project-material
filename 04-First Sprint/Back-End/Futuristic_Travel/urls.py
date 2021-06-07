"""Futuristic_Travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Futuristic_Travel.views import Main_page
from Futuristic_Travel.views import Login_page
from Futuristic_Travel.views import Show_firstPage
from Futuristic_Travel.views import tempPage
from Futuristic_Travel.views import Forget_page


urlpatterns = [
    path('',Show_firstPage.as_view()),
    path('login/',Login_page.as_view()),
    path('get_signin',Login_page.signin),
    path('tempPage/', tempPage.as_view()),
    path('login/forgot',Forget_page.as_view())


]
"""
    path('', Main_page.as_view()),
    path('get_bankNum', Main_page.CancelFunc),
    path('get_bankNum_change', Main_page.ChangeFunc)
"""