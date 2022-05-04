##############################
#   Project Euler Aufgaben   #
##############################

def A1():
    s = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s


def A2():
    a = 1
    b = 1
    s = 0
    while b < 4000000:
        if (b % 2 == 0):
            s += b
        temp = b
        b += a
        a = temp
    return s


def A3():
    a = 600851475143
    i = 2
    while i < a:
        if (a % i == 0):
            a //= i
        i += 1

    return a


def A4():
    p = 0
    for i in range(100, 1001):
        for j in range(100, 1001):
            k = i * j
            if isPalindromic(k):
                if k > p:
                    p = k
    return p


def A5():
    x = 0
    z = 0
    while (z < 19):
        z = 0
        x += 2
        for i in range(2, 21):
            if x % i == 0:
                z += 1
            else:
                break
    return x


def A6():
    s = 0
    sq = 0
    for i in range(1, 101):
        s += i*i
        sq += i
    sq *= sq
    return sq - s


def A7():
    x = 1
    zaehler = 1
    while zaehler < 10001:
        x += 2
        if checkPrime(x) == True:
            zaehler += 1
    return x


def freeA7(x):
    y = 2
    satz = "{}. Primzahl: {}"
    zaehler = 1
    while zaehler <= x:
        if checkPrime(y) == True:
            print(satz.format(zaehler, y))
            zaehler += 1
        y += 1
    return "Ende"


#######################
#   Hilfsfunktionen   #
#######################

def isPalindromic(x):
    y = invertNumber(x)
    return y == x


def invertNumber(x):
    s = str(x)
    ns = ""
    for i in range(0, len(s)):
        ns += s[-1-i]
    return int(ns)


def checkPrime(x):
    z = 3
    if x % 2 == 0:
        return False
    while z < x:
        if x % z == 0:
            return False
        z += 2
    return True


def produngerade(x):
    p = 1
    y = 1
    while x > 0:
        print(p)
        p *= y
        y += 2
        x -= 1
    return p

###############
#   Ausgabe   #
###############


# EINGABE:
print("Hello world")
