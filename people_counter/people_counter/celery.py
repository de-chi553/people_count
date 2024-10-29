# people_counter/celery.py

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'people_counter.settings')

app = Celery('people_counter')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
