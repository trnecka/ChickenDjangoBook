from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User, Skills
from cards.forms import UserInfoForm, UserSkillForm
from django.contrib import messages
from django.http import HttpResponse
import json

def chicken_book(request):
    cards = User.objects.all()
    context = {'cards': cards }
    return render(request, 'chickenbook.html', context)

def skill_list(request):
    skills = Skills.objects.filter(user=request.user)
    context = {'skills': skills }
    return render(request, 'skill_list.html', context)
    
@login_required
def user_profile(request):
    user_instance = request.user
    card = User.objects.get(pk=user_instance.id)
    
    info_form = UserInfoForm(instance=user_instance)
    skill_form = UserSkillForm()
    
    if request.method == 'POST':
        if 'infoform' in request.POST:
            info_form = UserInfoForm(request.POST, request.FILES, instance=user_instance)
            if info_form.is_valid():
                info_form.save()
                messages.success(request, 'Profile update successfully !')  
                return redirect('user_profile')
            else:
                print(info_form.errors)  
        elif 'skillform' in request.POST:
            skill_form = UserSkillForm(request.POST)
            if skill_form.is_valid():
                skill_form.instance.user = user_instance
                skill_form.save()
                print(request.POST)
                messages.success(request, 'Skill added !')
                return redirect('user_profile')      
            else:
                print(skill_form.errors)
    
    context = {
        'infoform': info_form, 
        'skillform': skill_form,
        'card': card,
    }
            
    return render(request, 'profile.html', context)

