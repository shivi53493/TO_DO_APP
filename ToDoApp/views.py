from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
# Create your views here.
def add_task(request):
    task = request.POST['task']
    added_task = Task(task = task)
    added_task.save()

    return redirect('home')

def complete_task(request,pk):
    task = get_object_or_404(Task,pk = pk)
    print(task)
    task.is_completed = True
    task.save()
    return redirect('home')

def undone_task(request,pk):
    task = get_object_or_404(Task,pk = pk)
    print(task)
    task.is_completed=False
    task.save()
    return redirect('home')