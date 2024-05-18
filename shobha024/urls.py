"""
URL configuration for shobha024 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from shobha import views as s
admin.site.site_header = "WeCareU"
admin.site.site_title = "WeCareU"
admin.site.index_title = "Welcome to WeCareU"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cors/',include('course.urls')),
    path('fee/',s.paypython),
    path('p/',include('practice.urls')),
    path('',include('ap4.urls')),
    path('health/',include('healthcare.urls')),
    path('temp/',include('internallab.urls')),

]
