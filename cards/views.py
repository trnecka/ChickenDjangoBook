from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# def homepage(request):
#     return HttpResponse('Main Page')

class HomepageView(View):
    template_name = 'cards.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)