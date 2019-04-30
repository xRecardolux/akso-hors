from django.shortcuts import render
from rest_framework import mixins, viewsets
from .serializers import DoctorScheduleSerializer, AppointmentSerializer
from .models import DoctorSchedule, Appointment

# Create your views here.


class DoctorScheduleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = DoctorSchedule.objects.all()
    serializer_class = DoctorScheduleSerializer


class AppointmentViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
