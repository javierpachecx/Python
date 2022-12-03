# Factorial of an integer

def factorial(n):
  # Base case: the factorial of 0 is 1.
  if n == 0:
    return 1
  # Recursive case: the factorial of a number n is n * the factorial of n - 1
  else:
    return n * factorial(n - 1)

# Let's test the program with an example
n = 5
print("The factorial of", n, "is", factorial(n))