# coding:utf-8
from django.shortcuts import render
from sub_vrworld.models import news
from sub_vrworld.forms import UserForm, ProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import MySQLdb
from django.db import connection, transaction
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html', {'home_active': True})


def user_login(request):  # 登陆
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse('/sub_vrworld/')
            else:
                errors.append('您的账号暂时无法使用')
                return render(request, 'login.html', {'errors': errors})
        else:
            errors.append('用户名或密码错误，请重试')
            return render(request, 'login.html', {'errors': errors})
    else:
        return render(request, 'login.html', {})


def new(request):
    news_list = []
    news_list1 = news.objects.order_by('-date')[:20]

    for one_news in news_list1:
        newsList = {}
        newsList['myurl'] = one_news.myurl
        newsList['picture'] = one_news.picture
        newsList['title'] = one_news.title
        newsList['date'] = one_news.date
        newsList['summary'] = one_news.summary

        news_list.append(newsList)  # 追加到news_list列表中
    # return render(request, 'sub_vrworld/zixun.html', {'news_list':
    # news_list})
    return render(request, 'zixun.html', {'news_list': news_list, 'news_active': True})


def new_1(request):
    news_list_1 = []
    news_list2 = news.objects.order_by('-date')[20:50]

    for one_news_1 in news_list2:
        newsList1 = {}
        newsList1['myurl'] = one_news_1.myurl
        newsList1['picture'] = one_news_1.picture
        newsList1['title'] = one_news_1.title
        newsList1['date'] = one_news_1.date
        newsList1['summary'] = one_news_1.summary

        news_list_1.append(newsList1)  # 追加到news_list列表中
    # return render(request, 'sub_vrworld/zixun.html', {'news_list':
    # news_list})
    return render(request, 'zixun1.html', {'news_list_1': news_list_1, 'news_active': True})


def videos(request):
    return render(request, 'video.html', {'videos_active': True})


def forvr(request):
    return render(request, 'forvr.html', {'forvr_active': True})


def register(request):  # 注册
    registered = False
    errors = []
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)  # 设置密码
            user.save()
            profile = profile_form.save(commit=False)  # 不保存
            profile.user = user

            if 'userImage' in request.FILES:  # 判断是否有上传头像
                profile.userImage = request.FILES['userImage']

            profile.save()  # 保存
            registered = True
        else:
            errors.append(user_form.errors)
            errors.append(profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'errors': errors, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/sub_vrworld/')
            else:
                return HttpResponse("Your itcastsubject account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
  
    logout(request)

  
    return HttpResponseRedirect('/sub_vrworld/')
