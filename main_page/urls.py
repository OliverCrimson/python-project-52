from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.Login.as_view(), name='login'),
    path('logout/', views.logout_u, name='logout')
]
