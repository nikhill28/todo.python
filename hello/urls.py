from django.urls import path
from . import views   #from currnet directory(app- hello) import views

urlpatterns=[
    path("index",views.index, name="index") , # search for httl://127:0:0:1/hello  as in hello folder & co related in main projct url   #name is included to esily reference from other parts of application 
    path("<str:name>/<str:branch>", views.greet,name='greet'),
    path("brian/",views.brian, name="brian") # search for http://127.0.0.1:8000/hello/brian to get this
] 
