import sys
import random
import math


num = int(sys.argv[1])
e = int(sys.argv[2])
d = int(sys.argv[3])

def amount_of_two(num):
    i = 0
    while num % 2 ==0 and num !=0:
        i+=1
        num= num/2
    return i



def test(num,e,d):
    factors=set()
    testnum = e*d-1
    v=amount_of_two(testnum)
    u= int((testnum)/(2**v))
    a = random.randint(1,num)
    #a = 185
    print(u,v,a,num)
    for i in range(0,v+1):
        o = (a**(2**i*u)) % num
        if o==0 and (a**(2**i*u)) != 1:
            factors.add(math.gcd(num,(a**((2**i)*u))-1))
    return factors


print("composite?",test(num,e,d))

