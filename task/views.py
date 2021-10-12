from django.db import models
from django.shortcuts import redirect, render
from .models import Task 

# Create your views here.


def task_list(request):
    if request.method == 'POST': 
        title = request.POST['title']
        Task.objects.create(title=title)
        context = {
            'tasks': Task.objects.filter(completed=False)
        }
    else: 
        context = {
            'tasks': Task.objects.filter(completed=False)
        }
    
    return render(request, 'task/task_list.html', context)

def task_delete(request, id):
    task = Task.objects.get(id=id) 
    task.delete()
    return redirect('/')

def task_completed(request, id): 
    task = Task.objects.get(id=id) 
    task.completed = True 
    task.save() 
    return redirect('/')
