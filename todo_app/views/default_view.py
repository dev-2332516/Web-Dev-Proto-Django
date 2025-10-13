from django.shortcuts import render, redirect
from django.views.generic.base import View

def CheckAuthenticated(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return None

class IndexView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('member/login')
        return render(request, "todo-list.html")