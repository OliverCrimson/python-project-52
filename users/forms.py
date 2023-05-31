from django.contrib.auth.forms import UserCreationForm
from . import models
from django.utils.translation import gettext_lazy as _


class UserRegistration(UserCreationForm):

    class Meta:
        model = models.User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2')
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'username': _('Username'),

        }
