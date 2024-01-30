from django.urls import path
from . import views

urlpatterns = [
    path('', views.chicken_book, name='chicken-book'),
    path('user-profile', views.user_profile, name='user_profile'),

    path('user-profile/skills', views.skill_list, name='skill_list'),
    path('user-profile/projects', views.project_list, name='project_list'),
    path('user_info/<str:user_id>/', views.user_info, name='user_info'),
    # path('user-profile/add_skill', views.add_skill, name='add_skill'),
    path('api/users/', views.users_api_view, name='users_api_view'),
    path('api/users/download/', views.users_api_download, name='users_api_download'),
    path('edit-profile-form', views.edit_profile_form, name='edit_profile_form'),
    path('about-project', views.about_project, name='about_project'),
    path('confirm-delete', views.confirm_delete, name='confirm_delete'),
    path('bye', views.bye_page, name='bye'),
    path('wrong-password', views.wrong_password, name='wrong_password'),
    path('acc-delete', views.acc_delete, name='acc_delete')

]