from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodoView.as_view(), name="todo-list"),
    path('newtodo', views.TodoFormView.as_view(), name="todo-form"),
    path('newcategory', views.CategoryFormView.as_view(), name="category-form"),
    path('deleteform/<int:id>', views.DeleteTodo, name='delete-todo'),
    path('completetodo/<int:id>', views.CompleteTodo, name='complete-todo'),
]
