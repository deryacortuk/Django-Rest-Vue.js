from __future__ import absolute_import, unicode_literals
import os
import sys
from celery import Celery
from django.conf import settings
import logging

logger = logging.getLogger("Celery")

import dotenv

env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), '.env')
dotenv.read_dotenv(env_file)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")
app = Celery("service",broker='redis://redis:6379/0')
app.config_from_object("django.conf:settings",namespace="CELERY")
app.conf.enable_utc=True

app.conf.update(
    CELERY_ACCEPT_CONTENT = ['json'],
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_RESULT_SERIALIZER = 'json',
)