"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',showcustomer,name="showcustomer"),
    path('index/',showcustomer,name="showcustomer"),
    path('register/',registercustomer,name="registercustomer"),
    path('update/<int:id>',updatecustomer,name="updatecustomer"),
    path('updateReq/<int:id>',updateRecord,name="updateRecord"),
    path('delete/<int:id>',deletecustomer,name="deletecustomer"),
    path('login/',logincustomer,name="logincustomer")
]
