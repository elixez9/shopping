from django.urls import path
from . import views


app_name = 'accuonts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('verify/', views.VerifyCodeView.as_view(), name='verify'),


]