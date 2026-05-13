from django.shortcuts import render
from ToDo_App.models import Task


def home(request):
    task = Task.objects.filter(is_completed = False).order_by('-updated_at') # here you can sort the value by asscending or decending order. - means decending
    
    
    completed_task = Task.objects.filter(is_completed = True)
    
    
    context = {
        "tasks" : task,  # from here we send tasks value to index.html to make 
        "completed_task" : completed_task
    }
    return render(request, 'home.html', context)


