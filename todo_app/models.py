from colorfield.fields import ColorField
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, verbose_name="Prenom")
    lastName = models.CharField(max_length=50, verbose_name="Nom")
    profilePicture = models.ImageField()
    def __str__(self):
        return self.id
    class Meta: 
        ordering = ('id', 'firstName', 'lastName', 'profilePicture')
        verbose_name = "user"
        verbose_name_plural = "user"

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="category",
        null=True, blank=True)
    
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



