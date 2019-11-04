from  django.http import HttpResponse
def func(request):
    str=""
    for i in range(1,10):
        str=""
        for j in range(1,i+1):
            str=str+("%s*%s=%s"(j,i,i*j))
        str+"</br>"
    return HttpResponse(str)