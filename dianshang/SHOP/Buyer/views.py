from django.shortcuts import render
from django.http import HttpResponseRedirect
from Qshop.models import *
from Quser.views import vaild_user
from SHOP.viwes import set_password

2


def goods_list(request):
    id=request.GET.get("id")
    goods_list=Goods.objects.all()
    if id:
        goods_type=GoodsType.objects.get(id=int(id))
        goods_list=goods_type.goods_set.filter(statue=1)
    return render(request,"buyer/goods_list.html",{"goods_list":goods_list})


def goods(request,id):
    goods_data=Goods.objects.get(id=int(id))
    return render(request, "buyer/goods.html", locals())




# @login_valid
# def cart(request):
#     cookie_user=request.COOKIES.get("email")
#     session_user=request.session.get("email")
#     if cookie_user and session_user and cookie_user==session_user :
#         return render(request,"Buyer/cart.html")
#     else:
#         return HttpResponseRedirect("Buyer/login.html")




# def login(request):
#     set_referer=request.META.get("HTTP_REFERER")
#     if request.method=="POST":
#         email=request.POST.get("email")
#         password=request.POST.get("pwd")
#         user=vaild_user(email)
#         if user:
#             db_password=user.password#????
#             request_password=set_password(password)
#             if db_password==request_password:
#                 referer=request.POST.get("referer")
#                 response=HttpResponseRedirect(referer)
#                 response.set_cookie("email",user.email)
#                 response.set_cookie("user_id",user.id)
#                 request.session["email"]=user.email
#                 return response
#             else:
#                 error="密码错误"
#         else:
#             error="用户不存在"
#     return render(request, "Buyer/login.html", locals())

def login(request):
    referer=request.GET.get("referer")
    print(referer)
    if not referer:
        referer= request.META.get("HTTP_REFERER")
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("pwd")
        user=vaild_user(email)
        if user:
            db_password=user.password
            request_password=set_password(password)
            if db_password==request_password:
                if request.POST.get("referer"):
                    referer=request.POST.get("referer")
                if referer in ('http://127.0.0.1:8000/Buyer/login/',"None"):
                    referer="/"
                response=HttpResponseRedirect(referer)
                response.set_cookie("email",user.email)
                response.set_cookie("user_id",user.id)
                request.session["email"]=user.email
                return response
            else:
                error="密码错误"
        else:
            error="用户不存在"
    return render(request,"buyer/login.html",locals())


def login_valid(func):
    def inner(request,*args,**kwargs):
        referer=request.GET.get("referer")
        cookie_user=request.COOKIES.get("email")
        session_user=request.session.get("email")
        if cookie_user and session_user and cookie_user==session_user:
           return func(request,*args,**kwargs)
        else:
            login_url="/Buyer/login"
            if referer:
                login_url="/Buyer/login/?referer=%s"%referer
            return HttpResponseRedirect(login_url)
    return inner



def index(request):
    type_list=GoodsType.objects.all()
    return render(request,"Buyer/index.html",locals())



# @login_valid
# def cart(request):
#     return render(request, "Buyer/cart.html")


@login_valid
def cart(request):
    cookie_user=request.COOKIES.get("email")
    session_user=request.session.get("email")
    if cookie_user and session_user and cookie_user==session_user :
        return render(request,"Buyer/cart.html")
    else:
        return HttpResponseRedirect("Buyer/login.html")

def pay_order(request):
    return render(request,"buyer/place_order.html",locals())

def pay_result(request):
    data=request.GET
    return render(request,"buyer/pay_result.html",locals())

import time
def get_pay(request):
    order_number = str(time.time()).replace(".","")
    order_price = "998"
    url = Pay(order_number,order_price)
    return HttpResponseRedirect(url)


