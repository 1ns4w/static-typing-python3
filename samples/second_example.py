"""
<object>: <type> specifies an object data type.
Sums two numbers and return their result.
"""
def sumTwoNumbers(n1: float, n2: float) -> float:
    return n1 + n2

"""
Now that we have included data types, let's check
if our program would run as we expect using mypy.
"""
result: float =  sumTwoNumbers("Hello, ", "World!") # mypy will idenitify and report this error
print(result)
