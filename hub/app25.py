# Solving systems of non-linear equations

def bisection(f, a, b, tol):
  # We check that f(a) and f(b) have opposite signs.
  if f(a) * f(b) >= 0:
    print("The bisection method cannot be applied on this interval.")
    return None

  # Iterate until we find a solution with the desired precision.
  while abs(b - a) > tol:
    # We calculate the midpoint of the interval
    c = (a + b) / 2

    # Check if the midpoint is a solution
    if f(c) == 0:
      return c

    # Determine in which subinterval the solution lies
    if f(c) * f(a) < 0:
      b = c
    else:
      a = c

  # Once a solution with the desired precision has been found, we return it
  return (a + b) / 2

# Example of using the bisection method to solve a system of non-linear equations

# We define the function f that represents the system of non-linear equations
def f(x):
  return x**2 - 3 * x + 2

# We call the function bisection with the appropriate parameters
solution = bisection(f, 0, 1, 0.0001)

# We print the obtained solution
print(solution)