# from alipay import AliPay
# def Pay(order_id,money):
#     alipay_public_key_string='''-----BEGIN PUBLIC KEY-----
#     MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApWEWNqQ+VBaJt318LCZuBXaXXGvnT0tial+nh0kY0JCV3/fCFwCvA/sQ6WWccpq4Ao0K4U00Nk+AETC1ZXJkwzDxYGIA7pG8OmjyC7DQ+6vJWwVD8v+a1Y1K0EFMm6+x8r9aAZ4rY8cdxW1z9LSFaLiOVaelLxNAcmkITD1HfWjaIW9NBxFmbi6uxdQwQdycXhYiyTxmfL7cKIYmzQFIo4nCgfH1vK8t986gqEdIL
#     -----END PUBLIC KEY-----'''
#     app_private_key_string='''-----BEGIN RES PRIVATE KEY-----
#     MIIEowIBAAKCAQEApWEWNqQ+VBaJt318LCZuBXaXXGvnT0tial+nh0kY0JCV3/fCFwCvA/sQ6WWccpq4Ao0K4U00Nk+AETC1ZXJkwzDxYGIA7pG8OmjyC7DQ+6vJWwVD8v+a1Y1K0EFMm6+x8r9aAZ4rY8cdxW1z9LSFaLiOVaelLxNAcmkITD1HfWjaIW9NBxFmbi6uxdQwQdycXhYiyTxmfL7cKIYmzQFIo4nCgfH1vK8t986gqEdIL+Id0H07aBU/UOeU/Ual9NuZxYFF2P/UxcN5jnj9TQ0pCWMc3XscCvg4V288sBnzQS21yUpIWzlADjAcLwMr5BryxJ0/pDsv2pv/nJTAgcAVdQIDAQABAoIBAGRtnsWz273IqfzpkRxmge2DZMtVI3R9vNgIGn4HH7CX/MuzcwPxAFcUgeKaN/VIi3HRIMhMz+YjRQwrXhyq6RG3iP0UxqgZjAqUbFg5Gc+bNH23ptnL6sTANqxc2x64BQH6vbe5y3OeGTApFX+GmHVNjfHqCl+Z+0r/CXDyzZUTuiPtnydlQHkJoSF3R8AvfW9BIUvaXKsD6AvjS35FZrHWSGPTfdJOQcgjpLWN1VO+xJN2levfcGiZrJ7Ux1j3B33ZZ6U6klRfHZCNh0ovfdS34KYu+z7Dks6Opg+BxcRybl9OhF5HAsw1+vq8DVb6bk5L6J+criqMDuaBbDNWYAECgYEA46yRTrKJpFW5qjVYQWMtS1fAO+UvDgiYma5/72laaPKCSDHyLvhgUvOgOyHUOqXbcx7SaTdKVeDR8aYJb1+BaroiFQd1hjMppK5ZGpA9hWHqpxIBmcsCIlN/nG4aQ/a83/ucqwyosyGX1RFP3Z+0FOd8bD1t/C4wOMsX1n6r1AECgYEAufRsww4Dyknlgg4bnjxVdQds6e76CCeSzrTFHFmSpNOKJVNouyn3bLWk8Ro2hH3KdOdyvyJ3FPj+M/3BF0JElJ7c6REHCR8aUHv2uAPLgm977MUIG5bLZx2D3XSZBuZZm89RtZCrObtAr3jXklRAwJqqmoqfQzGSbTKDcemkMXUCgYBHAS/EImxI4y9nRQHESsD6iWB7jYtyTf4Bl+lwaiP3LQKyr1j/ixjHZhGnv3In5EgfjBJFHChDxjzTp1uz7042UdyFQHFHrDclk/ZYEXoOWi5LcpMrOqPsvqvCxpfMcGwRUrBWrDkEvMpUefS1grQv/M3SGApwJpuFatmBXLoMAQKBgQCq9vygANyfOX2XKx1dSB9Rr3gFREABC1FAVpb6z6exfwP9+UfK/HSNMBvrx6vj+DsRbFHlROyzDZG5f03t8nFXKw/0AEG1szDgWnilCmgrDhCjySsBIozzywEXtEGVRGeShvOauN2UAIMiUTnxQSEfc5Py7gwrHQKAY23xakmQKBgDsFjwrNBzzWE5OaBhNuB0+4oBoa6ENN5+QCz/Kg8jtl1RFUAGlFd80FCdcuC/cvZ3/70nSMRVUvitWgTX8jtb1n1DLzxd/TeOwL4sfadPrQECSdjp38GZ7UaKxELyxPX6MAGlzy04tYfBlFJ7MbWlRlJdeOuN79KJIHjcpOJI6j
#     -----END RES PRIVATE KEY-----'''
#     alipay=AliPay(
#         appid="2016092300574326",
#         app_notify_url="",
#         app_private_key_string=app_private_key_string,
#         alipay_public_key_string=alipay_public_key_string,
#         sign_type="RSA2",
#     )
#     order_string = alipay.api_alipay_trade_page_pay(
#         out_trade_no=order_id,
#         total_amount=str(money),
#         subject="商城",
#         return_url=None,
#         notify_url=None
#     )
#     return "https://openapi.alipaydev.com/gateway.do?" + order_string
# if __name__ == '__main__':
#     print(Pay("100000002", "1000"))


