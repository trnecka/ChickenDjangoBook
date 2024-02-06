from django import forms
from accounts.models import User, Skills, Project

# Form for editing user profile on profile page 
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','work_focus', 'location','phone_number', 'about', 'profile_image', 'personal_web', 'git_hub', 'linked_in', 'instagram', 'is_visible']
        
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*'}))

# Form for adding and deleting Skills on profile page
class UserSkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['name', 'level']

# Form for adding and deleting Projects on profile page
class UserProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_link']

# Form for password confirmation on account delete action
class DeleteAccountForm(forms.Form):
    
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label="Confirm Your Password")

        