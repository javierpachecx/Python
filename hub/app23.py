# Calculating the sum of an infinite series

# We import the function "fabs" from the "math" module to calculate the absolute value
from math import fabs

# We define the function that calculates the nth term of the series
# In this case, we are calculating the sum of the series
# 1 + 1/2 + 1/3 + 1/4 + ...
def series_term(n):
    return 1 / n

# We initialise the variable that will hold the sum of the series
sum = 0

# We initialise the variable that will store the number of calculated terms
n = 1

# Initialise the variable that will store the absolute error between two consecutive terms
error = float("inf")

# Iterate until the absolute error is less than a given value
while error > 1e-6:
    # We calculate the nth term of the series
    term = series_term(n)

    # Calculate the absolute error between two consecutive terms
    error = fabs(term - sum)

    # Accumulate the term in the variable that holds the sum of the series
    sum = term

    # We increase the number of calculated terms
    n += 1

# Display the result
print("The sum of the series is:", sum)