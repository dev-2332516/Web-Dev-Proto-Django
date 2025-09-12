from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import TodoForm

from .models import Todo


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class TodoView(View):
    def get(self, request):
        todo = Todo.objects.all()
        
        context = {
            'todos': todo,
        }
        return render(request, 'todo-list.html', context)
        
class TodoFormView(View):
    def get(self, request):
        form = TodoForm()
        return render(request, 'todo-form.html', {'form': form})
    
    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-list')
        return render(request, 'todo-form.html', {'form': form})

def DeleteTodo(request, id):
    deletedTodo = Todo.objects.get(id=id)
    deletedTodo.delete()
    
    return redirect('todo-list')

def CompleteTodo(request, id):
    completedTodo = Todo.objects.get(id=id)
    completedTodo.isDone = True
    completedTodo.save()
    
    return redirect('todo-list')