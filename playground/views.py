from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request handler
#action


def say_hello(request):
    #return HttpResponse("Hello World")

    return render(request,"hello.html",{"name":"Mosh"})

def base(request):
    return render(request,"base.html")

def add(request): #GEt Method
    result=float(request.GET["n1"])+float(request.GET["n2"])
    return render(request,"result.html",{"result":result})

def login(request): #Post Method
    pass