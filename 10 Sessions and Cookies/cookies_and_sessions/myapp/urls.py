from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set_cookie/', views.set_cookie, name='set_cookie'),
    path('get_cookie/', views.get_cookie, name='get_cookie'),
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('clear_session/', views.clear_session, name='clear_session'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('protected/', views.protected_view, name='protected_view'),
    path('set_theme/', views.set_theme, name='set_theme'),
]
