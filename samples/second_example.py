"""
<object>: <type> specifies an object data type.
Sums two numbers and return their result.
"""
def sumTwoNumbers(n1: float, n2: float) -> float:
    return n1 + n2

"""
If we would run this program, Python would
concatenate the given arguments again, but...
"""
result: float = sumTwoNumbers("Hello ", "World!") # mypy will detect this error so you can correct it
print(result)
