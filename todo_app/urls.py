from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="todo-list"),

    path('todo/newtodo', view=TodoFormView.as_view(), name="todo-form"),
    path('todo/deleteform/<int:id>', view=DeleteTodo, name='delete-todo'),
    path('todo/completetodo/<int:id>', view=CompleteTodo, name='complete-todo'),
    path('todo/uncompletetodo/<int:id>', UncompleteTodo, name='uncomplete-todo'),

    path('category/newcategory', CategoryFormView.as_view(), name="category-form"),
]
