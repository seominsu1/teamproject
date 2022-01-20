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

import users.views
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', users.views.home),
    path('usersbase', users.views.base),

    path('users/signup', users.views.signup), # 가입

    path('users/login', users.views.userlogin), # 로그인
    path('users/logout', users.views.userlogout), # 로그아웃

    path('users/pwchange', users.views.userpwchange), # 비밀번호 변경
    path('users/delete', users.views.userdelete), # 회원탈퇴
]
