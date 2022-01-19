from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# 내가 가입시킨 사용자가 몇명인지 궁금하면 auth_user 테이블을 보면 됌.
# 가입시킨 애들은 여기에 저장이 된다.
# Create your views here.

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
            return redirect('/users/signup')

def userlogin(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        return render(request, 'users/login.html',
                      {'loginForm':loginForm})

    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST) # 애먄 두개임
        if loginForm.is_valid():
            login(request, loginForm.get_user()) # 사용자가 입력한 아이디와 패스워드를 입력하는것
            return redirect('/board/list') # 로그인이 되면 리스트로
        else:
            return redirect('/users/login')

def userlogout(request):
    logout(request)
    return redirect('/users/logout')