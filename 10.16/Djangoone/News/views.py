from django.shortcuts import render
from News.models import Foods
from News.serializers import FoodSerializers
from  rest_framework import viewsets
from rest_framework import mixins
class Foods_View(mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet
                 ):
    queryset=Foods.objects.all()
    serializer_class=FoodSerializers


