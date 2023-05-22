from django.urls import path
from . import views
from .models import Tasks


urlpatterns = [
    path('', views.FilteredTasks.as_view(model=Tasks), name='tasks_list'),
    path('create', views.TaskCreate.as_view(), name='task_create'),
    path('<int:pk>/edit', views.TaskEdit.as_view(), name='task_edit'),
    path('<int:pk>/delete', views.TaskDelete.as_view(), name='task_delete'),
    path('<int:pk>/', views.TaskDetails.as_view(), name='task_details'),

]