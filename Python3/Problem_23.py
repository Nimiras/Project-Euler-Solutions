
def divisors(x):
    divlist = [1]
    z = 2
    while (z <= x):
        if x % z == 0 and z != x:
            divlist.append(z)
        z += 1
    return divlist


sum = 0
for i in range(28123):


print(divisors(28))
