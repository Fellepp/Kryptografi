import math


def fact(n):
    f = [1, 1]
    d = 0
    i = 0
    while i <= n:
        d = math.sqrt(n+i**2)
        print(d)
        if d.is_integer():
            f[0] = d-i
            f[1] = d+i
            return f
        i += 1
    return f


if __name__ == "__main__":
    n = int(input("n: "))
    x = fact(n)
    print("Your factor is ", x)

