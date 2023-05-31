from django.forms import ModelForm
from .models import Labels
from django.utils.translation import gettext_lazy as _


class LabelForm(ModelForm):

    class Meta:
        model = Labels
        fields = ('name',)
        labels = {
            'name': _('Name'),
        }
