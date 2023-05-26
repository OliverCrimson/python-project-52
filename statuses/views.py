from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect
from .models import Statuses
from .forms import StatusCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.messages import Flashes
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class StatusesListView(LoginRequiredMixin, ListView):
    model = Statuses
    template_name = 'statuses/statuses_list.html'


class StatusCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Statuses
    template_name = 'statuses/status_create.html'
    success_url = reverse_lazy('status_list')
    fields = ('name',)
    success_message = Flashes.STATUS_CREATE.value


class StatusDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Statuses
    template_name = 'statuses/status_delete.html'
    success_url = reverse_lazy('status_list')
    success_message = Flashes.STATUS_DELETE.value

    def form_valid(self, form):
        try:
            self.object.delete()
            messages.warning(self.request, Flashes.STATUS_DELETE.value)
            return redirect(reverse_lazy('status_list'))
        except ProtectedError:
            messages.warning(self.request, Flashes.STATUS_ERROR.value)
            return redirect(reverse_lazy('status_list'))


class StatusEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Statuses
    form_class = StatusCreateForm
    template_name = 'statuses/status_edit.html'
    success_url = reverse_lazy('status_list')
    success_message = Flashes.STATUS_UPDATE.value
