from datetime import datetime

from enums import Selector


def mkselector(selector: str) -> Selector:
    return Selector(selector)

def mkdate(date: str) -> datetime:
    pass