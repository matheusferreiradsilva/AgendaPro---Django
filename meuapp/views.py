from django.shortcuts import render
from .models import Agendamento, Cliente
from django.shortcuts import redirect
from .forms import FormularioAgendamento, CadastrarProfissional
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def agendamentos(request):
    agendamento = Agendamento.objects.all()
    busca = request.GET.get('q', '') #essa variavel retorna false. string vazia == false
    if busca:
        agendamento = agendamento.filter(nome__nome__icontains=busca) #nomeforeignkey__nomemodelcliente__ignora maiuscula/minuscula=compara com a busca. __serve como um fio que liga uma informação a outra
    return render(request, 'meuapp/agendamentos.html', {'agendamentos': agendamento})

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
            cliente, criado = Cliente.objects.get_or_create(
                email=email,
                defaults={'nome': nome, 'whatsapp': whatsapp}
            )
            #se o cliente não existir, cria ele e salva os dados
            # ...
            # antes de redirecionar faz um save false(commit=False) liga o nome do cliente ao agendamento feito e segue
            agendamento = form.save(commit=False)
            agendamento.nome = cliente
            agendamento.save()
            return redirect('home')

    #se for GET ou qualquer outro metodo abre um formulario em branco
    else:
        form = FormularioAgendamento()

    return render(request, "meuapp/agendar.html", {"form": form})

def cadastro_profissional(request):
    if request.method == "POST":
        form = CadastrarProfissional(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CadastrarProfissional()
    
    return render(request, "meuapp/cadastrar_profissional.html", {"form": form})


class AgendamentoUpdate(UpdateView):
    model = Agendamento
    fields = ['profissional', 'data_hora', 'status']
    template_name = 'meuapp/editar_agendamento.html'
    success_url = reverse_lazy('agendamentos')

class ApagarAgendamento(DeleteView):
    model = Agendamento
    template_name = 'meuapp/excluir_agendamento.html'
    success_url = reverse_lazy('agendamentos')