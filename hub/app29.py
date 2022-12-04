# Calculation of probabilities and statistics in different types of randomised experiments

# Collect data from randomised experiment
print("Enter the data from the randomized experiment separated by commas:")
data = input()

# Split the data into a list
data = data.split(",")

# Convert data to integers
data = [int(x) for x in data] # Calculate the mean of the data

# Calculate the average of the data
mean = sum(data) / len(data)

# Calculate the standard deviation of the data
sum_square_differences = sum([(x - mean)**2 for x in data])
standard_deviation = (sum_square_differences / len(data))**0.5

# Calculate the probability of a given event
print("Enter the value of the event:")
event = int(input())
probability = len([x for x in data if x == event]) / len(data)

# print the results
print("Mean:", mean)
print("Standard deviation:", standard_deviation)
print("Probability of event", event, ":", probability)