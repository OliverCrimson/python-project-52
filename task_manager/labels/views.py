from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Labels
from .forms import LabelForm


class LabelsList(ListView):
    model = Labels
    template_name = 'labels/labels_list.html'


class LabelCreate(CreateView):
    model = Labels
    form_class = LabelForm
    template_name = 'labels/label_create.html'
    success_url = reverse_lazy('labels_list')


class LabelEdit(UpdateView):
    model = Labels
    form_class = LabelForm
    template_name = 'labels/label_edit.html'
    success_url = reverse_lazy('labels_list')


class LabelDelete(DeleteView):
    model = Labels
    template_name = 'labels/label_delete.html'
    success_url = reverse_lazy('labels_list')
    context_object_name = 'label'

