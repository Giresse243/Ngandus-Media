from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name='create-booking'),
    path('services-list/', views.get_services_list, name='services-list'),
]
