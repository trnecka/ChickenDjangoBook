from django.shortcuts import render
from accounts.models import User

# Create your views here.

# def homepage(request):
#     return HttpResponse('Main Page')

def chicken_book(request):
    cards = User.objects.all()
    print(cards)
    context = {'cards': cards }
    return render(request, 'chickenbook.html', context)

def user_profile(request):
    context = {}
    return render(request, 'profile.html', context)
