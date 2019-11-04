from django.urls import re_path
from django.urls import path
from django.urls import include
from Qshop.views import *
urlpatterns = [
    path("add_goods/", add_goods),
    re_path(r"set_goods/(?P<id>\d+)/", set_goods),
    path("list_goods/",list_goods),
    path('goods/',GoodsView.as_view()),
    re_path(r"^goods/(?P<id>\d+)/", goods),
    re_path(r"^update_goods/(?P<id>\d+)/",update_goods),
    path('vue_list_goods/',vue_list_goods),
    path( "Example/", Example),
    re_path( r"change_goods/(?P<id>\d+)", change_goods),
    # path("change_goods", change_goods),

]
