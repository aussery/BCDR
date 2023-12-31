from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from BCDR import consumers  

websocket_urlpatterns = [
    path('ws/updates/', consumers.YourConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})
