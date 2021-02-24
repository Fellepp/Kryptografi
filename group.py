import math
import sys
from factorize import factors


def group(p):
    start = 1
    for i in range(start, p):
        if math.gcd(i, p) == 1:
            yield i


if __name__ == "__main__":
    p = int(sys.argv[1])
    grop = list(group(p))
    print("group ",grop," length=",len(grop))
