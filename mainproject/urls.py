"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls import include

urlpatterns = [
    path('',include('mainsite.urls')), #처음 메인화면으로 고정
    path('admin/', admin.site.urls), #관리자페이지 이동
    path('attendance_check/', include('attendance_check.urls')), #출석체크로 이동
    path('temperature_management/', include('temperature_management.urls')), #체온관리로 이동
    path('infectious_disease_information/',include('infectious_disease_information.urls')), #감염병 정보, 확진자 정보 안내로 이동
    path('vaccine_hospital/',include('vaccine_hospital.urls')) #백신 접종 병원 안내
]
