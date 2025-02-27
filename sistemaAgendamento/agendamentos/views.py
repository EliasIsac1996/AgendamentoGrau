from django.shortcuts import render, redirect
from .forms import AlunoForm, AgendamentoForm
from django.http import HttpResponse
from .models import Aluno

def agendar(request):
    if request.method == 'POST':
        aluno_form = AlunoForm(request.POST)
        agendamento_form = AgendamentoForm(request.POST)
        
        if aluno_form.is_valid() and agendamento_form.is_valid():
            # Salvar o aluno
            aluno = aluno_form.save()

            # Associar o aluno ao agendamento
            agendamento = agendamento_form.save(commit=False)
            agendamento.aluno = aluno
            agendamento.save()

            return redirect('sucesso')
    else:
        aluno_form = AlunoForm()
        agendamento_form = AgendamentoForm()

    return render(request, 'agendamentos/agendar.html', {'aluno_form': aluno_form, 'agendamento_form': agendamento_form})

def sucesso(request):
    return render(request, 'agendamentos/sucesso.html')