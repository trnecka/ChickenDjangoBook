from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User, Skills, Project, Message
from cards.forms import UserInfoForm, UserSkillForm, UserProjectForm, MessageForm
from django.contrib import messages

def dashboard_view(request):

    context = {
        'pending_messages_count': Message.count_pending_messages() if request.user.is_authenticated else 0,
    }
    
    return render(request, 'main.html', context)

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

def user_info(request, user_id):
    skills = Skills.objects.filter(user_id=user_id)
    projects = Project.objects.filter(user_id=user_id)
    card = get_object_or_404(User, pk=user_id)
    
    context = {'card': card,
               'skills': skills,
               'projects': projects
               }
    
    return render(request, 'user_info.html', context)

def send_message(request, recipient):
    card = get_object_or_404(User, pk=recipient)

    # Initialize the form with sender's name and email if the user is logged in
    if request.user.is_authenticated:
        initial_data = {
            'sender_name': request.user.get_full_name(),  # Or just request.user.first_name
            'sender_email': request.user.email
        }
        message_form = MessageForm(initial=initial_data)
    else:
        message_form = MessageForm()

    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.recipient = card
            message.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('chicken-book')  # Replace 'some_view' with the desired redirect view name
        else:
            messages.error(request, 'There was an error in your form.')

    context = {'messageform': message_form, 'card': card}
    return render(request, 'send_message.html', context)

def message_list(request):
    messages = Message.objects.filter(recipient=request.user)
    context = {'messages': messages }
    return render(request, 'message_list.html', context)

def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    # Update the message status to 'Read' if it is 'Pending'
    if message.status == 'Pending':
        message.status = 'Read'
        message.save()

    return render(request, 'message_detail.html', {'message': message})

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



