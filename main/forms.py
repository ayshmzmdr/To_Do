from django import forms

class TodoForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'To-do name here','style':'width: 350px;height:50px;'}),
        max_length=150,
        label=""
    )

class TaskForm(forms.Form):
    name_task = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Task here',"style":"width: 350px;height:50px;"}),
        max_length=250,
        label="",
        required=False,
    )