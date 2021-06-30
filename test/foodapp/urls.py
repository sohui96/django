from django.urls import path
from . import views

urlpatterns = [
    path('bab/', views.main),
]