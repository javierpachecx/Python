# Determining the value of a function at a given point using the bisection method

def func(x):
  # Here is the definition of the function
  return x**2 - 2

# Prompt the user to enter the required values
a = float(input("Enter the lower bound value: "))
b = float(input("Enter the value of the upper limit: "))
tol = float(input("Enter the desired tolerance: "))

# Assign an initial value to the variable c
c = (a+b)/2.0

# Apply the bisection method
while abs(b-a) > tol:
  c = (a+b)/2.0
  if func(c) == 0:
    break
  if func(a)*func(c) < 0:
    b = c
  else:
    a = c

# Display the result
print("The value of the function at the given point is:", c)