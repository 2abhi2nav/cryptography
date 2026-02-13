
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)


# main

p = 3
q = 5
n = p * q
phi = (p - 1) * (q - 1)

e = 3
d = 3

print(f"RSA Parameters: p={p}, q={q}, n={n}, phi={phi}")
print(f"Public Key (e, n): ({e}, {n})")
print(f"Private Key (d, n): ({d}, {n})")

plaintext = int(input("Enter an integer < 15: "))

if plaintext >= n:
    print(f"Error: Plaintext must be less than {n}")

else:
    ciphertext = encrypt(plaintext, e, n)
    print(f"Encrypted Ciphertext: {ciphertext}")

    decrypted = decrypt(ciphertext, d, n)
    print(f"Decrypted Plaintext: {decrypted}")


for d in range(n):
    if (e * d) % n == 1:
        inv = d