def area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width


def perimeter(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return 2 * (length + width)