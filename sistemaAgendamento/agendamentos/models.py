# agendamentos/models.py
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)  # Relacionamento com Aluno
    data_agendamento = models.DateTimeField()

    def __str__(self):
        return f'{self.aluno.nome} - {self.data_agendamento}'