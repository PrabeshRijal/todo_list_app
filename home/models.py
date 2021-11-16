from django.db import models

# Create your models here.
class TodoList(models.Model):
    todoList = models.CharField(max_length=255)
    taskStart = models.DateTimeField(auto_now_add=True)
    taskEnd = models.DateTimeField()