# Least common multiple (MCM) of two integers

def mcm(a, b):
  # We calculate the greatest common divisor (GCD) of a and b.
  # using Euclid's algorithm
  while b != 0:
    a, b = b, a % b

  # The GCM of a and b is a, so the GCM of a and b is
  # a * b / MCD(a, b)
  return (a * b) / a

# Let's test the program with an example
a = 12
b = 18
print("The least common multiple of", a, "and", b, "is", mcm(a, b))