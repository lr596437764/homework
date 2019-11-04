from django.shortcuts import  render_to_response
from News.models import *
from django.http import HttpResponse
from django.db.models import Max,Min,Count,Sum,Avg,F,Q
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views import View
import json
# class FoodView(View):
#         def __init_(self,**kwargs):
#             super(FoodView,self).__init__()
#             self.result={
#                 "version": "v1.0",
#                 "code":200,
#                  "data":[
#
#                  ]
#             }
#         def get(self,request):
#             id=request.GET.get("id")
#             if id:
#                 try:
#                     data=Foods.objects.get(id=id)
#                 except Exception as e:
#                     self.result["code"]=500
#                     self.result["data"].append(str(e))
#                 else:
#                     d={"name":data.name,"price":data.price,"picture":data.picture.url,
#                      "description":data.description,"type":data.type_id.label}
#                     self.result["data"].append(d)
#             else:
#                 data = [{"name": data.name, "price": data.price, "picture": data.picture.url,
#                          "description": data.description, "type": data.type_id.label} for data in Foods.objects.all()]
#                 self.result["data"] = data
#             return JsonResponse(self.result)


# class FoodView(View):
#     def __init__(self,**kwargs):
#         super(FoodView,self).__init__()
#         self.result = {
#             "version": "v1.0",
#             "code": 200,
#             "data": [
#
#             ]
#         }
#     def get(self,request):
#         """
#         查询
#         """
#         id = request.GET.get("id")
#         #如果get请求由传递id,返回id对应的数据
#         #json格式无法封装python数据对象，所以要做数据转义
#         if id:
#             try:
#                 data = Foods.objects.get(id=id)
#             except Exception as e:
#                 self.result["code"] = 500
#                 self.result["data"].append(str(e))
#             else:
#                 d = {"name": data.name,"price": data.price,"picture": data.picture.url,"description": data.description,"type": data.type_id.label}
#                 self.result["data"].append(d)
#         #如果没有 id返回所有数据
#         else:
#             data = [{"name": data.name,"price": data.price,"picture": data.picture.url,"description": data.description,"type": data.type_id.label} for data in Foods.objects.all()]
#             self.result["data"] = data
#         return JsonResponse(self.result)

# from django.views import View
# class FoodView(View):
#     def __init__(self,**kwargs):
#         super(FoodView,self).__init__()
#         self.result={
#             "version":"1.0",
#             "code":200,
#             "data":[],
#         }
#     def is_exit(self,id):
#         try:
#             data=Foods.objects.get(id=id)
#         except Exception as e:
#             self.result["code"]=500
#             self.result["data"].append(str(e))
#             return False
#         else:
#             return data
#     def one_data(self,data):
#         d = {"name": data.name, "price": data.price, "picture": data.picture.url, "description": data.description,
#              "type": data.type_id.label}
#         self.result["data"].append(d)
#     def get(self,request):
#         id=request.GET.get("id")
#         if id:
#             data=self.is_exit(id)
#             if data:
#                 self.one_data(data)
#         else:
#                 data = [{"name": data.name, "price": data.price, "picture": data.picture.url,
#                         "description": data.description,
#                          "type": data.type_id.label} for data in Foods.objects.all()]
#                 self.result["data"]=data
#                 return  JsonResponse(self.result)
    # def post(self,request):
    #     post_data = request.POST
    #     name = post_data.get("name")
    #     price = post_data.get("price")
    #     picture = post_data.get("picture")
    #     description = post_data.get("description")
    #     type_id = post_data.get("type_id")
    #     foods = Foods()
    #     foods.name = name
    #     foods.price = price
    #     foods.picture = picture
    #     foods.description = description
    #     foods.type_id = Foods_type.objects.get(id=int(type_id))
    #     foods.save()
    #     self.one_data(foods)
    #     return JsonResponse(self.result)

    # def delete(self, request):
    #     delete_data = json.loads(request.body.decode())
    #     id = delete_data.get("id")
    #
    #     foods = self.is_exit(id)
    #     if foods:
    #         d = {
    #             "name": foods.name,
    #             "price": foods.price,
    #             "picture": foods.picture.url,
    #             "description": foods.description,
    #             "type": foods.type_id.label
    #         }
    #         self.result["data"].append(d)
    #         foods.delete()
    #     return JsonResponse(self.result)
