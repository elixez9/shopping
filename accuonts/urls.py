from django.urls import path
from . import views


app_name = 'accuont'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('verify/', views.VerifyCodeView.as_view(), name='verify'),


]