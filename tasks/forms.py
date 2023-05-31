from django import forms
from .models import Tasks
from django.utils.translation import gettext as _


class CreateTask(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('name',
                  'description',
                  'status',
                  'made_by',
                  'executor',
                  'labels')

        widgets = {
            'made_by': forms.HiddenInput(),
            'labels': forms.SelectMultiple(),
        }
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'made_by': _('Author'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }
