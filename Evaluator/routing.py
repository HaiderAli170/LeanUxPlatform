# Evaluator/routing.py
from django.urls import re_path
from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/some_path/$', consumer.FacialExpressionConsumer.as_asgi()),
]
