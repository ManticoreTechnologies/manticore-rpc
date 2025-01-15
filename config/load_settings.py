def load_settings():
    settings = {}
    with open('settings.conf', 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                settings[key.strip()] = value.strip()
    return settings