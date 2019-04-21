import xadmin

# Register your models here.

from .models import Hospital, Department


class HospitalAdmin(object):
    list_display = ["hospital_id", "hospital_name", "latitude", "longitude"]

    search_fields = ["hospital_name", ]


class DepartmentAdmin(object):

    list_display = ["department_name", ]


xadmin.site.register(Hospital, HospitalAdmin)
xadmin.site.register(Department, DepartmentAdmin)
