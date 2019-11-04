# from django import forms
# class UserFrom(forms.Form):
#     username=forms.CharField(max_length=12,min_length=6)
#     password=forms.CharField(
#         max_length=12,
#         min_length=6,
#         widget=forms.PasswordInput(attrs={"class":"title"}),
#         required=True,
#         label="密码",
#         error_messages={"required":"密码不能为空"}
#     )
#
#
# from django.forms import ModelForm
# from News.models import Foods
#
# # class UserForm(ModelForm):
# #     class Meta:
# #         model=Foods
# #         fields="__all__"
#
#
#
# class FoodsForm(ModelForm):
#     class Meta:
#         model=Foods
#         #ields=("name","price","description","picture")
#         fields = "__all__"
#         labels={
#             "name":"食品名称",
#             "price":"食品价格",
#             "picture":"食品图片",
#             "description":"食品描述",
#             "type_id":"食品类型",
#         }
#     def clean_name(self):#命名得规范 clean_
#         pool=["w","e"]
#         name=self.cleaned_data.get("name")
#         if name in pool:
#             self.add_error("name","ff")
#         else:
#             return name


from django import forms
class UserForm(forms.Form):#常规后端定义表单
    用户=forms.CharField(max_length=12,
                       min_length=6,
                       widget=forms.PasswordInput(attrs={"color":"red;"}),
                       required=True,
                       label="密码",
                       error_messages={"required":"密码不为空"},)
    密码=forms.CharField(max_length=12,min_length=6)


from django.forms import ModelForm
from News.models import Foods
class FoodsForm(ModelForm):#根据数据库定义表单
    class Meta:
        model=Foods
        fields="__all__"
        #fields = ("name","price","picture","description")
        labels={
            "name":"食品名称",
            "price": "食品价格",
            "picture": "食品图片",
            "description": "食品描述",
            "type_id": "食品类型",
        }
    def clean_name(self):#命名固定写法clean+下划线+字段名
        list=["admin","root"] #指定敏感词汇或正则
        name=self.cleaned_data.get("name")#获取指定字段数据
        if name in list :#判断数据与规则是否冲突
            self.add_error("name","ID已被占用")#若冲突返回error
        else:
            return name#不冲突返回原数据





