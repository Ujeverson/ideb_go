from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Importaremos nossas views customizadas em breve

app_name = 'accounts'

urlpatterns = [
    
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('profile/', views.profile_view, name='profile'),
    #path('register/', views.register, name='register'),
]
