from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, TemplateView, View
from django.urls import reverse_lazy
from accounts.models import User
from accounts.forms import RegistrationForm

class RegistrationFormView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    
class LoginView(TemplateView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('cards')
        messages.error(request, 'Wrong credentials')
        return redirect('login')
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('cards')
