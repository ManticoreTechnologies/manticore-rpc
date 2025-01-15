""" Manticore Technologies LLC 
    (c) 2025
    Evrmore RPC Client
    lib/send.py
"""

""" Import the necessary modules """
from .. import auth, url
import requests
from requests.exceptions import ConnectionError, HTTPError, InvalidURL
from json import JSONDecodeError
from .err import EvrmoreConnectionError, EvrmoreAuthenticationError, EvrmoreURLError, EvrmoreInternalServerError
""" Define the send function """
def send(command, params=[]):

    """ Generate the JSON-RPC payload """
    payload = {
        "jsonrpc": "2.0", 
        "id": "curltext", 
        "method": command, 
        "params": params
    }

    """ Set the headers """
    headers = {"Content-Type": "text/plain"}

    try:
        # Example request to localhost:8332
        response = requests.post(url, json=payload, headers=headers, auth=auth)

        """ Raise an exception if the response is not successful """
        response.raise_for_status()
        
        """ Return the response as JSON """
        try:
            return response.json()['result']
        except Exception as e:
            print(e)    
            return response.text
        
    except ConnectionError as e:
        """ We failed to connect to the Evrmore node """
        raise EvrmoreConnectionError("Failed to connect to the Evrmore node at " + url + " | Is the node running?")
    except HTTPError as e:
        """ We failed to authenticate with the Evrmore node """
        if e.response.status_code == 401:
            raise EvrmoreAuthenticationError("Invalid credentials provided for the Evrmore node at " + url + " | Check your credentials in evrmore.conf file")
        elif e.response.status_code == 500:
            """ There was an internal server error """
            error = response.json()['error']
            error_code = error['code']
            error_message = error['message']
            raise EvrmoreInternalServerError(f"Internal server error: {error_code} | {error_message}")
    except InvalidURL as e:
        """ We failed parse the URL """
        raise EvrmoreURLError("Failed to parse the URL at " + url + " | Check your URL in evrmore.conf file")
    except Exception as e:
        """ We failed to send the command to the Evrmore node """
        raise e



    