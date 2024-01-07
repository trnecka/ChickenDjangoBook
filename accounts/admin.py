from django.contrib import admin
from .models import User, Skills  # Import your models

admin.site.register(User)  # Register the User model
admin.site.register(Skills)  # Register the Skill model

# Register your models here.
