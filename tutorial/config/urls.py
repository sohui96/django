from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import firstapp.views as views
from member import views as m_views
from map import views as map_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstapp.urls')),
    path('polls/', include('polls.urls')),
    path('second/', include('secondapp.urls')),
    path('pagination/', include('pagination.urls')),
    # path('join/', include('member.urls')),
    path('join/',  m_views.join, name="join"),
    path('login2/',  m_views.login2, name="login2"),
    path('logout2/',  m_views.logout2, name="logout2"),
    path('upload1/',  m_views.upload1),
    path('download/', m_views.download),
    path('map/', map_views.map),
    path('map_data/', map_views.map_data),


    path(
        'login/', auth_views.LoginView.as_view(
            template_name='common/login.html'),
        name='login'),
    path(
        'logout/', auth_views.LogoutView.as_view(
            template_name='common/logout.html'),
        name='logout'),
    path('signup/', views.signup, name='signup'),  
]
