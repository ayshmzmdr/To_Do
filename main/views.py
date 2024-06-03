from django.shortcuts import render,redirect
from .forms import TodoForm,TaskForm
from django.contrib import messages
from .models import ToDos,tasks

def home(response):
    if response.method == "POST":
        if response.POST.get("login"):
            return redirect("login/")
        if response.POST.get("signup"):
            return redirect("signup/")    
    return render(response,"home.html",{})

def todo(response):
    user_todo=ToDos.objects.filter(account=response.user)
    user_todo_names=[filtered_todo.todoName for filtered_todo in user_todo]
    if response.method =="POST":
        form=TodoForm(response.POST)
        if response.POST.get("create"):
            if form.is_valid():
                tempname=form.cleaned_data["name"]
                ToDo=ToDos()
                ToDo.account=response.user
                ToDo.todoName=tempname
                ToDo.save()
                return redirect(".")
    else:
        form=TodoForm()
    return render(response,"todo.html",{"form":form,"todos":user_todo_names})

def tasktodo(response,name):
    temp=ToDos.objects.get(todoName=name)

    todo_item=tasks.objects.filter(todoName=temp)
    user_todo_names=[filtered_task.task for filtered_task in todo_item]
    user_todo_statuses=[filtered_task.status for filtered_task in todo_item]
    display=dict()
    for x,y in zip(user_todo_names, user_todo_statuses):
        display[x]=y

    if response.method == "POST":
        form=TaskForm(response.POST)
        if response.POST.get("newTask"):
            if form.is_valid():
                item=tasks()
                item.task=form.cleaned_data["name_task"]
                item.todoName=temp
                item.status=False
                item.save()
                return redirect(response.path_info)

        elif response.POST.get("updateTask"):
            for x in display.keys():
                doneTask=tasks.objects.get(todoName=temp,task=x)
                tempData=f"task{x}"
                mycheck=response.POST.get(tempData)
                if mycheck=="False":
                    doneTask.status = True
                    display[x]=doneTask.status
                    doneTask.save()
                elif mycheck==None:
                    doneTask.status = False
                    display[x]=doneTask.status
                    doneTask.save()
            return redirect(response.path_info)
    else:
        form=TaskForm()  
    return render(response,"tasks.html",{"form":form,"display":display})
