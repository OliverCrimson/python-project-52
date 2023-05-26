from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from task_manager.messages import Flashes


class LoginRequired(LoginRequiredMixin):

    def handle_no_permission(self):
        messages.warning(self.request, Flashes.UNAUTHORIZED.value)
        return redirect(reverse_lazy('login'))


class Permission(UserPassesTestMixin):

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def handle_no_permission(self):
        messages.warning(self.request, Flashes.NO_PERMISSION_USER_UPDATE.value)
        return redirect(reverse_lazy('users_list'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(self.request, Flashes.UNAUTHORIZED.value)
            return self.handle_no_permission()
        if not self.get_object().pk == self.request.user.pk:
            messages.warning(self.request,
                             Flashes.NO_PEREMISSION_USER_UPDATE.value)
            return redirect('users_list')
        return super().dispatch(request, *args, **kwargs)


class TaskPermission(UserPassesTestMixin):

    def test_func(self):
        author = self.get_object().made_by
        return author == self.request.user

    def handle_no_permission(self):
        messages.warning(self.request, Flashes.NO_PERMISSION_TASK.value)
        return redirect(reverse_lazy('tasks_list'))
