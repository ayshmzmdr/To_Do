from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("account/todo/",views.todo,name="todo"),
    path("account/todo/<str:name>",views.tasktodo,name="tasktodo")
]