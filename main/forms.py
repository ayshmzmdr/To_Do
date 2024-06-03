from django import forms

class TodoForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'To-do name here'}),
        max_length=150,
        label=""
    )

class TaskForm(forms.Form):
    name_task = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Task here'}),
        max_length=250,
        label="",
        required=False
    )