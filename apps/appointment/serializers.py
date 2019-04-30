# -*- coding: utf-8 -*-

# @Time  : 2019/4/26

# @Author : Randolph Lu

# 序列化模型
from rest_framework import serializers
from .models import Appointment, DoctorSchedule
from users.models import Patient, Doctor
from hospital.models import Outpatient
from hospital.serializers import OutpatientSerializer
from users.serializers import DoctorSerializer


class AppointmentSerializer(serializers.Serializer):
    # 获取当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault
    )
    # patient是一个外键，可以通过这方法获取patient object中所有的值
    # patient = serializers.PrimaryKeyRelatedField(required=True, queryset=Patient.objects.all())
    # doctor = serializers.PrimaryKeyRelatedField(required=True, queryset=Doctor.objects.all())
    # outpatient = serializers.PrimaryKeyRelatedField(required=True, queryset=Outpatient.objects.all())
    appointment = serializers.PrimaryKeyRelatedField(required=True, queryset=Appointment.objects.all())

    def create(self, validated_data):
        patient = self.context["request"].user


    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Appointment
        fields = '__all__'


class DoctorScheduleSerializer(serializers.ModelSerializer):

    doctor = DoctorSerializer()
    outpatient = OutpatientSerializer()
    time_range = serializers.ChoiceField(choices=DoctorSchedule.TIME_RANGE, source="get_time_range_display")

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = DoctorSchedule
        fields = '__all__'
