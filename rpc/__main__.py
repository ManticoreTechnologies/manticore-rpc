""" Manticore Technologies LLC 
    (c) 2025
    Evrmore RPC Client
    __main__.py
"""

""" Import the necessary modules """
from .lib.send import send
from .lib.arg_check import check_args
import sys

""" When this module is run, check the arguments and send the command to the Evrmore node """
if __name__ == "__main__":

    try:

        # Check user provided command and arguments
        command, args = check_args()

        # Send the command to the Evrmore node
        result = send(command, args)

        # Print the result
        print(result)

    except Exception as e:
        # Print the error message
        print(f"{e}")

        # Exit the program
        sys.exit(1)
