from django.urls import path
from . import views


urlpatterns = [
    path('', views.TasksList.as_view(), name='tasks_list'),
]