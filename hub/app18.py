# Calculating the value of a polynomial at a given point

# We ask the user to enter the degree of the polynomial
degree = int(input("Enter the degree of the polynomial: "))

# We ask the user to enter the coefficients of the polynomial
coefficients = []
for i in range(degree + 1):
    coefficients.append(float(input("Enter the coefficient x^{}: ".format(degree - i))))

# We ask the user to enter the point at which the polynomial is to be calculated.
x = float(input("Enter the point at which you want to calculate the polynomial: "))

# We calculate the value of the polynomial at the given point using Horner's method
value = coefficients[0]
for i in range(1, degree + 1):
    value = value * x + coefficients[i]

# Display the value of the polynomial on screen
print("The value of the polynomial at point {} is: {}".format(x, value))