from turtledemo.chaos import g

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.messages.storage import session
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



# 내가 가입시킨 사용자가 몇명인지 궁금하면 auth_user 테이블을 보면 됌.
# 가입시킨 애들은 여기에 저장이 된다.
# Create your views here.

import getpass

def home(request):
    return render(request, 'test.html')

def base(request):
    return render(request, 'usersbase.html')

def main_page(request):
    return render(request, 'main.html')

 #모든 함수보다 먼저 실행되는 함수
def signup(request):
    if request.method == "GET":
        signupForm = UserCreationForm()
        return render(request, 'users/signup.html',
                      {'signupForm':signupForm}) # 담아주고 담아준것 html 페이지에서 signupform을 반환해줌댐

    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid(): # 문제 있는지 검사
            signupForm.save() # 문제 없으면 저장
            return redirect('/users/login') #다시 돌아간다 (로그인 페이지가 없으니)
        else:
            messages.info(request, '비밀번호가 일치하지 않습니다.')
            return redirect('/users/signup')

@csrf_exempt
def userlogin(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        return render(request, 'users/login.html',
                      {'loginForm':loginForm})

    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST) # 애먄 두개임
        if loginForm.is_valid():
            login(request, loginForm.get_user()) # 사용자가 입력한 아이디와 패스워드를 입력하는것
            return redirect('/main') # 로그인이 되면 메인으로
        else:
            messages.info(request, '아이디와 비밀번호가 일치하지 않습니다.')
            return redirect('/users/login')

def userlogout(request):
        logout(request)
        return redirect('/main')


@login_required
def userpwchange(request):
    if request.method == "GET":
        pwchangeform = PasswordChangeForm(request.user)
        return render(request, 'users/pwchange.html',
                      {'pwchangeform':pwchangeform}) # 담아주고 담아준것 html 페이지에서 signupform을 반환해줌댐

    elif request.method == 'POST':
        pwchangeform = PasswordChangeForm(request.user, request.POST)
        if pwchangeform.is_valid():
            user = pwchangeform.save()
            update_session_auth_hash(request, user)
            return redirect('/users/login')
        else:
            pwchangeform = PasswordChangeForm(request.user)
            messages.info(request, '비밀번호가 일치하지 않습니다.')
            return render(request, 'users/pwchange.html', {'pwchangeform': pwchangeform})

@login_required
def userdelete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/main')
    return render(request, 'users/delete.html')

