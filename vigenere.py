
alphabegin = 65
modval = 26

plaintext = input().upper()
keystring = input().upper()

key = ""
for i in range(len(plaintext)):
    key += keystring[i % len(keystring)]

ciphertext = ""
for i in range(len(plaintext)):
    p = ord(plaintext[i]) - alphabegin
    k = ord(key[i]) - alphabegin
    ciphertext += chr(alphabegin + (p + k) % modval)

decryptedtext = ""
for i in range(len(ciphertext)):
    c = ord(ciphertext[i]) - alphabegin
    k = ord(key[i]) - alphabegin
    decryptedtext += chr(alphabegin + (c - k) % modval)

print(f"Key: {key}")
print(f"Encrypted text: {ciphertext}")
print(f"Decrypted text: {decryptedtext}")

