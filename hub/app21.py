# Solving ordinary differential equations

# We import the function "fabs" from the "math" module to calculate the absolute value
from math import fabs

# We define the function f(x, y) that appears in the differential equation
# In this case, we are solving the differential equation
# y' = x + y with initial condition y(0) = 0
def f(x, y):
    return x + y

# We request the value of the initial point and of the interval of integration
# from the user
x0 = float(input("Enter the initial point: "))
xf = float(input("Enter the end point: "))

# we request the value of the increment on the abscissa axis
h = float(input("Enter the increment on the abscissa axis: "))

# Initialise the variable that will store the solution of the differential equation
y = 0

# Initialise the variable that will hold the point on the abscissa axis
x = x0

# We carry out iterations as long as the point on the abscissa axis
# is less than or equal to the end point
while x <= xf:
    # Calculate the value of the function and its derivative at the point x
    y_prime = f(x, y)

    # Calculate the new value of the solution of the differential equation
    y += y_prime * h

    # We update the value of the point on the abscissa axis
    x += h

# Display the result
print("The solution of the differential equation at the end point is:", y)