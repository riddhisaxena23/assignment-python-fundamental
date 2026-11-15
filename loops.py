def is_automorphic(number):
    if number < 0:
        return False
    digit_count = len(str(number))
    return number * number % (10 ** digit_count) == number


def palindrome_numbers(start, end):
    if start > end:
        raise ValueError("Start of range must not exceed end of range.")
    return [number for number in range(max(0, start), end + 1)
            if str(number) == str(number)[::-1]]


def hcf(first, second):
    first, second = abs(first), abs(second)
    while second != 0:
        first, second = second, first % second
    return first


def lcm(first, second):
    if first == 0 or second == 0:
        return 0
    return abs(first * second) // hcf(first, second)


def password_retry(correct_password, attempts):
    for attempt_number, entered_password in enumerate(attempts):
        if attempt_number == 3:
            break
        if entered_password == correct_password:
            return "Access granted"
    return "Blocked"


def triangle_pattern(height):
    _validate_height(height)
    return "\n".join("*" * width for width in range(1, height + 1))


def pyramid_pattern(height):
    _validate_height(height)
    return "\n".join(" " * (height - row) + "*" * (2 * row - 1)
                     for row in range(1, height + 1))


def diamond_pattern(height):
    _validate_height(height)
    top = [" " * (height - row) + "*" * (2 * row - 1)
           for row in range(1, height + 1)]
    bottom = [" " * (height - row) + "*" * (2 * row - 1)
              for row in range(height - 1, 0, -1)]
    return "\n".join(top + bottom)


def _validate_height(height):
    if height < 1:
        raise ValueError("Pattern height must be at least one.")