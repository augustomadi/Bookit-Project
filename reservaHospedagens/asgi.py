"""Módulo asgi."""

import os

from django.core.asgi import get_asgi_application

"""
ASGI config for reservaHospedagens project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reservaHospedagens.settings')

application = get_asgi_application()
