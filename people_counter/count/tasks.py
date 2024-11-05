from celery import shared_task
from .models import PeopleCounter

@shared_task
def reset_people_count():
    PeopleCounter.objects.update_or_create(id=1, defaults={'count': 0})
