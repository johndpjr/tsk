from configparser import ConfigParser


class Settings(ConfigParser):
    """Models the settings for tsk."""

    def __init__(self):
        super().__init__()
        self.read('config.ini')
