from django.shortcuts import render
from django.views.generic.base import View

class IndexView(View):
    template_name = "todo-list.html"

    def get(self, request):
        return render(request, self.template_name)