from  django.http import HttpResponse

# def index(request):
#     return HttpResponse("刘浪")
#
#
# def func1(request):
#     return HttpResponse("<div style='height:400px;background-color:red;'>这我找谁说理去</div>")
#
# #def func(request,name):
#    str="<div><a href='https://lpl.qq.com/'>欢迎来到英雄联盟</a></div>"
#    return HttpResponse(str)

"""def func(request,day,month):
    str="你的生日为今年第%s"%(int(month)*30+int(day))
    return HttpResponse(str)
import time
def rq(request,month,day):

    str="天数%s"
    pass
for i in range(1,10):
    for j in range(1,i):"""


# import time
# def get_birthday(request,month,day):
#     birthday = time.mktime((2019, int(month), int(day), 0, 0, 0, 0, 0, 0))
#     dayth = time.localtime(birthday).tm_yday
#     html = """
#         <html>
#             <head>
#                 <title>
#                 </title>
#                 <style>
#         		 .content {
#                        color: red;
#                        text-align: center;
#                     }
#                 </style>
#             </head>
#             <body>
#                 <h1 align="center">算算你的生日是今年的第几天</h1>
#                 <p class='content'>%s</p>
#             </body>
#         </html>
#     """
#     string = "你的生日是 %s 月 %s 日,是今年的第%s天"%(month,day,dayth)
#     return HttpResponse(html%string)



"""def func(request):
    str=""
    for i in range(1,10):
        row=""
        for j in range(1,i+1):
            row=row+("{}*{}={}".format(j,i,i*j))
        str=str+row+"</br>"
    return HttpResponse(str)"""

# import random
# num=random.uniform(0,255)
# def func(request):
#
#     str = ""
#     for i in range(1, 10):
#         row = ""
#         for j in range(1, i + 1):
#             row = row + ("{}*{}={}".format(j, i, i * j))
#         str = str + row + "</br>"
#     html = """
#            <html>
#                <head>
#                    <title>
#                    </title>
#                    <style>
#            		 .content {
#                           color: rgb({},{},{});
#                           text-align: center;
#                        }
#                    </style>
#                </head>
#                <body>
#
#                    <p class='content'>%s</p>
#                </body>
#            </html>
#        """
#     return HttpResponse(.fromat(num,num,num),html%str)
#
#


# def cfb(request):
#     str="<table>"
#     for i in range(1,10):
#         str+="<tr>"
#         for j in range(1,i+1):
#             str+='<td>'+("{}*{}={}".format(j,i,i*j))+'<td>'
#         str+='<tr>'
#     str+='</table>'
#     html = """
#                 <html>
#                     <head>
#                         <title>
#                         </title>
#                         <style>
#                 		 .content {
#                                color: red;
#                                text-align: center;
#                             }
#                         </style>
#                     </head>
#                     <body>
#
#                         <b class='content'>%s</b>
#                     </body>
#                 </html>"""
#     return HttpResponse(html%str)
#
#
# from  django.http import HttpResponse
# from  django.template.loader import  get_template
# # def index_page(request):
# #     template=get_template("index.html")
# #     rsponse=template.render({"name":"z","other_name":12})
# #     return HttpResponse(request)
#
# from django.shortcuts import  render_to_response
# def  index_page(request):
#     name="laozhang"
#     list_nmae=[1,2,3,4]
#     tupl_name=(1,2,3,4)
#     dict_name={"a":1}
#     fun_name=lambda x:x
#     return render_to_response("index.html",locals())
#



from  django.http import HttpResponse
from  django.template.loader import  get_template
from django.shortcuts import  render_to_response
# class Example:
#     num=1
# def
# def index_page(request):
#     """
#     当前视图加载index.html,index.html的路径来源于settings当中的TEMPLATES配置
#     """
#     #加载前端页面
#     template = get_template("index.html") #加载的步骤
#     #将后端数据渲染到前端页面上
#     response = template.render(
#         {
#             "name":"laozhang",
#             "list_name":[1,2,3,4],
#             "tuple_name":(1,2,3,4),
#             "dict_name": {"a":1},
#             "fun_name": lambda x: x,
#
#          }
#     ) #渲染数据
#     #返回渲染结果
#     return HttpResponse(response) #返回一个响应，响应的内容时一个渲染的结果


