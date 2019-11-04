import hashlib
from Quser.models import *
def set_password(password):#加密
    md5=hashlib.md5()
    md5.update(password.encode())
    result= md5.hexdigest()
    return result


def vaild_user(email):#验证邮箱是否存在
    try:
        user=Quser.objects.get(email=email)
    except Exception as e:
        return False
    else:
        return user



def add_user(**kwargs):#添加用户
    if "email" in kwargs and "user"  not in kwargs:
        kwargs["user"]= kwargs["email"]
    user=Quser.objects.create(**kwargs)
    return user






