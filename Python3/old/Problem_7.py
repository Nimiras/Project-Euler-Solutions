##############################
#   Project Euler Problem 7  #
##############################

# Checks all the odd numbers after 2 if they're prime numbers.
# If so, a counter counts one up to know, wich prime number the checked number is.
#

def A7():
    #x is the number we want to check if it is a prime number
    x = 1
    #the counter saves wich prime number we currently have
    counter = 1
    #The loop works as long as we are not finding the 10001th prime number
    while counter < 10001:
        x += 2
        if checkPrime(x) == True:
            counter += 1
    return x

#The funktion that checks if the number x is a prime number
def checkPrime(x):
    z = 3
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    while z*z <= x:
        if x % z == 0:
            return False
        z += 2
    return True
