import secrets
import string
from random import choice


def generate_code(size = choice(range(6, 10))):
    alphanumeric_characters = string.ascii_letters + string.digits
    code = "".join(secrets.choice(alphanumeric_characters) for _ in range(size))
    return code
