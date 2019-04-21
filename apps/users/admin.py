from django.contrib import admin

# Register your models here.
import xadmin
from xadmin import views
# from .models import Hospital, Department, Doctor, Patient


class GlobalSetting (object):
    # 设置后台管理标题
    site_title = 'Akso医院预约就诊管理后台'

    # 设置后台管理底部信息
    site_footer = '2019@中南民族大学计算机科学学院 鲁王兰夫'

    # menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)


class BaseSetting(object):
    # 启用主题管理器   
    enable_themes = True

    # 使用主题   
    use_bootswatch = True


# 注册主题设置
xadmin.site.register(views.BaseAdminView, BaseSetting)



# 医院
# class HospitalAdmin(object):
#     pass
#
#
# xadmin.site.register(Hospital, HospitalAdmin)
#
#
# # 医生
# class DoctorAdmin(object):
#     pass
#
#
# xadmin.site.register(Doctor, DoctorAdmin)
#
#
# # 科室
# class DepartmentAdmin(object):
#     pass
#
#
# xadmin.site.register(Department, DepartmentAdmin)
#
#
# # 患者
# class PatientAdmin(object):
#     pass
#
#
# xadmin.site.register(Patient, PatientAdmin)