# def post(self,request):
#     post_data= request.POST
#     name=post_data.get("name")
#     price=post_data.get("price")
#     pictur = post_data.get("pictur")
#     description = post_data.get("description")
#     type_id = post_data.get("type_id")
#     foods=Foods()
#     foods.name=name
#     foods.price = price
#     foods.pictur = pictur
#     foods.description = description
#     foods.type_id = Foods_type.objects.get(id=int(type_id))
#     foods.save()
#     self.one_data(foods)
#     return  JsonResponse(self.result)
#
# def put(self,request):
#     put_data=json.load(request.body.decode())
#     id=put_data.get("id")
#     name = put_data.get("name")
#     price = put_data.get("price")
#     pictur = put_data.get("pictur")
#     description = put_data.get("description")
#     type_id = put_data.get("type_id")

from django.http import JsonResponse
from django.views import View
import json
class FoodView(View):
    def __init__(self):
        super(FoodView,self).__init__()
        self.result={
            "version":"v1.0",
            "code":200,
            "data":[

            ]

        }

    def get(self,request):
        id=request.GET.get("id")
        if id:
            try:
                data=Foods.objects.get(id=id)
            except Exception as e:
                self.result["code"]=500
                self.result["data"].append(str(e))
            else:
                d = {"name": data.name,
                     "price": data.price,
                     "picture": data.picture.url ,
                    "description":data.description,
                     "type":data.type_id.label}
                self.result["data"].append(d)
        else:
            data=[{"name": data.name,
                     "price": data.price,
                     "picture": data.picture.url ,
                    "description":data.description,
                     "type":data.type_id.label}
                  for data in Foods.objects.all()]
            self.result["data"]=data
        return JsonResponse(self.result)



    def post(self,request):
        post_data=request.POST#
        price=post_data.get("name")
        name = post_data.get("price")
        picture = post_data.get("picture")
        description = post_data.get("description")
        type = post_data.get("type_id")
        foods=Foods()
        foods.name=name
        foods.price = price
        foods.picture = picture
        foods.description = description
        foods.type_id = Foods_type.objects.get(id=int(type))
        foods.save()
        d = {"name": foods.name,
             "price": foods.price,
             "picture": foods.picture.url,
             "description": foods.description,
             "type": foods.type_id.label}
        self.result["data"] .append(d)
        return JsonResponse({"data":"这是个post请求"})



    def put(self,request):#????????????????
        put_data=json.loads(request.body.decode())
        price = put_data.get("name")
        name = put_data.get("price")
        picture = put_data.get("picture")
        description = put_data.get("description")
        type = put_data.get("type_id")
        try:
            foods=Foods.objects.get(id=int(id))
        except Exception as e:
            self.result["code"] = 500
            self.result["data"].append(str(e))
        else:
            foods.name = name
            foods.price = price
            foods.picture = picture
            foods.description = description
            foods.type_id = Foods_type.objects.get(id=int(type))
            foods.save()
            d = {"name": foods.name,
                 "price": foods.price,
                 "picture": foods.picture.url,
                 "description": foods.description,
                 "type": foods.type_id.label}
            self.result["data"].append(d)
        return JsonResponse({"data":"这是个put请求"})




    def delete(self,request):
        delete_data=json.loads(request.body.decode())
        id=delete_data.get("id")
        try:
            foods=Foods.objects.get(id=int(id))
        except Exception as e:
            self.result["code"] = 500
            self.result["data"].append(str(e))
        else:
            d = [{"name": data.name,
                     "price": data.price,
                     "picture": data.picture.url,
                     "description": data.description,
                     "type": data.type_id.label}
                    for data in Foods.objects.all()]
            self.result["data"].append(d)
            foods.delete()
        return JsonResponse({"data":"这是个delete请求"})















# import requests
# url="http://127.0.0.1:8000/News/"
# # data={
# #     "Content-type":"application/json"
# # }
# data={
#     "name":"牛",
#     "price":"12",
#     "picture":"1.jpg",
#     "description":"解耦",
#     "type_id":"1",
# }
# respons= requests.post(url=url,data=data)












#import requests
# from lxml import etree
# import random
#
# url = "https://www.meishij.net/chufang/diy/"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
# }
#
# response = requests.get(url,headers=headers)
#
# html = etree.HTML(response.content.decode())
# name = html.xpath("//strong")
#
# url = "http://127.0.0.1:8000/foods/"
# data = {"name": "姜汁松花蛋", "price": "18", "picture": "1.jpg", "description": "蛋", "type_id": "1"}
#
# for n in name:
#     food_name = n.text
#     data["name"] = food_name
#     data["price"] = random.randint(20,100)
#     response = requests.post(url = url,data = data)
#     print(response.json())
#








