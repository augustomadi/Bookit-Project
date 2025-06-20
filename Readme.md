# ReservaHospedagens - Sistema de Reservas de Hospedagem

Sistema de gerenciamento de reservas de hospedagem desenvolvido em Django REST Framework.

## 🚀 Características

- ✅ API REST completa para propriedades e reservas
- ✅ Validação de disponibilidade e capacidade
- ✅ Filtros avançados por localização e preço
- ✅ Timezone brasileiro configurado
- ✅ Linter configurado (flake8)
- ✅ Configurações de produção prontas
- ✅ Logging configurado
- ✅ Segurança implementada

## 🛠️ Tecnologias

- **Django 5.2.3** - Framework web
- **Django REST Framework** - API REST
- **Django Filter** - Filtros avançados
- **SQLite/PostgreSQL** - Banco de dados
- **Flake8** - Linter de código

## 📋 Pré-requisitos

- Python 3.8+
- pip

## 🔧 Instalação

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd reservaHospedagens
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente**
```bash
# Copie o arquivo de exemplo
cp env.example .env

# Edite o .env com suas configurações
```

4. **Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crie um superusuário (opcional)**
```bash
python manage.py createsuperuser
```

6. **Execute o servidor**
```bash
python manage.py runserver
```

## 🌐 Acesso

- **Admin Django**: http://127.0.0.1:8000/admin/
- **API REST**: http://127.0.0.1:8000/api/

## 📁 Estrutura do Projeto

```
reservaHospedagens/
├── propriedades/          # App de propriedades
│   ├── models/           # Modelos de dados
│   ├── views/            # ViewSets e APIs
│   ├── serializers/      # Serializers da API
│   └── filters/          # Filtros personalizados
├── reservas/             # App de reservas
│   ├── models/           # Modelos de dados
│   ├── views/            # ViewSets e APIs
│   ├── serializers/      # Serializers da API
│   ├── services/         # Lógica de negócio
│   └── filters/          # Filtros personalizados
├── reservaHospedagens/   # Configurações do projeto
├── logs/                 # Arquivos de log
├── staticfiles/          # Arquivos estáticos (produção)
└── requirements.txt      # Dependências
```

## 🔒 Configuração de Produção

O projeto está configurado para produção com:

- **Variáveis de ambiente** para configurações sensíveis
- **Configurações de segurança** automáticas
- **Logging** configurado
- **Static files** configurados
- **Timezone brasileiro** configurado

### Variáveis de Ambiente para Produção

```bash
# .env
DEBUG=False
SECRET_KEY=sua-chave-secreta-muito-segura
ALLOWED_HOSTS=seudominio.com,www.seudominio.com

# Banco PostgreSQL
DB_ENGINE=django.db.backends.postgresql
DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432

# Timezone
TIME_ZONE=America/Sao_Paulo
```

## �� Testes e Qualidade

### Linter
```bash
# Executar linter
python lint.py

# Ou diretamente
flake8 .
```

### Verificação do Django
```bash
python manage.py check
```

## 📝 API Endpoints

### Propriedades
- `GET /api/properties/` - Listar propriedades
- `POST /api/properties/` - Criar propriedade
- `GET /api/properties/{id}/` - Detalhes da propriedade
- `PUT /api/properties/{id}/` - Atualizar propriedade
- `DELETE /api/properties/{id}/` - Deletar propriedade

### Reservas
- `GET /api/reservations/` - Listar reservas
- `POST /api/reservations/` - Criar reserva
- `GET /api/reservations/{id}/` - Detalhes da reserva
- `PUT /api/reservations/{id}/` - Atualizar reserva
- `DELETE /api/reservations/{id}/` - Cancelar reserva

### Disponibilidade
- `GET /api/properties/availability/` - Verificar disponibilidade

## 🔧 Comandos Úteis

```bash
# Verificar status do projeto
python manage.py check

# Shell do Django
python manage.py shell

# Coletar static files (produção)
python manage.py collectstatic

# Executar testes
python manage.py test

# Ver logs
tail -f logs/django.log
```

## 📄 Licença

Este projeto está sob a licença MIT.

## 👥 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para suporte, envie um email ou abra uma issue no repositório.