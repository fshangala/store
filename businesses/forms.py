from django import forms
from .models import Inventory, Business, Stock, Cart, Purchase
from django.contrib.auth.models import User

class RegisterBusinessForm(forms.Form):
  name=forms.CharField(widget=forms.TextInput(attrs={
    "class":"form-control",
    "required":True
  }))
  
  def __init__(self,*args,**kwargs):
    self.request=kwargs.pop("request")
    super(forms.Form, self).__init__(*args,**kwargs)
  
  def save(self):
    Business.objects.create(
      owner=self.request.user,
      name=self.cleaned_data["name"]
    )
    
class BuyForm(forms.Form):
  cart=forms.ModelChoiceField(Cart.objects.all())
  stock=forms.ModelChoiceField(Stock.objects.all())
  quantity=forms.IntegerField()
  
  def __init__(self,*args,**kwargs):
    self.request=kwargs.pop("request")
    super(forms.Form, self).__init__(*args,**kwargs)
    self.fields["cart"].queryset=self.request.user.carts.all()
  
  def save(self):
    purchase=Purchase.objects.create(
      cart=self.cleaned_data["cart"],
      stock=self.cleaned_data["stock"],
      quantity=self.cleaned_data["quantity"]
    )

class InventoryCreateForm(forms.Form):
  name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={
    "class":"form-control"
  }))
  description=forms.CharField(widget=forms.Textarea(attrs={
    "class":"form-control"
  }))