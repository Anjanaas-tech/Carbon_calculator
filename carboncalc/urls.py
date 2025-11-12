from django.urls import path
# from .views import calculate_footprint
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate_footprint/', views.calculate_footprint, name='calculate_footprint'),
    path('causes/', views.causes, name='causes'),
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
]