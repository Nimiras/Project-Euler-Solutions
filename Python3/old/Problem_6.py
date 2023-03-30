##############################
#   Project Euler Problem 6  #
##############################

#Defineing:
#   s as the sum of the squares of the first one hundred natural numbers
#   sq as the square of the sum of the first one hundred natural numbers
s = 0
sq = 0
for i in range(1, 101):
#   Calculateing s and sq
    s += i*i
    sq += i
# take the square of sq
sq *= sq

#print out the difference between sq and s
print(sq - s)
