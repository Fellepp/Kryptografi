from get_int_from_letter import get_letter
from inverse_modular import egcd, modinv
# Prints a transposition table for an affine cipher.
# a must be coprime to m=26.

def get_alpha(x,y,a,mod):
    print(f"alpha = (3*{x}**2+{a})*modinv(2*{y},{mod})) % {mod}")
    print(f"alpha = ({3*x**2}+{a})*{modinv(2*y,mod)}) % {mod} = {((3*x**2+a)*modinv(2*y,mod)) % mod}")
    return ((3*x**2+a)*modinv(2*y,mod)) % mod

def get_x(a,x,mod):
    print(f"x = ({a}**2 -2*{x})%{mod} = {(a**2 -2*x)%mod}")
    return (a**2 -2*x)%mod

def get_y(a,x,x2,y,mod):
    print(f"y= ({a}*({x}-{x2})-{y})%{mod} = {(a*(x-x2)-y)%mod}")
    return (a*(x-x2)-y)%mod



if __name__ == "__main__":
    import sys
    # X**3 + a*X + b
    x =int(sys.argv[1])
    y = int(sys.argv[2])
    a = int(sys.argv[3])
    mod = int(sys.argv[4])
    alpha = get_alpha(x,y,a,mod)
    x3 = get_x(alpha,x,mod)
    y3 = get_y(alpha,x,x3,y,mod)
    print(f"The fast exponentail of ({x},{y}) % {mod} and ax where a={a} is \n ({x3},{y3})")
