from django.shortcuts import render
from ToDo_App.models import Task


def home(request):
    task = Task.objects.filter(is_completed = False).order_by('-updated_at') # here you can sort the value by asscending or decending order. - means decending
    context = {
        "tasks" : task  # from here we send tasks value to index.html to make 
    }
    return render(request, 'home.html', context)


