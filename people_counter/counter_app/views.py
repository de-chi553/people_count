from django.http import JsonResponse
from .models import PeopleCount

# 人数を取得するビュー
def get_people_count(request):
    count_instance = PeopleCount.objects.last()  # 最新のカウントを取得
    if count_instance:
        return JsonResponse({"people_count": count_instance.count})
    else:
        return JsonResponse({"people_count": 0})

# 人数を更新するビュー
def update_people_count(request, count):
    count_instance = PeopleCount.objects.last()
    if count_instance:
        count_instance.count = count
        count_instance.save()
    else:
        PeopleCount.objects.create(count=count)
    return JsonResponse({"status": "success", "updated_count": count})
