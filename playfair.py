
import random
import string

def create_random_keyword(length=7):
    alphabet_no_j = string.ascii_uppercase.replace("J", "")
    return "".join(random.sample(alphabet_no_j, length))

def create_keyword_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix_chars = []
    for char in keyword.upper().replace("J", "I"):
        if char not in matrix_chars:
            matrix_chars.append(char)
    for char in alphabet:
        if char not in matrix_chars:
            matrix_chars.append(char)
    
    return [matrix_chars[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)
    return None

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    i = 0
    while i < len(text):
        prepared += text[i]
        if i + 1 < len(text):
            if text[i] == text[i+1]:
                prepared += "X" 
            else:
                prepared += text[i+1]
                i += 1
        else:
            prepared += "X"
        i += 1
    return prepared

def playfair_encrypt(plaintext, matrix):
    prepared = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(prepared), 2):
        char1, char2 = prepared[i], prepared[i+1]
        r1, c1 = find_position(matrix, char1)
        r2, c2 = find_position(matrix, char2)
        
        if r1 == r2:
            ciphertext += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            ciphertext += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
    return ciphertext

def playfair_decrypt(ciphertext, matrix):
    decrypted_text = ""
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        r1, c1 = find_position(matrix, char1)
        r2, c2 = find_position(matrix, char2)
        
        if r1 == r2: 
            decrypted_text += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2: 
            decrypted_text += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else: 
            decrypted_text += matrix[r1][c2] + matrix[r2][c1]
    return decrypted_text


# main

keyword = "ABHINAV"
matrix = create_keyword_matrix(keyword)

print(f"Keyword: {keyword}")
print("Key Matrix:")
for row in matrix: 
    print(" ".join(row))

message = input().upper()

encrypted = playfair_encrypt(message, matrix)                   
decrypted = playfair_decrypt(encrypted, matrix)

print(f"\nOriginal: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

