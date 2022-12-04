# Generation of random numbers and their statistical distribution

# We import the randint function from the random module
from random import randint

# Ask the user to enter the number of random numbers to generate
num_random = int(input("Enter the number of random numbers to generate: "))

# Generate a list of random numbers between 1 and 10
random_numbers = [randint(1, 10) for _ in range(num_random)]

# Show the statistical distribution of the random numbers
for i in range(1, 11):
  num_appearances = random_numbers.count(i)
  print(f"The number {i} appears {num_appearances} times")