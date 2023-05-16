import datetime
from django.contrib import auth
from django.shortcuts import render, redirect
from app01.models import *


def login(request):
    return render(request, 'index.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('/')


def home(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'home.html', locals())


def user(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'user.html', locals())


def userinfo(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'userinfo.html', locals())


def admin_home(request):
    # 用户总数
    user_count = UserInfo.objects.count()

    # 数据总数
    job_count = Article.objects.count()

    # 评论总数
    comment_count = 3

    # 封面总数
    apply_job_count = 5

    # 主题总数
    signup_count = 28

    now = datetime.date.today()

    # 今日注册
    today_sign = UserInfo.objects.filter(
        date_joined__gte=now
    ).count()

    #  今日发布
    today_job = 0

    online_count = 1  # 在线人数
    return render(request, 'admin_home.html', locals())


def time(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'time.html', locals())