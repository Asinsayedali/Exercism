import random
import string


class Robot:

    def __init__(self):
        self.name = None
        self.generate_name()

    def generate_name(self):
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        name = ''.join(random.choices(uppercase_letters, k=2) + random.choices(digits, k=3))
        self.name = name

    def reset(self):
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        name = ''.join(random.choices(uppercase_letters[1], k=2) + random.choices(digits[1], k=3))
        self.name = name
