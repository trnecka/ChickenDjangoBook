from django.urls import path
from . import views

urlpatterns = [
    path('', views.chicken_book, name='chicken-book'),
    path('user-profile', views.user_profile, name='user_profile'),
]