from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.filter(parent=None)
    return render(request, 'todoapp/index.html', {'tasks': tasks})
