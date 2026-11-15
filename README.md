# Python Exercise Solutions

Each topic is in its own module. Import a function to try it with your own values, for example:

```python
from conditional_statements import electricity_bill

print(electricity_bill(350))
```

The modules cover conditional statements, loops, strings, data structures, functions and recursion, exceptions, and standard library modules. `geometry` is a package containing `circle` and `rectangle` modules.

Assumptions used where the exercise did not specify a rule:

- Loan approval is conditional when exactly two of the three conditions are met.
- Exam marks from 33% through 39.99% pass but have no division.
- Student marks below 40 are failures by default; `analyze_student_marks` accepts a different pass mark.
- The palindrome number range includes both endpoints and ignores negative numbers.

Example package import:

```python
from geometry import circle, rectangle

print(circle.area(3))
print(rectangle.perimeter(4, 5))
```