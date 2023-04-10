from django import forms
from businesses.models import Inventory, Stock

class StockCreateForm(forms.Form):
  inventory=forms.ModelChoiceField(queryset=Inventory.objects.all(),widget=forms.Select(attrs={
    "class":"form-control",
    "required":True
  }))
  order=forms.FloatField(widget=forms.NumberInput(attrs={
    "class":"form-control",
    "required":True
  }))
  retail=forms.FloatField(widget=forms.NumberInput(attrs={
    "class":"form-control",
    "required":True
  }))
  quantity=forms.IntegerField(widget=forms.NumberInput(attrs={
    "class":"form-control",
    "required":True
  }))
  
  def __init__(self,*args,**kwargs):
    self.business=kwargs.pop("business")
    super(forms.Form, self).__init__(*args,**kwargs)
    self.fields['inventory'].queryset=self.business.inventory
    self.fields["quantity"].initial=0
  
  def save(self):
    stock = Stock.objects.create(**self.cleaned_data)