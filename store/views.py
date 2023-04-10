from django.views import View
from django.shortcuts import render
from businesses.models import Inventory

class StoreView(View):
    template_name="store.html"
    def get(self,request):
        context={
            "inventory":Inventory.objects.all()
        }
        return render(request, self.template_name, context=context)