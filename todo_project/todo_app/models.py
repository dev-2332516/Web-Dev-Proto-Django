from django.db import models

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="Nom")
    description = models.CharField(max_length=150, verbose_name="Description")
    isDone = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('id', 'name','description' ,'isDone')
        verbose_name = "todo"
        verbose_name_plural = "todo"