from  django.http import HttpResponse
from  django.template.loader import  get_template
from django.shortcuts import  render_to_response
# def index_page(request):
#     template = get_template("index.html")
#     list=[
#         {"name":"张","age":18},
#         {"name": "李", "age": 19},
#         {"name": "赵", "age": 38},
#         {"name": "孙", "age": 28},
#         {"name": "周", "age": 18}
#     ]
#
#     return render_to_response("index.html",locfrom

from django.http import HttpResponse
from django.template.loader import get_template

# def index_pag(request):
#     template=get_template("index.html")
#     response=template.render()
#     return HttpResponse(response)


from django.http import HttpResponse
from django.template.loader import get_template

# def index_page(request):
#     template=get_template("index.html")
#     response=template.render({"name":"张","other_name":"边"})
#     return HttpResponse(response)

# from django.http import HttpResponse
# from django.template.loader import get_template
#
# class Example:
#     num=32
# def show(self):
#     print("头疼")
# def index_page(request):
#     template = get_template("index.html")
#     response = template.render(
#         {
#             "name": "laozhang",
#             "list_name": [1, 2, 3, 4],
#             "tuple_name": (1, 2, 3, 4),
#             "dict_name": {"a": 1},
#             "fun_name": lambda x: x,
#             "class_name": Example
#         }
#     )
#
#     return HttpResponse(response)

from django.http import HttpResponse
from django.template.loader import get_template
# def index_page(request):
#      template = get_template("index.html")
#      response = template.render(
#              {
#
#                  "dm": ["小米","糯米"],
#                  "dzy": ("黄豆","巴豆"),
#                  "r": ["牛肉","猪肉"],
#                  "dy": ["美元", "金条"],
#                  "yf":["上衣","裤子"]
#              } )
#
#      return HttpResponse(response)




#
# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.shortcuts import  render_to_response
# def index_page(request):
#     template = get_template("index.html")
#     list=[
#                 {"name":"张","age":18},
#                 {"name": "李", "age": 19},
#                 {"name": "赵", "age": 38},
#                 {"name": "孙", "age": 28},
#                 {"name": "周", "age": 18},
#             ]
#     number=2
#     dh=["首页","新闻","关于我们"]
#
#     return render_to_response("index.html",locals())
#
# def dog(request):
#
#     doglist=[
#         {"name": "哈士奇", "price": "100$", "tz": "拆家"},
#         {"name": "泰迪", "price": "100$", "tz": "怼"},
#         {"name": "萨摩耶", "price": "100$", "tz": "笑"},
#         {"name": "阿拉斯加", "price": "100$", "tz": "胖"},
#         {"name": "拉布拉多", "price": "100$", "tz": "傻"},
#     ]
#
#     return render_to_response("index.html",locals())


# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.shortcuts import  render_to_response
# def index_page(request):
#    meishi=[
#        {"name":"海鲜芝士大虾","price":"49元"},
#        {"name": "草莓布丁杯", "price": "12元"},
#        {"name": "菲力黑椒牛排", "price": "69元"},
#        {"name": "香煎排意面", "price": "69元"},
#        {"name": "鲜香培根披萨", "price": "59元"},
#
#    ]
#    return render_to_response("index.html", locals())
#

from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import  render_to_response


# def index_page(request):
#     dizhi=[
#         {"name":"北京朝阳区1","src":"/static/img/shop-pic1.jpg","pd":1},
#         {"name":"北京朝阳区2", "src": "/static/img/shop-pic2.jpg","pd":1},
#         {"name": "北京朝阳区3", "src": "/static/img/shop-pic3.jpg","pd":0},
#         {"name": "北京朝阳区4", "src": "/static/img/shop-pic4.jpg","pd":1},
#         {"name": "北京朝阳区5", "src": "/static/img/shop-pic5.jpg","pd":1},
#         {"name": "北京朝阳区6", "src": "/static/img/shop-pic6.jpg","pd":0},
#     ]
#     return render_to_response("sp.html", locals())


