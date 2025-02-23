from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Dados

@login_required
@permission_required('insights.view_arquivos_enviados', raise_exception=True)
def ia_import_list(request):
    data = {}
    data['dados'] = Dados.objects.all()
    return render(request, 'insights/ia_import_list.html', data)
