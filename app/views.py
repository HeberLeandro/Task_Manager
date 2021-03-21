from django.shortcuts import render, redirect
from .forms import TaskForm
from .entities.Task import Task
from .services import task_service


# Create your views here.
def task_list(request):
    tasks = task_service.list_tasks()
    return render(request, 'tasks/task_list.html', {"tasks": tasks})


def register_task(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            title = task_form.cleaned_data["title"]
            description = task_form.cleaned_data["description"]
            expiration_date = task_form.cleaned_data["expiration_date"]
            priority = task_form.cleaned_data["priority"]
            new_task = Task(title=title, description=description,
                            expiration_date=expiration_date, priority=priority)
            task_service.register_task(new_task)
            return redirect('task_list')
    else:
        task_form = TaskForm()
    return render(request, 'tasks/task_form.html', {'task_form': task_form})


def edit_task(request, id):
    task_db = task_service.list_task_id(id)
    task_form = TaskForm(request.POST or None, instance=task_db)
    if task_form.is_valid():
        title = task_form.cleaned_data["title"]
        description = task_form.cleaned_data["description"]
        expiration_date = task_form.cleaned_data["expiration_date"]
        priority = task_form.cleaned_data["priority"]
        new_task = Task(title=title, description=description,
                        expiration_date=expiration_date, priority=priority)
        task_service.edit_task(task_db, new_task)
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {"task_form": task_form})


def remove_task(request, id):
    task_db = task_service.list_task_id(id)
    if request.method == "POST":
        task_service.remove_task(task_db)
        return redirect('task_list')
    return render(request, 'tasks/confirm_remotion.html', {'task': task_db})
