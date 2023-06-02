from django.forms import ModelForm
from .models import Statuses
from django.utils.translation import gettext_lazy as _


class StatusCreateForm(ModelForm):

    class Meta:
        model = Statuses
        fields = ['name']
        labels = {'name': _('Name')}
