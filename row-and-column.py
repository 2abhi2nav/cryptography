
plaintext = input()
cols = int(input())

plaintext = plaintext.replace(" ", "")

cipher = ""
for c in range(cols):
    i = c
    while i < len(plaintext):
        cipher += plaintext[i]
        i += cols

print("Encrypted:", cipher)

rows = (len(cipher) + cols - 1) // cols
plain = [""] * len(cipher)

k = 0
for c in range(cols):
    i = c
    while i < len(cipher) and k < len(cipher):
        plain[i] = cipher[k]
        k += 1
        i += cols

print("Decrypted:", "".join(plain))
