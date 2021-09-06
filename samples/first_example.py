"""
Sums two numbers and return their result.
"""
def sumTwoNumbers(n1, n2):
  return n1 + n2

"""
Concatenates the given arguments, which is
not sumTwoNumbers expected behavior.
"""
result = sumTwoNumbers("Hello, ", "World!")
print(result) # prints Hello, World!
