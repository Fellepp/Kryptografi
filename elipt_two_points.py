from get_int_from_letter import get_letter
from inverse_modular import egcd, modinv


# Prints a transposition table for an affine cipher.
# a must be coprime to m=26.

def get_alpha(x1, y1, x2, y2, mod):
    print(f"alpha =((y2-y1)*modinv(x2-x1,mod)) % mod")
    print(f"alpha =(({y2}-{y1})*modinv({x2}-{x1},mod)) % {mod}")
    print(f"alpha =(({y2 - y1})*modinv({x2 - x1},mod)) % {mod}")
    print(f"alpha =(({y2 - y1})*{modinv(x2 - x1, mod)}) % {mod} = {((y2 - y1) * modinv(x2 - x1, mod)) % mod}")
    return ((y2 - y1) * modinv(x2 - x1, mod)) % mod


def get_x(a, x1, x2, mod):
    print(f"x = ({a}**2 -{x1} -{x2})%{mod} = {(a ** 2 - x1 - x2) % mod}")
    return (a ** 2 - x1 - x2) % mod


def get_y(a, x1, x2, y, mod):
    print(f"y= ({a}*({x1}-{x2})-{y})%{mod} = {(a * (x1 - x2) - y) % mod}")
    return (a * (x1 - x2) - y) % mod


if __name__ == "__main__":
    import sys

    x1 = int(sys.argv[1])
    y1 = int(sys.argv[2])
    x2 = int(sys.argv[3])
    y2 = int(sys.argv[4])
    mod = int(sys.argv[5])
    if x1 == x2 and y1 == (mod - y2):
        print(f"x1=x2 and y1 is the negative of y2")
        print(" 0,0 ")
    alpha = get_alpha(x1, y1, x2, y2, mod)
    x3 = get_x(alpha, x1, x2, mod)
    y3 = get_y(alpha, x1, x3, y1, mod)
    print(f"The fast exponentail of ({x1},{y1}) and ({x2},{y2}) % {mod} and  is \n ({x3},{y3})")
