from django.shortcuts import  render_to_response
from News.models import *
from django.http import HttpResponse
from django.db.models import Max,Min,Count,Sum,Avg,F,Q



# def  about_us(request):
#     return render_to_response("about-us.html", locals())
#
#
# def  index(request):
#     return render_to_response("index.html", locals())
#
#
# def aboutus(request):
#     aboutus=News.objects.all()
#     return render_to_response("about-us.html", locals())
#
#
# def add(request):
    # new=NewsType()
    # new.label="ww"
    # new.decription="wwwww"
    # new.save()


#     new=NewsType(label="se",decription="wqwq")
#     new.save()
#     return HttpResponse("save success")
#
#
# def addNews(request):
#     new = News()
#     new.title="新闻标题"
#     new.time="1993-10-01"
#     new.description="描述"
#     new.image="wqeqewq"
#     new.content ="wqqeqweq"
#     new.type_id=NewsType.objects.get(id=1)
#     new.save()
#     new.editor_id.add(
#         Editor.objects.get(id=1)
#     )
#     new.save()
#     return HttpResponse("save success")
#
# def addEditor(request):
#     new=Editor()
#     new.name="李白"
#     new.email= "12313123@qq.com"
#     new.save()
#     return HttpResponse("save success")
#
#
#
# def cxb(request):
   # new=News.objects.all()
   #  news = News.objects.get(id=3)
   #  newlist=News.objects.filter(title="新闻标题",time="1993-10-01")
   # ne =News.objects.filter(title="新闻标题",time="1993-10-01").first()
    #n=News.objects.filter(title="新闻标题" ).last()
    # n = News.objects.filter(id__lt=2 )# id<2
    # n = News.objects.filter(id__lte=2)# id<=2
    # n = News.objects.filter(id__gt=2 )# id>2
    # n = News.objects.filter(id__gte=2 )# id>=2
    # n = News.objects.filter(id__in=[1,2,3])  # id in [1,2,3]
    # n = News.objects.filter(title__contains="标")  # 模糊查询
    # new = News.objects.all()#查所有
    # n = News.objects.order_by("id")#id正排序
    # n = News.objects.order_by("-id")  # id倒排序
    # n = News.objects.order_by("-id")[:2]#limit 分页
#外键查询
    # n=NewsType.objects.get(id=1).News_set.all()
    # e=News.objects.get(id=1).news_set.all()
    # e=Editor.object.get(id=1).news_set.all()
    #
    #
    # n=News.objects.get(id=1).news_set.all()#删
    # n.delete()
    #
    #
    # n = News.objects.get(id=9)#改
    # n.time="2019-01-21"
    # n.save()
    #
    #
    # new = News.objects.all()
    # new.update(time="2121-21-12")#只能批量改
    # new.save()
    #
    # return render_to_response("cx.html", locals())


#def chaxun(request):
    #new = News.objects.all()
    #news = News.objects.get(id=6)
    #news = News.objects.filter(title="新闻标题", time="1993-10-01")
    #news = News.objects.filter(id__in=[1,2,3,4]).first()
    #news = News.objects.filter(id__in=[1, 2, 3, 4]).last()
    #news = News.objects.filter(title="新闻标题")
    #news = News.objects.filter(title__contains="诸")
    #news= News.objects.order_by("id")
    #news = NewsType.objects.get(id=1).news_set.all()
    #news = Editor.objects.get(id=3).news_set.all()
    # news = NewsType.objects.get(id=1).news_set.all()
    # news.delete()
    # news = News.objects.get(title="新闻标题")
    # news.title= "吕布"
    # news.save()
    # new = not News.objects.get(id=2).all()
    #news=News.objects.raw("select * from auth_user")
    # news = News.objects.values(" title").all()
    #
    # return render_to_response("cx.html", locals())




# def chaxun(request):
#     news=News.objects.all().aggregate(
#         idavg=Avg("id"),idcount=Count("id"),idmax=Max("id")
#     )
#     return render_to_response("cx.html", locals())

# def chaxun(request):
#     news=News.objects.all().aggregate(
#         idavg=Avg("id"),idcount=Count("id"),idmax=Max("id")
#     )
#     return render_to_response("cx.html", locals())

