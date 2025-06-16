import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# py -m celery -A config worker -l info
# celery -A config worker --beat --scheduler django --loglevel=info
# celery -A config beat -l info --scheduler django_celery_beat.schedulers:DatabaseSchedulern