from django.urls import path
from . import views

app_name = "playground"
#URLConf
urlpatterns=[
    path("",views.welcome_playground,name="playground"),
    path("hello/",views.say_hello,name="hello"),
    path("operations/",views.operation,name="operations"),
    path("operations/result/",views.get_result, name="result"),
    path("home/",views.base,name="home"),
    path("login/",views.login_page,name="login"),
    path("lobby/",views.login,name="lobby"),
    path("signup/",views.signup_page,name="signup"),
    path("signup/success",views.signup,name="success")
]
