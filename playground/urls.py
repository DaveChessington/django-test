from django.urls import path
from . import views

#URLConf
urlpatterns=[
    path("",views.welcome_playground),
    path("hello/",views.say_hello),
    path("operations/",views.operation),
    path("operations/result/",views.get_result, name="result"),
    path("home/",views.base) 
]
