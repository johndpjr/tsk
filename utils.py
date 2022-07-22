import random, string
from datetime import datetime


def get_id() -> str:
    """Returns a random alphanumeric id."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def tstamp_to_datestr(tstamp):
    return tstamp.strftime('%x (%a)')

def tstamp_to_timestr(tstamp):
    return tstamp.strftime('%I:%M %p')

def tstamp_to_tstr(tstamp):
    return f'{tstamp_to_datestr(tstamp)} {tstamp_to_timestr(tstamp)}'

def tstr_to_tstamp(tstr):
    return datetime.strptime(tstr[:-4], '%Y-%m-%dT%H:%M:%S')
