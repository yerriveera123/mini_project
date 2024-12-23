from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from app.forms import *

def index(request, pk=None ):
   
    tasks = Task.objects.all()
    form = Taskform()
    update_mode = False

    # Check if we are updating an existing task
    if pk:
        task =Task.objects.get(id=pk)
        form = Taskform(instance=task)
        update_mode = True

        if request.method == 'POST':
            form = Taskform(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('/')
    # Handle new task creation
    elif request.method == 'POST':
        
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks': tasks,'form': form,'update_mode': update_mode,}
    return render(request, 'index.html', context)

def delete_task(request, pk):
    
    task =Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return redirect('/')  