# def chaxun(request):
#     news=money.objects.all().aggregate(
#         idavg=Avg("m1"),idcount=Count("m2"),idmax=Max("m2")
#     )
#     return render_to_response("cx.html",locals())



# def chaxun(request):
#
#     news=News.objects.all().annotate(t=Count("title")).valuse("title")
#
#     return render_to_response("cx.html", locals())


# def chaxun(request):
#     news=News.objects.values("title").annotate(Count("title"))
#     return  render_to_response("cx.html",locals())

# def chaxun(request):
#     news=News.objects.values("title").annotate(Max("description"))
#     return render_to_response("cx.html",locals())

# def chaxun(request):
#     news=money.objects.filter(m1__lt=F("m2"))#m1<m2的数据
#     return render_to_response("cx.html",locals())


# def chaxun(resquest):
#     news=money.objects.filter(id__gte=F("m1"))#id>=m1的数据
#     return render_to_response("cx.html",locals())

# def chaxun(request):
#     news=money.objects.all()
#     news.update(m1=F("m1")+100)
#     return render_to_response("cx.html",locals())


# def chaxun(request):
#     #news=News.objects.filter(title="喜洋洋",time="2019-10-10")#and
#     #news=News.objects.filter(Q(title="喜洋洋")|Q(time="2019-10-10"))#or
#     news=money.objects.all()
#     return render_to_response("cx.html",locals())


# def chaxun(request):  # 分组
#
#     news=News.objects.filter(id__it=3)
#
#     return render_to_response("cx.html", locals())
#
#
# class m(models.Model):#建工资表
#     pass
#     return render_to_response("cx.html", locals())
#
#
# class chaxun(request):
#    # news=News.objects.filter("title"= "曹操",id=3)#and
#     news = News.objects.filter(Q("title" = "曹操")|( id = 3))#or
#
#     return render_to_response("cx.html", locals())


# def index(request):
#     new=News.objects.all()
#     return render_to_response("index.html",locals())
#
#
# def news_con(request,id):
#     nr="%s假装有内容"%id
#     cont=News.objects.filter(id=int(id))
#
#
#     return render_to_response("news-con.html",locals())
#

# def addFoodstype(request):
#     fy=Foods_type()
#     fy.label="炒饭"
#     fy.description="蛋炒饭"
#     fy.save()
#     return HttpResponse("save success")
#
# def Shop(request):
#     shoop_list=Foods_type.object.all()
#     return render_to_response("shop.html",locals())


from django.shortcuts import  render
#def cxb(request):
    #re=dir(request)
    # date=request.GET.get("username")
    # d = request.GET.get("object")
    # da = request.GET.get("tj")
    # dat = request.GET.get("xb")
    # d=request.GET.get("username")
   #  if request.method=="POST":
   #     grgs=request.POST
   #  name=request.GET.get("name")#获取form表单数据,get请求,表单必须加name属性
   #  if name:
   #      date=Foods.objects.filter(name__contains=name)#Foods数据库模糊查询可渲染到html
   #  else:
   #      date="null"
   #  return render_to_response("cx.html",locals())



# from django.shortcuts import render
# def cxb(request):
#     if request.method=="POST":
#         a=request.POST
#         a1=a.get("username")
#         a2 = a.get("xb")
#         a3 = a.get("object")
#         a4 = a.get("tj")
#     return render(request,"cx.html",locals())

#
# def  Post1(request):
#     return render(request,"cx.html",locals())
#
#
# def Post(request):
#     if request.method=="POST":
#         argu=request.POST
#
#         u = argu.get("u")
#         g = argu.get("g")
#         p = argu.get("p")
#         return render(request,"cx.html",locals())
#
#
from django.shortcuts import  render_to_response
from News.models import *
from django.http import HttpResponse
from django.db.models import Max,Min,Count,Sum,Avg,F,Q
from django.http import  JsonResponse
# from django.shortcuts import render
# def requestExample(request):
#     return render(request,"cx.html",locals())
#
#
# def  find_food(request):
#     food_name=request.GET.get("food_name")
#     food_data = []
#     if food_name:
#         food_list=Foods.objects.filter(name__contains=food_name)
#         for i in food_list:
#             food_data.append({"name":i.name})
#     return JsonResponse({"food_data":food_data})


