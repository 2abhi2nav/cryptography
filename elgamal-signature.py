import math

p = 7
g = 3
x = 5
y = pow(g, x, p)

message = "ABHINAV"
m_values = [ord(char) for char in message]

k = 5
k_inv = pow(k, -1, p - 1)

signatures = []
for m in m_values:
    r = pow(g, k, p)
    s = (k_inv * (m - x * r)) % (p - 1)
    signatures.append((r, s))

verified = []
for m, (r, s) in zip(m_values, signatures):
    v1 = pow(g, m, p)
    v2 = (pow(y, r, p) * pow(r, s, p)) % p
    verified.append(v1 == v2)

is_valid = all(verified)

print(f"primes = {p}, {5}")
print(f"public key (p, g, y) = ({p}, {g}, {y})")
print(f"private key x = {x}")
print(f"message = {message}")
print(f"signed message (signature) = {signatures}")
print(f"verification {'succeeded' if is_valid else 'failed'}")
