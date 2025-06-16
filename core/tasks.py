import time
from celery import shared_task

@shared_task
def export_data():
    print('start')
    time.sleep(4)
    print('end')