from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User, Skill
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
    all_skills = Skill.objects.all()
    
    if request.method == 'POST':
        print(request.POST)
        form = UserInfoForm(request.POST, request.FILES, instance=user_instance)
        if form.is_valid():
            user_instance.skills.set(form.cleaned_data['skills']) # SKILLS
            form.save()
            messages.error(request, 'Profile update successfully !')  
            return redirect('user_profile')
        else:
            print(form.errors)  
    else:
        form = UserInfoForm(instance=user_instance)
    
    context = {
        'infoform': form, 
        'card': card,
        'all_skills': all_skills # SKILLS
        }
            
    return render(request, 'profile.html', context)
