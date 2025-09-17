# forms.py
from django import forms
from .models import Todo
from .models import Category
from colorfield.forms import ColorField

class TodoForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=150)
    

    class Meta:
        model = Todo
        fields = ['name', 'description', 'category']

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    color = ColorField(initial="#FF0000")

    class Meta:
        model = Category
        fields = ['name', 'color',]
        widgets = {
                   'name': forms.TextInput(attrs={'class': 'form-control'}),
               }
