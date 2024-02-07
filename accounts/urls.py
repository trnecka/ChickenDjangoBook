from django.urls import path
from accounts import views

urlpatterns = [
    path('password_reset/', views.ChickenBookPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.ChickenBookPasswordResetDoneView.as_view(), name='password_reset_done'),    
    path('reset/<uidb64>/<token>/', views.ChickenBookPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', views.ChickenBookPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.RegistrationFormView.as_view(), name='registration'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),    
    path('password_change/', views.ChickenBookPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', views.ChickenBookPasswordChangeDoneView.as_view(), name='password_change_done'),
]