from alipay import AliPay
def Pay(order_id,money):
    alipay_public_key_string='''-----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApWEWNqQ+VBaJt318LCZuBXaXXGvnT0tial+nh0kY0JCV3/fCFwCvA/sQ6WWccpq4Ao0K4U00Nk+AETC1ZXJkwzDxYGIA7pG8OmjyC7DQ+6vJWwVD8v+a1Y1K0EFMm6+x8r9aAZ4rY8cdxW1z9LSFaLiOVaelLxNAcmkITD1HfWjaIW9NBxFmbi6uxdQwQdycXhYiyTxmfL7cKIYmzQFIo4nCgfH1vK8t986gqEdIL
    -----END PUBLIC KEY-----'''
    app_private_key_string='''-----BEGIN RES PRIVATE KEY-----
    MIIEowIBAAKCAQEApWEWNqQ+VBaJt318LCZuBXaXXGvnT0tial+nh0kY0JCV3/fCFwCvA/sQ6WWccpq4Ao0K4U00Nk+AETC1ZXJkwzDxYGIA7pG8OmjyC7DQ+6vJWwVD8v+a1Y1K0EFMm6+x8r9aAZ4rY8cdxW1z9LSFaLiOVaelLxNAcmkITD1HfWjaIW9NBxFmbi6uxdQwQdycXhYiyTxmfL7cKIYmzQFIo4nCgfH1vK8t986gqEdIL+Id0H07aBU/UOeU/Ual9NuZxYFF2P/UxcN5jnj9TQ0pCWMc3XscCvg4V288sBnzQS21yUpIWzlADjAcLwMr5BryxJ0/pDsv2pv/nJTAgcAVdQIDAQABAoIBAGRtnsWz273IqfzpkRxmge2DZMtVI3R9vNgIGn4HH7CX/MuzcwPxAFcUgeKaN/VIi3HRIMhMz+YjRQwrXhyq6RG3iP0UxqgZjAqUbFg5Gc+bNH23ptnL6sTANqxc2x64BQH6vbe5y3OeGTApFX+GmHVNjfHqCl+Z+0r/CXDyzZUTuiPtnydlQHkJoSF3R8AvfW9BIUvaXKsD6AvjS35FZrHWSGPTfdJOQcgjpLWN1VO+xJN2levfcGiZrJ7Ux1j3B33ZZ6U6klRfHZCNh0ovfdS34KYu+z7Dks6Opg+BxcRybl9OhF5HAsw1+vq8DVb6bk5L6J+criqMDuaBbDNWYAECgYEA46yRTrKJpFW5qjVYQWMtS1fAO+UvDgiYma5/72laaPKCSDHyLvhgUvOgOyHUOqXbcx7SaTdKVeDR8aYJb1+BaroiFQd1hjMppK5ZGpA9hWHqpxIBmcsCIlN/nG4aQ/a83/ucqwyosyGX1RFP3Z+0FOd8bD1t/C4wOMsX1n6r1AECgYEAufRsww4Dyknlgg4bnjxVdQds6e76CCeSzrTFHFmSpNOKJVNouyn3bLWk8Ro2hH3KdOdyvyJ3FPj+M/3BF0JElJ7c6REHCR8aUHv2uAPLgm977MUIG5bLZx2D3XSZBuZZm89RtZCrObtAr3jXklRAwJqqmoqfQzGSbTKDcemkMXUCgYBHAS/EImxI4y9nRQHESsD6iWB7jYtyTf4Bl+lwaiP3LQKyr1j/ixjHZhGnv3In5EgfjBJFHChDxjzTp1uz7042UdyFQHFHrDclk/ZYEXoOWi5LcpMrOqPsvqvCxpfMcGwRUrBWrDkEvMpUefS1grQv/M3SGApwJpuFatmBXLoMAQKBgQCq9vygANyfOX2XKx1dSB9Rr3gFREABC1FAVpb6z6exfwP9+UfK/HSNMBvrx6vj+DsRbFHlROyzDZG5f03t8nFXKw/0AEG1szDgWnilCmgrDhCjySsBIozzywEXtEGVRGeShvOauN2UAIMiUTnxQSEfc5Py7gwrHQKAY23xakmQKBgDsFjwrNBzzWE5OaBhNuB0+4oBoa6ENN5+QCz/Kg8jtl1RFUAGlFd80FCdcuC/cvZ3/70nSMRVUvitWgTX8jtb1n1DLzxd/TeOwL4sfadPrQECSdjp38GZ7UaKxELyxPX6MAGlzy04tYfBlFJ7MbWlRlJdeOuN79KJIHjcpOJI6j
    -----END RES PRIVATE KEY-----'''
    alipay=AliPay(
        appid="2016092300574326",
        app_notify_url="",
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",
    )
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_id,
        total_amount=str(money),
        subject="商城",
        return_url=None,
        notify_url=None
    )
    return "https://openapi.alipaydev.com/gateway.do?" + order_string
if __name__ == '__main__':
    print(Pay("100000002", "1000"))


from Buyer.models import *
from django.http import JsonResponse

def add_car(request):
    result={"state":"error","data":""}
    if request.method=="POST":
        user=request.COOKIES.get("email")
        goods_id=request.POST.get("goods_id")
        number=request.POST.get("number",1)
        try:
            goods=Goods.objects.get(id=goods_id)
        except Exception as e:
            result["data"]=str(e)
        else:
            car=BuyCat()
            car.car_user=user
            car.goods_name=goods.name
            car.goods_picture=goods.picture
            car.goods_price=goods.price
            car.goods_number=number
            car.goods_total=number*goods.price
            car.goods_store=goods.goods_store.id
            car.save()
            result["state"]="success"
            result["data"]="加入购物车成功"
    return JsonResponse(result)












