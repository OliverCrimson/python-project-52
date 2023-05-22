from django import forms
from .models import Tasks


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
