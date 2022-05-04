##############################
#   Project Euler Problem 5  #
##############################
# Checks linear every multiple of 20 if its divisible by all the numbers between 2 and 19
x = 20
counter = 0

while (counter < 19):
    counter = 0
    x += 20
    for i in range(2, 21):
        if x % i == 0:
            counter += 1
        else:
            break


print(x)
