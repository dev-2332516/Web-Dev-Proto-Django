from colorfield.fields import ColorField
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="Nom")
    color = ColorField(default='#FF0000')
    # backgroundColor = hex_to_rgba(color)
    def __str__(self):
        return self.name
    
    class Meta: 
        ordering = ('id', 'name', 'color',)
        verbose_name = "categorie"
        verbose_name_plural = "categorie"

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="Nom")
    description = models.CharField(max_length=150, verbose_name="Description")
    isDone = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="todos", 
        null=True, blank=True
    ) 
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('id', 'name','description' ,'isDone')
        verbose_name = "todo"
        verbose_name_plural = "todo"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"



