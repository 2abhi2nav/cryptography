def mod_inverse(a, m):
    return pow(a, m - 2, m)


def keygen(q):
    alpha = 2
    Xa = 13
    Ya = pow(alpha, Xa, q)
    return (q, alpha, Ya), Xa


def encrypt_number(M, public_key):
    q, alpha, Ya = public_key
    k = 5
    K = pow(Ya, k, q)
    C1 = pow(alpha, k, q)
    C2 = (K * M) % q
    return (C1, C2)


def decrypt_number(cipher, Xa, q):
    C1, C2 = cipher
    K = pow(C1, Xa, q)
    M = (C2 * mod_inverse(K, q)) % q
    return M


def main():
    q = 131
    user_input = int(input("Plaintext: "))
    public_key, Xa = keygen(q)
    encrypted = encrypt_number(user_input, public_key)
    decrypted = decrypt_number(encrypted, Xa, q)
    print(f"Public key (q, alpha, Ya): {public_key}")
    print(f"Private key (Xa): {Xa}")
    print(f"Ciphertext (C1, C2): {encrypted}")
    print(f"Decrypted: {decrypted}")


main()