from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Agendamento, Cliente, Profissional


class AgendaTests(TestCase):
    def setUp(self):
        self.staff = get_user_model().objects.create_user(
            username='admin',
            password='strong-password',
            is_staff=True,
        )
        self.profissional = Profissional.objects.create(
            nome='Dra. Ana',
            especialidade='Clínica',
        )
        self.data_hora = timezone.localtime(timezone.now() + timedelta(days=1)).replace(
            second=0,
            microsecond=0,
        )

    def criar_agendamento(self, email='cliente@example.com'):
        cliente = Cliente.objects.create(
            nome='Cliente',
            whatsapp='11999999999',
            email=email,
        )
        return Agendamento.objects.create(
            nome=cliente,
            profissional=self.profissional,
            data_hora=self.data_hora,
        )

    def test_agendamento_publico_cria_cliente_e_redireciona(self):
        response = self.client.post(reverse('agendar'), {
            'profissional': self.profissional.pk,
            'data_hora': self.data_hora.strftime('%Y-%m-%dT%H:%M'),
            'nome_cliente': 'Novo Cliente',
            'whatsapp': '11988887777',
            'email': 'novo@example.com',
        })

        self.assertRedirects(response, reverse('home'))
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Agendamento.objects.count(), 1)

    def test_listagem_exige_login(self):
        response = self.client.get(reverse('agendamentos'))
        self.assertRedirects(
            response,
            f'{reverse("login")}?next={reverse("agendamentos")}',
        )

    def test_edicao_e_exclusao_exigem_staff(self):
        agendamento = self.criar_agendamento()
        self.client.login(username='admin', password='strong-password')
        self.client.post(reverse('editar_agendamento', args=[agendamento.pk]), {
            'profissional': self.profissional.pk,
            'data_hora': (self.data_hora + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M'),
            'status': Agendamento.Status.CONCLUIDO,
        })
        self.assertEqual(
            Agendamento.objects.get(pk=agendamento.pk).status,
            Agendamento.Status.CONCLUIDO,
        )
        response = self.client.post(reverse('excluir_agendamento', args=[agendamento.pk]))
        self.assertRedirects(response, reverse('agendamentos'))
        self.assertFalse(Agendamento.objects.filter(pk=agendamento.pk).exists())

    def test_nao_permite_horario_duplicado(self):
        self.criar_agendamento()
        response = self.client.post(reverse('agendar'), {
            'profissional': self.profissional.pk,
            'data_hora': self.data_hora.strftime('%Y-%m-%dT%H:%M'),
            'nome_cliente': 'Outro Cliente',
            'whatsapp': '11888887777',
            'email': 'outro@example.com',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Agendamento.objects.count(), 1)

    def test_profissional_inativo_nao_aparece_no_formulario(self):
        self.profissional.ativo = False
        self.profissional.save(update_fields=['ativo'])
        response = self.client.get(reverse('agendar'))
        self.assertNotContains(response, 'Dra. Ana')
