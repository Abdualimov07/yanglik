from django.urls import path
from .views import user_login,profile,register,custom_logout, edit_user
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView



urlpatterns = [
    path('login/', user_login, name='login'),
    path('profile/', profile, name='user_profile'),
    path('password-change/', PasswordChangeView.as_view(template_name ='account/password-change-form.html'), name="password-change"),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name ='account/password-change-done.html'), name="password-change-done"),
    path('register/', register, name='register'),
    path('logout/', custom_logout, name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name = 'account/password_reset_form.html'), name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name = 'account/password_reset_done.html'), name='password-reset-done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'account/password_reset_confirm.html'), name='password-confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name = 'account/password_reset_complete.html'), name='password-complete'),
    path("profile/edit", edit_user, name="profile_edit_page")
    
]   