# from django.shortcuts import render
# def requestExample(request):
#     food_type_list = Foods_type.objects.values("id","label").all()
#     if request.method == "POST":
#         #接受数据
#         args = request.POST
#         name = args.get("name")
#         price = args.get("price")
#         description = args.get("description")
#         type_id = args.get("type_id")
#         picture = request.FILES.get("picture") #文件需要用request.FILES接受
#         #保存数据
#         food = Foods()
#         food.name = name
#         food.price = price
#         food.description = description
#         food.type_id = Foods_type.objects.get(id = int(type_id))
#         food.picture = picture
#         food.save()
#     return render(request,"test_request.html",locals())
#

# from django.http import JsonResponse
# from django.shortcuts import render
# def shuju(request):
#     return render(request,"cx.html",locals())
#
#
# def func(request):
#     food_name=request.GET.get("food_name")
#     food_data=[]
#     if food_name:
#         food_list=Foods.objects.filter(name__contains=food_name)
#         for i in food_list:
#             food_name.append({"name":i.name})
#     return JsonResponse({"food_data":food_data})



# from django.http import JsonResponse
# from django.shortcuts import render
# def shuju(request):
#     return render_to_response('cx.html',locals())
# def func(request):
#     food_name=request.GET.get("food_name")
#     food_data=[]
#     if food_name:
#         food_list=Foods.objects.filter(name__contains=food_name)
#         for f in food_list:
#             food_data.append({"name":f.name})
#     return JsonResponse({"food_data":food_data})


from django.shortcuts import render
from django.http import JsonResponse

# def yemian(request):
#     return render(request,"cx.html")
#
#
#
# def ajx(request):
#     result=""
#     if request.method=="POST":
#         name=request.POST.get("name")
#         result="你是%s"%name
#         return JsonResponse({"result":result})


from django.shortcuts import render
from django.http import JsonResponse

# def fromchace(request):
#     return render(request, "cx.html",locals())


# def shop(request):
#     shop_list=Shop.objects.all()
#     return render_to_response("shop.html",locals())
#
# def shop_con(request,id):
#     shop=Shop.objects.get(id=int(id))
#     foods_list=shop.foods_id.all()
#     return render_to_response("shop-con.html",locals())




#from django.shortcuts import  render
# def cxb(request):
#    # d=request.GET.get()
#     if request.method=="POST":
#        grgs=request.POST
#     return render(request,"cx.html",locals())
#

# def  form_check(request):
#     if request.method=="POST":
#         username=request.POST.get("username")
#         password=request.POST.get("password")
#         if username and password:
#             pass
#         else:
#             error="用户名不空"
#     return render(request,"cx.html")


# from django.shortcuts import  render
# from News.forms import *
# def p_form(request):
#     #userform=UserForm()
#     foodform=FoodsForm()
#     if request.method=='POST':
#         from_data=FoodsForm(request.POST,request.FILES)#图不在post
#         if from_data.is_valid():
#             request_data=from_data.cleaned_data
#             food =Foods()
#             food.name=request_data.get("name")
#             food.price=request_data.get("price")
#             food.price = request_data.get("picture")
#             food.price = request_data.get("description")
#             food.price = request_data.get("type_id")
#             food.save()
#         else:
#             errore=from_data.errors
#     return render(request,"cx.html",locals())
#
#
# from django.core.paginator import Paginator
# def news(request,page):
#     article_list=News.objects.order_by("-time")#按时间倒序分组
#     page_obj=Paginator(article_list,3)#进行分页
#     page_data=page_obj.page(int(page))#根据传入数字返回对应页
#     page_range=page_obj.page(int(page))#页面范围
#     return render(request,"news.html",locals())
#


# def combine_word_documents(files):
#     combined_document = Document('empty.docx')
#     count, number_of_files = 0, len(files)
#     for file in files:
#         sub_doc = Document(file)
#
#         # Don't add a page break if you've
#         # reached the last file.
#         if count < number_of_files - 1:
#             sub_doc.add_page_break()
#
#         for element in sub_doc._document_part.body._element:
#             combined_document._document_part.body._element.append(element)
#         count += 1
#
#     combined_document.save('combined_word_documents.docx')
#
# combine_word_documents(files)


