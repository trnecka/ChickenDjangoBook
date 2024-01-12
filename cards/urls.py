from django.urls import path
from . import views

urlpatterns = [
    path('', views.chicken_book, name='chicken-book'),
    path('user-profile', views.user_profile, name='user_profile'),
    path('user-profile/skills', views.skill_list, name='skill_list'),
    path('user-profile/projects', views.project_list, name='project_list'),
    path('user_info/<str:user_id>/', views.user_info, name='user_info'),
    path('send_message/<str:recipient>/', views.send_message, name='send_message'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:message_id>/', views.message_detail, name='message_detail')
    # path('user-profile/add_skill', views.add_skill, name='add_skill'),
]