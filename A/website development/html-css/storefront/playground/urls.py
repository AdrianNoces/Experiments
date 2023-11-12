from django.urls import  path
from . import views


#UrlConf
urlPatterns = [

    path('hello/', views.say_hello)

]