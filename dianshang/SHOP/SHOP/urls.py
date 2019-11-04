from django.views import *
from django.contrib import admin
from django.urls import path
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Quser/',include('Quser.urls')),
    path('Qshop/',include('Qshop.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('Buyer/', include('Buyer.urls')),
]
