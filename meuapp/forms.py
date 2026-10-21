from django import forms
from .models import Agendamento, Profissional


class FormularioAgendamento(forms.ModelForm):
    nome_cliente = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'bg-gray-700 text-white rounded p-2'}))
    whatsapp = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'bg-gray-700 text-white rounded p-2'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'bg-gray-700 text-white rounded p-2'}))
    class Meta:
        model = Agendamento
        fields = ['profissional', 'data_hora']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'bg-gray-700 text-white rounded p-2'}),
            'profissional': forms.Select(attrs={'class': 'bg-gray-700 text-white rounded p-2'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profissional'].queryset = Profissional.objects.filter(ativo=True)

    def clean_email(self):
        return self.cleaned_data['email'].strip().lower()

class CadastrarProfissional(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'especialidade']

class FormularioEditar(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['profissional', 'data_hora', 'status']
        widgets = {
            'profissional': forms.Select(attrs={'class': 'bg-gray-700 text-white rounded p-2'}),
            'data_hora': forms.DateTimeInput( format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local', 'class': 'bg-gray-700 text-white rounded p-2'}),
            'status': forms.Select(attrs={'class': 'bg-gray-700 text-white rounded p-2'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profissional'].queryset = Profissional.objects.filter(ativo=True)
