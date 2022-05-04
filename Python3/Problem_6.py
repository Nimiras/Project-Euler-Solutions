##############################
#   Project Euler Problem 6  #
##############################

s = 0
sq = 0
for i in range(1, 101):
    s += i*i
    sq += i
sq *= sq
print(sq - s)
