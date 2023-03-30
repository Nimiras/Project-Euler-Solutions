##############################
#   Project Euler Problem 3  #
##############################
# Starts with the smalest possible number (2) and divides it with the final number n as long as n > i. If n = i == n % i = 0, then we found the biggest primefactor.

# The number where we have to find the larges prime factor
n = 600851475143
# The number we check and divide n with
i = 2

# As long as i < n:
while i < n:
    # Check if n is evenely divisible by i
    if (n % i == 0):
        # if so: divide n by i and repeat
        n //= i
    i += 1

# It makes no difference if we output i or n. There are both the same numbers
print(n)
