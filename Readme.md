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
- **Documentação Completa**: [Postman Documentation](https://documenter.getpostman.com/view/43303618/2sB2x9jqWr)

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

## 🧪 Testes e Qualidade

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

## 📝 API Endpoints - Documentação Completa

### 🔗 **Base URL**: `http://127.0.0.1:8000`

---

### 🏠 **PROPRIEDADES (Properties)**

#### **Listar Propriedades**
```http
GET /properties/
```

**Parâmetros de Filtro:**
- `address_city` (string) - Filtrar por cidade
- `address_state` (string) - Filtrar por estado
- `country` (string) - Filtrar por país
- `capacity` (number) - Capacidade mínima
- `price_per_night` (number) - Preço máximo por noite

**Exemplo de Resposta:**
```json
[
    {
        "id": 1,
        "title": "Casa na Praia",
        "address_street": "Rua das Palmeiras",
        "address_number": "123",
        "address_neighborhood": "Centro",
        "address_city": "Florianópolis",
        "address_state": "SC",
        "country": "BRA",
        "rooms": 3,
        "capacity": 6,
        "price_per_night": "250.00",
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-15T10:30:00Z"
    }
]
```

#### **Criar Propriedade**
```http
POST /properties/
```

**Body:**
```json
{
    "title": "Apartamento no Centro",
    "address_street": "Rua das Flores",
    "address_number": "456",
    "address_neighborhood": "Centro",
    "address_city": "São Paulo",
    "address_state": "SP",
    "country": "BRA",
    "rooms": 2,
    "capacity": 4,
    "price_per_night": "180.00"
}
```

#### **Detalhes da Propriedade**
```http
GET /properties/{id}/
```

#### **Atualizar Propriedade**
```http
PUT /properties/{id}/
PATCH /properties/{id}/
```

#### **Deletar Propriedade**
```http
DELETE /properties/{id}/
```

**Resposta:**
```json
{
    "message": "Propriedade 'Nome da Propriedade' deletada."
}
```

---

### 📅 **RESERVAS (Reservations)**

#### **Listar Reservas**
```http
GET /reservations/
```

**Parâmetros de Filtro:**
- `client_email` (string) - Filtrar por email do cliente
- `property_id` (number) - Filtrar por propriedade

**Exemplo de Resposta:**
```json
[
    {
        "id": 1,
        "property_id": 1,
        "client_name": "João Silva",
        "client_email": "joao@email.com",
        "start_date": "2024-02-01",
        "end_date": "2024-02-05",
        "guests_quantity": 4,
        "created_at": "2024-01-20T14:30:00Z",
        "updated_at": "2024-01-20T14:30:00Z"
    }
]
```

#### **Criar Reserva**
```http
POST /reservations/
```

**Body:**
```json
{
    "property_id": 1,
    "client_name": "Maria Santos",
    "client_email": "maria@email.com",
    "start_date": "2024-03-01",
    "end_date": "2024-03-05",
    "guests_quantity": 3
}
```

**Validações Automáticas:**
- ✅ Propriedade existe
- ✅ Capacidade suficiente
- ✅ Período disponível
- ✅ Datas válidas

**Possíveis Erros:**
```json
{
    "error": "Propriedade não encontrada"
}
```
```json
{
    "error": "Número de hóspedes excede a capacidade máxima da propriedade"
}
```
```json
{
    "error": "A propriedade não está disponível para o período solicitado"
}
```

#### **Detalhes da Reserva**
```http
GET /reservations/{id}/
```

#### **Atualizar Reserva**
```http
PUT /reservations/{id}/
PATCH /reservations/{id}/
```

#### **Cancelar Reserva**
```http
DELETE /reservations/{id}/
```

**Resposta:**
```json
{
    "message": "Reserva de Nome do Cliente cancelada com sucesso."
}
```

---

### 🔍 **VERIFICAR DISPONIBILIDADE**

#### **Verificar Disponibilidade de Propriedade**
```http
GET /properties/availability
```

**Parâmetros:**
- `property_id` (number) - ID da propriedade
- `start_date` (date) - Data de início (YYYY-MM-DD)
- `end_date` (date) - Data de fim (YYYY-MM-DD)
- `guests_quantity` (number) - Quantidade de hóspedes

**Exemplo de Uso:**
```
GET /properties/availability?property_id=1&start_date=2024-02-01&end_date=2024-02-05&guests_quantity=4
```

**Resposta - Disponível:**
```json
{
    "available": true
}
```

**Resposta - Indisponível:**
```json
{
    "available": false,
    "error": "Propriedade indisponível para o período solicitado."
}
```

**Possíveis Erros:**
```json
{
    "available": false,
    "error": "Propriedade não encontrada."
}
```
```json
{
    "available": false,
    "error": "Número de hóspedes excede a capacidade máxima."
}
```

---

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

## 📊 **Exemplos de Uso**

### **Filtrar Propriedades por Cidade e Preço**
```bash
curl "http://127.0.0.1:8000/properties/?address_city=Florianópolis&price_per_night=300"
```

### **Buscar Reservas por Email**
```bash
curl "http://127.0.0.1:8000/reservations/?client_email=joao@email.com"
```

### **Verificar Disponibilidade**
```bash
curl "http://127.0.0.1:8000/properties/availability?property_id=1&start_date=2024-02-01&end_date=2024-02-05&guests_quantity=4"
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

---

**📖 Documentação Completa**: [Postman Collection](https://documenter.getpostman.com/view/43303618/2sB2x9jqWr)
