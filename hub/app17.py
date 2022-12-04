# Calculation of the derivative of a function

# We ask the user to enter the function to derive
function = input("Enter the function to be derived: ")

# Define a function that calculates the value of the function at a given point
def eval(f, x):
    return eval(f)

# We ask the user to enter the point at which the derivative is to be calculated
x = float(input("Enter the point at which you want to calculate the derivative: "))

# Calculate the value of the derivative at the given point using the finite difference method
h = 0.00001
derivative = (eval(function, x + h) - eval(function, x)) / h

# Display the value of the derivative on the screen
print("The derivative of the function at the point {} is: {}".format(x, derivative))