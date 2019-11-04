"""Djangoone URL Configuration

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
from django.urls import path ,re_path,include
from  Djangoone.views import *
from  Djangoone.shitu import *


urlpatterns = [
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    # path('about_us/',about_us),
    # path('index/',index),
    # path('add/',add),
    # path('addNews/',addNews),
    # path('addEditor/',addEditor),
    #path('cxb/',cxb),
    # re_path(r'news_con/(?P<id>\d+)/', news_con),
    #path('chaxun/',chaxun),
    #path('addFoodstype/',addFoodstype),
    # path('Post1/',Post1),
    # path('Post/',Post),
    #path('add_food_type/',add_food_type),
    #path('add_food/', add_food),
    #path('add_news/', add_news),
    #path('add_shop/', add_shop),
    #path('rE/', requestExample),
    #path('find_food/', find_food),
    #path('shop/',shop),
    #re_path(r'shop_con/(?P<id>\d+)', shop_con),
    #path('baocun/',baocun),
    #path('rE/',cxb),
    # path('food_name/',func),
    # path("shuju/",shuju),
    # path('yemian/', yemian),
    # path('ajx/', ajx),
    #path('fromchack/',fromchack),
    #path('form_check/',form_check),
   # path('p_form/', p_form),
   #  path('ym/', ym),
   #  path('ajx/',ajx),
   #  path("qinqiu/",qinqiu),
   #  path("ajx/",ajx),
    #path("from_check/",from_check),
    #path("endfromcheck/",endfromcheck),
    #path('p_from/
    #re_path(r'news/(?P<page>\d+)/',news),
    #path('setCookie/',setCookie),
    #path('delcook/',delcook),
    #re_path(r'news/(?P<page>\d+)/',news),
    # path('news/', news),
    # path('cx/',cx),
    # path('set_session/', set_session),
    # path('use_session/', use_session),
    # path('del_session/', del_session),
    # path('set_password/',set_password),
    # path('register/',register),
    #path('registers/', registers),
    path('index/', index),
    path('register/', register),
    path('login/',login),
    path('logout/',logout),
    #path('vue/',vue),
    re_path(r'news_con/(?P<id>\d+)',news),
    re_path(r'news/(?P<id>\d+)',news),
    path('meishi_con/',meishi_con),
    path('meishi/',meishi),
    path('about_us/',about_us),
    path('pinpai/',pinpai),
]


urlpatterns += [
    path("ajax_vue/",ajax_vue),

]




from django.views.decorators.csrf import csrf_exempt
urlpatterns += [
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('foods/', csrf_exempt(FoodView.as_view())),

]


from News.urls import router
urlpatterns+=router.urls