
def row_transposition_encrypt(plaintext, key_str):
    num_cols = len(key_str)
    while len(plaintext) % num_cols != 0:
        plaintext += 'X'
    
    grid = [list(plaintext[i:i+num_cols]) for i in range(0, len(plaintext), num_cols)]
    
    print("\nEncryption matrix:")
    for row in grid:
        print(" ".join(row))

    key_order = sorted(range(num_cols), key=lambda k: key_str[k])
    ciphertext = "".join(row[col] for col in key_order for row in grid)
    return ciphertext

def row_transposition_decrypt(ciphertext, key_str):
    num_cols = len(key_str)
    num_rows = len(ciphertext) // num_cols
    key_order = sorted(range(num_cols), key=lambda k: key_str[k])
    
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    curr = 0
    for col in key_order:
        for row in range(num_rows):
            grid[row][col] = ciphertext[curr]
            curr += 1
            
    return "".join("".join(row) for row in grid)

plaintext = "ABHINAV"
key = "9006"

encrypted = row_transposition_encrypt(plaintext, key)
decrypted = row_transposition_decrypt(encrypted, key)

print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Ciphertext: {encrypted}")
print(f"Decrypted Message: {decrypted}")
