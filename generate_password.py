import string
import random


def generate_password(length):
    """Generate a random password with letters and digits"""
    letters = string.ascii_letters
    digits = string.digits
    possible_chars = letters + digits
    password = ''.join(random.choice(possible_chars) for i in range(length))

    return password