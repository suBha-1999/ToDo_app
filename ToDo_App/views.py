from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']   # this POST['task'] belongs to form <input name="task" 
# this [task] we need to save into database 
    Task.objects.create(task = task) # here we need to provide 4 types of attribuits for models.py. but except task all are by default vallue, so no need to provide
    return redirect('home') # this is basically homepage belongs to urls.py of ToDo_App



def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def mark_as_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')


def mark_as_edit(request, pk):
    get_task = get_object_or_404(Task, pk = pk)
    if request.method == 'POST':
        new_task = request.POST['task']  #'task' is the input name of form 
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task' : get_task,
        }
        return render(request, 'edit_task.html', context)