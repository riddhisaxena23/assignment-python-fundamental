def rotate_list(items, positions, direction="left"):
    if direction not in ("left", "right"):
        raise ValueError("Direction must be 'left' or 'right'.")
    if not items:
        return []

    positions %= len(items)
    if direction == "right":
        positions = -positions
    return items[positions:] + items[:positions]


def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def find_missing_number(numbers):
    expected_count = len(numbers) + 1
    expected_sum = expected_count * (expected_count + 1) // 2
    return expected_sum - sum(numbers)


def subject_tuple_details(subjects):
    if len(subjects) != 5:
        raise ValueError("Exactly five subjects are required.")
    return subjects[2], len(subjects), subjects.index(subjects[0])


def pairs_to_dictionary(pairs):
    return dict(pairs)


def swap_tuple_ends(items):
    if len(items) < 2:
        return items
    return (items[-1], *items[1:-1], items[0])


def is_subset(candidate, container):
    return candidate.issubset(container)


def analyze_student_marks(marks_by_student, pass_mark=40):
    if not marks_by_student:
        raise ValueError("At least one student is required.")
    topper = max(marks_by_student, key=marks_by_student.get)
    average = sum(marks_by_student.values()) / len(marks_by_student)
    failures = [name for name, mark in marks_by_student.items() if mark < pass_mark]
    return {"topper": topper, "top_mark": marks_by_student[topper],
            "average": average, "failures": failures}


def borrow_book(library, book_name):
    if library.get(book_name, 0) <= 0:
        return False
    library[book_name] -= 1
    return True


def return_book(library, book_name):
    library[book_name] = library.get(book_name, 0) + 1