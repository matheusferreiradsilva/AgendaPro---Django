from django.contrib import admin
from . import models

#list_display — campos que aparecem na listagem
#list_filter — filtros na lateral direita
#search_fields — barra de busca
#reandoly_fields - trava campos editaveis para apenas leitura

@admin.register(models.Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display= ['nome', 'especialidade','ativo']

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display= ['nome', 'whatsapp','email']

@admin.register(models.Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display= ['nome', 'profissional','data_hora', 'status']