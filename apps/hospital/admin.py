import xadmin

# Register your models here.

from .models import Hospital, Department, Outpatient, HospitalCategory


class HospitalAdmin(object):
    list_display = ["user", "hospital_name", "department_category",
                    "province", "city", "area", "address", "update_time"]
    list_filter = ["province", "city", "area"]
    search_fields = ["hospital_name", "province", "city", "area", ]


class DepartmentAdmin(object):

    list_display = ["hospital", "department_category", "department_name", "create_time", "update_time"]
    list_filter = ["hospital", "department_category", "department_name"]
    search_fields = ["hospital", "department_name"]


class OutpatientAdmin(object):
    list_display = ["department", "outpatient_name", "create_time", "update_time"]
    list_filter = ["department", "outpatient_name"]
    # search_fields = ["hospital", "department_name"]


class DepartmentCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "create_time", "update_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]


xadmin.site.register(Hospital, HospitalAdmin)
xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Outpatient, OutpatientAdmin)
xadmin.site.register(HospitalCategory, DepartmentCategoryAdmin)

