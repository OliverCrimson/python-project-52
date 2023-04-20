from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.Authorize.as_view(), name='login')
]