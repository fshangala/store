from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

class StoreAdminSite(admin.AdminSite):
    site_header="E-Store"
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('admin/password_reset/',PasswordResetView.as_view(),name='admin_password_reset'),
            path('admin/password_reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
            path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
            path('reset/done/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
        ]
        return urls + custom_urls

storeAdmin = StoreAdminSite(name="admin")