
alphabegin = 65
alphaend = 90

alphabet = [chr(i) for i in range (alphabegin, alphaend + 1)]
modval = 26

plaintext = input()
key = int(input())

ciphertext = ""
for i in plaintext:
    ciphertext += chr(alphabegin + ((ord(i) - alphabegin + key) % 26)) 

decryptedtext = ""
for i in ciphertext:
    decryptedtext += chr(alphabegin + ((ord(i) - alphabegin - key) % 26)) 


print(f"Encrypted text: {ciphertext}")
print(f"Decrypted text: {decryptedtext}")
