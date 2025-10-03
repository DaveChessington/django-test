from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request handler
#action

def welcome_playground(request):
    return render(request,"playground.html")

def say_hello(request):
    #return HttpResponse("Hello World")
    name=request.GET.get("name",0)
    return render(request,"hello.html",{"name":name})

def base(request):
    return render(request,"base.html")

def operation(request):
    return render(request,"operations.html")

def get_result(request):
    print(request.GET)
    operation=request.GET.get("operations")
    n1,n2=float(request.GET.get("n1",0)),float(request.GET.get("n2",0))

    match operation.lower():
        case "add":
            res=n1+n2
        case "substract":
            res=n1-n2
        case "multiply":
            res=n1*n2
        case "divide":
            res=n1/n2
    return render(request,"result.html",{"result":res})

def login(request): #Post Method
    pass