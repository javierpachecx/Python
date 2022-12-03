# Second-degree equations

import math

def solve_equation(a, b, c):
  # We calculate the roots of the equation using the general formula.
  # x = (-b ± √(b^2 - 4ac)) / 2a
  root1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
  root2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

  # We return both roots
  return root1, root2

# We test the program with an example
a = 1
b = -5
c = 6
print("The roots of the equation", a, "x^2 +", b, "x +", c, "are:")
print(solve_equation(a, b, c))