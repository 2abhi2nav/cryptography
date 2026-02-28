p = 5
q = 7
n = p * q
phi = (p - 1) * (q - 1)

e = 5 
d = pow(e, -1, phi)

message = "ABHINAV"
m_values = [ord(char) for char in message]

signatures = [pow(m % n, d, n) for m in m_values]

verified_values = [pow(s, e, n) for s in signatures]

is_valid = all((m % n) == v for m, v in zip(m_values, verified_values))

print(f"primes = {p}, {q}")
print(f"n = {n}")
print(f"public key = ({n}, {e})")
print(f"private key = ({n}, {d})")
print(f"message = {message}")
print(f"signed message (signature) = {signatures}")
print(f"verification {'succeeded' if is_valid else 'failed'}")

