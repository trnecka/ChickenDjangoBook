from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User, Skills, Project
from cards.forms import UserInfoForm, UserSkillForm, UserProjectForm, DeleteAccountForm
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse
# API
from accounts.models import User
import json, csv

def chicken_book(request):
    '''
    Main page(chickenbook) on ~/
    
    '''
    cards = User.objects.all()
    context = {'cards': cards }
    return render(request, 'chickenbook.html', context)

def about_project(request):
    '''
    About project page on ~/about-project
    '''
    return render(request, 'about_project.html')

def bye_page(request):
    '''
    Bye Bye msg after succesfull deletion of the account
    '''
    return render(request, 'bye.html')
    
def wrong_password(request):
    '''
    Wrong password message after unsuccessfull enter of password on delete acc action
    '''
    return render(request, 'wrong_password.html')

def user_info(request, user_id):
    '''
    User Info view on main page (more info button)
    '''
    skills = Skills.objects.filter(user_id=user_id)
    projects = Project.objects.filter(user_id=user_id)
    card = get_object_or_404(User, pk=user_id)
    
    context = {'card': card,
               'skills': skills,
               'projects': projects
               }
    
    return render(request, 'user_info.html', context)


@login_required
def user_profile(request):
    '''
    User Profile page, with all Forms.
    '''
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
    '''
    List of skills on Profile page
    '''
    skills = Skills.objects.filter(user=request.user)
    context = {'skills': skills }
    return render(request, 'skill_list.html', context)

def project_list(request):
    '''
    List of projects on Profile page
    '''
    projects = Project.objects.filter(user=request.user)
    context = {'projects': projects }
    return render(request, 'project_list.html', context)

@login_required
def edit_profile_form(request):
    '''
    Edit profile form
    '''
    user_instance = request.user
    form = UserInfoForm(instance=user_instance)
    
    if request.method == "POST":
        
        if 'delete_conf' in request.POST:  # Check if the delete action was triggered
            return redirect('confirm_delete')  # Redirect to home or a specific page
        
        form = UserInfoForm(request.POST, request.FILES, instance=user_instance)
        if form.is_valid():
            form.save()
            messages.error(request, 'Profile update successfully !') 
            return HttpResponse(status=204)
    context = {
        'profile_form': form
    }
    
    return render(request, 'edit_profile_form.html', context)

@login_required
def confirm_delete(request):
    '''
    Confirmation password form on delete acc action
    '''
    
    confirm_delete_form = DeleteAccountForm()
    
    context = {
        'delete_account_form': confirm_delete_form
    }
    
    return render(request, 'confirm_delete.html', context)

@login_required
def acc_delete(request):
    '''
    Actual Delete Account view
    '''
    user_instance = request.user

    if request.method == "POST":
        # Get the plaintext password from the form
        password_confirmation = request.POST.get('password_confirmation')
        
        # Use check_password to compare the password
        if user_instance.check_password(password_confirmation):
            user_instance.delete()  # Delete the user
            logout(request)  # Log the user out
            messages.success(request, 'Your account has been deleted successfully.')
            # If you're using HTMX or need to force a redirect, adjust accordingly
            response = HttpResponse(status=204)
            response['HX-Redirect'] = '/bye'  # This tells HTMX to navigate to '/' on the client side
            return response  # Redirect to home or a specific page  # Redirect to a goodbye page or home as needed
        
        else:
            # You might want to redirect back to the form or stay on the page for another attempt
            response = HttpResponse(status=204)
            response['HX-Redirect'] = '/wrong-password'  # This tells HTMX to navigate to '/' on the client side
            return response
            
    # If the request is not POST, just show the form again (or handle differently as needed)
    return render(request, 'confirm_delete.html')

def serialize_users(queryset):
    '''
    Sserializer for users data for API/data what will show in generated querry
    '''
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

def users_api_view(request):
    '''
    HTTP response API view
    '''
    users = User.objects.filter(is_visible=True)
    data = serialize_users(users)
    return JsonResponse({'users': data})

def users_api_download(request):
    '''
    API download view JSON/CSV
    '''
    format_type = request.GET.get('format', 'json')  # Default format is JSON
    users = User.objects.filter(is_visible=True)
    data = serialize_users(users)

    if format_type == 'json':
        response = HttpResponse(json.dumps({'users': data}), content_type="application/json")
        response['Content-Disposition'] = 'attachment; filename="chickens.json"'
        return response
    elif format_type == 'csv':
        # Create an HTTP response with the correct content-type
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="chickens.csv"'

        # Create a csv writer and write the header and data
        writer = csv.writer(response)
        
        if data:
            # Writing the header (keys of the dictionary)
            writer.writerow(data[0].keys())

            # Writing the data rows
            for user in data:
                writer.writerow(user.values())

        return response
    else:
     
        return JsonResponse({'users': data})
    
