from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task = (request.POST['task'])   # this POST['task'] belongs to form <input name="task" 
# this [task] we need to save into database 
    Task.objects.create(task = task) # here we need to provide 4 types of attribuits for models.py. but except task all are by default vallue, so no need to provide
    return redirect('home') # this is basically homepage belongs to urls.py of ToDo_App