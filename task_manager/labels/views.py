from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.messages import Flashes
from .forms import LabelForm
from .models import Labels


class LabelsList(ListView):
    model = Labels
    template_name = 'labels/labels_list.html'


class LabelCreate(SuccessMessageMixin, CreateView):
    model = Labels
    form_class = LabelForm
    template_name = 'labels/label_create.html'
    success_message = Flashes.LABEL_CREATED.value
    success_url = reverse_lazy('labels_list')


class LabelEdit(SuccessMessageMixin, UpdateView):
    model = Labels
    form_class = LabelForm
    template_name = 'labels/label_edit.html'
    success_url = reverse_lazy('labels_list')
    success_message = Flashes.LABEL_UPDATED.value


class LabelDelete(SuccessMessageMixin, DeleteView):
    model = Labels
    template_name = 'labels/label_delete.html'
    success_url = reverse_lazy('labels_list')
    context_object_name = 'label'
    success_message = Flashes.LABEL_DELETED.value

    def form_valid(self, form):
        try:
            self.object.delete()
            messages.warning(self.request, Flashes.LABEL_DELETED.value)
            return redirect(reverse_lazy('labels_list'))
        except ProtectedError:
            messages.warning(self.request, Flashes.LABEL_ERROR.value)
            return redirect(reverse_lazy('labels_list'))



