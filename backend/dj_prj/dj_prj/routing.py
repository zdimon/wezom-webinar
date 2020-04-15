from channels.routing import ProtocolTypeRouter


from django.urls import re_path

from account.consumer import OnlineConsumer

websocket_urlpatterns = [
    re_path(r'online/$', OnlineConsumer),
]

from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})