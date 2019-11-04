from django.urls import path,re_path
from Shop.views import *
urlpatterns=[
    re_path(r"^$",index),
    path("index/",index),
    path("register/",register),
    path("login/",login),
    path("logout/",login),
    path("forget_password/",forget_password),
    path("reset_password/",reset_password),
    path("change_password/",change_password),
]