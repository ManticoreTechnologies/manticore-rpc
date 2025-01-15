from .load_settings import load_settings
from .load_evrmore_conf import load_evrmore_conf

settings = load_settings()

__all__ = [
    'load_settings',
    'load_evrmore_conf',
    'settings'
]