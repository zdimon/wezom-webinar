from channels.testing import WebsocketCommunicator
import pytest
from dj_prj.routing import application

def setup():
    print ("basic setup into module")

def teardown():
    print ("basic teardown into module")

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

