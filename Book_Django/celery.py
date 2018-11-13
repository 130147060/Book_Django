from __future__ import absolute_import

import os
from celery import Celery

from Book_Django import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Book_Django.settings')

app = Celery('django_proj', backend='redis', broker=settings.CELERY_BROKER_URL)

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)