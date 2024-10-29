# counter_app/tasks.py

from celery import shared_task
from .models import PeopleCount

@shared_task
def reset_people_count():
    count_instance = PeopleCount.objects.last()
    if count_instance:
        count_instance.count = 0
        count_instance.save()
