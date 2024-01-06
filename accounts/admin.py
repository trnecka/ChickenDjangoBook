from django.contrib import admin
from .models import User, Skill  # Import your models

admin.site.register(User)  # Register the User model
admin.site.register(Skill)  # Register the Skill model

# Register your models here.
