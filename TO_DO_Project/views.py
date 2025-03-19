from django.shortcuts import render
from ToDoApp.models import Task
def home(request):
    completed_tasks = Task.objects.filter(is_completed = True)
    incompleted_tasks = Task.objects.filter(is_completed = False)
    context = {
        'completed_tasks':completed_tasks,
        'incompleted_tasks':incompleted_tasks
    }

    return render(request,'home.html',context)