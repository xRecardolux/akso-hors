"""hors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import xadmin
# from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from hospital.views import CategoryViewSet, HospitalView


router = DefaultRouter()
router.register(r'hospital', HospitalView, base_name='hospital')
router.register(r'category', CategoryViewSet, base_name='category')


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('login/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='Akso医院预约系统')),
    re_path('^', include(router.urls)),
    path('hospital/', HospitalView.as_view(), name='hospital-page'),

]
