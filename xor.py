
def xor_cipher_program():
    plaintext = "ABHINAV"
        
    numeric_key = "47"

    generated_key = "".join(numeric_key[i % 2] for i in range(len(plaintext)))

    pt_ascii = [ord(c) for c in plaintext]
    key_ascii = [ord(c) for c in generated_key]
    
    print(f"\nPlaintext: {plaintext}")
    print(f"Plaintext ASCII: {pt_ascii}")
    print(f"Generated Key: {generated_key}")
    print(f"Key ASCII: {key_ascii}")


    cipher_bytes = [pt_ascii[i] ^ key_ascii[i] for i in range(len(plaintext))]

    cipher_binary = [format(b, '08b') for b in cipher_bytes]
    cipher_chars = "".join(chr(b) for b in cipher_bytes)

    print(f"\nCiphertext binary: {' '.join(cipher_binary)}")
    print(f"Ciphertext character: {repr(cipher_chars)}")


    decrypted_bytes = [cipher_bytes[i] ^ key_ascii[i] for i in range(len(plaintext))]
    decrypted_text = "".join(chr(b) for b in decrypted_bytes)

    print(f"\nDecrypted Text: {decrypted_text}")


# main

xor_cipher_program()
