from django.db import models
class  Quser(models.Model):
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=32)
    user=models.CharField(max_length=32,null=True,blank=True)
    gender=models.CharField(max_length=8,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    picture=models.ImageField(upload_to="image")







