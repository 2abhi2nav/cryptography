
modval = 26

a = int(input())
for i in range(1, modval):
    if (a * i) % modval == 1:
        print(i, " mod ", modval)
