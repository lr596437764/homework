from django.shortcuts import render
from django.http import HttpResponseRedirect
from SHOP.viwes import *

def register(request):
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        error=""
        if vaild_user(email):
            error="当前用户存在"
        else:
            password=set_password(password)
            add_user(email = email,password=password)
            return HttpResponseRedirect("/Quser/login/")
    return render(request, "quser/register.html", locals())


def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=vaild_user(email)
        if user:
            db_password=user.password#????
            request_password=set_password(password)
            if db_password==request_password:
                response=HttpResponseRedirect('/Quser/index/')
                response.set_cookie("email",user.email)
                response.set_cookie("user_id",user.id)
                request.session["email"]=user.email
                return response
            else:
                error="密码错误"
        else:
            error="用户不存在"
    return render(request, "quser/login.html", locals())

def login_valid(func):
    def inner(request,*args,**kwargs):
        cookie_user=request.COOKIES.get("email")
        session_user=request.session.get("email")
        if cookie_user and session_user and cookie_user==session_user:
            user=Quser.objects.get(email=cookie_user)
            identity=user.identity
            if identity>=1:
                return func(request,*args,**kwargs)
            return HttpResponseRedirect("/Buyer/index/")
        else:
            return HttpResponseRedirect("/Quser/login/")
    return inner

@login_valid
def index(request):
    return render(request, "quser/index.html", locals())


def logout(request):
    response=HttpResponseRedirect("/Quser/login/")
    response.delete_cookie("email")
    response.delete_cookie("user_id")
    request.session.clear()
    return response

def forget_password(request):
    return render(request, "quser/forgot-password.html")


import smtplib
from email.mime.text import MIMEText
def sendMial(content, email):
    from SHOP.settings import MAIL_SENDER, MAIL_PASSWORD, MAIL_SERVER, MAIL_PORT
    content = """
    如果确认是本人修改密码，请点击下放链接进行密码修改
        <a href="%s">点击链接确认</a>
        """ % content
    print(content)
    message = MIMEText(content, "html", "utf-8")
    message["To"] = email
    message["From"] = MAIL_SENDER
    message["Subject"] = "修改密码"
    smtp = smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT)
    smtp.login(MAIL_SENDER, MAIL_PASSWORD)
    smtp.sendmail(MAIL_SENDER, [email], message.as_string())
    smtp.close()


def reset_password(request):
    if request.method=="POST":
        email=request.POST.get("email")
        if email and vaild_user(email):
            hash_code=set_password(email)
            content = "http://127.0.0.1:8000/Quser/change_password/?email=%s&token=%s" % (email, hash_code)
            try:
                sendMial(content,email)
            except Exception as e:
                print(e)
            print(content)
    return HttpResponseRedirect("/Quser/forget_password/")

def change_password(request):
    if request.method=="POST":
        email= request.COOKIES.get("change_email")
        password=request.POST.get("password")

        e = Quser.objects.get(email=email)
        e.password=set_password(password)
        e.save()
        return HttpResponseRedirect("/Quser/login")
    email=request.GET.get("email")
    token=request.GET.get("token")
    now_token=set_password(email)
    if vaild_user(email) and now_token==token:
        response=render(request, "quser/change_password.html")
        response.set_cookie("change_email",email)
        return response
    else:
        return HttpResponseRedirect("/Quser/forget_password")


from django.http import HttpResponse
from CeleryTask.tasks import add
def get_celery(request):
    x=1
    y=3
    add.delay(x,y)
    return HttpResponse("调用完成")

# from Quser.models import *
# @login_valid
# def profile(request):
#     user_email=request.COOKIES.get("email")
#     user=Quser.objects.get(email=user_email)
#     return render(request,"profile.html",{"user":user})

from Quser.models import Quser
@login_valid
def profile(request):
    user_email=request.COOKIES.get("email")
    user_data=Quser.objects.get(email=user_email)#在数据库中找出对应用户的所有数据
    return render(request, "quser/profile.html", {"user":user_data})


@login_valid
def set_profile(request):
    user_email=request.COOKIES.get("email")
    user=Quser.objects.get(email=user_email)
    if request.method=="POST":
        post_data=request.POST
        email=post_data.get("email")
        user_data = post_data.get("user")
        age = post_data.get("age")
        gender = post_data.get("gender")
        address = post_data.get("address")
        picture=request.FILES.get("picture")

        user.user=user_data
        user.email = email
        user.age = age
        user.gender = gender
        user. address =address
        user.picture=picture
        if picture:
            user.picture=picture
        user.save()
        return HttpResponseRedirect("/Quser/profile/")
    return render(request, "quser/set_profile.html", {"user":user})






