#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependências
pip install -r requirements.txt

# Coletar arquivos estáticos
python jump_checkin/manage.py collectstatic --no-input

# Executar migrações
python jump_checkin/manage.py migrate