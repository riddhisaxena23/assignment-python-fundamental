def electricity_bill(units):
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")

    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 200 * 7 + (units - 300) * 10

    if bill > 2000:
        bill *= 1.05
    return bill


def loan_decision(salary, credit_score, age):
    conditions_met = sum((salary >= 30000, credit_score >= 700, 21 <= age <= 60))
    if conditions_met == 3:
        return "Approved"
    if conditions_met == 2:
        return "Conditionally Approved"
    return "Rejected"


def classify_number(number):
    sign = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"
    parity = "Even" if number % 2 == 0 else "Odd"
    divisible_by_3_and_5 = number % 3 == 0 and number % 5 == 0
    return sign, parity, divisible_by_3_and_5


def analyze_exam_marks(marks):
    if len(marks) != 5:
        raise ValueError("Exactly five subject marks are required.")
    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100.")

    average = sum(marks) / 5
    if any(mark < 33 for mark in marks):
        result = "Fail"
        division = None
    elif average >= 60:
        result = "Pass"
        division = "First"
    elif average >= 50:
        result = "Pass"
        division = "Second"
    elif average >= 40:
        result = "Pass"
        division = "Third"
    else:
        result = "Pass"
        division = "No division"

    return {"result": result, "average": average, "division": division}