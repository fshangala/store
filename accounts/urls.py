from django.urls import path
from .views import (
    AccountLogin,
    AccountProfile,
    AccountMain,
    UserRegister
)
from django.contrib.auth.views import logout_then_login

app_name="accounts"
urlpatterns = [
    path('login/',AccountLogin.as_view(),name="login"),
    path('logout/',logout_then_login,name="logout"),
    path('id/<pk>/',AccountProfile.as_view(),name="profile"),
    path('',AccountMain.as_view(),name="main"),
    path('profile/',AccountMain.as_view(),name="user-profile"),
    path('register/',UserRegister.as_view(),name="register"),
]
