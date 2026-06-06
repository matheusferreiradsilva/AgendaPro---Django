# AgendaPro 🗓️

Sistema de agendamentos desenvolvido com **Django** e **PostgreSQL**, criado como projeto de portfólio para demonstrar habilidades em desenvolvimento web back-end.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.14**
- **Django 6.x**
- **PostgreSQL** (hospedado no Supabase)
- **Tailwind CSS** (via CDN)
- **Font Awesome** (ícones)

---

## 📋 Funcionalidades

- ✅ Criar agendamento com cadastro automático de cliente
- ✅ Listar agendamentos com busca por nome de cliente
- ✅ Editar agendamento (status, profissional, data e hora)
- ✅ Excluir agendamento com confirmação
- ✅ Painel administrativo Django

---

## 🧠 Conceitos Demonstrados

- **CRUD** completo (Create, Read, Update, Delete)
- **Function-Based Views (FBV)** — listagem com filtro de busca e criação de agendamento
- **Class-Based Views (CBV)** — `UpdateView` e `DeleteView`
- **ModelForm** com campos personalizados e widgets customizados
- **ForeignKey** e relacionamento entre models
- **`get_or_create`** para gerenciamento de clientes
- **`commit=False`** para manipulação de dados antes de salvar
- Filtro de busca com `__icontains` em campos relacionados
- Herança de templates com `{% extends %}` e `{% block %}`
- Proteção CSRF em formulários
- Variáveis de ambiente com `python-dotenv`

---

## 🖥️ Preview

<img width="1914" height="955" alt="print agendapro 3" src="https://github.com/user-attachments/assets/8437dac5-69f4-4326-aec0-8a7b979e2215" />
<img width="1914" height="952" alt="print agendapro 2" src="https://github.com/user-attachments/assets/3672c708-6287-4372-bc49-402d93d92c7c" />
<img width="1913" height="951" alt="print agendapro" src="https://github.com/user-attachments/assets/4d5d15b8-786e-4b11-a3e7-50d912a91c6b" />




---

## ⚙️ Como Rodar Localmente

```bash
# Clone o repositório
git clone https://github.com/matheusferreiradsilva/AgendaPro---Django.git
cd AgendaPro---Django

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
# Crie um arquivo .env na raiz com as seguintes variáveis:
SECRET_KEY=sua_secret_key
DB_NAME=postgres
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=seu_host
DB_PORT=5432

# Rode as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

---

## 🔗 Acesse o Projeto

> [*AgendaPro*](https://agendapro-django.onrender.com)

---

## 👨‍💻 Autor

**Matheus Ferreira**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matheus-ferreira-2718b8310/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/matheusferreiradsilva)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/_matheus_ferreira_silva/)
