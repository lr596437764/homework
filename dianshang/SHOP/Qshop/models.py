from django.db import models
from ckeditor.fields import RichTextField
from Quser.models import *



class GoodsTypeManager(models.Manager):
    def hello(self,id):
        return self.get(id=id).goods_set.all()[:4]


class GoodsType(models.Model):
    name=models.CharField(max_length=32)

    picture=models.ImageField(upload_to="SHOP/static/img",default="/qshop/img/1.jpg")
    objects=GoodsTypeManager()



class Goods(models.Model):
    name=models.CharField(max_length=32)
    price=models.FloatField()
    number=models.IntegerField(default=1)
    production=models.DateTimeField()
    safe_date=models.CharField(max_length=32)
    picture=models.ImageField(upload_to="Qshop/img",default="Qshop/img/a.jpg")
    description=RichTextField()
    #1上架 0下架
    statue=models.IntegerField(default=1)
    goods_type=models.ForeignKey(to=GoodsType,on_delete=models.CASCADE)
    goods_store=models.ForeignKey(to=Quser,on_delete=models.CASCADE)


