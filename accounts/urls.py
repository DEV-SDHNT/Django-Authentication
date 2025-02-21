from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (loginView,signupView,forgotPasswordView,changePasswordView,dashboardView,profileView,logoutView)

urlpatterns = [
    path('login/',loginView,name='login'),
    path('signup/',signupView,name='signup'),
    path('change-password/',changePasswordView,name='change_password'),
    path('dashboard/',dashboardView,name='dashboard'),
    path('profile/',profileView,name='profile'),
    path('logout/',logoutView,name='logout'),
    path('forgot-password/',auth_views.PasswordResetView.as_view(template_name='accounts/forgot_password.html'),name='password_reset'),
    path('forgot-password/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_complete'),
]
