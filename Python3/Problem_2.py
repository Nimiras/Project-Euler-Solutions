##############################
#   Project Euler Problem 2  #
##############################
# Generates a series of the Fibonacci-Numbers with a = n'th Fib-number,
# b = n+1th Fib-number and s being the sum of every even fib-number.

# Both a and b starting as 1 where a = zero'th fib-number and b = first fib-number
a = 1
b = 1

# Sum of the even fib-numbers
s = 0

while b < 4000000:
    # Checks if b is even
    if (b % 2 == 0):
        s += b

    # Generates next Fib-Number
    temp = b
    b += a
    a = temp

print(s)
