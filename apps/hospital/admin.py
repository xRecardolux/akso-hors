import xadmin

# Register your models here.

from .models import Hospital, Department, Outpatient, HospitalCategory


class HospitalAdmin(object):
    list_display = ["hospital_name", "latitude", "longitude"]

    search_fields = ["hospital_name", ]


class DepartmentAdmin(object):

    list_display = ["department_name", ]


class OutpatientAdmin(object):
    list_display = ["outpatient_name"]


class DepartmentCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "create_time", "update_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]


xadmin.site.register(Hospital, HospitalAdmin)
xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Outpatient, OutpatientAdmin)
xadmin.site.register(HospitalCategory, DepartmentCategoryAdmin)

