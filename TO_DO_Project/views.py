from django.shortcuts import render
from ToDoApp.models import Task
def home(request):
    completed_tasks = Task.objects.filter(is_completed = True).order_by('-updated_at')
    incompleted_tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    context = {
        'completed_tasks':completed_tasks,
        'incompleted_tasks':incompleted_tasks
    }

    return render(request,'home.html',context)