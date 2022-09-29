from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from to_do.models import Task
from to_do.choice_config import CHOICES
from to_do.forms import TaskForm


def index_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        context = {
            'CHOICES': CHOICES,
            'tasks': tasks,
        }
        return render(request, 'index.html', context)

def add_task_view(request):
    form = TaskForm()
    if request.method == 'GET':
        context = {'form': form}
        return render(request, 'add_task.html', context)
    form = TaskForm(request.POST)
    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'add_task.html', context)
    task = Task.objects.create(**form.cleaned_data)
    return redirect('task_detail', pk=task.pk)

def task_view(request, pk):
    if request.POST.get("task_text") == '':
        task_text = 'тема не определена'
    else:
        task_text = request.POST.get("task_text")
    if request.POST.get("task_description") == '':
        task = Task.objects.get(pk=pk)
        task_description = task.task_description
    if request.POST.get("deadline") == '':
        deadline = None
    else:
        deadline = request.POST.get("deadline")
    if request.method == 'POST':
        Task.objects.filter(pk=pk).update(
            task_text=task_text,
            task_description=request.POST.get("task_description"),
            state=request.POST.get("state"),
            deadline=deadline
        )
        print(f'Обновление записи ID {pk}')
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={'task': task, 'CHOICES': CHOICES})

def task_edit_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'task_text': task.task_text,
            'state': task.state,
            'task_description': task.task_description,
            'deadline': task.deadline
        })
        return render(request, 'edit_task.html', context={'form': form, 'task': task})
    form = TaskForm(request.POST)
    if not form.is_valid():
        context = {
            'choices': CHOICES,
            'form': form
        }
        return render(request, 'add_task.html', context)
    task = Task.objects.create(**form.cleaned_data)


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task
    }
    return render(request, 'task_confirm_delete.html', context)

def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
