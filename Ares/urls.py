"""Ares URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from cmdb import views
from django.conf.urls import url

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login_index/', views.login_index),
    url(r'^submit/', views.login),
    url(r'^flot/', views.flot),
    url(r'^morris/', views.morris),
    url(r'^tables/', views.tables),
    url(r'^forms/', views.forms),
    url(r'^panels/', views.panels),
    url(r'^buttons/', views.buttons),
    url(r'^notifications/', views.notifications),
    url(r'^typography/', views.typography),
    url(r'^icons/', views.icons),
    url(r'^grid/', views.grid),
]
