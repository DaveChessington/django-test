from django.shortcuts import render
from django.http import HttpResponse

import database as db
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

def login_page(request):
    return render(request,"login.html")


def login(request): #Post Method
    error=None
    state=False
    try:
        user=request.POST.get("user")
        password=request.POST.get("password")
        if db.retrieve_user(user)["exists"]:
            if db.verify_credentials(user,password)["access_granted"]:
                state=True
            else:
                state=False
        else:
            state=False
    except Exception as e:
        error = str(e)
    return render(request, "lobby.html",{"state":state,"error":error})

def signup_page(request):
    return render(request,"signup.html")

def signup(request):
    try:
        name=request.POST["name"]
        user=request.POST["user"]
        password=request.POST["password"]
        reg=False
        if not db.retrieve_user(user)["exists"]:
            db.add_user(name,user,password)
            message="User Registered correctly"
            reg=True
        else:
            message="Awww! username already taken :("
    except Exception as e:
        message=f"Te following error(s) occurred:{e}"
    return render(request,"success.html",{"registered":reg,"message":message})