# from docx import Document
# # 合并文档的列表
# files = ['1.docx', '2.docx']
# #合并操作
# def combine_word_documents(files):
#     merged_document = Document()
#
#     for index, file in enumerate(files):
#         sub_doc = Document(file)
#
#         # Don't add a page break if you've reached the last file.
#         if index < len(files)-1:
#            sub_doc.add_page_break()
#
#         for element in sub_doc.element.body:
#             merged_document.element.body.append(element)
#
#     merged_document.save('merged.docx')
#
# combine_word_documents(files)



# from django.shortcuts import render
# def baocun(request):
#     #d=request.GET.get()
#     if request.method=='POST':
#         a=request.POST
#         n=a.get("name")
#         p=a.get("price")
#         d=a.get("description")
#         t=a.get("type_id")
#         pi=request.FILES.get("picture")
#
#
#         f=Foods()
#         f.name=n
#         f.price=p
#         f.description=d
#         f.picture=pi
#         f.type_id=t
#         f.save()
#         return render(request,"cx.html",locals())
#





# def add_food_type(request):
#     type_list = ["经典牛排","意面/烩饭","风味披萨","甜品小食","酒水饮料","其他"]
#     for types in type_list:
#         t = Foods_type()
#         t.label = types
#         t.description = "%s 好吃不贵"%types
#         #t.save()
#     return HttpResponse("类型保存成功")
# #添加商品
# import random
# def add_food(request):
#     food_list = ["茶漱海鲜汤","玉米海螺沟","芝士蛋糕卷","芝士大虾","西冷牛排","草莓布丁杯","黑椒牛排","西红柿炒鸡蛋"]
#     for food in food_list:
#         t = Foods()
#         t.name = food
#         t.price = random.randint(1,400)
#         t.picture = "1.jpg"
#         t.description = "%s 好吃，有点小贵"%food
#         t.type_id = Foods_type.objects.get(id = random.randint(1,6))
#         t.save()
#     return HttpResponse("食品保存成功")
# #添加文章
import random
# def add_news(request):
#     address = ['石河子', '阿拉尔市', '图木舒克', '五家渠', '哈密', '吐鲁番', '阿克苏', '喀什', '和田', '伊宁', '塔城', '阿勒泰', '奎屯', '博乐', '昌吉', '阜康', '库尔勒', '阿图什', '乌苏']
#     for i in range(100):
#         news = News()
#         title = "贵族食代牛排%s餐厅开业"%random.choice(address)
#         news.title = title
#         news.time = "%s-%s-%s"%(
#             random.randint(1000, 3000),
#             random.randint(1, 12),
#             random.randint(1, 28)
#         )
#         news.description = title*10
#         news.image = "1.jpg"
#         news.content = title*50
#         news.type = "新闻资讯"
#         news.save()
#
#     return HttpResponse("文章保存成功")

# #添加文章
# def add_shop(request):
#     address = ['石河子', '阿拉尔市', '图木舒克', '五家渠', '哈密', '吐鲁番', '阿克苏', '喀什', '和田', '伊宁', '塔城', '阿勒泰', '奎屯', '博乐', '昌吉', '阜康', '库尔勒', '阿图什', '乌苏']
#     for i in range(100):
#         shop = Shop()
#         shop.name = "贵族食代牛排%s餐厅"%random.choice(address)
#         shop.picture = "1.jpg"
#         shop.open_time = "上午10:00-11:00 下午15:30-17:00"
#         shop.stop_car = "付费停车，30元/平米/小时/"
#         shop.address = random.choice(address)
#         shop.label = "法国菜,有包间,有车位,可刷卡,崇文区,地铁1号线,地铁2号线,地铁5号线,崇文门外大街,前门总医院,天坛,祈年殿,龙潭湖公园,北京体育馆,中央戏剧学院,崇文区儿童医院,新世界商场,北京站,新闻大厦,北京饭店,北京市政府,东交民巷,天安门,朋友聚会,家人就餐,谈情约会"
#         shop.save()
#         for i in range(random.randint(6,8)):
#             shop.foods_id.add(
#                 Foods.objects.get(id = random.randint(1,8))
#             )
#             shop.save()
#
#     return HttpResponse("店铺保存成功")
#

