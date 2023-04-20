from django.forms import ModelForm
from .models import Statuses


class StatusCreateForm(ModelForm):

    class Meta:
        model = Statuses
        fields = ('name',)
