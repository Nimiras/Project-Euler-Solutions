##############################
#   Project Euler Problem 5  #
##############################
# Checks linear every multiple of 20 if its divisible by all the numbers between 2 and 20
x = 20
counter = 0

# Uses a counter to check if x is divisible by the numbers from 2 to 20
while (counter < 19):
    counter = 0
    x += 20
    #Checks x with all the numbers from 2 to 20
    for i in range(2, 21):
        if x % i == 0:
            # If its divisible by i, the counter goes up
            counter += 1
        else:
            break


print(x)
