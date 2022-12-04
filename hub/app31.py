# Calculating the trajectory of a moving object under the influence of different forces

# Prompt the user to enter the required data
mass = float(input("Enter the mass of the object in kg: "))
start_position = float(input("Enter the initial position in metres: "))
start_velocity = float(input("Enter the initial velocity in m/s: "))
acceleration = float(input("Enter the acceleration in m/s^2: "))
time = float(input("Enter the time in seconds: "))

# Calculate the final position of the object
final_position = start_position + start_velocity * time + 0.5 * acceleration * time ** 2

# Display the final position of the object
print("The final position of the object is:", final_position, "meters")