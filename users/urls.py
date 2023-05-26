from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.Registration.as_view(), name='user_create'),
    path('', views.UsersList.as_view(), name='users_list'),
    path('<int:pk>/update', views.UpdateUserView.as_view(), name='update'),
    path('<int:pk>/delete',
         views.DeleteUserView.as_view(),
         name='delete_user'),
]
