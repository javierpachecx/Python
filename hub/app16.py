# Third-degree equations

# We import the sqrt function from the math library to calculate square root
from math import sqrt

# Ask the user to enter the coefficients of the equation
a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))
d = int(input("Enter the coefficient d: "))

# We calculate the constants that will allow us to factor the equation
p = (3 * a * c - b**2) / (3 * a**2)
q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)

# We calculate the radical part of the equation
r = (q / 2 + sqrt(q**2 / 4 + p**3 / 27))**(1 / 3)

# We calculate the roots of the equation
x1 = r + p / r - b / (3 * a)
x2 = -(r + p / r) / 2 - b / (3 * a) + sqrt(3) * (r - p / r) / 2 * 1j
x3 = -(r + p / r) / 2 - b / (3 * a) - sqrt(3) * (r - p / r) / 2 * 1j

# We show the roots of the equation on the screen1
print("The roots of the equation are: x1 = {}, x2 = {}, x3 = {}".format(x1, x2, x3))