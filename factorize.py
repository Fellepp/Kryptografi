from functools import reduce
import sys


def factors(n):
    while n > 1:
        for i in range(2, n+ 1):
            if n % i == 0:
                n //= i
                yield i
                break


if __name__ == "__main__":
    n = int(sys.argv[1])
    print("prime factorer of ",n," is ",list(factors(n)))
