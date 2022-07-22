import random, string
from datetime import datetime


def get_id() -> str:
    """Returns a random alphanumeric id."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def tstamp_to_datestr(tstamp: datetime) -> str:
    return tstamp.strftime('%m/%d/%y')

def tstamp_to_timestr(tstamp: datetime) -> str:
    return tstamp.strftime('%H:%M:%S')

def tstamp_to_tstr(tstamp: datetime) -> str:
    return f'{tstamp_to_datestr(tstamp)} {tstamp_to_timestr(tstamp)}'

def tstr_to_tstamp(tstr: str) -> datetime:
    return datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
