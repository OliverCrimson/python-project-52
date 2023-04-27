from django.forms import ModelForm
from .models import Tasks


class CreateTask(ModelForm):
    class Meta:
        model = Tasks
        fields = ('name', 'description', 'status', 'executor')
