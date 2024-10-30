from django.http import JsonResponse
from .models import PeopleCounter

def UpdateCountView(request, current_count):
    # Update the count in the database
    PeopleCounter.objects.update_or_create(id=1, defaults={'count': current_count})
    return JsonResponse({'status': 'success', 'count': current_count})
