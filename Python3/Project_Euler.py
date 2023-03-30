import helper_methods
import itertools
import math
import resources


def Problem1(limit):
    sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


def Problem2(limit):
    sum = 0
    fib1 = 1
    fib2 = 2
    while fib2 <= limit:
        if fib2 % 2 == 0:
            sum += fib2
        temp = fib2
        fib2 += fib1
        fib1 = temp
    return sum


def Problem3(limit):
    return max(helper_methods.getTeiler(limit))


def Problem4():
    x = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            k = i * j
            if helper_methods.checkPalindronic(str(k)):
                if k > x:
                    x = k
    return x


def Problem5():
    x = 3
    z = 0
    while z < 19:
        z = 0
        for i in range(2, 21):
            if x % i == 0:
                z += 1
            else:
                break
        x += 1
    return x


def Problem6():
    s = 0
    sq = 0
    for i in range(1, 101):
        s += i * i
        sq += i
    sq *= sq
    return sq - s


def Problem7():
    x = 1
    zaehler = 0
    while zaehler < 1001:
        x += 1
        if helper_methods.checkPrime(x):
            zaehler += 1
            print(x)
    return x


def Problem8():
    s = resources.Problem8_Number
    z = 0
    x = 0
    b = 1
    while z < 987:
        for i in range(z, z + 13):
            b *= int(s[i])
        if b > x:
            x = b
        z += 1
        b = 1
    return x


def Problem9():
    pythagorean_triples = []
    for a in range(1, 450):
        for b in range(1, 450):
            for c in range(1, 450):
                if a * a + b * b == c * c:
                    pythagorean_triples.append((a, b, c))
    for triples in pythagorean_triples:
        if triples[0] + triples[1] + triples[2] == 1000:
            print(triples)
            return triples[0] * triples[1] * triples[2]


def Problem10(upper_limit):
    sum = 2
    for counter in range(3, upper_limit, 2):
        if helper_methods.checkPrime(counter):
            sum += counter
    return sum


def Problem11():
    grid = resources.Problem11_Grid
    greatest_product = 1

    # Left/Right
    for index in range(397):
        if grid[index] * grid[index + 1] * grid[index + 2] * grid[index + 3] > greatest_product:
            greatest_product = grid[index] * grid[index + 1] * grid[index + 2] * grid[index + 3]

    # Up/Right
    for index in range(340):
        if grid[index] * grid[index + 20] * grid[index + 40] * grid[index + 60] > greatest_product:
            greatest_product = grid[index] * grid[index + 20] * grid[index + 40] * grid[index + 60]

    # Diagonal (Top Left to bottom right)
    for index in range(337):
        if grid[index] * grid[index + 21] * grid[index + 42] * grid[index + 63] > greatest_product:
            greatest_product = grid[index] * grid[index + 21] * grid[index + 42] * grid[index + 63]

    # Diagonal (Top Right to bottom left) => Has the solution in it!
    for index in range(3, 340):
        if grid[index] * grid[index + 19] * grid[index + 38] * grid[index + 57] > greatest_product:
            greatest_product = grid[index] * grid[index + 19] * grid[index + 38] * grid[index + 57]

    return greatest_product


# Toodoo: Muss noch bearbeitet werden!
def Problem12():
    return 0


def Problem20():
    n = 1
    s = 0
    for i in range(2, 101):
        n *= i
    n = str(n)
    for i in range(0, len(n)):
        s += int(n[i])
    return s


def Problem22():
    sum = 0
    names = resources.Problem28_NameList
    names.sort()
    print(names[0])
    for i in range(0, len(names)):
        zwischensumme = 0
        for j in range(0, len(names[i])):
            zwischensumme += int(ord((names[i])[j])) - 64
        sum += zwischensumme * (i + 1)
    return sum


def Problem24():
    a = []
    perm = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in list(perm):
        a.append(i)
    a.sort()
    return a[999999]


def Problem25():
    a = 1
    b = 1
    z = 2
    while len((str(b))) < 1000:
        temp = b
        b += a
        a = temp
        z += 1
    return z


# Muss noch bearbeitet werden!


def Problem29():
    ar = [2]
    for a in range(2, 101):
        for b in range(2, 101):
            for i in range(len(ar)):
                if math.pow(a, b) != ar[i]:
                    if math.pow(a, b) > ar[i]:
                        ar.append(math.pow(a, b))
                    else:
                        break
                else:
                    break
                if math.pow(b, a) != ar[i]:
                    if math.pow(b, a) > ar[i]:
                        ar.append(math.pow(b, a))
                    else:
                        break
                else:
                    break
        print(ar)
    return len(ar) + 1


def Problem48():
    s = 0
    for i in range(501):
        s += math.pow(i, i)
    return s


def Problem27():
    n = 0
    nmax = 0
    maxa = 0
    maxb = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            while helper_methods.checkPrime(n * n + a * n + b):
                n += 1
            if n > nmax:
                nmax = n
                maxa = a
                maxb = b
            n = 0
    return maxa * maxb


def Problem30():
    s = 0
    for i in range(100000):
        if helper_methods.digitPower(i):
            s += i
    return s


print("hello world")
