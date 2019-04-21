from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

from hospital.models import Department, Hospital
from django.conf import settings

# Create your models here.

# 用户登录注册
# @Author Randolph Lu
# @Date 2019-3-31


# 用户模型
class UserPro(AbstractUser):
    PATIENT = 1
    DOCTOR = 2
    HOSPITAL = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (PATIENT, '患者'),
        (DOCTOR, '医生'),
        (HOSPITAL, '医院'),
        (ADMIN, '管理员'),
    )
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
        ('O', '其他'),
    )
    role = models.PositiveSmallIntegerField('用户角色', choices=ROLE_CHOICES, null=True, blank=True)
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    full_name = models.CharField('姓名', max_length=100, null=True, blank=True)
    date_of_birth = models.DateField('出生年月', null=True, blank=True)
    mobile = models.CharField("电话", max_length=11)
    email = models.EmailField("邮箱", max_length=100, null=True, blank=True)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.username


# 医生
class Doctor (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    doctor_id = models.BigIntegerField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


# 患者
class Patient (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)


# 日程表
class DaySchedule (models.Model):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    DAYS = (
        (MONDAY, '周一'),
        (TUESDAY, '周二'),
        (WEDNESDAY, '周三'),
        (THURSDAY, '周四'),
        (FRIDAY, '周五'),
        (SATURDAY, '周六'),
        (SUNDAY, '周天'),
    )
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    day = models.PositiveSmallIntegerField(choices=DAYS)
    time_slot_from = models.TimeField()
    time_slot_to = models.TimeField()
