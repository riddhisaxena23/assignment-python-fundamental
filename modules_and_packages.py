import math
import random
from datetime import date, datetime


def math_examples(number, base, exponent, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    return {
        "square_root": math.sqrt(number),
        "power": math.pow(base, exponent),
        "factorial": math.factorial(int(number)),
        "sine": math.sin(angle_radians),
        "cosine": math.cos(angle_radians),
        "tangent": math.tan(angle_radians),
    }


def generate_otp(length=6):
    if length < 1:
        raise ValueError("OTP length must be at least one.")
    return "".join(random.choice("0123456789") for _ in range(length))


def generate_password(length=12):
    if length < 1:
        raise ValueError("Password length must be at least one.")
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))


def random_numbers(count, minimum=1, maximum=100):
    if count < 0 or minimum > maximum:
        raise ValueError("Invalid count or number range.")
    return [random.randint(minimum, maximum) for _ in range(count)]


def current_date_time():
    return datetime.now()


def calculate_age(birth_date, today=None):
    today = today or date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age