##############################
#   Project Euler Problem 5  #
##############################

x = 20
z = 0
while (z < 19):
    z = 0
    x += 20
    for i in range(2, 21):
        if x % i == 0:
            z += 1
        else:
            break
print(x)

# Kleiner test
