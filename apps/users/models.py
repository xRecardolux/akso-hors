from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

from hospital.models import Department, Hospital, Outpatient
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
    mobile = models.CharField("电话", max_length=11, null=True, blank=True)
    email = models.EmailField("邮箱", max_length=100, null=True, blank=True)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.username


# 医生
class Doctor (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, verbose_name='账户')
    doctor_id = models.BigIntegerField(null=True, blank=True, verbose_name='医生工号')
    doctor_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='姓名')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='医院')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='科室')
    outpatient = models.ForeignKey(Outpatient, on_delete=models.CASCADE, verbose_name='诊室')
    introduction = models.TextField(max_length=500, null=True, blank=True, verbose_name='简介')
    attending = models.TextField(max_length=200, null=True, blank=True, verbose_name='主治范围')

    class Meta:
        verbose_name = "医生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.doctor_name


# 患者
class Patient (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, verbose_name='账户')
    patient_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='姓名')
    id_card = models.CharField(max_length=20, null=True, blank=True, verbose_name='身份证号')
    patient_card = models.CharField(max_length=20, null=True, blank=True, verbose_name='就诊卡号')

    class Meta:
        verbose_name = "患者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.patient_name


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField("验证码", max_length=10)
    mobile = models.CharField("电话", max_length=11)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
