from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User, Skills, Project
from cards.forms import UserInfoForm, UserSkillForm, UserProjectForm
from django.contrib import messages
from django.http import HttpResponse
# API
from django.core.serializers import serialize
from accounts.models import User
from django.http import JsonResponse

#main_page(chickenbook)
def chicken_book(request):
    cards = User.objects.all()
    context = {'cards': cards }
    return render(request, 'chickenbook.html', context)

def user_info(request, user_id):
    skills = Skills.objects.filter(user_id=user_id)
    projects = Project.objects.filter(user_id=user_id)
    card = get_object_or_404(User, pk=user_id)
    
    context = {'card': card,
               'skills': skills,
               'projects': projects
               }
    
    return render(request, 'user_info.html', context)

# user_profile
@login_required
def user_profile(request):
    user_instance = request.user
    card = User.objects.get(pk=user_instance.id)
    
    info_form = UserInfoForm(instance=user_instance)
    skill_form = UserSkillForm()
    project_form= UserProjectForm()
    
    if request.method == 'POST':

        if 'skillform' in request.POST:
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


def skill_list(request):
    skills = Skills.objects.filter(user=request.user)
    context = {'skills': skills }
    return render(request, 'skill_list.html', context)

def project_list(request):
    projects = Project.objects.filter(user=request.user)
    context = {'projects': projects }
    return render(request, 'project_list.html', context)



@login_required
def edit_profile_form(request):
    user_instance = request.user
    form = UserInfoForm(instance=user_instance)
    
    if request.method == "POST":
        form = UserInfoForm(request.POST, request.FILES, instance=user_instance)
        if form.is_valid():
            form.save()
            messages.error(request, 'Profile update successfully !') 
            return HttpResponse(status=204)
    context = {
        'profile_form': form
    }
    
    return render(request, 'edit_profile_form.html', context)


# API ....mozno spravit vlastnu appku

def serialize_users(queryset):
    users_list = []
    for user in queryset:
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            # Add other fields you want to include
        }
        users_list.append(user_data)
    return users_list

def users_api(request):
    
    users = User.objects.filter(is_visible=True)
    data = serialize_users(users)
    print(data)
    return JsonResponse({'users': data})