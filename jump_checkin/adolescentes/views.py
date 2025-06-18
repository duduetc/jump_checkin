from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AdolescenteForm
from .models import Adolescente

@login_required
def cadastrar_adolescente(request):
    if request.method == 'POST':
        form = AdolescenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Adolescente cadastrado com sucesso!')
            return redirect('listar_adolescentes')
    else:
        form = AdolescenteForm()
    return render(request, 'adolescentes/cadastro.html', {'form': form})

@login_required
def listar_adolescentes(request):
    adolescentes = Adolescente.objects.all()
    return render(request, 'adolescentes/lista.html', {'adolescentes': adolescentes})

@login_required
def editar_adolescente(request, id):
    adolescente = get_object_or_404(Adolescente, id=id)
    if request.method == 'POST':
        form = AdolescenteForm(request.POST, request.FILES, instance=adolescente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Adolescente atualizado com sucesso!')
            return redirect('listar_adolescentes')
    else:
        form = AdolescenteForm(instance=adolescente)
    return render(request, 'adolescentes/cadastro.html', {'form': form})

@login_required
def excluir_adolescente(request, id):
    adolescente = get_object_or_404(Adolescente, id=id)
    if request.method == 'POST':
        adolescente.delete()
        messages.success(request, 'Adolescente excluído com sucesso!')
        return redirect('listar_adolescentes')
    return render(request, 'adolescentes/confirmar_exclusao.html', {'adolescente': adolescente})