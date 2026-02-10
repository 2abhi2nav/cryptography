
alphabet = [chr(i) for i in range(65, 91)]

def encrypt(text, key):
    encrypted_string = ""

    for i in range(len(text)):
        encrypted_string += chr((ord(text[i]) + key - 65) % 26 + 65)

    return encrypted_string

def decrypt(text, key):
    decrypted_string = ""

    for i in range(len(text)):
        decrypted_string += chr((ord(text[i]) - key - 65) % 26 + 65)

    return decrypted_string


# main

key = int(input())
plaintext = input()

ciphertext = encrypt(plaintext, key)
print(ciphertext)

decrypted = decrypt(ciphertext, key)
print(decrypted)

