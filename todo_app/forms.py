# forms.py
from django import forms
from .models import Todo
from .models import Category
from .models import UserProfile
from colorfield.forms import ColorField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()


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
            
class SignUpForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False, label="Profile Picture")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if hasattr(self, 'cleaned_data') and 'profile_picture' in self.cleaned_data:
                profile_picture = self.cleaned_data['profile_picture']
                if profile_picture:
                    user.profile.picture = profile_picture
                    user.profile.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
