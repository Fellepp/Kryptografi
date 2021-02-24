import math
from random import randrange

def millerboi(e, d, n):
    u = (e*d-1)//2
    while u%2 == 0:
        u = u//2
    v = int(math.log2((e*d-1)//u))
    print(u,v)
    r = 0
    while r < 15:
        print(r)
        a = randrange(n)
        seq = []

        for i in range(v + 1):
            seq.append(math.gcd(a ** ((2 ** i) * u) - 1, n))

        for element in seq:
            if element == 1 or element == n: continue
            if n % element == 0: return element, (1/(r+1))
        r += 1
    return -1

if __name__ == "__main__":
    import sys

    e = int(sys.argv[1])
    d = int(sys.argv[2])
    n = int(sys.argv[3])
    print(f"{e=}") 
    factor = millerboi(e, d, n)

    if factor == -1:
        print("Could not find any factors")
    else: print("A factor of " + str(n) + " is " + str(factor[0]) + ", with the probability of "+ str(factor[1] * 100) + "%")



