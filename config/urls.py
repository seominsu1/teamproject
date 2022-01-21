"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path


import app01.views
import restaurant.views
import menu.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/restInput', restaurant.views.rest_input),
    path('staff/menuInput/<bid>',restaurant.views.rest_menu_input),
    path('rest_detail/<bid>', restaurant.views.rest_detail),
    path('test', restaurant.views.home),
    path('main', app01.views.main_page),
    path('testtest',restaurant.views.testtest),
    path('Tmon_star',restaurant.views.Tmon)
]