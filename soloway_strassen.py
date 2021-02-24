import random


def jacobi(a, n):
    j = 1  # j is jacobi symbol
    while (a != 0):

        while (a % 2 == 0):  # loop till a is even number
            j = j * pow(-1, (n * n - 1) / 8)  # if n=3(mod 8) or n=5(mod 8) or simply (-1)^((n^2-1)/2)==-1 then j = -j
            a = a / 2

        if not ((a - 3) % 4 or (n - 3) % 4):  # if a=3(mod 4) and n=3(mod 4) [So, (a-3)%4 and (n-3)%4 = 0] or simply (-1)^((n 1)/2)==-1 then j = -j
            j = -j

        a, n = n, a  # interchange(a,n)
        a = a % n
    return j


def solovay_strassen(n, k=10):
    if n == 2 or n == 3:
        return True
    if not n & 1:
        return False

    for i in range(k):
        a = random.randrange(2, n - 1)  # choose any random number from 1 to (n-1)
        x = jacobi(a, n)  # find n's jacobi number
        y = pow(a, (n - 1) // 2, n)  # calculate legendre symbol from euler criterion formula
        if y != 1 and y != 0:
            y = -1

        if (x == 0) or (y != x):  # if jecobi and eular criterion formula are not same (y != x) then the number is not prime
            return False
    return True

if __name__ == "__main__":
    import sys
    a = int(sys.argv[2])
    n = int(sys.argv[3])
    print(jacobi(a,n))
