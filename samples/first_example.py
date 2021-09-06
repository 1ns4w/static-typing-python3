"""
Sums two numbers and return their result.
"""
def sumTwoNumbers(n1, n2):
  return n1 + n2

"""
Concatenates the given arguments, which is
syntactically correct, so there won't be
any error and we will receive an ouput, but
sumTwoNumbers isn't supposed to behave so.
"""
result = sumTwoNumbers("Hello, ", "World!")
print(result) # prints Hello, World!
