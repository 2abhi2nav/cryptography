
import math

def get_primitive_roots(p):
    roots = []
    phi = p - 1
    factors = []
    n = phi
    d = 2

    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1

    if n > 1:
        factors.append(n)

    for res in range(2, p):
        is_root = True
        for f in factors:
            if pow(res, phi // f, p) == 1:
                is_root = False
                break
        if is_root:
            roots.append(res)

    return roots

p = int(input("Enter prime number p: "))
roots = get_primitive_roots(p)

if len(roots) < 1:
    print("No primitive roots.")

else:
    print(f"Primitive roots: {roots}")

    g = roots[0]
    print(f"\nSelected root g: {g}")
    
    a = 1750
    b = 1755
    c = 1760
    
    print(f"Alice private key a: {a}")
    print(f"Bob private key b: {b}")
    print(f"Charlie private key c: {c}")

    A_round1 = pow(g, a, p)
    B_round1 = pow(g, b, p)
    C_round1 = pow(g, c, p)
    print(f"\nRound 1: \nAlice: {A_round1} \nBob: {B_round1} \nCharlie: {C_round1}")

    A_round2 = pow(C_round1, a, p)
    B_round2 = pow(A_round1, b, p)
    C_round2 = pow(B_round1, c, p)
    print(f"\nRound 2: \nAlice: {A_round2} \nBob: {B_round2} \nCharlie: {C_round2}")

    alice_shared = pow(C_round2, a, p)
    bob_shared = pow(A_round2, b, p)
    charlie_shared = pow(B_round2, c, p)

    print(f"\nAlice shared secret: {alice_shared}")
    print(f"Bob shared secret: {bob_shared}")
    print(f"Charlie shared secret: {charlie_shared}")

    if alice_shared == bob_shared == charlie_shared:
        print("\nShared secrets match")
    else:
        print("\nShared secrets don't match")

