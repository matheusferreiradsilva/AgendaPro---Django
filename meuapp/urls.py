from django.urls import path
from django.contrib.auth import views as auth_views
from .views import agendamentos, home, agendar, cadastro_profissional, AgendamentoUpdate, ApagarAgendamento
urlpatterns = [
    path('home/', home, name='home'),
    path('agendamentos/', agendamentos, name='agendamentos'),
    path('agendar/', agendar, name='agendar'),
    path('cadastro_profissional/', cadastro_profissional, name='cadastro_profissional'),
    path('agendamento/<int:pk>/editar/', AgendamentoUpdate.as_view(), name = 'editar_agendamento'),
    path('agendamento/<int:pk>/excluir/', ApagarAgendamento.as_view(), name = 'excluir_agendamento'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]