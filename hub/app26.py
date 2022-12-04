# Calculating the median of a numerical data set

# Ask the user to enter the data
data = input("Enter data separated by commas: ")

# Convert the string to a list of numbers
data = [int(x) for x in data.split(",")]

# Sort the list of numbers
data.sort()

# Calculate the length of the list
n = len(data)

# If the list is of odd length, the median is the middle item
if n % 2 != 0:
    median = data[n//2]

# If the list is of even length, the median is the average of the two middle items
else:
    median = (data[n//2 - 1] + data[n//2]) / 2

# Print the median
print("The median is:", median)