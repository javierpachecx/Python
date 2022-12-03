# Area of a circle given its radius

import math

def area_circle(radius):
  # We calculate the area of the circle using the formula.
  # A = π * r^2
  area = math.pi * radius**2
  return area

# We test the program with a value of radius
radius = 2
print("The area of the circle with radius", radius, "is", area_circle(radius))