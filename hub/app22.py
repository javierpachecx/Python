# Calculation of definite and indefinite integrals

import math

def func(x):
    # This is the function to integrate.
    # In this case we are calculating the integral
    # of the cosine function on the interval [0, pi/2].
    return math.cos(x)

# We request the lower limit and upper limit of the interval from the user.
lower_limit = float(input("Enter the lower limit of the interval: "))
upper_limit = float(input("Enter the upper limit of the interval: "))

# We define the number of sub-intervals in which we will divide the interval into
n = 100

# Calculate the width of each sub-interval
width = (upper_limit - lower_limit) / n

# Initialise the variable that will store the result of the integral
integral = 0

# We go through each of the subintervals
for i in range(n):
    # We calculate the midpoint of the subinterval
    x = lower_limit + (i + 0.5) * width

    # Calculate the value of the integral in the subinterval using Simpson's method
    int_value = (func(lower_limit + i * width) + 4 * func(x) + func(lower_limit + (i + 1) * width)) * width / 6

    # We accumulate the value of the integral in the variable that holds the result of the integral
    integral += int_value

# Display the result of the definite integral
print("The value of the definite integral is:", integral)

# Calculate the value of the indefinite integral at the lower boundary
lower_value = 0

# Calculate the value of the indefinite integral at the upper boundary
upper_value = integral

# Display the result of the indefinite integral
print("The value of the indefinite integral is:", upper_value - lower_value)