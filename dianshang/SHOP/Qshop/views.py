from django.shortcuts import render
from django.http import HttpResponseRedirect
from SHOP.viwes import *
from  Qshop.models import *



def add_goods(request):
    if request.method=="POST":
        post_data=request.POST
        name=post_data.get("name")
        price = post_data.get("price")
        number = post_data.get("number")
        production = post_data.get("production")
        safe_date = post_data.get("safe_date")
        picture= request.FILES.get("picture")
        description = post_data.get("description")

        goods=Goods()
        goods.name=name
        goods.price = price
        goods.number = number
        goods.production = production
        goods.safe_date = safe_date
        goods.description = description
        goods.picture = picture
        goods.statue=1
        goods.save()
        return HttpResponseRedirect("/Qshop/list_goods/")
    return render(request, "qshop/add_goods.html")

def list_goods(request):
    goods_list=Goods.objects.all()
    return render(request, "qshop/list_goods.html", locals())


def set_goods(request,id):
    set_type=request.GET.get("set_type")
    goods=Goods.objects.get(id=id)
    if set_type=="up":
        goods.statue=1
    elif set_type=="down":
        goods.statue=0
    goods.save()
    return HttpResponseRedirect("/Qshop/list_goods/")


def goods(request,id):
    goods_data=Goods.objects.get(id=int(id))
    return render(request, "qshop/goods.html", locals())


def update_goods(request,id):
    goods_data = Goods.objects.get(id=id)
    if request.method == "POST":
        post_data = request.POST
        name = post_data.get("name")
        price = post_data.get("price")
        number = post_data.get(" number")
        production = post_data.get("production")
        safe_date = post_data.get("safe_date")
        picture = request.FILES.get("picture")
        description = post_data.get("description")

        goods_data.name = name
        goods_data.price = price
        goods_data.number = 2
        goods_data.production = production.replace("年", "-").replace("月", "-").replace("日", "")
        goods_data.safe_date = safe_date
        goods_data.description = description
        goods_data.picture = picture
        goods_data.statue=1
        if picture:
            goods_data.picture = picture
        goods_data.save()
        return HttpResponseRedirect("/Qshop/goods/%s/"%id)
    return render(request,"Qshop/update_goods.html",locals())

from django.views import View
from django.http import JsonResponse
from django.core.paginator import Paginator
from SHOP.settings import PAZE_SIZE
class GoodsView(View):
    print(1111111)
    def get(self,request):
        result={
            "version":"v1",
            "code":"200",
            "data":[],
            "page_range":[],
            "referer":"",
        }
        id=request.GET.get("id")
        if id:
            goods_data=Goods.objects.get(id=int(id))#获取对相应id数据
            result["data"].append(
                {  "id":goods_data.id,
                   "name": goods_data.name,
                   "price": goods_data.price,
                   "number": goods_data.number,
                   "production": goods_data.production,
                   "safe_date": goods_data.safe_date,
                   "picture": goods_data.picture.url,
                   "description": goods_data.description,
                   "statue": goods_data.statue,
                   } )
        else:
            page_number=request.GET.get("page",1)#分页
            keywords=request.GET.get("keywords")
            all_goods=Goods.objects.all()

            if  keywords:#有关键词
                all_goods=Goods.objects.filter(name__contains=keywords)#模糊查询
                result["referer"]="&keywords=%s"%keywords
            print(all_goods)
            paginator=Paginator(all_goods,1)
            page_data = paginator.page(page_number)
            # page_data=paginator.page_range(page_number)#返回模糊查询的数据
            result["page_range"]=list(paginator.page_range)
            goods_data=[
                {
                    "id": g.id,
                    "name": g.name,
                    "price": g.price,
                    "number": g.number,
                    "production": g.production,
                    "safe_date": g.safe_date,
                    "picture": g.picture.url,
                    "description": g.description,
                    "statue": g.statue} for g in page_data
            ]
            result["data"]=goods_data
        return JsonResponse(result)
def vue_list_goods(request):
    return render(request,"Qshop/vue_list_goods.html")


def change_goods(request,id=0):
    type_list=GoodsType.objects.all()
    if id:
        goods_data=Goods.objects.get(id=id)
    else:
        goods_data=Goods()
    if request.method=="POST":
        post_data=request.POST
        name=post_data.get("name")
        price = post_data.get("price")
        number = post_data.get("number")
        production= post_data.get("production")
        safe_date = post_data.get("safe_date")
        description = post_data.get("description")
        picture = request.FILES.get("picture")
        goods_type=post_data.get("goods_type")

        goods_data.name=name
        goods_data.price = price
        goods_data.number = number
        goods_data.production = production.replace("年","-").replace("月","-").replace("日","")
        goods_data.safe_date =safe_date
        goods_data.description = description
        goods_data.goods_type=1
        goods_data.goods_type=GoodsType.objects.get(id=int(goods_type))
        store_id=request.COOKIES.get("email")
        goods_data.goods_store=Quser.objects.get(email=store_id)
        if picture:
            goods_data.picture=picture
        goods_data.save()
        return HttpResponseRedirect("/qshop/goods/%s"%id)
    return  render(request,"qshop/change_goods.html",locals())


def Example(request):
    method=dir(request)
    request.META.get("HTTP_PEFERER")

    # type_list = GoodsType.objects.all()
    # four_goods = GoodsType.objects.hello(1)
    return render(request,"Qshop/Example.html",locals())

