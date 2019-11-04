from django.db import models


# class NewsType(models.Model):
#     label = models.CharField(max_length = 32)
#     decription = models.TextField()
#     def __str__(self):
#         return self.label
#
# class Editor(models.Model):
#     name = models.CharField(max_length = 32)
#     email = models.EmailField()
#     def __str__(self):
#         return self.name
#
#
# class money(models.Model):
#     m1=models.IntegerField()
#     m2 = models.IntegerField()


# class News(models.Model):
#     title = models.CharField(max_length = 32,verbose_name="新闻标题")
#     time = models.DateField()
#     description = models.TextField()
#     image = models.ImageField(upload_to="img/upload")
#     content = models.TextField()
#     type_id = models.ForeignKey(to=NewsType,on_delete=models.CASCADE)
#     editor_id = models.ManyToManyField(to=Editor)
#     def __str__(self):
#         return self.title



# class Foods_type(models.Model):
#     label=models.CharField(max_length=32)
#     description=models.TextField()

# class Foods(models.Model):
#     name=models.CharField(max_length=32)
#     price=models.FloatField()
#     pircture=models.TextField()
#     type_id=models.Foreignkey(to=Foods_type,on_delete=models.CASCAD)

#
# class Shop(models.Model):
#     name=models.CharField(max_length=32)
#     picture=models.ImageField(upload_to="img")
#     foods_id=models.ManyToManyField(to = Foods)
#     open_time=models.CharField(max_length=32)
#     stop_car=models.charField(max_length=32)
#     address=models.TextField()
#     label=models.TextField()
#
# class Company(models.Model):
#     name = models.CharField(max_length=32)
#     picture = models.ImageField(upload_to="img")
#     phone = models.CharField(max_length=32)
#     fax = models.CharField(max_length=32)
#     stop_car = models.charField(max_length=32)
#     post_car = models.charField(max_length=32)
#     address = models.TextField()
#
# class News(models.Model):
#         title = models.CharField(max_length=32)
#         time = models.DateField()
#         description = models.TextField()
#         image = models.ImageField(upload_to="img/upload")
#         content = models.TextField()
#         type = models.CharField(max_length=32)
#


class Foods_type(models.Model):
    label = models.CharField(max_length = 32)
    description = models.TextField()

class Foods(models.Model):
    name = models.CharField(max_length = 32)
    price = models.FloatField()
    picture = models.ImageField(upload_to="img")
    description = models.TextField()
    type_id = models.ForeignKey(to=Foods_type,on_delete=models.CASCADE)

class Shop(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to="img")
    foods_id = models.ManyToManyField(to = Foods)
    open_time = models.CharField(max_length=32)
    stop_car = models.CharField(max_length=32)
    address = models.TextField()
    label = models.TextField()

class Company(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to="img")
    phone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    post_code = models.CharField(max_length=32)
    address = models.TextField()

# class News(models.Model):
#     title = models.CharField(max_length=32)
#     time = models.DateField()
#     description = models.TextField()
#     image = models.ImageField(upload_to="img/upload")
#     content = models.TextField()
#     type = models.CharField(max_length = 32)

from ckeditor.fields import RichTextField
class News(models.Model):
    title = models.CharField(max_length=32)
    time = models.DateField()
    description =RichTextField()
    image = models.ImageField(upload_to="img/upload")
    content = RichTextField()
    type = models.CharField(max_length = 32)
    def __str__(self):
        return self.title

class User(models.Model):
    name= models.CharField(max_length=32)
    password = models.CharField(max_length=32)


