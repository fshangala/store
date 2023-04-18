from django.urls import path
from .views import (
  BusinessList,
  BusinessView
)

app_name="businesses"
urlpatterns = [
  path('',BusinessList.as_view(),name="list"),
  path('<pk>/',BusinessView.as_view(),name="detail"),
]
