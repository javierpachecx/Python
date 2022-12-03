# Prime factor decomposition of an integer

def decompose_into_prime_factors(n):
  # We create a list to store the prime factors.
  prime_factors = []

  # We apply the algorithm of decomposition into prime factors
  i = 2
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
      prime_factors.append(i)
  if n > 1:
    prime_factors.append(n)

  # Return the list of prime factors
  return prime_factors

# We test the program with an example
n = 315
print("The prime factors of", n, "are", decompose_into_prime_factors(n))