from django.shortcuts import  render_to_response
def lsdz1(request):

    product=[
        {"src":"images/pro1.jpg","name":"锻造绞线盘","explain":"法兰：——采用高强度的铝合金材料，经高压锻造程序，因此具有良好的刚性和耐久性。芯轴：——采用高强度的铝合金材料..."},
        {"src":"images/pro1.jpg","name":"锻造绞线盘", "explain": "法兰：——采用高强度的铝合金材料，经高压锻造程序，因此具有良好的刚性和耐久性。芯轴：——采用高强度的铝合金材料..."},
        {"src":"images/pro1.jpg","name": "锻造绞线盘", "explain": "法兰：——采用高强度的铝合金材料，经高压锻造程序，因此具有良好的刚性和耐久性。芯轴：——采用高强度的铝合金材料..."},
        {"src":"images/pro1.jpg","name": "锻造绞线盘", "explain": "法兰：——采用高强度的铝合金材料，经高压锻造程序，因此具有良好的刚性和耐久性。芯轴：——采用高强度的铝合金材料..."},
        {"src":"images/pro1.jpg","name": "锻造绞线盘", "explain": "法兰：——采用高强度的铝合金材料，经高压锻造程序，因此具有良好的刚性和耐久性。芯轴：——采用高强度的铝合金材料..."},
        {"src":"images/pro1.jpg","name": "锻造绞线盘", "explain": "法兰：——采用高强度的铝合金材料，经高压锻造程序，因此具有良好的刚性和耐久性。芯轴：——采用高强度的铝合金材料..."},
    ]
    return render_to_response("lsdz1.html", locals())



from django.shortcuts import  render_to_response
def lsdz2(request):
    return render_to_response("lsdz2.html", locals())


from django.shortcuts import  render_to_response
def lsdz3(request):
    list1 = [1,2,3,4,5,6]
    list2=[
        {"Jump":"首  页"},
        {"Jump": "产品中心"},
        {"Jump": "人才招聘"},
        {"Jump": "技术服务"},
        {"Jump": "联系我们"}
    ]
    return render_to_response("lsdz3.html", locals())


def lsdz4(request):
    list1=[
        {"id":"m1","href":"index.html","jump":"网站首页"},
        {"id":"m2","href":"about.html","jump":"关于我们"},
        {"id":"m3","href":"product_list.html","jump":"产品中心"},
        {"id":"m4","href":"/","jump":"服务支持"},
        {"id":"m5","href":"/","jump":"招贤纳士"},
         {"id": "m6","href":"contact.html ","jump":"联系我们"},
    ]
    list2 = [
        {"introduce": "公司名称:","details":"浙江戴卡宏鑫科技有限公司"},
        {"introduce": "所在地:","details":"浙江/台州市"},
        {"introduce": "联系人:","details":"徐小姐"},
        {"introduce": "联系方式:","details":"13906587665"},
        {"introduce": "注册资本:", "details": "94117600人民币"},
        {"introduce": "公司规模:", "details": "200-500人"},
        {"introduce": "注册年份:", "details": "2006年"},
        {"introduce": "公司类型:", "details": "企业单位制造商"},
        {"introduce": "公司地址:", "details": "浙江省台州市黄岩区经济开发区食品工业园三期"},
        {"introduce": "经营范围:", "details": "经编机配件"},
    ]


    list3 = [
        {"Jump": "首  页"},
        {"Jump": "产品中心"},
        {"Jump": "人才招聘"},
        {"Jump": "技术服务"},
        {"Jump": "联系我们"}
    ]


    return render_to_response("lsdz4.html", locals())



def lsdz5(request):
    list1 = [
        {"id": "m1", "href": "index.html", "jump": "网站首页"},
        {"id": "m2", "href": "about.html", "jump": "关于我们"},
        {"id": "m3", "href": "product_list.html", "jump": "产品中心"},
        {"id": "m4", "href": "/", "jump": "服务支持"},
        {"id": "m5", "href": "/", "jump": "招贤纳士"},
        {"id": "m6", "href": "contact.html ", "jump": "联系我们"},
    ]

    list2 = [
        {"Jump": "首  页"},
        {"Jump": "产品中心"},
        {"Jump": "人才招聘"},
        {"Jump": "技术服务"},
        {"Jump": "联系我们"}
    ]
    return render_to_response("lsdz5.html", locals())



from django.shortcuts import  render_to_response
def  news_con(request):
    return render_to_response("news-con.html", locals())


from django.shortcuts import  render_to_response
def  base(request):
    return render_to_response("base.html", locals())


from django.shortcuts import  render_to_response
def  shop_con(request):
    return render_to_response("shop-con.html", locals())