from django.shortcuts import render
from django.http import HttpResponseRedirect
from Quser.views import *


def register(request):#先获取页面数据
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")

        if valid_user(email):
            error="邮件已经注册"
        else:
            password=set_password(password)
            add_user(email=email,password=password)

            # def add_user(**kwargs):
            #     user = Quser()
            #     user.password = kwargs["password"]
            #     user.email = kwargs["email"]
            #     user.save()


            return HttpResponseRedirect("/Shop/login/")
    return render(request,"shop/register.html",locals())

def login_valid(fun):
    def inner(request,*args,**kwargs):
        cookie_user=request.COOKIES.get("email")
        session_user=request.session.get("email")
        if cookie_user and session_user and cookie_user==session_user:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/Shop/login/")
    return inner




def login(request):#登录判断
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")


        user=valid_user(email)
        # def valid_user(email):
        #     try:
        #         user = Quser.objects.get(email=email)  # 判断数据库的email字段与表单是否一致
        #     except Exception as e:
        #         return False
        #     else:
        #         return user
        if user:
            db_password=user.password
            request_password=set_password(password)
            if db_password==request_password:
                response=HttpResponseRedirect("/Shop/")
                response.set_cookie("email",user.email)
                response.set_cookie("user_id",user.id)
                return response
            else:
                error="密码错误"
        else:
            error="查无此人"
    return render(request,"shop/login.html",locals())


@login_valid
def index(request):#首页
    return render(request,"shop/index.html",locals())

def reset_password(request):

    email=request.POST.get("email")
    if email and valid_user(email):
        hash_code=set_password(email)
        content="http://127.0.0.1:8000/shop/change_password/?email=%s&token=%s"%(email,hash_code)
        print(content)
    return HttpResponseRedirect("shop/forgot_password")
def forget_password(request):
    return HttpResponseRedirect(request,"shop/forgot_password.html")

def change_password(request):
    email=request.GET.get("email")
    token=request.GET.get("token")
    now_token=set_password(email)
    if valid_user(email) and token==now_token :
        return render(request,"shop/change_password.html")
    else:
        return HttpResponseRedirect("shop/forgot_password")
# import smtplib
# from email.mime.text import MIMEText
# def sendMial(content,email):
#     from Qshop.settings import MAIL_SENDER,MAIL_PASSWORD,MAIL_SERVER,MAIL_PORT
#     content="""
#     修改密码:<a href="%s" >点击链接<a>
#     """%content
#     print(content)
#     message=MIMEText(content,"html","utf-8")
#     message["TO"]=email
#     message["From"] = MAIL_SERVER
#     message["Subject"] = "密码修改"
#     smtp=smtplib.SMTP_SSL(MAIL_SERVER,MAIL_PORT)
#     smtp=login(MAIL_SENDER,MAIL_PASSWORD)
#     smtp.sendmail(MAIL_SENDER,[email],message.as_string())
#     smtp.close()
