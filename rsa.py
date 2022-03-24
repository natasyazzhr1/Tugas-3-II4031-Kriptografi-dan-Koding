from pydoc import plain
from random import randrange, getrandbits
from math import gcd
import os
import time

# get the size of file
# size = os.path.getsize('f:/file.txt') 
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
        num = randrange(getrandbits(8))
        if is_prime(num):
            return num


def publickey_generator(phi):
    notfound = True
    while notfound:
        e = randrange(getrandbits(8))
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


def filter(plaintext):
    clean = ''.join(i for i in plaintext if i.isalnum())
    clean = ''.join(
        i for i in clean if not i.isdigit())
    return(clean.lower())


def to_ascii(text):
    result = []
    for letter in text:
        result.append(ord(letter) - ord('a'))
    return result

def to_string(text):
    result = []
    for number in text:
        result.append(chr(number + ord('a')))
    return ''.join(result)


# def divide_chunks(list):
#     result = []
#     for i in range(0, len(list), 2):
#         result.append(list[i: i+2])
#     return result


def encrypt (text, e, n):
    ciphertext = []
    for number in text:
        c = (number ** e) % n
        ciphertext.append(c)
    return ciphertext

def decrypt (text, d, n):
    plaintext = []
    for number in text:
        m = (number ** d) % n
        plaintext.append(m)
    return plaintext

    
p = prime_generator()
q = prime_generator()
n = p * q
phi = (p-1) * (q-1)
e = publickey_generator(phi)
d = privatekey_generator(e, phi)

plaintext = input("Enter your plaintext: ")
plaintext_number = to_ascii(filter(plaintext))
print('plaintext_number =', plaintext_number)

print("p =", p)
print("q =", q)
print("n =", n)
print("phi =", phi)
print("e =", e)
print("d =", d)

encrypted = encrypt(plaintext_number, e, n)
print('encrypted =', encrypted)

decrypted = decrypt(encrypted, d, n)
print('decrypted =', decrypted)

ciphertext = to_string(decrypted)
print('ciphertext =', ciphertext)

# timelater = time.time()
# printtime = timelater - timenow

# print(printtime)
