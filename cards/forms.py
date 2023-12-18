from django import forms
from accounts.models import User


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'about', 'is_visible', 'profile_image']
        
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*'}))