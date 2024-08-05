# from channels.routing import URLRouter, ProtocolTypeRouter
# from django.urls import re_path, path
# from main import consumers
#
# websocket_urlpatterns = [
#     re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
# ]

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
]