# Area and perimeter of a circle given its radius

# We import the constant pi from the math library
from math import pi

# Define a function to calculate the area and perimeter of a circle
def area_perimeter_circle(radius):
  # Calculate the area of the circle
  area = pi * radius ** 2

  # Calculate the perimeter of the circle
  perimeter = 2 * pi * radius

  # Return a tuple with the area and perimeter of the circle
  return (area, perimeter)

# We test the function with an example
radius = 2
area, perimeter = area_perimeter_circle(radius)
print("The area of the circle of radius", radius, "is", area)
print("The perimeter of the circle of radius", radius, "is", perimeter)