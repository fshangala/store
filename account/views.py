from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings

# Create your views here.
class AccountView(LoginRequiredMixin,RedirectView):
    def get(self, request, *args, **kwargs):
        return redirect("account:main",pk=request.user.id)

class AccountDetail(DetailView):
    model=User
    template_name="account/user_detail.html"

class LoginView(LoginView):
    template_name="account/login.html"

class LogoutView(LoginRequiredMixin,LogoutView):
    template_name="account/logout.html"

class RegisterView(FormView):
    form_class=UserCreationForm
    template_name="account/register.html"
    success_url=settings.LOGIN_URL
    
    def form_valid(self, form):
        user = User.objects.create(username=form.cleaned_data["username"])
        user.set_password(form.cleaned_data["password1"])
        user.save()
        return super().form_valid(form)

class ChangeUserView(LoginRequiredMixin,UpdateView):
    model=User
    template_name="account/user_update.html"
    fields=["username","email","first_name","last_name"]
    success_url=settings.PROFILE_URL