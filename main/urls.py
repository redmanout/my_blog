from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts_send, name='contacts'),
    path('success/', views.success_send, name='success')
]
