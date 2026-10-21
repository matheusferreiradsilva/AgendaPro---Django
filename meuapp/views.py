from django.shortcuts import render
from django.contrib import messages
from .models import Agendamento, Cliente
from django.shortcuts import redirect
from .forms import FormularioAgendamento, CadastrarProfissional, FormularioEditar
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import IntegrityError, transaction
from django.urls import reverse_lazy
from django.core.paginator import Paginator
# Create your views here.

def staff_required(view):
    return user_passes_test(lambda user: user.is_staff)(view)

@login_required
def agendamentos(request):
    agendamento = Agendamento.objects.select_related('nome', 'profissional').order_by('data_hora')
    busca = request.GET.get('q', '') #essa variavel retorna false. string vazia == false
    if busca:
        agendamento = agendamento.filter(nome__nome__icontains=busca) #nomeforeignkey__nomemodelcliente__ignora maiuscula/minuscula=compara com a busca. __serve como um fio que liga uma informação a outra
    paginator = Paginator(agendamento, 20)
    pagina = paginator.get_page(request.GET.get('page'))
    return render(request, 'meuapp/agendamentos.html', {'agendamentos': pagina})

def home(request):
    return render(request, 'meuapp/home.html')



def agendar(request):
    # se for POST
    if request.method == "POST":
        #cria a instancia do formulario e preenche com os dados do request
        form = FormularioAgendamento(request.POST)
        # checa se é valido
        if form.is_valid():
            nome = form.cleaned_data['nome_cliente']
            whatsapp = form.cleaned_data['whatsapp']
            email = form.cleaned_data['email']
            try:
                with transaction.atomic():
                    cliente = Cliente.objects.filter(email__iexact=email).first()
                    criado = cliente is None
                    if criado:
                        cliente = Cliente.objects.create(
                            email=email,
                            nome=nome,
                            whatsapp=whatsapp,
                        )
                    if not criado and (cliente.nome != nome or cliente.whatsapp != whatsapp):
                        cliente.nome = nome
                        cliente.whatsapp = whatsapp
                        cliente.save(update_fields=['nome', 'whatsapp'])

                    agendamento = form.save(commit=False)
                    agendamento.nome = cliente
                    agendamento.save()
            except IntegrityError:
                form.add_error(
                    'data_hora',
                    'Este profissional já possui um agendamento neste horário.',
                )
                return render(request, "meuapp/agendar.html", {"form": form})
            messages.success(request, 'Agendamento feito com sucesso!')
            return redirect('home')

    #se for GET ou qualquer outro metodo abre um formulario em branco
    else:
        form = FormularioAgendamento()

    return render(request, "meuapp/agendar.html", {"form": form})

@staff_required
def cadastro_profissional(request):
    if request.method == "POST":
        form = CadastrarProfissional(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CadastrarProfissional()

    return render(request, "meuapp/cadastrar_profissional.html", {"form": form})


class AgendamentoUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Agendamento
    form_class = FormularioEditar
    template_name = 'meuapp/editar_agendamento.html'
    success_url = reverse_lazy('agendamentos')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        # Em CBVs, usamos 'self.request' em vez de apenas 'request'
        messages.success(self.request, 'Agendamento editado!')

        # Chama o comportamento padrão que salva o formulário e redireciona para o success_url
        return super().form_valid(form)

class ApagarAgendamento(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Agendamento
    template_name = 'meuapp/excluir_agendamento.html'
    success_url = reverse_lazy('agendamentos')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, 'Agendamento excluído!')
        return super().form_valid(form)