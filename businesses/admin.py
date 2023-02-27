from django.contrib import admin
from .models import (
  Business,
  Inventory,
  Stock,
  Purchase
)

# Register your models here.
@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
  pass

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
  pass

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
  pass

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
  pass