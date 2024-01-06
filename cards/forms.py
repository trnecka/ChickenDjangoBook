from django import forms
from accounts.models import User, Skill


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','work_focus', 'location','phone_number', 'about', 'profile_image', 'is_visible', 'skills']
        
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*'}))
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'select2'}), required=False) # SKILLS