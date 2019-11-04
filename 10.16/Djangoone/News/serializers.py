from rest_framework import serializers
from  News.models import Foods
# class FoodSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=Foods
#         fields=["name","price","picture","description"]


class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model=Foods#序列化的模型
        fields=["name","price","picture","description"]#序列化返回的字段


