from datetime import datetime


def mkdate(date: str) -> datetime:
    return datetime.strptime(date, '%m/%d/%y')
