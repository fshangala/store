from django import forms
from .models import Inventory, Business

class InventoryCreateForm(forms.Form):
  name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={
    "class":"form-control"
  }))
  description=forms.CharField(widget=forms.Textarea(attrs={
    "class":"form-control"
  }))