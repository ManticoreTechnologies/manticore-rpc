""" Manticore Technologies LLC 
    (c) 2025
    Evrmore RPC Client
    __init__.py
"""

""" Import the configuration module """
from config import load_evrmore_conf

""" Load the Evrmore configuration """
evrmore_conf = load_evrmore_conf()

""" Set the authentication credentials """
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth(evrmore_conf['rpcuser'], evrmore_conf['rpcpassword'])

""" Set the URL for the Evrmore node """
url = f"http://{evrmore_conf['rpcbind']}:{evrmore_conf['rpcport']}"

""" Get the send command function """
from .lib.send import send

""" Define the test connection function """
def connected():
    """ Test the connection to the Evrmore node """
    try:
        send('getblockcount')
        return True
    except Exception as e:
        return False

""" Export the authentication credentials, URL, and send command function """
__all__ = [
    'auth',
    'url',
    'send',
    'connected'
]