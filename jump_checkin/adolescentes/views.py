from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import AdolescenteForm
from .models import Adolescente

def cadastrar_adolescente(request):
    if request.method == 'POST':
        form = AdolescenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_adolescentes')  # redireciona após salvar
    else:
        form = AdolescenteForm()
    return render(request, 'adolescentes/cadastro.html', {'form': form})

def listar_adolescentes(request):
    adolescentes = Adolescente.objects.all()
    return render(request, 'adolescentes/lista.html', {'adolescentes': adolescentes})
