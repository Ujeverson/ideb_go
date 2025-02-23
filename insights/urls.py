from django.urls import path
from . import views

app_name = 'insights'  

urlpatterns = [
    path('importar/', views.ia_import, name='ia_import'),
    path('lista/', views.ia_import_list, name='ia_import_list'),
]