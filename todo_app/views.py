from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import TodoForm
from .forms import CategoryForm
from .forms import SignUpForm
from .forms import UserProfileForm
from .models import Todo,UserProfile


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


# Auth Views
# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             try:
#                 auth_login(request, user)
#             except PermissionError:
#                 messages.error(request, 'Server cannot create session (PermissionError). Contact the administrator.')
#                 return render(request, 'auth/signup.html', {'form': form})
#             messages.success(request, f'Welcome {user.username}! Your account has been created.')
#             return redirect('todo-list')
#         messages.error(request, 'Please correct the errors below.')
#     else:
#         form = SignUpForm()
#     return render(request, 'auth/signup.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # ensure profile exists for this user (covers users created before signals were active)
            UserProfile.objects.get_or_create(user=user)
            try:
                auth_login(request, user)
            except PermissionError:
                messages.error(request, 'Server cannot create session (PermissionError). Contact the administrator.')
                return render(request, 'auth/signup.html', {'form': form})
            messages.success(request, f'Welcome {user.username}! Your account has been created.')
            return redirect('todo-list')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            try:
                auth_login(request, user)
                # ensure profile exists for this user (covers users created before signals were active)
                UserProfile.objects.get_or_create(user=user)
            except PermissionError:
                messages.error(request, 'Server cannot create session (PermissionError). Contact the administrator.')
                return render(request, 'auth/login.html', {'form': form})
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('todo-list')
        messages.error(request, 'Invalid username or password.')
    else:
        # pass request to the form (some auth backends expect it)
        form = AuthenticationForm(request)
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('todo-list')

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'auth/profile.html', {'form': form})
