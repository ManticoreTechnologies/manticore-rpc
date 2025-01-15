from .load_settings import load_settings
import os
import sys

def load_evrmore_conf():
    
    """ First check if the evrmore.conf file exists """
    if not os.path.exists(load_settings()['evrmore_root'] + '/evrmore.conf'):
        print("evrmore.conf file not found, please check settings.conf")
        sys.exit(1)

    """ Read the evrmore.conf file """
    with open(load_settings()['evrmore_root'] + '/evrmore.conf', 'r') as file:
        """ Convert the file to a dictionary """
        lines = file.readlines()
        settings = {}
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                settings[key.strip()] = value.strip()
        return settings
