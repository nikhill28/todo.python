from django.urls import path

from . import views

app_name="tasks" # namespacing  # it help uniqy identify taskss as index can be of other appss also
urlpatterns =[
    path("",views.index,name="index"),
    path("add",views.add,name="add_new_tasks")
]