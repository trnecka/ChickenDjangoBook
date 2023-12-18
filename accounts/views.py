from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import RegistrationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView

class RegistrationFormView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    
class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('user_profile')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Login successful!')
        return response
    
# class LoginView(TemplateView):
#     template_name = 'login.html'
#     form_class = AuthenticationForm
    
#     def post(self, request, *args, **kwargs):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             messages.success(request, 'Login successfully')
#             return redirect('cards')
#         messages.success(request, 'Wrong credentials')
#         return redirect('login')
    
# class LogoutView(View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         messages.success(request, 'Logout Successfully !')
#         return redirect('cards')
