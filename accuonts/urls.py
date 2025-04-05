from django.urls import path
from . import views


app_name = 'accuont'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),


]