from django.urls import include
from django.contrib import admin
from django.urls import path
from django.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('Buyer/', include('Buyer.urls')),
    # path('Home/', admin.site.urls),
    path('Shop/', include('Shop.urls')),
]


