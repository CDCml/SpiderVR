#coding:utf-8
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime

# Create your models here.


class UserProfile(models.Model):  # 用户信息表
    user = models.OneToOneField(User)  # 与django自带的User表 OneToOne映射
    userGrade = models.IntegerField(default=1)  # 用户等级
    # 用户头像
    userImage = models.ImageField(
        upload_to='static/user_image', default='static/images/default.gif', blank=True, null=True)
    loginCount = models.IntegerField(default=1)  # 登陆次数
    lastLogin = models.DateTimeField(auto_now=True)  # 最后一次登陆时间
    likeCount = models.IntegerField(default=0)  # 点赞次数
    commentCount = models.IntegerField(default=0)  # 评论次数

    def __unicode__(self):
        return self.user.username


class news(models.Model):  # 新闻表
    myurl = models.CharField(max_length=256, null=True)  # 来源
    picture = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=128, unique=True)  # 标题
    date = models.CharField(max_length=100, null=True)  # 生成时间
    summary = models.CharField(max_length=100,unique=True)  # 概要

    def __unicode__(self):
        return self.newsTitle

