# System of linear equations given in matrix form

import numpy as np

def solve_system(A, b):
  # We convert the array A and vector b into numpy arrays.
  A = np.array(A)
  b = np.array(b)

  # We apply Gaussian elimination to solve the system of equations
  x = np.linalg.solve(A, b)

  # We return the solution of the system
  return x

# We test the program with an example
A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]
print("The solution to the system is", solve_system(A, b))