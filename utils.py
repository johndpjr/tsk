import random, string


def get_id() -> str:
    """Returns a random alphanumeric id."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
