from django.urls import path
from . import views

urlpatterns = [
    path('', views.StatusesListView.as_view(), name='status_list'),
    path('create/', views.StatusCreate.as_view(), name='create_status'),
    path('<int:pk>/delete', views.StatusDelete.as_view(), name='delete_status'),
    path('<int:pk>/edit', views.StatusEdit.as_view(), name='edit_status')
]