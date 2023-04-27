from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Tasks
from .forms import CreateTask


class TasksList(ListView):
    model = Tasks
    template_name = 'tasks/tasks_list.html'


class TaskCreate(CreateView):
    model = Tasks
    form_class = CreateTask
    template_name = 'tasks/tasks_create.html'
    success_url = reverse_lazy('tasks_list')


class TaskEdit(UpdateView):
    model = Tasks
    form_class = CreateTask
    template_name = 'tasks/tasks_edit.html'
    success_url = reverse_lazy('tasks_list')


class TaskDelete(DeleteView):
    model = Tasks
    template_name = 'tasks/tasks_delete.html'
    success_url = reverse_lazy('tasks_list')


class TaskDetails(DetailView):
    template_name = 'tasks/task_detail.html'
    model = Tasks
    context_object_name = 'tasks'

