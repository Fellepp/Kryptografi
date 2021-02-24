from get_int_from_letter import get_letter
from inverse_modular import egcd, modinv
# Prints a transposition table for an affine cipher.
# a must be coprime to m=26.


def decrypt(a,b,l):
    return chr(((modinv(a,26)*(l-b)%26) +ord('A')))


if __name__ == "__main__":
    import sys
    a =int(sys.argv[1])
    b = int(sys.argv[2])
    word = sys.argv[3]
    s = ""
    for let in word:
        s += str(decrypt(a,b,get_letter(let)))
    print(s)
