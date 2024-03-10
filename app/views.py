from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('list')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'app/task_confirm_delete.html'
    success_url = reverse_lazy('list')
