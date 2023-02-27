from django.shortcuts import render
from django.views import generic
from .models import Business

# Create your views here.
class BusinessList(generic.ListView):
  model=Business
  context_object_name="businesses"