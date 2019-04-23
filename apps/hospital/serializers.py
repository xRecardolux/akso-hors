# -*- coding: utf-8 -*-

# @Time  : 2019/4/22

# @Author : Randolph Lu

from rest_framework import serializers
from .models import Hospital


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
