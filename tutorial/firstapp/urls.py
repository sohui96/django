from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('template/', views.template),
    path('check/', views.check, name='check'),  
]
