from django.shortcuts import render
from django.views import generic, View
from .models import Business
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BusinessView(LoginRequiredMixin,View):
  template_name="businesses/business_detail.html"
  def get(self,request):
    context=self.get_context_data()
    return render(request, self.template_name, context=context)
  
  def get_context_data(self):
    context = {}
    return context
  
class BusinessList(generic.ListView):
  model=Business
  context_object_name="businesses"