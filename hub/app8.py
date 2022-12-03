# Square root of a real number

def square_root(n, precision=0.00001):
  # We set an initial value for the square root.
  root = n / 2

  # We apply Newton's algorithm for finding the square root
  while abs(root ** 2 - n) > precision:
    root = (root + n / root) / 2

  # Return the square root found
  return root

# We test the program with an example
n = 2
print("The square root of", n, "is", square_root(n))