import math


def checkPalindronic(s):
    inverts = ""
    for i in range(0, len(s)):
        inverts = s[i] + inverts
    if int(inverts) == int(s):
        return True
    else:
        return False


def checkPrime(x):
    if x < 1:
        return False
    if x == 2:
        return True
    if x >= 2 and x % 2 == 0:
        return False
    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i += 2
    return True


def freeA7(x):
    y = 2
    satz = "{}. Primzahl: {}"
    zaehler = 1
    while zaehler <= x:
        if checkPrime(y):
            print(satz.format(zaehler, y))
            zaehler += 1
        y += 1
    return "Ende"


def getTeiler(number):
    teilerliste = [1]
    for teiler in range(2, int(number/2+1)):
        if number % teiler == 0:
            teilerliste.append(teiler)
    teilerliste.append(number)
    return teilerliste


def digitPower(x):
    s = 0
    xs = str(x)
    for i in range(len(xs)):
        s += math.pow(int(xs[i]), 5)
    if s == x:
        print(s)
    return s == x
