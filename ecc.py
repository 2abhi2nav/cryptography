
id="eccdemo01"
print("Elliptic Curve: y^2 = x^3 + ax + b (mod p)")

p = 97
a = 2
b = 3

# Check if point lies on curve
def is_on_curve(P):
    if P is None:
        return True
    x, y = P
    return (y*y - (x*x*x + a*x + b)) % p == 0

# Modular inverse
def inv(n):
    return pow(n, -1, p)

# Point addition
def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P != Q:
        m = ((y2 - y1) * inv(x2 - x1)) % p
    else:
        m = ((3*x1*x1 + a) * inv(2*y1)) % p

    x3 = (m*m - x1 - x2) % p
    y3 = (m*(x1 - x3) - y1) % p
    return (x3, y3)

# Scalar multiplication
def mul(k, P):
    R = None
    while k:
        if k & 1:
            R = add(R, P)
        P = add(P, P)
        k >>= 1
    return R

# Compute all points on curve
points = []
for x in range(p):
    for y in range(p):
        if is_on_curve((x, y)):
            points.append((x, y))
points.append(None)  # point at infinity

print("Total points:", len(points))

# Base point
G = points[0]
print("Base point G:", G, "On curve:", is_on_curve(G))

# Key generation
dA = 5
dB = 7
QA = mul(dA, G)
QB = mul(dB, G)

# Shared secret (ECDH)
S1 = mul(dA, QB)
S2 = mul(dB, QA)

print("Shared secrets match:", S1 == S2)

# Simple encryption (toy)
msg = 42
k = 3
C1 = mul(k, G)
C2 = (msg + S1[0]) % p

# Decryption
S = mul(dB, C1)
dec = (C2 - S[0]) % p

print("Encrypted:", (C1, C2))
print("Decrypted message:", dec)

