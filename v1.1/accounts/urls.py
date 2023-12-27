from django.urls import path
from . import views
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .views import VendorCreateView


urlpatterns = [
    path('register', views.register, name='register'),
    path('register/vendor', views.registerVendor, name='registervendor'),
    path('signin', views.signin, name='signin'),
    path('signin/vendor', views.signinv, name='signin2'),
    path('vendor/signin', views.vsignin, name='signinv'),
    path('logout', views.signout, name='logout'),
    path('password-reset/', 
         PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password-reset'),
    path('password-reset/done/',
          PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
          PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',
          PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    #path('vendor/create/', views.VendorCreateView, name='vendor_create'),
    path('vendor/create/', VendorCreateView.as_view(), name='vendor_create'),
     
]

