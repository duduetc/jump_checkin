from django import forms
from .models import Adolescente

class AdolescenteForm(forms.ModelForm):
    class Meta:
        model = Adolescente
        fields = ['nome', 'sobrenome', 'foto', 'data_nascimento', 'genero', 'pg', 'data_inicio']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
        }