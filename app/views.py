from django.shortcuts import render
from .forms import TaskForm


# Create your views here.
def task_list(request):
    task_name = 'Practice Python e Django'
    return render(request, 'tasks/task_list.html', {"task_name": task_name})


def register_task(request):
    task_form = TaskForm()
    return render(request, 'tasks/task_form.html', {'task_form': task_form})
