# Solving a system of linear equations by Gaussian elimination

# We obtain the number of equations of the system
n = int(input("Enter the number of equations of the system: "))

# We create an empty matrix to store the coefficients
A = []

# We ask the user to enter the coefficients of each equation
print("Enter the coefficients of each equation:")
for i in range(n):
    # We create a list to store the coefficients of the current equation.
    a = []
    for j in range(n+1):
        # We request the corresponding coefficient
        a.append(float(input(f"Coefficient a[{i},{j}]: ")))
    # Add the coefficients of the equation to the matrix A
    A.append(a)

# We create a list to store the solutions of the system
x = [0] * n

# Perform Gaussian elimination
for k in range(n):
    # We look for the largest element in column k
    max_index = k
    max_value = abs(A[k][k])
    for i in range(k+1, n):
        if abs(A[i][k]) > max_value:
            max_index = i
            max_value = abs(A[i][k])
    
    # If the largest element is not the one on the diagonal, swap the rows.
    if k != max_index:
        A[k], A[max_index] = A[max_index], A[k]
    
    # We perform the elementary operations for each row
    for i in range(k+1, n):
        f = A[i][k] / A[k][k]
        for j in range(k+1, n+1):
            A[i][j] -= f * A[k][j]
        A[i][k] = 0

# We perform backward substitution to obtain the solutions
for i in range(n-1, -1, -1):
    x[i] = A[i][n] / A[i][i]
    for j in range(i-1, -1, -1):
        A[j][n] -= A[j][i] * x[i]

# We print the solutions of the system
print("Solutions: ")
for i in range(n):
    print(f"x[{i}] = {x[i]}")