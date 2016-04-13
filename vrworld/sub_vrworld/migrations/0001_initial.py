# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('myurl', models.CharField(max_length=256, null=True)),
                ('picture', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(unique=True, max_length=128)),
                ('date', models.CharField(max_length=100, null=True)),
                ('summary', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userGrade', models.IntegerField(default=1)),
                ('userImage', models.ImageField(default=b'static/images/default.gif', null=True, upload_to=b'static/user_image', blank=True)),
                ('loginCount', models.IntegerField(default=1)),
                ('lastLogin', models.DateTimeField(auto_now=True)),
                ('likeCount', models.IntegerField(default=0)),
                ('commentCount', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
