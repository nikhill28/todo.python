from django.shortcuts import render

# Create your views here.

tasks=["learn","code","run"]

def index(request):
    return render(request,"tasks/index.html",{
             "tasks":tasks
    })

def add(request):
    return render(request,"tasks/add.html")
        
        
         
#when django is renderd , HTML teplate will access by , so django has acces to 
#to left side variable name tasks, taht has the value on the right 
#this value tasks take the value of above variable tasks