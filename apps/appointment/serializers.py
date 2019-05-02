# -*- coding: utf-8 -*-

# @Time  : 2019/4/26

# @Author : Randolph Lu

# 序列化模型
from rest_framework import serializers
from .models import Appointment, DoctorSchedule
from users.models import Patient, Doctor
from hospital.models import Outpatient
from hospital.serializers import OutpatientSerializer
from users.serializers import DoctorSerializer, PatientSerializer


class DoctorScheduleSerializer(serializers.ModelSerializer):

    doctor = DoctorSerializer()
    outpatient = OutpatientSerializer()
    time_range = serializers.ChoiceField(choices=DoctorSchedule.TIME_RANGE, source="get_time_range_display")

    class Meta:
        model = DoctorSchedule
        fields = '__all__'


class ScheduleAppointmentSerializer(serializers.ModelSerializer):
    pass


class AppointmentSerializer(serializers.Serializer):
    # 获取当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault
    )
    # patient是一个外键，可以通过这方法获取patient object中所有的值
    # patient = Patient.objects.filter(user=user)
    # doctor = serializers.PrimaryKeyRelatedField(required=True, queryset=Doctor.objects.all())
    # outpatient = serializers.PrimaryKeyRelatedField(required=True, queryset=Outpatient.objects.all())
    doctor_schedule = serializers.PrimaryKeyRelatedField(required=True, queryset=Appointment.objects.all())

    def create(self, validated_data):
        user = self.context["request"].user


    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Appointment
        fields = '__all__'



