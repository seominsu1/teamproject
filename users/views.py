from turtledemo.chaos import g


from django.contrib import messages
from django.contrib.auth import login, logout, user_logged_in
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.messages.storage import session
import requests
import jwt
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from analytics.ga_api2 import get_all_data

import httplib2
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client import tools
import argparse


def get_accounts_ids(service):
    accounts = service.management().accounts().list().execute()
    ids = []
    props=[]
    tmp_id = ""
    properties=''
    if accounts.get('items'):
        for account in accounts['items']:
            tmp_id=account['id']
            ids.append(tmp_id)
        properties=service.management().webproperties().list(accountId=tmp_id).execute().get('items')
        # print(properties)
        for num in range(len(properties)):
            # print(num)
            if properties[num].get('id'):
                props.append(properties[num].get('defaultProfileId'))

    return ids, props

def get_page_data(props,start_date,end_date):
    ids = "ga:" + props[0]
    metrics = "ga:pageviews,ga:timeOnPage"
    dimensions = "ga:pagePath,ga:pageTitle"
    data = service.data().ga().get(
        ids=ids, start_date=start_date, end_date=end_date, metrics=metrics,
        dimensions=dimensions).execute()
    # return dict(
    #     data["rows"] + [["total", data["totalsForAllResults"][metrics]]])
    return data['rows']

def get_user_data(props,start_date,end_date):
    ids = "ga:" + props[0]
    metrics = "ga:users"
    dimensions = "ga:date"
    data = service.data().ga().get(
        ids=ids, start_date=start_date, end_date=end_date, metrics=metrics,
        dimensions=dimensions).execute()
    # return dict(
    #     data["rows"] + [["total", data["totalsForAllResults"][metrics]]])
    return data['rows']

def get_device_data(props,start_date,end_date):
    ids = "ga:" + props[0]
    metrics = "ga:users"
    dimensions = "ga:deviceCategory"
    data = service.data().ga().get(
        ids=ids, start_date=start_date, end_date=end_date, metrics=metrics,
        dimensions=dimensions).execute()
    # return dict(
    #     data["rows"] + [["total", data["totalsForAllResults"][metrics]]])
    return data['rows']



# ?????? ???????????? ???????????? ???????????? ???????????? auth_user ???????????? ?????? ???.
# ???????????? ????????? ????????? ????????? ??????.
# Create your views here.

import getpass


def base(request):
    return render(request, 'usersbase.html')

def main_page(request):
    return render(request, 'main.html')

 #?????? ???????????? ?????? ???????????? ??????
def signup(request):
    if request.method == "GET":
        signupForm = UserCreationForm()
        return render(request, 'users/signup.html',
                      {'signupForm':signupForm}) # ???????????? ???????????? html ??????????????? signupform??? ???????????????

    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid(): # ?????? ????????? ??????
            signupForm.save() # ?????? ????????? ??????
            return redirect('/users/login') #?????? ???????????? (????????? ???????????? ?????????)
        else:
            messages.info(request, '??????????????? ???????????? ????????????.')
            return redirect('/users/signup')

@csrf_exempt
def userlogin(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        return render(request, 'users/login.html',
                      {'loginForm':loginForm})

    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST) # ?????? ?????????
        if loginForm.is_valid():
            login(request, loginForm.get_user()) # ???????????? ????????? ???????????? ??????????????? ???????????????
            return redirect('/main') # ???????????? ?????? ????????????
        else:
            messages.info(request, '???????????? ??????????????? ???????????? ????????????.')
            return redirect('/users/login')

def userlogout(request):
        logout(request)
        return redirect('/main')


@login_required
def userpwchange(request):
    if request.method == "GET":
        pwchangeform = PasswordChangeForm(request.user)
        return render(request, 'users/pwchange.html',
                      {'pwchangeform':pwchangeform}) # ???????????? ???????????? html ??????????????? signupform??? ???????????????

    elif request.method == 'POST':
        pwchangeform = PasswordChangeForm(request.user, request.POST)
        if pwchangeform.is_valid():
            user = pwchangeform.save()
            update_session_auth_hash(request, user)
            return redirect('/users/login')
        else:
            pwchangeform = PasswordChangeForm(request.user)
            messages.info(request, '??????????????? ???????????? ????????????.')
            return render(request, 'users/pwchange.html', {'pwchangeform': pwchangeform})

@login_required
def userdelete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/main')
    return render(request, 'users/delete.html')

def kakao_api(request):
    return redirect('https://kauth.kakao.com/oauth/authorize?client_id=063c80f58fac2db741db46dc4b3d203e&redirect_uri=http://127.0.0.1:8000/oauth&response_type=code')
    # ???????????? ?????? ???????????? client_id = redierct_uri ?????? ?????? ???????????????.

def kakao_api1(request):
    print(request.GET.get('code'))  # ???????????? ???????????? ???
    headers = {"Content-Type": "application/x-www-form-urlencoded"}  # h???
    data = {"grant_type": 'authorization_code',
            'client_id': '063c80f58fac2db741db46dc4b3d203e',
            'redirect_uri': 'http://127.0.0.1:8000/oauth',
            'code': request.GET.get('code')}  # ????????????

    res = requests.post('https://kauth.kakao.com/oauth/token', data=data, headers=headers)

    token_json = res.json()
    access_token = token_json.get("access_token")
    profile_request = requests.get("https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"},)
    profile_json = profile_request.json()

    # kakao_account = profile_json.get("kakao_account")
    # email = kakao_account.get("email", None)

    kakao_id = profile_json.get("id")
    email = profile_json['kakao_account']['email']
    #kakao_id = profile_json['kakao_account']['id']

    if User.objects.filter(username=email).exists():
        user = User.objects.get(username=email)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/main')

    else:
        User(username=email, email=email,).save()
        User.objects.filter(username=email).exists()
        user = User.objects.get(username=email)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/main')

def staff_manage_page(request):
    page_data,user_data,device_data=get_all_data()

    #user data ?????? -> ????????????
    user_date=[]
    user_num=[]
    for row in user_data:
        user_date.append(str(row[0]))
        user_num.append(row[1])
    # print(user_date)

    #device data ?????? -> ????????????
    device_name=[]
    device_num=[]
    for row in device_data:
        device_name.append(row[0])
        device_num.append(row[1])
    print(device_name)

    return render(request, 'staff_index.html',{'user_date':user_date,'user_num':user_num,'device_name':device_name,'device_num':device_num,'page_data':page_data})





