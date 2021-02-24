import sys
import random
import math

a = int(sys.argv[1])
b = int(sys.argv[2])


def exp_func(x, y):
    mult=0
    sqr=0
    exp = bin(y)
    value = x
    for i in range(3, len(exp)):
      value = value * value
      sqr+=1
      print (i-1,":\t",value,"(square)")
      if(exp[i:i+1]=='1'):
        mult+=1
        value = value*x
      print (i-2,":\t",value,"(multiply)")
    print("mult",mult,"sqr",sqr)
    return value

print ("We will calculate a^b")
print ("a=",a)
print ("b=",b)
print ("==== Calculation ====")
res=exp_func(a,b)
print ("Result:",res)
