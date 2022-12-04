# Calculation of the area under a curve in a given interval

# We import the function "pi" from the module "math".
import math

def func(x):
    # This is the function to integrate.
    # In this case we are calculating the area under the curve
    # of the cosine function in the interval [0, pi/2].
    return math.cos(x)

# We request the lower limit and upper limit of the interval from the user.
lower_limit = float(input("Enter the lower limit of the interval: "))
upper_limit = float(input("Enter the upper limit of the interval: "))

# We define the number of sub-intervals in which we will divide the interval into
n = 100

# Calculate the width of each sub-interval
width = (upper_limit - lower_limit) / n

# Initialise the variable that will store the result of the integral
area = 0

# We go through each of the subintervals
for i in range(n):
    # We calculate the midpoint of the subinterval
    x = lower_limit + (i + 0.5) * width

    # Calculate the area of the rectangle
    rect_area = func(x) * width

    # Accumulate the area of the rectangle in the variable that stores the result of the integral
    area += rect_area

# Display the result
print(area)