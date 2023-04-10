from django.urls import path
from .views import (
  BusinessList,
  BusinessView,
  CartView,
  BuyStock
)

app_name="businesses"
urlpatterns = [
  path('',BusinessList.as_view(),name="list"),
  path('<pk>/',BusinessView.as_view(),name="detail"),
  path('buy/<pk>/<quantity>/',BuyStock.as_view(),name="buy"),
  path('cart/<pk>/',CartView.as_view(),name="cart"),
]
