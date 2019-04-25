from django.db import models
from datetime import datetime
from hospital.models import Outpatient
from users.models import Doctor, Patient

# Create your models here.


class DoctorSchedule(models.Model):
    """
    医生当日可预约时刻表模型
    """
    # 时间段
    TIME_RANGE = (
        (1, "08:00 - 09:00"),
        (2, '09:00 - 10:00'),
        (3, '10:00 - 11:00'),
        (4, '11:00 - 12:00'),
        (5, '12:00 - 14:00'),
        (6, '14:00 - 15:00'),
        (7, '15:00 - 16:00'),
        (8, '16:00 - 15:00'),
        (9, '17:00 - 18:00'),
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='医生')
    outpatient = models.ForeignKey(Outpatient, on_delete=models.CASCADE, verbose_name='门诊部')
    # 就诊时间段
    time_range = models.PositiveIntegerField(choices=TIME_RANGE, verbose_name='时间段')
    # 时刻表对应日期
    date = models.DateField(verbose_name='日期')
    # 剩余号量
    residual_num = models.IntegerField(verbose_name='剩余号量')

    class Meta:
        verbose_name = "时刻表"
        verbose_name_plural = verbose_name


class Appointment(models.Model):
    """
    患者预约模型
    """
    CONFIRMED = 1
    CANCELLED = 2
    WAITING = 3
    FAILURE = 4
    STATUS_CODES = (
        (CONFIRMED, '确认'),
        (CANCELLED, '取消'),
        (WAITING, '等待'),
        (FAILURE, '失效')
    )
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='患者')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='医生')
    outpatient = models.ForeignKey(Outpatient, on_delete=models.CASCADE, verbose_name='诊室')
    appointment = models.ForeignKey(DoctorSchedule, on_delete=models.CASCADE, verbose_name='预约时刻表')
    # 就诊码
    token_no = models.IntegerField(verbose_name='就诊码')
    status = models.PositiveIntegerField(choices=STATUS_CODES, verbose_name='状态')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = "预约就诊"
        verbose_name_plural = verbose_name
