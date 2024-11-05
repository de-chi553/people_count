from django.http import JsonResponse
from .models import PeopleCounter

def UpdateCountView(request, current_count):
    PeopleCounter.objects.update_or_create(id=1, defaults={'count': current_count})
    return JsonResponse({'status': 'success', 'count': current_count})

def GetCountView(request):
    # 現在の人数を取得
    try:
        people_counter = PeopleCounter.objects.get(id=1)
        count = people_counter.count
    except PeopleCounter.DoesNotExist:
        count = 0
    return JsonResponse({'current_count': count})
