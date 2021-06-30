from django.urls import path
# from . import views
import pagination.views as views

urlpatterns = [
    path('insert2/', views.insert2),
    path('pagination/', views.pagination),
    path('list/', views.list),
]