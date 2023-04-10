from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Business, Stock, Cart
from .forms import BuyForm, RegisterBusinessForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CartView(View):
  template_name="businesses/cart.html"
  def get(self,request,pk):
    context=self.get_context_data(pk)
    return render(request, self.template_name, context=context)
  
  def get_context_data(self,pk):
    context={
      "cart":Cart.objects.get(pk=pk)
    }
    return context
  
class BuyStock(LoginRequiredMixin,View):
  template_name="businesses/buy_stock.html"
  def get(self,request,pk,quantity):
    cart = Cart.objects.create(
      customer=self.request.user
    )
    stock=Stock.objects.get(pk=pk)
    buyForm=BuyForm(request=request,data={
      "cart":cart,
      "stock":stock,
      "quantity":quantity
    })
    if buyForm.is_valid():
      buyForm.save()
      
    return redirect("businesses:cart",pk=cart.id)
  
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
  
class BusinessList(LoginRequiredMixin,View):
  template_name="businesses/business_list.html"
  
  def get(self,request):
    context=self.get_context_data()
    return render(request, self.template_name, context=context)
  
  def get_context_data(self):
    context = {
      "businesses":self.request.user.businesses.all(),
      "registerBusinessForm":RegisterBusinessForm(self.request.GET)
    }
    return context