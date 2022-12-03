# Distance between two points in the Cartesian plane

# We import the sqrt function from the math library
from math import sqrt

# We define a function to calculate the distance between two points
def distance_points(x1, y1, x2, y2):
  # Calculate the distance between the points
  distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

  # Return the distance between the points
  return distance

# We test the function with an example
x1 = 2
y1 = 3
x2 = 4
y2 = 5
distance = distance_points(x1, y1, x2, y2)
print("The distance between the points (", x1, ",", y1, ") and (", x2, ",", y2, ") is", distance)