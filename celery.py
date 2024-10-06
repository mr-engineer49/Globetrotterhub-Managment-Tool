from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set default settings for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globetrotterhub.settings')

app = Celery('globetrotterhub')

# Load settings from Django settings file
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks in Django apps
app.autodiscover_tasks()
