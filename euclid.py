
def euclid(a, b):
    while (b != 0):
        q = a // b
        r = a - q*b
        a = b
        b = r

    print("GCD: ", a)

# main

a = int(input())
b = int(input())

euclid(a, b)

