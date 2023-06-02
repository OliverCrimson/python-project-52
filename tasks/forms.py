from django import forms
from .models import Tasks
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as T


class CreateTask(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name',
                  'description',
                  'status',
                  'made_by',
                  'executor',
                  'labels']

        widgets = {
            'made_by': forms.HiddenInput(),
            'labels': forms.SelectMultiple(),
        }
        labels = {
            'name': T('Name'),
            'description': T('Description'),
            'status': T('Status'),
            'executor': T('Executor'),
            'labels': T('Labels')
        }
