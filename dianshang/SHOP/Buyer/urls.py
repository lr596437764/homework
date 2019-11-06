from django.urls import re_path
from django.urls import path
from django.urls import include
from Buyer.views import *
urlpatterns = [
    re_path(r"goods/(?P<id>\d+)/",goods),
    path("goods_list/",goods_list),
    path(r"^$", index),
    path("index/", index),
    path("cart/", cart),
    path("login/", login),
    path("pay_order/",pay_order),
    path("get_pay/",get_pay),
    path("pay_result/", pay_result),
    path("pay_order/",pay_order),
    path("add_car/",add_car),
    path("user_center_info/",user_center_info),
    path("user_center_site/",user_center_site),

]