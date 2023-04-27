from .forms import UserRegistration
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import User


class Registration(CreateView):
    form_class = UserRegistration
    model = User
    template_name = 'users/user_create.html'
    success_url = '/login'


class UpdateUserView(UpdateView):
    model = User
    form_class = UserRegistration
    template_name = 'users/user_update.html'


class UsersList(ListView):
    model = User
    template_name = 'users/users_list.html'


class DeleteUserView(DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    success_url = '/'
