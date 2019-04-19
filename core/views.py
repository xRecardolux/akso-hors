from django.shortcuts import render

# Create your views here.
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Akso医院预约挂号系统API')

urlpatterns = [
    url(r'^$', schema_view)
]