import configparser

""" Load the settings """
settings = configparser.ConfigParser()
settings.read('settings.conf')

config = configparser.ConfigParser()
config.read(settings['General']['config_path'])