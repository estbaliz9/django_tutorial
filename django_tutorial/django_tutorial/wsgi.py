"""
WSGI config for django_tutorial project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
import sys
import os
from django.core.wsgi import get_wsgi_application

# Añade la ruta base de tu proyecto (donde está manage.py)
sys.path.insert(0, '/home/estibaliz/python/django_tutorial')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutorial.settings')
application = get_wsgi_application()
