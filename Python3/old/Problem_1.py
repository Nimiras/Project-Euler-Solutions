##############################
#   Project Euler Problem 1  #
##############################

# Checks every number between 1 and 1000 if they are divisible by 3 or 5.

s = 0

for i in range(1001):
    # Checks if divisible by 3 or 5:
    if i % 3 == 0 or i % 5 == 0:
        s += i
print(s)
