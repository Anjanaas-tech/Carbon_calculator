from django.urls import path
from .views import calculate_footprint

urlpatterns = [
    path('', calculate_footprint, name='calculate_footprint'),
]