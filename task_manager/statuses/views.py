from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Statuses
from .forms import StatusCreateForm
# Create your views here.


class StatusesListView(ListView):
    model = Statuses
    template_name = 'statuses/statuses_list.html'


class StatusCreate(CreateView):
    model = Statuses
    template_name = 'statuses/status_create.html'
    success_url = reverse_lazy('status_list')
    fields = ('name',)


class StatusDelete(DeleteView):
    model = Statuses
    template_name = 'statuses/status_delete.html'
    success_url = reverse_lazy('status_list')


class StatusEdit(UpdateView):
    model = Statuses
    form_class = StatusCreateForm
    template_name = 'statuses/status_edit.html'
    success_url = reverse_lazy('status_list')
