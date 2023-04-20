from django.contrib.auth.forms import UserCreationForm
from . import models


class UserRegistration(UserCreationForm):

    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username': 'Username',

        }