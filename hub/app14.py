# Area and volume of a cylinder given its radius and height

# We import the constant pi from the math library
from math import pi

# Define a function to calculate the area and volume of a cylinder
def area_volume_cylinder(radius, height):
  # Calculate the side area of the cylinder
  lateral_area = 2 * pi * radius * height

  # Calculate the total area of the cylinder
  total_area = 2 * pi * radius ** 2 + lateral_area

  # Calculate the volume of the cylinder
  volume = pi * radius ** 2 * height

  # Return a tuple with the area and volume of the cylinder
  return (total_area, volume)

# We test the function with an example
radius = 2
height = 3
area, volume = area_volume_cylinder(radius, height)
print("The total area of the cylinder of radius", radius, "and height", height, "is", area)
print("The volume of the cylinder of radius", radius, "and height", height, "is", volume)