##############################
#   Project Euler Problem 4  #
##############################
# Checks every combination of i*y with 100 <= x <= y <= 1000. Let p be the biggest known palindronic number so far and k the palindronic number in the current itteration.
# Checks every new found palindronic k if k > p. If so then p = k. After every posibile variant of x*y is p the greatest palindronic number found in all possible palindronic numbers from 100 <= x <= y <= 1000 and the function returns p.


# Other Functions in use:

# Checks if a number x is palindronic
def isPalindromic(x):
    # Sets the invertet number as y
    y = invertNumber(x)
    # returns true if y is equal with the imput x
    return y == x


def invertNumber(x):
    # convertes the imput x into a string s
    s = str(x)
    # creates an empty string wich will become
    ns = ""
    for i in range(0, len(s)):
        ns += s[-1-i]
    return int(ns)


# Biggest palindronic number so far wich starts with p = 0
p = 0
# Starts a for loop with every possible combination
for i in range(100, 1001):
    for j in range(100, 1001):
        # Calculates the current number k
        k = i * j
        # Checks if k is palindronic
        if isPalindromic(k):
            # if so: checks if k is greater than the current greatest known palindronic p
            if k > p:
                # if so: p becomes k
                p = k
print(p)
