from Quser.models import *
import hashlib
from django.http import HttpResponseRedirect
def set_password(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result




def valid_user(email):
    try:
        user=Quser.objects.get(email=email)#判断数据库的email字段与表单是否一致
    except Exception as e:
        return False
    else:
        return user

def add_user(**kwargs):
    user=Quser()
    user.password=kwargs["password"]
    user.email=kwargs["email"]
    user.save()

def updata_user(id,**kwargs):
    pass


def delete_user(id):
    pass

