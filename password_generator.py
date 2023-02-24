import string
import random


def generate_password(length):
    """Generate a random password with letters and digits"""
    letters = string.ascii_letters
    digits = string.digits
    possible_chars = letters + digits

    if length < 8 or length > 20:
        raise ValueError("Lenght of password must be between 8 and 20 characters")

    password = ''.join(random.choice(possible_chars) for i in range(length))

    return password
