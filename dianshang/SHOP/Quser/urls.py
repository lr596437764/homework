from django.urls import re_path
from django.urls import path
from django.urls import include
from Quser.views import *
urlpatterns = [
    #re_path(r"^$", index),
    path("register/", register),
    path("login/", login),
    path("index/", index),
    path("logout/", logout),
    path("forget_password/",forget_password),
    path("change_password/",change_password),
    path("get_celery/",get_celery),
]


urlpatterns += [
    path("profile/", profile),
    path("set_profile/", set_profile),



]