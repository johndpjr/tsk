from configparser import ConfigParser


class Settings(ConfigParser):
    """Models the settings for tsk."""

    def __init__(self):
        super().__init__()
        self.read('config.ini')

    def commit(self):
        """Commit settings changes."""
        with open('config.ini', 'w') as configfile:
            self.write(configfile)
