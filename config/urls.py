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
from django.template.defaulttags import url
from django.urls import path, include
from django.views.generic import TemplateView

import app01.views
import restaurant.views
import users.views
import menu.views
import review.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/restInput', restaurant.views.rest_input),
    path('staff/menuInput/<bid>', restaurant.views.rest_menu_input),
    path('rest_detail/<bid>', restaurant.views.rest_detail),
    path('test', restaurant.views.home),
    path('rest_list', restaurant.views.rest_list),

    path('main', app01.views.main_page),                      # 메인페이지
    path('main/<str:cate>', app01.views.main_page_with_tag),  # 메인페이지에서 카테고리 눌렀을 때
    path('main/<str:cate>/<str:rest_title>', app01.views.main_page_with_rest_img),

    path('reviewRegister', review.views.register),
    path('reviewList', review.views.posts),
    path('reviewRead/<int:bid>', review.views.read),
    path('reviewDelete/<int:bid>', review.views.delete),

    path('users/test', users.views.home),
    path('usersbase', users.views.base),

    path('users/signup', users.views.signup),  # 가입

    path('users/login', users.views.userlogin),  # 로그인
    path('users/logout', users.views.userlogout),  # 로그아웃

    path('users/pwchange', users.views.userpwchange),  # 비밀번호 변경
    path('users/delete', users.views.userdelete),  # 회원탈퇴

    path('accounts/', include('allauth.urls')),
    path('kakao', users.views.kakao_api),  # 먼저 실행하면 토큰을 oauth라는 애한테 보냄
    path('oauth', users.views.kakao_api1),

    path('apitest',app01.views.apitest),

]

