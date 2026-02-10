import numpy as np

modval = 26

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modInverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist for this key.')
    else:
        return x % m

def gcd(a, b):
    while (b != 0):
        q = a // b
        r = a - q * b
        a = b
        b = r
    return a

def encrypt(s):
    input_m = np.array([[ord(s[0]) - ord('A')], [ord(s[1]) - ord('A')], [ord(s[2]) - ord('A')]])
    encrypted_m = key @ input_m
    encrypted_m = encrypted_m % modval
    return encrypted_m

def decrypt(encrypted_m):
    det = int(round(np.linalg.det(key)))
    det_mod = det % modval

    det_inv = modInverse(det_mod, modval)

    key_inv_float = np.linalg.inv(key)
    adjugate = key_inv_float * det

    key_inv_int = (adjugate * det_inv) % modval
    key_inv_int = np.round(key_inv_int).astype(int)

    decrypted_m = key_inv_int @ encrypted_m
    decrypted_m = decrypted_m % modval

    decrypted_s = ""
    for row in decrypted_m:
        decrypted_s += chr(row[0] + ord('A'))

    return decrypted_s

# main

key = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])

encrypted = encrypt("ACT")
for i in encrypted:
    for j in i:
        print(chr((j%26 + 65)))

decrypted_text = decrypt(encrypted)
print(decrypted_text)
