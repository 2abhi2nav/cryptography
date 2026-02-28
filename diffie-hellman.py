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

    a = 6
    b = 15
    print(f"Alice private key a: {a}")
    print(f"Bob private key b: {b}")

    A = pow(g, a, p)
    B = pow(g, b, p)
    print(f"\nAlice sends value A: {A}")
    print(f"Bob sends value B: {B}")

    alice_shared = pow(B, a, p)
    bob_shared = pow(A, b, p)
    print(f"\nAlice shared secret: {alice_shared}")
    print(f"Bob shared secret: {bob_shared}")

    if alice_shared == bob_shared:
        print("\nShared secrets match")
    else:
        print("\nShared secrets don't match")
