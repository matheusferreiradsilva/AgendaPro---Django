from django.db import models
from django.core.exceptions import ValidationError

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

    def clean(self):
        if self.profissional_id and not self.profissional.ativo:
            raise ValidationError({'profissional': 'Este profissional está inativo.'})
        if (
            self.profissional_id
            and self.data_hora
            and Agendamento.objects.filter(
                profissional_id=self.profissional_id,
                data_hora=self.data_hora,
            ).exclude(pk=self.pk).exists()
        ):
            raise ValidationError({
                'data_hora': 'Este profissional já possui um agendamento neste horário.'
            })

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['profissional', 'data_hora'],
                name='unique_profissional_data_hora',
            ),
        ]