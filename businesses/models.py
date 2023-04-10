from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Business(models.Model):
  owner=models.ForeignKey(User, related_name="businesses", on_delete=models.CASCADE)
  name=models.CharField(max_length=200,unique=True)
  
  def __str__(self):
    return self.name

class Inventory(models.Model):
  business=models.ForeignKey(Business,related_name="inventory",on_delete=models.CASCADE)
  name=models.CharField(max_length=200,unique=True)
  description=models.TextField()
  
  def __str__(self):
    return self.name

class Stock(models.Model):
  inventory=models.ForeignKey(Inventory,related_name="stock",on_delete=models.CASCADE)
  order=models.FloatField()
  retail=models.FloatField()
  quantity=models.IntegerField()
  
  def sold(self)->int:
    purchases=self.purchases.all()
    return len(purchases)
  
  def in_stock(self)->int:
    return self.quantity - self.sold()
  
  def __str__(self):
    return self.inventory.name + " " + str(self.retail)

class Cart(models.Model):
  customer=models.ForeignKey(User, related_name="carts", on_delete=models.CASCADE)
  status=models.CharField(max_length=200,choices=[
    ("pending","PENDING"),
    ("paid","PAID"),
    ("canceled","CANCELED"),
  ],default="pending")

class Purchase(models.Model):
  cart=models.ForeignKey(Cart, related_name="purchases", on_delete=models.CASCADE)
  stock=models.ForeignKey(Stock, related_name="purchases", on_delete=models.CASCADE)
  quantity=models.IntegerField()
  discount=models.FloatField(default=0.0)
  
  def amount(self)->float:
    return (self.quantity*self.stock.retail) - self.discount
  
  def profit(self)->float:
    return self.amount() - (self.quantity*self.stock.order)
