# forms.py
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=150)
    
    class Meta:
        model = Todo
        fields = ['name', 'description']
