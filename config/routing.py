from django.conf.urls import url

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from tiveU.messager.consumers import MessagerConsumer
from tiveU.notifications.consumers import NotificationsConsumer
# from tiveU.notifications.routing import notifications_urlpatterns
# from tiveU.messager.routing import messager_urlpatterns

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                url(r'^notifications/$', NotificationsConsumer),
                url(r'^(?P<username>[^/]+)/$', MessagerConsumer),
            ])
        ),
    ),
})
