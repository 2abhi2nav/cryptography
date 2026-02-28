
p = 8081
q = 101
e1 = 6968
e2 = 2038
d = 61
h_M = 5000
r = 61

s1 = pow(e1, r, p) % q

r_inv = pow(r, -1, q)
s2 = (r_inv * (h_M + d * s1)) % q

w = pow(s2, -1, q)

u1 = (h_M * w) % q
u2 = (s1 * w) % q

v = (pow(e1, u1, p) * pow(e2, u2, p) % p) % q

is_valid = (v == s1)

print(f"p = {p}, q = {q}")
print(f"e1 = {e1}, e2 = {e2}")
print(f"Private Key d = {d}")
print(f"h(M) = {h_M}, r = {r}")
print(f"S1 = {s1}")
print(f"S2 = {s2}")
print(f"v = {v}")
print(f"verification {'succeeded' if is_valid else 'failed'}")
