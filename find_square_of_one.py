from functools import reduce
from chin import chinese_remainder
from factorize import factors
import sys

def roots(n):
    fac = list(factors(n))
    root = {}
    for fa in fac:
        for i in range(2,fa + 2):
            if i**2%fa==1:
                if fa in root.keys():
                    root[fa].append(i)
                else:
                    root[fa] = [i]
    return root

def dict_to_mesh(roo):
    eq = {}
    for key in roo.keys():
        for val in roo[key]:
            for key2 in roo.keys():
                for val2 in roo[key2]:
                    if (key != key2):
                        eq[(val,val2)]=(key,key2)
    return eq

def get_remainders(mesh):
    remainders = set()
    for key in mesh.keys():
        print(key,mesh[key])
        remainders.add(int(chinese_remainder(mesh[key],key)))
    return remainders




if __name__ == "__main__":
    import sys
    root = roots(int(sys.argv[1]))
    print(root)
    mesh= dict_to_mesh(root)
    remainders = get_remainders(mesh)
    print(remainders)
    #print(chinese_remainder(n,a))
