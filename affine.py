
modval = 26
alphabet = [chr(i) for i in range(65, 91)]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modular_inverse(a):
    for i in range(1, modval):
        if (a * i) % modval == 1:
            return i
    
    return -999 

def encrypt(text, a, b):
    encrypted_text = ""

    for char in text.upper():
        if 'A' <= char <= 'Z':
            P_num = ord(char) - ord('A')
            C_num = (a * P_num + b) % modval
            encrypted_text += chr(C_num + ord('A'))
        else:
            encrypted_text += char
    
    return encrypted_text
    
def decrypt(text, a, b):
    decrypted_text = ""
    a_inv = modular_inverse(a)

    if a_inv == -999:
        print("Cannot decrypt")
        return ""

    for char in text.upper():
        if 'A' <= char <= 'Z':
            C_num = ord(char) - ord('A')
            
            P_num = (a_inv * (C_num - b + modval)) % modval 
            decrypted_text += chr(P_num + ord('A'))
        else:
            decrypted_text += char

    return decrypted_text

# main

a = int(input())
b = int(input())
plaintext = input()

if gcd(a, modval) != 1:
    print("Cannot decrypt")

ciphertext = encrypt(plaintext, a, b)
print(ciphertext)

decrypted = decrypt(ciphertext, a, b)
print(decrypted)
