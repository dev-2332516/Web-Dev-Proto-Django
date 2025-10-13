from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.TodoView.as_view(), name="todo-list"),
    path('newtodo', views.TodoFormView.as_view(), name="todo-form"),
    path('newcategory', views.CategoryFormView.as_view(), name="category-form"),
    path('deleteform/<int:id>', views.DeleteTodo, name='delete-todo'),
    path('completetodo/<int:id>', views.CompleteTodo, name='complete-todo'),
    path('uncompletetodo/<int:id>', views.UncompleteTodo, name='uncomplete-todo'),

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    # Password management
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='auth/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'), name='password_change_done'),
]
