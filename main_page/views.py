from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from users.models import User
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.messages import Flashes
from django.contrib import messages
from django.contrib.auth import logout


def index(request):
    return render(request, 'main_page/index.html')


class Login(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    model = User
    template_name = 'main_page/login.html'
    success_url = 'users_list'
    success_message = Flashes.LOGGED_IN.value


def logout_u(request):
    logout(request)
    messages.success(request, Flashes.LOGGED_OUT.value)
    return redirect('home')
