class PasswordValidationError(Exception):
    pass


class PasswordTooShortError(PasswordValidationError):
    pass


class MissingUppercaseError(PasswordValidationError):
    pass


class MissingNumberError(PasswordValidationError):
    pass


def validate_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return True


def withdraw(balance, amount):
    if balance < 0 or amount < 0:
        raise ValueError("Balance and withdrawal amount cannot be negative.")
    if amount > balance:
        raise ValueError("Withdrawal exceeds the available balance.")
    return balance - amount


def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters.")
    if not any(character.isupper() for character in password):
        raise MissingUppercaseError("Password must contain an uppercase letter.")
    if not any(character.isdigit() for character in password):
        raise MissingNumberError("Password must contain a number.")
    return True