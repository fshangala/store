from django.urls import path
from .views import (
  Dashboard,
  Businesses,
  InventoryView
)

app_name="seller"
urlpatterns = [
  path("dashboard/<pk>/",Dashboard.as_view(),name="dashboard"),
  path("dashboard/<pk>/inventory/",InventoryView.as_view(),name="inventory"),
  path("",Businesses.as_view(),name="dashboard"),
]
