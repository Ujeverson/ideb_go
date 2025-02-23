from django.shortcuts import render

def home_view(request):
    return render(request, 'core/home.html')

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
@login_required
def minha_view_protegida(request):
    return render(request, 'minha_template.html')

@login_required
@permission_required('insights.view_arquivos_enviados', raise_exception=True)
def ia_import_list(request):
    data = {}
    data['dados'] = Dados.objects.all()
    return render(request, 'insights/ia_import_list.html', data)