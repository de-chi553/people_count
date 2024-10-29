from django.urls import path
from . import views

urlpatterns = [
    path('get-count/', views.get_people_count, name='get_people_count'),
    path('update-count/<int:count>/', views.update_people_count, name='update_people_count'),
]
