from django.shortcuts import render, redirect
from django.views.generic.base import View

from ..forms import CategoryForm


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