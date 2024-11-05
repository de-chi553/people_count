#people_count/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Djangoの設定モジュールを環境変数として設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'people_count.settings')

# プロジェクトのCeleryアプリケーションのインスタンスを作成
app = Celery('people_count')

# Djangoの設定から読み込む
app.config_from_object('django.conf:settings', namespace='CELERY')

# Djangoのすべてのアプリケーション内のtasks.pyを自動的に探索する
app.autodiscover_tasks()
