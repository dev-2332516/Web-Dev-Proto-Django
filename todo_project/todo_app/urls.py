from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('todo', views.TodoView.as_view(), name="todo-list"),
    path('newtodo', views.TodoFormView.as_view(), name="todo-form"),
    path('deleteform/<int:id>', views.DeleteTodo, name='delete-todo'),
    path('completetodo/<int:id>', views.CompleteTodo, name='complete-todo'),
]
