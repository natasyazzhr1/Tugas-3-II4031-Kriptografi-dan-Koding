from pydoc import plain
from random import randrange, getrandbits
from math import gcd
import os
import time

# # get the size of file
# size = os.path.getsize(
#     'D:/Kuliah/Semester 6/Kripto/Tugas-3-II4031-Kriptografi-dan-Koding/chipertext.txt')
# print('Size of file is', size, 'bytes')

# timenow = time.time()


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
        num = randrange(0, getrandbits(32))
        if is_prime(num):
            return num


def publickey_generator(phi):
    notfound = True
    while notfound:
        e = randrange(0, getrandbits(16))
        res = gcd(e, phi)
        if res == 1:
            return e


def privatekey_generator(pub, phi):
    pri = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while pub > 0:
        temp1 = temp_phi//pub
        temp2 = temp_phi-temp1*pub
        temp_phi = pub
        pub = temp2

        x = x2-temp1*x1
        y = pri-temp1*y1

        x2 = x1
        x1 = x
        pri = y1
        y1 = y

    if temp_phi == 1:
        return pri+phi


def filter(plaintext):
    clean = ''.join(i for i in plaintext if i.isalnum())
    clean = ''.join(
        i for i in clean if not i.isdigit())
    return(clean.lower())


def to_ascii(list):
    result = []
    for letter in list:
        result.append(ord(letter) - ord('a'))
    return result


def to_string(list):
    result = []
    for number in list:
        result.append(chr(number + ord('a')))
    return ''.join(result)


def to_hex(list):
    result = []
    for number in list:
        result.append((hex(number) + ' ').replace('0x', ''))
    return ''.join(result)


def process(text, key, n):
    list = to_ascii(text)

    result = []
    for number in list:
        result.append((number**key) % n)
    return result


def initialize(p, q):
    # p = prime_generator()
    # q = prime_generator()
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

    txtprivate = open('private.pri', 'w')
    txtprivate.write(str(d))
    txtprivate.close()

    txtpublic = open('public.pub', 'w')
    txtpublic.write(str(e))
    txtpublic.close()

    return(n, e, d)


def export(text):
    txt = open('ciphertext.txt', 'w')
    txt.write(text)
    txt.close()


# properties = initialize()
# n = properties[0]
# e = properties[1]
# d = properties[2]

# plaintext = input("Enter your plaintext: ")
# plaintext_number = to_ascii(filter(plaintext))
# # print('plaintext_number =', plaintext_number)

# encrypt = process(plaintext_number, e, n)
# print('encrypt =', encrypt)

# ciphertext = to_hex(encrypt)
# print('ciphertext =', ciphertext)

# export(plaintext_number, e, n)

# decrypt = process(encrypt, d, n)
# print('decrypt =', decrypt)

# plaintext = to_string(decrypt)
# print('plaintext =', plaintext)

# timelater = time.time()
# printtime = timelater - timenow

# print(printtime)
