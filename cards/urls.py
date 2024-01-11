from django.urls import path
from . import views

urlpatterns = [
    path('', views.chicken_book, name='chicken-book'),
    path('user-profile', views.user_profile, name='user_profile'),
    path('user-profile/skills', views.skill_list, name='skill_list'),
    path('user-profile/projects', views.project_list, name='project_list'),
    # path('user-profile/add_skill', views.add_skill, name='add_skill'),
]