# from djangoimport  render_to_response
# from News.models import *
# from django.http import HttpResponse
# from django.db.models import Max,Min,Count,Sum,Avg,F,Q
# from django.http import  JsonResponse

# from django.http import JsonResponse
# def ym(request):
#     return render(request,"cx.html")
#
#
# def ajx(request):
#     HTML="<span style='color:red;'>牛</span>"
#     shop_list=[{"name":shop.name.replace("牛",HTML)} for shop in Shop.objects.all()]
#     return JsonResponse({"shop_list":shop_list})
#


# from django.shortcuts import render
# def qinqiu(request):
#     return render(request,"cx.html",locals())
#
# def ajx(request):
#     html="<span style='color:red;'>牛</span>"
#     shop_list=[{"name":shop .name.replace("牛",html)}for shop in Shop.objects.all()]
#     return JsonResponse({"shop_list":shop_list})

# from django.shortcuts import render
# def from_check(request):
#     return render(request,"cx.html")


# from django.shortcuts import render
# def endfromcheck(request):
#     if request.method=="POST":
#         user=request.POST.get("user")
#         password=request.POST.get("password")
#         if user and password :
#             pass
#         else:
#             error="用户名或密码不为空"
#     return render(request,"cx.html",locals())
#

# from django.shortcuts import render
# #导入后端定义的form表单
# #前端使用form.as_p,form.as_ul,form.as_table,for循环
# from News.forms import *#导入
# def p_from(request):
#     #userform=UserForm()#实例化
#     foodform=FoodsForm()
#     if request.method=="POST":
#         data=FoodsForm(request.POST,request.FILES)#获取数据
#         if data.is_valid():#校验数据
#             rqdata=data.cleaned_data#获取校验后的数据
#             food=Foods()#实例表
#             food.name=rqdata.get("name")
#             food.price = rqdata.get("price")
#             food.picture = rqdata.get("picture")
#             food.description = rqdata.get("description")
#             food.type_id =rqdata.get("type_id")
#             food.save()#存数据
#
#         else:
#             errors=data.errors
#     return render(request,"cx.html",locals())#传递到前端页面,通过路由

from django.shortcuts import render
# def news(request):
#     cookie_username = request.COOKIES.get("username")
#     article_list=News.objects.order_by("-time")
#     return render(request,"news.html",locals())


from django.shortcuts import render
from django.core.paginator import Paginator
# def setCookie(request):
#     response=render(request, "cx.html")#响应请求
#     response.set_cookie("username","eeeeeeqwqwqeeeeeeeeeeeeeeeeee")#设置cookie属性值
#     response.set_cookie("age", "19")
#     return response#返回携带cookie的响应
#
# def delcook(request):
#     response=render(request,"cx.html")
#     response.delete_cookie("username")#删除cookie username属性
#     return response#返回删除cookie 某属性的响应
#del删变量不删地址

# def news(request,page):
#     art=News.objects.order_by("-time")
#     obj=Paginator(art,3)
#     data=obj.page(int(page))
#     return render(request,"news.html",locals())


# def news(request):
#     return render(request,"news.html",locals())
# def cx(request):
#     return render(request,"cx.html",locals())



# from django.shortcuts import render
# def set_session(request):
#     request.session["username"]="zhangsan"
#     response=render(request,"cx.html")
#     return response
#
# def use_session(request):
#     session_username=request.session.get("username")
#
# def del_session(request):
#     session_username=request.session.get("username")
#     del request.session["username"]




