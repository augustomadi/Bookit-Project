# Configuração de Timezone - reservaHospedagens

## Problema Identificado
Quando o servidor roda em nuvens estrangeiras (AWS, Google Cloud, etc.), o timezone padrão pode ser UTC, causando problemas com horários brasileiros.

## Solução Implementada

### 1. Configurações no settings.py
```python
TIME_ZONE = os.environ.get('TIME_ZONE', 'America/Sao_Paulo')
LANGUAGE_CODE = 'pt-br'
USE_TZ = True
USE_L10N = True

# Formatos de data brasileiros
DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'
DATE_FORMAT = '%d/%m/%Y'
TIME_FORMAT = '%H:%M:%S'
```

### 2. Uso Correto nos Modelos
Os modelos já estão usando `timezone.now()` corretamente:
```python
from django.utils import timezone

created_at = models.DateTimeField(default=timezone.now)
updated_at = models.DateTimeField(auto_now=True)
```

### 3. Configuração de Ambiente
Use o arquivo `env.example` como base para criar seu `.env`:

```bash
# Copie o arquivo de exemplo
cp env.example .env

# Edite o .env com suas configurações
TIME_ZONE=America/Sao_Paulo
SECRET_KEY=sua-chave-secreta
DEBUG=False  # Para produção
```

## Timezones Brasileiros Disponíveis
- `America/Sao_Paulo` - Horário de Brasília (padrão)
- `America/Manaus` - Horário do Amazonas
- `America/Belem` - Horário do Pará
- `America/Fortaleza` - Horário do Nordeste
- `America/Recife` - Horário de Recife

## Verificação
Para verificar se está funcionando:
```python
from django.utils import timezone
print(timezone.now())  # Deve mostrar horário de Brasília
```

## Configurações de Produção
O projeto agora está configurado para produção com:
- ✅ Variáveis de ambiente
- ✅ Configurações de segurança automáticas
- ✅ Logging configurado
- ✅ Static files configurados
- ✅ Timezone brasileiro

## Comandos Úteis
```bash
# Instalar dependências
pip install -r requirements.txt

# Ver timezone atual do sistema
python manage.py shell
>>> from django.utils import timezone
>>> timezone.now()

# Coletar static files (produção)
python manage.py collectstatic
``` 