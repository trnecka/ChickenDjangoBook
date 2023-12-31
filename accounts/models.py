from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
import os


class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name=None, last_name=None, **extra_fields):
        if not email:
            raise ValueError('Enter an email address')
        if not first_name:
            raise ValueError('Enter a first name')
        if not last_name:
            raise ValueError('Enter a last name')
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # user info
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    about = models.TextField(max_length=1000, blank=True, null=True)
    is_visible = models.BooleanField(default=False)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users', null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    work_focus = models.CharField(max_length=100, blank=True, null=True)
    
    
    # Zmensovanie img
    def save(self, *args, **kwargs):
        
        try:
            old_image = User.objects.get(pk=self.pk).profile_image
            if old_image.name != 'default-avatar.png':
                old_image_path = os.path.join('media', old_image.name)
                if os.path.isfile(old_image_path):
                    os.remove(old_image_path)
        except User.DoesNotExist:
            pass
        
        super().save(*args, **kwargs)
        
        img = Image.open(self.profile_image.path)
        if img.width > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    username = None
    
    objects = UserManager()