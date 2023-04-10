from django.shortcuts import render
from django.views import generic
from django.views import View
from businesses.models import (
  Business,
  Inventory
)
from django.contrib.auth.mixins import LoginRequiredMixin
from businesses.forms import InventoryCreateForm, RegisterBusinessForm
from .forms import (
  StockCreateForm,
)

class StockView(LoginRequiredMixin,View):
  template_name="seller/stock.html"
  
  def get(self,request,pk):
    context = self.get_context_data(request, pk)
    context["stockCreateForm"]=StockCreateForm(business=context["business"])
    return render(request, self.template_name, context=context)
  
  def post(self,request,pk):
    context = self.get_context_data(request, pk)
    stockCreateForm=StockCreateForm(business=context["business"],data=request.POST)
    
    if stockCreateForm.is_valid():
      stockCreateForm.save()
    
    context["stockCreateForm"]=stockCreateForm
      
    return render(request, self.template_name, context=context)
  
  def get_context_data(self,request,pk)->dict:
    context = {
      "business":request.user.businesses.get(pk=pk),
    }
    return context
  
# Create your views here.
class InventoryView(LoginRequiredMixin,View):
  template_name="seller/inventory.html"
  def get(self,request,pk):
    context = self.get_context_data(request, pk)
    
    return render(request, self.template_name, context=context)
  
  def post(self,request,pk):
    context = self.get_context_data(request, pk)
    inventoryCreateForm = InventoryCreateForm(data=request.POST)
    context["inventoryCreateForm"] = inventoryCreateForm
    
    if inventoryCreateForm.is_valid():
      inventory=Inventory.objects.create(
        name=inventoryCreateForm.cleaned_data["name"],
        business=Business.objects.get(pk=pk),
        description=inventoryCreateForm.cleaned_data["description"],
      )
    
    template_name = "seller/inventory.html"
    return render(request, template_name, context=context)
  
  def get_context_data(self,request,pk)->dict:
    context = {
      "business":request.user.businesses.get(pk=pk),
      "inventoryCreateForm":InventoryCreateForm()
    }
    return context
  
class Businesses(LoginRequiredMixin,View):
  template_name="seller/businesses.html"
  
  def get(self,request):
    context=self.get_context_data()
    return render(request, self.template_name, context=context)
  
  def post(self,request):
    context=self.get_context_data()
    registerBusinessForm=RegisterBusinessForm(request=request,data=request.POST)
    if registerBusinessForm.is_valid():
      registerBusinessForm.save()
    return render(request, self.template_name, context=context)
  
  def get_context_data(self):
    context = {
      "businesses":self.request.user.businesses.all(),
      "registerBusinessForm":RegisterBusinessForm(request=self.request,data=self.request.GET)
    }
    return context
  
class Dashboard(LoginRequiredMixin,generic.DetailView):
  model=Business
  context_object_name="business"
  template_name="seller/dashboard.html"