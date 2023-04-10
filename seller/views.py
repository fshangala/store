from django.shortcuts import render
from django.views import generic
from django.views import View
from businesses.models import (
  Business,
  Inventory
)
from django.contrib.auth.mixins import LoginRequiredMixin
from businesses.forms import InventoryCreateForm

# Create your views here.
class InventoryView(View):
  
  def get(self,request,pk):
    context = self.get_context_data(request, pk)
    
    template_name = "seller/inventory.html"
    return render(request, template_name, context=context)
  
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
  
class Businesses(LoginRequiredMixin,generic.ListView):
  model=Business
  context_object_name="businesses"
  template_name="seller/businesses.html"
  
  def get_queryset(self):
    return self.request.user.businesses.all()
  
class Dashboard(LoginRequiredMixin,generic.DetailView):
  model=Business
  context_object_name="business"
  template_name="seller/dashboard.html"