""" Manticore Technologies LLC 
    (c) 2025
    Evrmore RPC Client
    lib/err.py
"""

""" Define the UnknownCommand exception """
class UnknownCommand(Exception):
    """Raised when an unknown command is provided"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

""" Define the InvalidArguments exception """
class InvalidArguments(Exception):
    """Raised when invalid arguments are provided"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

""" Define the EvrmoreConnectionError exception """
class EvrmoreConnectionError(Exception):
    """Raised when a connection error occurs"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

""" Define the EvrmoreAuthenticationError exception """
class EvrmoreAuthenticationError(Exception):
    """Raised when an authentication error occurs"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

""" Define the EvrmoreURLError exception """
class EvrmoreURLError(Exception):
    """Raised when an URL error occurs"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

""" Define the EvrmoreInternalServerError exception """
class EvrmoreInternalServerError(Exception):
    """Raised when an internal server error occurs"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)