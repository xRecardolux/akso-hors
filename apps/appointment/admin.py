import xadmin

# Register your models here.
from .models import Appointment, DoctorSchedule


class DoctorScheduleAdmin(object):
    list_display = ["doctor", "outpatient", "time_range",
                    "date", "residual_num", ]


class AppointmentAdmin(object):
    list_display = ["patient", "doctor", "outpatient",
                    "appointment", "token_no", "status"]


xadmin.site.register(DoctorSchedule, DoctorScheduleAdmin)
xadmin.site.register(Appointment, AppointmentAdmin)
