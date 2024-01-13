from django.urls import path
from . import views

urlpatterns = [
    path('send_message/<str:recipient>/', views.send_message, name='send_message'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:message_id>/', views.message_detail, name='message_detail')
    # path('user-profile/add_skill', views.add_skill, name='add_skill'),
]