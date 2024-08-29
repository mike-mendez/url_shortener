import secrets
import string


def generate_random_key(size = 8):
    alphanumeric_characters = string.ascii_letters + string.digits
    random_key = "".join(secrets.choice(alphanumeric_characters) for _ in range(size))
    return random_key
