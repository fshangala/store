from django.urls import path
from .views import (
  BusinessList
)

app_name="businesses"
urlpatterns = [
  path('',BusinessList.as_view(),name="list"),
]
