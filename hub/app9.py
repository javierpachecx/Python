# Given integer is either prime or not

def is_prime(n):
  # if the number is less than 2, then it is not prime.
  if n < 2:
    return False

  # Check if the number is divisible by any integer between 2 and the square root of the number
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False

  # If no divisor was found, then the number is prime.
  return True

# We test the program with an example
n = 7
if is_prime(n):
  print(n, "is a prime number")
else:
  print(n, "is not a prime number")