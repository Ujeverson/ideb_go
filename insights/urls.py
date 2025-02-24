from django.urls import path
from . import views

app_name = 'insights'

urlpatterns = [
    path('importar/', views.ia_import, name='ia_import'),
    path('lista/', views.ia_import_list, name='ia_import_list'),
    path('visualizar/<int:pk>/', views.visualizar_dados, name='visualizar_dados'),
    path('treinar/<int:pk>/', views.treinar_knn, name='treinar_knn'),
    path('grafico/', views.grafico_view, name='grafico'),
]