from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse


def index(request):
    return render(request, 'main_page/index.html')


class Authorize(LoginView):
    form_class = AuthenticationForm
    template_name = 'main_page/login.html'
    success_url = reverse_lazy('users/users_list')