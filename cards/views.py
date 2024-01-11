from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User, Skills, Project
from cards.forms import UserInfoForm, UserSkillForm, UserProjectForm
from django.contrib import messages

def chicken_book(request):
    cards = User.objects.all()
    context = {'cards': cards }
    return render(request, 'chickenbook.html', context)

def skill_list(request):
    skills = Skills.objects.filter(user=request.user)
    context = {'skills': skills }
    return render(request, 'skill_list.html', context)

def project_list(request):
    projects = Project.objects.filter(user=request.user)
    context = {'projects': projects }
    return render(request, 'project_list.html', context)

@login_required
def user_profile(request):
    user_instance = request.user
    card = User.objects.get(pk=user_instance.id)
    
    info_form = UserInfoForm(instance=user_instance)
    skill_form = UserSkillForm()
    project_form= UserProjectForm()
    
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
        elif 'projectform' in request.POST:
            project_form = UserProjectForm(request.POST)
            if project_form.is_valid():
                project_form.instance.user = user_instance
                project_form.save()
                print(request.POST)
                messages.success(request, 'Project added !')
                return redirect('user_profile')      
            else:
                print(project_form.errors)
        elif 'delete_skill' in request.POST:
            pk = request.POST.get('delete_skill')
            skill = Skills.objects.get(id=pk)
            skill.delete()
            return redirect('user_profile') 
        elif 'delete_project' in request.POST:
            pk = request.POST.get('delete_project')
            project = Project.objects.get(id=pk)
            project.delete()
            return redirect('user_profile') 
    
    
    context = {
        'infoform': info_form, 
        'skillform': skill_form,
        'projectform': project_form,
        'card': card,
    }
            
    return render(request, 'profile.html', context)



