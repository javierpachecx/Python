# Calculation of the limit of a function at a given point

# We import the function "fabs" from the "math" module to calculate the absolute value
from math import fabs

def func(x):
    # This is the function whose limit we want to calculate at the point x = 1.
    # In this case, we are calculating the limit of the function
    # f(x) = x^2 - x at x = 1.
    return x**2 - x

# We request the point at which we want to calculate the limit of the function from the user.
point = float(input("Enter the point at which you want to calculate the limit: "))

# Define the maximum number of iterations to be performed to calculate the limit
max_iter = 1000

# We initialise the variable that will store the limit result
limit = 0

# We initialise the variable that will store the absolute error between the last and the penultimate iteration
error = float("inf")

# We perform iterations until the maximum number of iterations is reached
# or until the absolute error is less than a given value
for i in range(max_iter):
    # Calculate the value of the function at the given point.
    x = point + 1 / (i + 1)

    # Calculate the absolute error between the last and the penultimate iteration
    error = fabs(x - limit)

    # If the absolute error is less than a given value, we terminate the cycle
    if error < 1e-6:
        break

    # We update the result of the limit
    limit = x

# Show the result of the limit and the absolute error
print("The limit of the function at the given point is:", limit)
print("The absolute error between the last and the penultimate iteration is:", error)