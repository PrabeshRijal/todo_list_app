from django import forms
from django.db.models.fields import files
from django.forms import fields, widgets
from django import forms
from home.models import TodoList

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'
        widgets = {
            'todoList' : forms.TextInput(attrs={'class':'form-control', 'type':'text',  'placeholder':'Add Your Task....'}),
            'taskEnd' : forms.TextInput(attrs={'class':'form-control','type':'datetime-local'}),
        }