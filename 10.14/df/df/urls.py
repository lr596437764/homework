"""df URL Configuration

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
from django.urls import path ,re_path
from  df.views import *

"""urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('func1/',func1),
    re_path('get_birthday/(?P<month>\d{2})/(?P<day>\d{2})/',get_birthday),
    re_path()

]"""

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('func/',func)
    #path('cfb/',cfb),
    #path('index_page/',index_page),
    path('lsdz1/', lsdz1),
    path('lsdz2/', lsdz2),
    path('lsdz3/', lsdz3),
    path('lsdz4/', lsdz4),
    path('lsdz5/', lsdz5),
    path('news_con/', news_con),
    path('base/', base),
    path('shop_con/', shop_con),
    #path('dog/',dog),


]