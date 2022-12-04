# Calculating the distance between two points in three-dimensional space

import math

def distance(p1, p2):
  # p1 and p2 are tuples containing the coordinates (x, y, z) of the points.
  x1, y1, z1 = p1
  x2, y2, z2 = p2
  return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

# We ask for the coordinates of the points from the user
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
z1 = float(input("Enter the z-coordinate of the first point: "))
p1 = (x1, y1, z1)

x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
z2 = float(input("Enter the z-coordinate of the second point: "))
p2 = (x2, y2, z2)

# Calculate the distance between the points
d = distance(p1, p2)

# Print the result on the screen
print("The distance between the two points is:", d)