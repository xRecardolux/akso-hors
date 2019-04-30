# -*- coding: utf-8 -*-

# @Time  : 2019/4/22

# @Author : Randolph Lu

from rest_framework import serializers
from .models import Hospital, HospitalCategory, Department, Outpatient


class CategorySerializer3rd(serializers.ModelSerializer):
    """
    三级机构序列化
    """
    class Meta:
        model = HospitalCategory
        fields = '__all__'


class CategorySerializer2nd(serializers.ModelSerializer):
    """
    二级机构
    """
    sub_cat = CategorySerializer3rd(many=True)

    class Meta:
        model = HospitalCategory
        fields = '__all__'


class CategorySerializer1st(serializers.ModelSerializer):
    """
    一级机构
    """
    sub_cat = CategorySerializer2nd(many=True)

    class Meta:
        model = HospitalCategory
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    department_category = CategorySerializer1st()

    class Meta:
        model = Hospital
        exclude = ('user', )


class DepartmentSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer()
    department_category = CategorySerializer2nd()

    class Meta:
        model = Department
        fields = '__all__'


class OutpatientSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    department_category = CategorySerializer3rd()

    class Meta:
        model = Outpatient
        fields = '__all__'
