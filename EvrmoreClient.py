import logging
import colorlog
import requests
from setupLogging import setupLogging

class EvrmoreClient:
    
    logger_initialized = False
    
    def __init__(self):
        host = "127.0.0.1:8819"
        self.url = f"http://{host}/"
        self.auth = ("user", "shie9jurballs")
        
        self.logger = setupLogging('EvrmoreClient')
        self.logger.setLevel(logging.INFO)

        
    def send_command(self, command, params=[]):
        payload = {"jsonrpc": "2.0", "id": "curltext", "method": command, "params": params}
        headers = {"Content-Type": "application/json"}
        try:
            #self.logger.debug(f"Sending `{command}` to {self.url} with params {params}")
            response = requests.post(self.url, json=payload, headers=headers, auth=self.auth).json()
            #self.logger.debug(f"{response}")
            if 'error' in response and response['error']: 
                error = response['error']
                message = error['message']
                self.logger.error(f"Node replied with error: {message}")
                if message == "Block not found":
                    self.logger.error(f"Block not found.")
                    raise ValueError("Block not found")
                raise requests.HTTPError(f"Node replied with error: {message}")
            else:
                result = response['result']
                if result is not None:
                    pass
                    #self.logger.info(f"Node replied with result of length {len(str(result))}")
                return result
        except requests.ConnectionError as connection_error:
            self.logger.critical(f"Unable to connect to Evrmore node {self.url}. Is the node running?")
            raise requests.HTTPError(f"Unable to connect to Evrmore node {self.url}. Is the node running?")