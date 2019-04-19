from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 用户登录注册
# @Author Randolph Lu
# @Date 2019-3-31


class User(AbstractUser):
    PATIENT = 1
    DOCTOR = 2
    HOSPITAL = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor'),
        (HOSPITAL, 'Hospital'),
        (ADMIN, 'Admin'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hospital_id = models.BigIntegerField(max_length=255, null=True, blank=True)
    hospital_name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    longitude = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.hospital_name


class Department(models.Model):
    department_id = models.ForeignKey(Hospital, on_delete=models.CASCADE, primary_key=True)
    department_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.department_name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    education = models.CharField(max_length=500)
    time_slot = models.DurationField()

    def __str__(self):
        return self.user.get_full_name()


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.get_full_name()

