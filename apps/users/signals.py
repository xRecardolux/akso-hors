# -*- coding: utf-8 -*-

# @Time  : 2019/5/3

# @Author : Randolph Lu

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

User = get_user_model()


# post_save:接收信号的方式
# sender: 接收信号的model
@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()
