from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/<slug:slug>/', views.DetailView.as_view(), name='detail')
]
