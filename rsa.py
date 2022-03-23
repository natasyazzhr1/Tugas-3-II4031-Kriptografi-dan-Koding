from random import randrange, getrandbits
from math import gcd


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def prime_generator():
    notprime = True
    while notprime:
        num = randrange(1, getrandbits(32))
        if is_prime(num):
            return num


def publickey_generator(phi):
    notfound = True
    while notfound:
        e = randrange(1, getrandbits(32))
        res = gcd(e, phi)
        if res == 1:
            return e


def privatekey_generator(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


p = prime_generator()
q = prime_generator()
n = p * q
phi = (p-1) * (q-1)
e = publickey_generator(phi)
d = privatekey_generator(e, phi)

print("p =", p)
print("q =", q)
print("n =", n)
print("phi =", phi)
print("e =", e)
print("d =", d)
