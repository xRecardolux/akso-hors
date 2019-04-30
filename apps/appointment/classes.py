# -*- coding: utf-8 -*-

# @Time  : 2019/4/26

# @Author : Randolph Lu

# 对应VO前端展示对象


class Appointment:
    patient_name = ''
    doctor_name = ''
    outpatient = ''
    schedule_time = ''
    token_no = ''
    status = ''
    appointment_time = ''

    def __init__(self, pname, doctor):
        self.patient_name = pname,
        self.doctor_name = doctor
