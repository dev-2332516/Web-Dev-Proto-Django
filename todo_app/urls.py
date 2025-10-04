from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="todo-list"),

    path('todo/newtodo', views.TodoFormView.as_view(), name="todo-form"),
    path('todo/deleteform/<int:id>', views.DeleteTodo, name='delete-todo'),
    path('todo/completetodo/<int:id>', views.CompleteTodo, name='complete-todo'),
    path('todo/uncompletetodo/<int:id>', views.UncompleteTodo, name='uncomplete-todo'),

    path('category/newcategory', views.CategoryFormView.as_view(), name="category-form"),
]
