# Solving a trigonometric equation

import math

# I ask the user to enter the coefficient a, b and c of the trigonometric equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# I calculate the discriminant
discriminant = b**2 - 4**a**c

# If discriminant is less than 0, there is no real solution
if discriminant < 0:
    print("There is no real solution to the equation.")

# If the discriminant is equal to 0, there is only one real solution
if discriminant == 0:
    x = (-b + math.sqrt(discriminant)) / (2 * a)
    print("The unique solution is x = ", x)

# If the discriminant is greater than 0, there are two real solutions
else:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The solutions are x1 = ", x1, " and x2 = ", x2)