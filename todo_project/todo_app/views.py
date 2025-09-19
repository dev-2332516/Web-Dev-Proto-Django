from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import JsonResponse

from .forms import TodoForm
from .forms import CategoryForm
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
    
class CategoryFormView(View):
    def get(self, request):
        category = CategoryForm()
        return render(request, 'category-form.html', {'form': category})
    
    def post(self, request):
        categoryForm = CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('todo-list')
        return render(request, 'category-form.html', {'categoryForm': categoryForm})

def DeleteTodo(request, id):
    deletedTodo = Todo.objects.get(id=id)
    deletedTodo.delete()
    
    return redirect('todo-list')

def CompleteTodo(request, id):
    if request.method == 'POST':
        try:
            completedTodo = Todo.objects.get(id=id)
            completedTodo.isDone = True
            completedTodo.save()
            return JsonResponse({'status': 'success', 'message': 'Todo marked as done'})
        except Todo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Todo not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def UncompleteTodo(request, id):
    if request.method == 'POST':
        try:
            completedTodo = Todo.objects.get(id=id)
            completedTodo.isDone = False
            completedTodo.save()
            return JsonResponse({'status': 'success', 'message': 'Todo marked as done'})
        except Todo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Todo not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
