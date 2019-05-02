from django.db import models
from datetime import datetime

# Create your models here.

from django.conf import settings


class HospitalCategory(models.Model):
    """
    机构分级目录
    """
    hospital_Category_Type = (
        (1, "一级机构"),
        (2, "二级机构"),
        (3, "三级机构")
    )
    name = models.CharField('机构名', default="", max_length=30, help_text="机构名")
    code = models.CharField("机构code", default="", max_length=30, help_text="机构code")
    desc = models.TextField("机构描述", default="", help_text="机构描述")
    # 目录树级别
    category_type = models.IntegerField("机构级别", choices=hospital_Category_Type, help_text="机构级别")
    # 设置models有一个指向自己的外键
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE,
                                        null=True, blank=True,
                                        verbose_name="父机构级别", help_text="父机构", related_name="sub_cat")
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = "所属机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 医院
class Hospital(models.Model):

    """
    医院详情信息
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='账户')
    department_category = models.ForeignKey(HospitalCategory, on_delete=models.CASCADE,
                                            related_name='hospital', verbose_name='机构类别')
    hospital_name = models.CharField('医院名', max_length=100, null=True, blank=True)
    province = models.CharField('省', max_length=100, null=True, blank=True)
    city = models.CharField('市', max_length=100, null=True, blank=True)
    area = models.CharField('区', max_length=100, null=True, blank=True)
    address = models.CharField('地址', max_length=255, null=True, blank=True)
    latitude = models.DecimalField('经度', max_digits=5, decimal_places=2, null=True, blank=True)
    longitude = models.DecimalField('纬度', max_digits=5, decimal_places=2, null=True, blank=True)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '医院信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hospital_name


# 科室
class Department(models.Model):
    """
    医院下科室信息
    """
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='医院')
    department_category = models.ForeignKey(HospitalCategory, on_delete=models.CASCADE,
                                            related_name='department', verbose_name='机构类别')
    department_name = models.CharField('科室名称', max_length=50, null=True, blank=True)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        # 联合索引 限制医院出现两个同名科室
        unique_together = (
            ('hospital', 'department_name'),
        )
        verbose_name = '科室信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.department_name


# 门诊
class Outpatient(models.Model):
    """
    科室门诊部
    """
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='所属科室')
    department_category = models.ForeignKey(HospitalCategory, on_delete=models.CASCADE,
                                            related_name='outpatient', verbose_name='机构类别')
    outpatient_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='门诊名称')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        # 联合索引 限制同一医院下同一科室重复绑定门诊
        unique_together = (
            ('department', 'outpatient_name')
        )
        verbose_name = '门诊信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.outpatient_name



