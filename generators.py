import math
import sys
from factorize import factors


def group(p):
    start = 1
    for i in range(start, p):
        if math.gcd(i, p) == 1:
            yield i


def get_generators(grp,p):
    factors_gen = list(factors(p-1))
    for i in grp:
        broken=False
        for prime_fact in factors_gen:
            if i**((p-1)/prime_fact) %p ==1:
                broken=True
        if not broken:
            yield i

if __name__ == "__main__":
    p = int(sys.argv[1])
    grop = group(p)
    generators = list(get_generators(grop,p))
    print("generators",generators," length=",len(generators))
