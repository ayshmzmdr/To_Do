from django.db import models
from django.contrib.auth.models import User

class ToDos(models.Model):
    account=models.ForeignKey(User,on_delete=models.CASCADE)
    todoName=models.CharField(max_length=100,unique=True)

class tasks(models.Model):
    todoName=models.ForeignKey(ToDos,on_delete=models.CASCADE)
    task=models.TextField()
    status=models.BooleanField(default=False)
