from django.urls import path
from django.conf.urls.static import static
from shoping import settings
from . import views

app_name = 'accuonts'
urlpatterns = [
                  path('register/', views.UserRegisterView.as_view(), name='register'),
                  path('verify/', views.UserVerifyCodeView.as_view(), name='verify_code'),

              ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
