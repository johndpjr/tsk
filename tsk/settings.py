from configparser import ConfigParser
from datetime import datetime, timedelta

import utils


class Settings(ConfigParser):
    """Models the settings for tsk."""

    def __init__(self):
        super().__init__(allow_no_value=True)
        self.read('../config.ini')

    def commit(self):
        """Commit settings changes."""
        with open('../config.ini', 'w') as configfile:
            self.write(configfile)

    def get_default_val(self, key: str):
        if key == 'date_due':
            num_days_due = self.getint('TaskDefaults', 'date_due')
            if num_days_due == -1:
                return None
            return utils.tstamp_to_american_datestr(
                datetime.now().date()
                + timedelta(days=num_days_due)
            )
