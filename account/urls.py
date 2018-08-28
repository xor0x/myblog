from django.urls import path, include
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('signup/', views.signup, name='signup'),
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),


        # Block urls
        path('password_reset/', views.password_reset, name='password_reset'),
        path('password_reset/done/', views.password_reset, name='password_reset_done'),
        path('reset/done/', views.password_reset, name='password_reset_confirm'),
        path('reset/<uidb64>/<token>/', views.password_reset, name='password_reset_complete'),

]
