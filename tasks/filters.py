from .models import Tasks
import django_filters

from users.models import User
from statuses.models import Statuses
from labels.models import Labels


from django.utils.translation import gettext_lazy as _
from django import forms


class TaskFilter(django_filters.FilterSet):

    def self_widget_filter(self, queryset, name, value):
        if value:
            made_by = getattr(self.request, 'user', None)
            if made_by:
                return queryset.filter(creator=made_by)
            return queryset.none()
        return queryset

    status = django_filters.ModelChoiceFilter(
        queryset=Statuses.objects.all(),
        label=_('Status'),
        widget=forms.Select(attrs={
            'class': 'form-select',
        }))

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_('Executor'),
        widget=forms.Select(attrs={
            'class': 'form-select',
        }))
    labels = django_filters.ModelChoiceFilter(
        label=_('Label'),
        queryset=Labels.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )
    self_task = django_filters.BooleanFilter(
        label=_('My tasks'),
        method='self_widget_filter',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        }))

    class Meta:

        model = Tasks
        fields = (
            'status',
            'executor',
            'labels',
        )
