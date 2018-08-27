from django.urls import path, include
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('signup/', views.signup, name='signup'),
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),
        path('password_change/', views.password_change, name='password_change'),
        path('password_change/done/', views.password_change_done, name='password_change_done'),
]
