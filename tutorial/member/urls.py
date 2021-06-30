from django.urls import path
from . import views

urlpatterns = [
    path('', views.join),
    path('', views.login2),
    path('', views.upload1),

]
