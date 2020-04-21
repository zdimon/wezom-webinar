## Test socket connection.

### Requirements.

    pytest==5.4.0
    pytest-django==3.9.0
    pytest-asyncio==0.11.0
    channels==2.4.0
    djangochannelsrestframework==0.0.5

## Install channels.

    INSTALLED_APPS = [
        ...
        'channels',
    ]




Create a new file pytest.ini

    [pytest]
    DJANGO_SETTINGS_MODULE = dj_prj.settings
    python_files = */tests/test_*.py

### Create a new test in account/tests/test_socket.py


    from channels.testing import WebsocketCommunicator
    import pytest
    from dj_prj.routing import application

    @pytest.mark.asyncio
    async def test_socket_connection():
        communicator = WebsocketCommunicator(
            application=application,
            path='/online/',
            headers=[(
                b'cookie',
                f'sessionid=test'.encode('ascii')
            )]
        )
        connected, _ = await communicator.connect()
        assert connected is True
        await communicator.disconnect()


### Run test

    pytest

Result.

    ModuleNotFoundError: No module named 'dj_prj.routing'

Create a new dj_prj/routing.py and define routing application.


    from channels.routing import ProtocolTypeRouter


    from django.urls import re_path

    from account.consumer import OnlineConsumer

    websocket_urlpatterns = [
        re_path(r'online/$', OnlineConsumer),
    ]

    from channels.auth import AuthMiddlewareStack
    from channels.routing import URLRouter

    application = ProtocolTypeRouter({
        'websocket': AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        ),
    })

Add ASGI_APPLICATION in settings.py.

    ASGI_APPLICATION = "dj_prj.routing.application"

Create the consumer.

    # account/consumer.py

    import json
    from channels.generic.websocket import WebsocketConsumer

    class OnlineConsumer(WebsocketConsumer):
        def connect(self):
            print('websocket connecting')
            self.accept()

        def disconnect(self, close_code):
            pass

        def receive(self, text_data):
            text_data_json = json.loads(text_data)
            print(text_data_json)


Run test with printing out.

    pytest -s





