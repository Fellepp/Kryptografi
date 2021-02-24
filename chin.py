from functools import reduce
import sys
def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod/n_i
        print(f"a*n_i*inv(p,n_i) = {a_i}* {p}*",mul_inv(p,n_i))
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod
def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1
#n=[23,31]
#a=[8,7]
if __name__ == "__main__":
    a = [int(i) for i in sys.argv[1].split(",")]
    n = [int(i) for i in sys.argv[2].split(",")]
    for i,num in enumerate(a):
        print(num," % ", n[i])
    print(chinese_remainder(n,a))
