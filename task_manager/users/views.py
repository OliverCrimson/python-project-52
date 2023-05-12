from .forms import UserRegistration
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.messages import Flashes
from .models import User
from task_manager.utils import LoginRequired, Permission


class Registration(SuccessMessageMixin, CreateView):
    form_class = UserRegistration
    model = User
    template_name = 'users/user_create.html'
    success_url = '/login'
    success_message = Flashes.USER_REGISTERED.value


class UpdateUserView(LoginRequired, Permission, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserRegistration
    template_name = 'users/user_update.html'
    success_message = 'Update successful'


class UsersList(ListView):
    model = User
    template_name = 'users/users_list.html'


class DeleteUserView(LoginRequired, Permission, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_list')
    success_message = Flashes.USER_DELETE.value
