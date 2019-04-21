from django.db import models

# Create your models here.

from django.conf import settings


# 医院
class Hospital(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    hospital_id = models.BigIntegerField('医院id', null=True, blank=True)
    hospital_name = models.CharField('医院名', max_length=100)
    latitude = models.DecimalField('经度', max_digits=5, decimal_places=2, null=True, blank=True)
    longitude = models.DecimalField('纬度', max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = '医院信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hospital_name


# 科室
class Department(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    department_name = models.CharField('科室名称', max_length=50, unique=True)

    class Meta:
        verbose_name = '科室信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.department_name

