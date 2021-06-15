"""Library URL Configuration

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
from .views import Create_View,List_View,Update_View,Delete_View,Registration_View,Login_page,Home_Page

urlpatterns = [
    path("create",Create_View,name="created"),
    path("list",List_View,name="listed"),
    path("update/<int:id>",Update_View,name="updated"),
    path("delete/<int:id>",Delete_View,name="deleted"),
    path("regis",Registration_View,name="regised"),
    path("login",Login_page,name="loged"),
    path("home",Home_Page,name="home"),
]
