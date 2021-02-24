import sys
import random
import math

num = int(sys.argv[1])

def amount_of_two(num):
    i = 0
    while num % 2 ==0 and num !=0:
        i+=1
        num= int(num//2)
    return i



def test(num):
    v=amount_of_two(num-1)
    u= int((num-1)//(2**v))
    print(u,v)
    a_list = [random.randint(1,num)]
    a_list = [4]
    #a_list = [2,3,5,7,11,13,17]
    for a in a_list:
        b = a**u %num
        print("b",b)
        if b==1:
            return False
        for j in range(0,v):
            if b==num-1:
                return False
            else:
                b=b**2 %num
                print(b)
        #return True
    return True
print("composite?",test(num))
print("factor of number could be found by taking gcd of b-1 and number if composite")
