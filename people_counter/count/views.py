from django.http import JsonResponse
from .models import PeopleCounter
from django.shortcuts import redirect

def redirect_to_get_count(request):
    return redirect('get_count')  # 名前付きURLを使って`/counter/get-count/` へリダイレクト


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
