"""
URL configuration for people_count project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from count.views import UpdateCountView, GetCountView, reset_count_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('counter/update-count/<int:current_count>/', UpdateCountView, name='update_count'),
    path('counter/get-count/', GetCountView, name='get_count'),  # 人数取得用のURL
    path('counter/reset-count/', reset_count_view, name='reset_count'),  # リセット用エンドポイント
]
