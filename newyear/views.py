from django.shortcuts import render
import datetime


# Create your views here.

def index(request):
    today= datetime.datetime.now()

    return render(request,'newyear/index.html',{
        'newyear':today.month==1 and now.day==1
     })