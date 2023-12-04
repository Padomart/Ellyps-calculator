p = 751
X = [1, 0]
Y = [0, 1]
a = 1
x_initial = X.copy()
y_initial = Y.copy()


def extended_evklid_alg(a, b, x, y):
    if a and b != 0:
        q = a // b
        r = a % b
        x.append(x[-2] - q * x[-1])
        y.append(y[-2] - q * y[-1])
        a = b
        b = r
        extended_evklid_alg(a, b, x, y)
    if x[-2] > 0:
        c = x[-2]
        return c
    else:
        c = x[-2]
        return p + c


def equal_alph(x1, y1):
    X = x_initial.copy()
    Y = y_initial.copy()
    chislitel = (3 * (x1 ** 2) - a)
    znam = 2 * y1
    if chislitel < 0:
        value = int(((-1 % p) * ((-chislitel / znam) % p)) % p)
        return value
    else:
        value = int(((chislitel % p) * extended_evklid_alg(znam, p, X, Y)) % p)
        return value


def unequal(x1, y1, x2, y2):
    X = x_initial.copy()
    Y = y_initial.copy()
    chislitel = y2 - y1
    znam = x2 - x1
    if (chislitel == 0) or (znam == 0):
        return 0
    if (chislitel < 0 and znam < 0) or (chislitel > 0 and znam > 0):
        znam = abs(znam)
        chislitel = abs(chislitel)
        alpa = ((chislitel % p) * (extended_evklid_alg(znam, p, X, Y))) % p
        return alpa
    elif (chislitel < 0 < znam) or (znam < 0 < chislitel):
        znam = znam % p
        alpa = ((chislitel % p) * (extended_evklid_alg(znam, p, X, Y))) % p
        return alpa


def proverka(x, y):
    return f"{y}^2 mod751 = ({x}^3-{x}+1) mod 751 ===> {(y ** 2) % p} = {((x ** 3) - x + 1) % p}"


def tru_proverka(x, y):
    if ((y ** 2) % p) == (((x ** 3) - x + 1) % p):
        return True
    return False
