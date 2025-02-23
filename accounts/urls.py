from django.urls import path
from django.contrib.auth import views as auth_views

# Importaremos nossas views customizadas em breve

app_name = 'accounts'

urlpatterns = [
    # Usando as views prontas do Django:
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
