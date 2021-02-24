import random

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    neg = False
    if (a< 0):
        a = abs(a)
        neg=True
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m if not neg else -x%m
if __name__ == "__main__":
    import sys

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("inverse of ",a,"and",b,"is",modinv(a,b))
