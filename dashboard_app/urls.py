# dashboard_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data_points_view, name='data-point-list'),
    path('', views.dashboard_view, name='dashboard'),
]
