# encoding: utf-8

from django import forms
from sub_vrworld.models import UserProfile,  news
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('userImage',)
