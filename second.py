
alphabegin = 65
alphaend = 90

alphabet = [chr(i) for i in range (alphabegin, alphaend + 1)]
modval = 26

key = ord('U') - ord('E')

plaintext = ""

ciphertext = "FQOCUDEM"

for i in ciphertext:
    plaintext += chr(alphabegin + ((ord(i) - alphabegin - key) % 26)) 

print(plaintext)
