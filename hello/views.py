from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def anyone(request,name):
#     return HttpResponse(f"hello {name}  !!") #'f'. F-strings allow you to embed expressions inside string literals, using curly braces {} to enclose the expressions.


def index(request):
    return render(request,"hello/index.html")

def brian(request):
    return HttpResponse("hello brian")

def greet(request,name,branch): # taking name as an argument
    return render(request,"hello/greet.html",{
        "name":name.capitalize(),
        "bc":branch
        
    })


