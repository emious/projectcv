"""
ASGI config for projectcv project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
#
# import os
#
# from django.core.asgi import get_asgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectcv.settings')
#
# application = get_asgi_application()
#
# projectcv/asgi.py
#
# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from main import routing  # Import your routing configuration from the app
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectcv.settings')
#
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             routing.websocket_urlpatterns  # Add your websocket URLs
#         )
#     ),
# })

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from main.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectcv.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})