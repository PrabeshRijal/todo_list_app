from django.contrib import admin
from home.models import TodoList

# Register your models here.
@admin.register(TodoList)
class TodoList(admin.ModelAdmin):
    list_display = ["id", "todoList", "taskStart", "taskEnd"]