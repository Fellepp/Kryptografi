import math
from inverse_modular import modinv

def get_pairs(g, n,sq):
    l = []
    for i in range(sq):
        l.append ((i,g ** i % (n)))
    return l

def get_a_inv(g,n,sq):
    sq_mod = (g ** sq )% n
    inv = modinv(sq_mod, (n))
    return inv

def baby_shark(g,b,n):
    sq = math.ceil(math.sqrt(n - 1))
    pairs = get_pairs(g,n,sq)
    print("pairs:",pairs)
    a_inv = get_a_inv(g, n,sq)
    b_w = b
    for i in range(sq):
        for j,val in pairs:
            if val ==b_w:
                return i,j,sq
        b_w= b_w*a_inv %n
    print("shiet")



if __name__ == "__main__":
    import sys
    g = int(sys.argv[1])
    b = int(sys.argv[2])
    n = int(sys.argv[3])
    i,j,sq = baby_shark(g,b,n)
    print(f"g={g},n={n}. {g}^x={b} mod {n}")
    print(i,j)
    print(f"x ={i}*{sq} + {j} = {i*sq+j}")
