from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from cards.forms import UserInfoForm
from django.contrib import messages

def chicken_book(request):
    cards = User.objects.all()
    context = {'cards': cards }
    return render(request, 'chickenbook.html', context)

@login_required
def user_profile(request):
    user_instance = request.user
    card = User.objects.get(pk=request.user.id)
    
    if request.method == 'POST':
        print(request.POST)
        form = UserInfoForm(request.POST, request.FILES, instance=user_instance)
        if form.is_valid:
            form.save()
            messages.error(request, 'Profile update successfully !')  
            return redirect('user_profile')
        else:
            print(form.errors)  
    else:
        form = UserInfoForm(instance=user_instance)
    
    context = {
        'infoform': form, 
        'card': card
        }
            
    return render(request, 'profile.html', context)
