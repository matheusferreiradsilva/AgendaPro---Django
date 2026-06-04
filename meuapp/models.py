from django.db import models

# Create your models here.
class Profissional(models.Model):
    #model do profissional
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        #muda como a informação desse model vai aparecer
        return f'{self.nome.capitalize()} - {self.especialidade.capitalize()}'
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100, editable=True)
    whatsapp = models.CharField(max_length=20, editable=True)
    email = models.EmailField(unique=True, editable=True)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    class Status(models.TextChoices):
        #configuração do choice usado no status
        AGENDADO = 'Agendado'
        CONCLUIDO = 'Concluído'
        CANCELADO = 'Cancelado'
    nome = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.AGENDADO)

    def __str__(self):
        return f'CLIENTE-{self.nome} - STATUS:{self.status} - HORÁRIO:{self.data_hora}'