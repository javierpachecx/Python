# Area and volume of a sphere given its radius

# We import the constant pi from the math library
from math import pi

# Define a function to calculate the area and volume of a sphere
def area_volume_sphere(radius):
  # Calculate the area of the sphere
  area = 4 * pi * radius ** 2

  # We calculate the volume of the sphere
  volume = (4 / 3) * pi * radius ** 3

  # We return a tuple with the area and volume of the sphere
  return (area, volume)

# We test the function with an example
radius = 2
area, volume = area_volume_sphere(radius)
print("The area of the sphere of radius", radius, "is", area)
print("The volume of the sphere of radius", radius, "is", volume)