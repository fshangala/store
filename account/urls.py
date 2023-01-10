from django.urls import path
from account.views import (
    AccountView, 
    AccountDetail, 
    LoginView,
    LogoutView,
    RegisterView,
    ChangeUserView
)

app_name="account"
urlpatterns=[
    path('',AccountView.as_view(),name="account"),
    path('profile/',AccountView.as_view(),name="profile"),
    path('id/<pk>/',AccountDetail.as_view(),name="main"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('register/',RegisterView.as_view(),name="register"),
    path('id/<pk>/change',ChangeUserView.as_view(),name="change")
]