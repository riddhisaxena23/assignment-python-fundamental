def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


def sum_natural_numbers(number):
    if number < 0:
        raise ValueError("Enter a non-negative number.")
    if number == 0:
        return 0
    return number + sum_natural_numbers(number - 1)


def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]


def power(base, exponent):
    if exponent < 0:
        return 1 / power(base, -exponent)
    if exponent == 0:
        return 1
    half_power = power(base, exponent // 2)
    squared = half_power * half_power
    return squared if exponent % 2 == 0 else base * squared