# Greatest common divisor (MCD) of two integers

def mcd(a, b):
  # We apply Euclid's algorithm to calculate the DCM.
  while b != 0:
    a, b = b, a % b

  # The DCM is the value of a at the end of the algorithm.
  return a

# We test the program with an example
a = 12
b = 18
print("The greatest common divisor of", a, "and", b, "is", mcd(a, b))