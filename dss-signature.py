p = 7  
q = 3  
g = 2  

x = 2  
y = pow(g, x, p)  

message = "ABHINAV"
m_values = [ord(char) for char in message]

signatures = []
k = 2 
k_inv = pow(k, -1, q)

for m in m_values:
    
    r = (pow(g, k, p)) % q
    s = (k_inv * (m + x * r)) % q
    
    if s == 0:
        s = (k_inv * ((m + 1) + x * r)) % q
        
    signatures.append((r, s))

verification_results = []
for m, (r, s) in zip(m_values, signatures):
    
    w = pow(s, -1, q)
    u1 = (m * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    verification_results.append(v == r)

is_valid = all(verification_results)

print(f"primes (p, q) = {p}, {q}")
print(f"public key (y) = {y}")
print(f"private key (x) = {x}")
print(f"message = {message}")
print(f"signed message (r, s) = {signatures}")
print(f"verification {'succeeded' if is_valid else 'failed'}")
