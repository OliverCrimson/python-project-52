from django.urls import path
from . import views

urlpatterns = [
    path('', views.LabelsList.as_view(), name='labels_list'),
    path('create/', views.LabelCreate.as_view(), name='label_create'),
    path('<int:pk>/update', views.LabelEdit.as_view(), name='label_edit'),
    path('<int:pk>/delete', views.LabelDelete.as_view(), name='label_delete'),
]
