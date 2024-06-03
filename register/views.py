from django.shortcuts import render,redirect
from . import forms

def signup(response):
    if response.method=="POST":
        form=forms.signupForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("../")
    else:
        form=forms.signupForm()
    return render(response,"signup.html",{"form":form})

def account(response):
    if response.method == "GET":
        if response.GET.get("ToDos"):
            return redirect("todo/")
    return render(response,"account.html",{})
