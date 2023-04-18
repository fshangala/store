from django.shortcuts import render
from django.views import generic, View
from .models import Business
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BuyStock(LoginRequiredMixin,View):
  template_name="businesses/buy_stock.html"
  def get(self,request,pk):
    context=self.get_context_data(pk)
    return render(request, self.template_name, context=context)
  
  def get_context_data(self,pk):
    context = {
      "business":Business.objects.get(pk=pk)
    }
    return context
  
class BusinessView(LoginRequiredMixin,View):
  template_name="businesses/business_detail.html"
  def get(self,request,pk):
    context=self.get_context_data(pk)
    return render(request, self.template_name, context=context)
  
  def get_context_data(self,pk):
    context = {
      "business":Business.objects.get(pk=pk)
    }
    return context
  
class BusinessList(generic.ListView):
  model=Business
  context_object_name="businesses"