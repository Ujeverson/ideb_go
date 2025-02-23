from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.pessoa_list, name='pessoa_list'),
    path('create/', views.pessoa_create, name='pessoa_create'),
    path('update/<int:pk>/', views.pessoa_update, name='pessoa_update'),
    path('delete/<int:pk>/', views.pessoa_delete, name='pessoa_delete'),
]