# import hashlib
# def set_password(password):
#     md5=hashlib.md5()
#     md5.update(password.encode())
#     result=md5.hexdigest()
#     return result
#
# def register(request):
#     if request.method=='POST':
#         user=request.POST.get("user")
#         password = request.POST.get("password")
#         newuser=User()
#         newuser.name= user
#         newuser.password = set_password(password)
#         newuser.save()
#     return render(request,"register.html",locals())
#
#
# def index(request):
#     ckusername=request.COOKIES.get("username")
#     siusername=request.session.get("username")
#     if ckusername and ckusername and ckusername==ckusername:
#         news_list=News.objects.order_by('-time')[:8]
#         return render(request,"index.html",locals())
#     else:
#         return HttpResponseRedirect("/login/")
#
#
# from django.http import HttpResponseRedirect
# def login(request):
#     if request.method=="POST":
#         username=request.POST.get("user")
#         password=request.POST.get("password")
#         print(username,password)
#         user=User.objects.filter(name=username).first()#取出数据库字段name和username相当的数据
#         if user:
#             post_password=set_password(password)#加密表单的密码数据
#             if user.password==post_password:#比对表单的密码数据是否等于数据库的数据
#
#               response=HttpResponseRedirect("/index/")#都通过返回登录页面
#               response.set_cookie("username",user.name)#设置cookie
#               request.session["username"]=user.name
#               return response
#     return render(request,"login.html")

# def login(request):
#     if request.metod=="POST":
#         username=request.POST.get("name")
#         password = request.POST.get("password")
#         user=User.objects.filter(name=username).first()
#         if user:
#             post_password=set_password(password)
#             if user.password==post_password:
#                 response=HttpResponseRedirect("/index/")
#                 response.set_cookie("name",user.name)
#                 request.session["username"]=user.username
#                 return response
#     return render(request,"cx.html")

def logout(request):
    response=HttpResponseRedirect("/longin")
    response.delete_cookie("username")
    del request.session["username"]
    return response

# def loginValid(fun):
#     def inner(request,*args,**keywords):
#         cookie_username=request.COOKIES.get("name")
#         session_username=request.session.get("name")
#         if cookie_username and session_username and cookie_username==session_username :
#             return fun(request,*args,**keywords)
#         else:
#             return HttpResponseRedirect("cx")
#     return inner
# @loginValid
# def index(request):
#     news_list=News.objects.order_by("-time")[:8]
#     return render_to_response("index.html",locals())

# def loginValid(index):
#     def inner(request,*args,**kwargs):
#         cookie_username=request.COOKIES.get("username")
#         session_username=request.session.get("username")
#         if cookie_username and session_username and cookie_username==session_username:
#            return index(request,*args,**kwargs)
#         else:
#             return HttpResponseRedirect("/login/")
#     return inner
#
# @loginValid
# def index(request):
#     news_list=News.objects.order_by("-time")[:3]
#     return render_to_response("index.html",locals())
#
#
# def vue(request):
#     return render_to_response("text.html",locals())


def meishi_con(request,id):
    meishi=Foods.objects.get(id=int(id))
    return render_to_response("meishi-con.html",locals())

def meishi(request):
    return render(request,"meishi.html")

def  about_us(request):
     return render_to_response("about-us.html", locals())

def news(request):
    return render(request,"news.html")

def pinpai(request):
    return render(request,"pinpai.html")



import hashlib
def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


def register(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        password = request.POST.get("password")
        newuser = User()
        newuser.name = user
        newuser.password = set_password(password)
        newuser.save()
    return render(request, "register.html", locals())


def index(request):
    ckusername = request.COOKIES.get("username")
    siusername = request.session.get("username")
    if ckusername and ckusername and ckusername == ckusername:
        news_list = News.objects.order_by('-time')[:8]
        return render(request, "index.html", locals())
    else:
        return HttpResponseRedirect("/login/")


from django.http import HttpResponseRedirect
def login(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")
        print(username, password)
        user = User.objects.filter(name=username).first()  # 取出数据库字段name和username相当的数据
        if user:
            post_password = set_password(password)  # 加密表单的密码数据
            if user.password == post_password:  # 比对表单的密码数据是否等于数据库的数据

                response = HttpResponseRedirect("/index/")  # 都通过返回登录页面
                response.set_cookie("username", user.name)  # 设置cookie
                request.session["username"] = user.name
                return response
    return render(request, "login.html")



def ajax_vue(request):

    return render(request,"ajax_vue.html")