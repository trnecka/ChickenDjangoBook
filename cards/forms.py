from django import forms
from accounts.models import User, Skills, Project


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','work_focus', 'location','phone_number', 'about', 'profile_image', 'personal_web', 'git_hub', 'linked_in', 'instagram', 'is_visible']
        
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*'}))

class UserSkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['name', 'level']
        
class UserProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_link']