#!/usr/bin/env python3
import math

if __name__ == "__main__":
    import sys
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(f"The gcd of {x} and {y} is {math.gcd(x,y)}")
