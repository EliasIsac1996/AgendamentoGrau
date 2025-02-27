from django import forms
from .models import Agendamento,Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'matricula', 'curso']


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['aluno', 'data_agendamento']