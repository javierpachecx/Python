# Calculating the standard deviation of a numerical data set

# Prompts the user to enter the data
data = input("Enter data separated by commas: ")

# Converts the input string to a list of numbers
data = [float(x) for x in data.split(",")]

# Calculate the average of the data
mean = sum(data) / len(data)

# Calculate the variance of the data
variance = sum([(x - mean)**2 for x in data]) / len(data)

# Calculates the standard deviation of the data
standard_deviation = variance**0.5

# Print the result
print("The standard deviation is:", standard_deviation)