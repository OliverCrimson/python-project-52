from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView,\
    CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from .models import Tasks
from .forms import CreateTask
from .filters import TaskFilter
from task_manager.messages import Flashes
from task_manager.utils import TaskPermission
from django.contrib.auth.mixins import LoginRequiredMixin


class TasksList(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'


class FilteredTasks(LoginRequiredMixin, FilterView):
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter


class TaskCreate(LoginRequiredMixin,
                 SuccessMessageMixin,
                 CreateView):
    model = Tasks
    form_class = CreateTask
    template_name = 'tasks/tasks_create.html'
    success_url = reverse_lazy('tasks_list')
    success_message = Flashes.TASK_CREATED.value

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['made_by'].initial = self.request.user.pk
        return context


class TaskEdit(LoginRequiredMixin,
               SuccessMessageMixin,
               UpdateView):
    model = Tasks
    form_class = CreateTask
    template_name = 'tasks/tasks_edit.html'
    success_url = reverse_lazy('tasks_list')
    success_message = Flashes.NO_PERMISSION_TASK.value


class TaskDelete(LoginRequiredMixin,
                 TaskPermission,
                 SuccessMessageMixin,
                 DeleteView):
    model = Tasks
    template_name = 'tasks/tasks_delete.html'
    success_url = reverse_lazy('tasks_list')
    success_message = Flashes.NO_PERMISSION_TASK.value


class TaskDetails(LoginRequiredMixin, DetailView):
    template_name = 'tasks/task_detail.html'
    model = Tasks
    context_object_name = 'tasks'
