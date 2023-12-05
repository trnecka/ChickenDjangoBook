from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    about = models.CharField(max_length=1000)


