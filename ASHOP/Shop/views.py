from django.shortcuts import render

def base(request):
    return render(request, "Shop/base.html", locals())
