import sys
import random
from inverse_modular import modinv

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
m1 = int(sys.argv[4])
m2 = int(sys.argv[5])
m3 = int(sys.argv[6])

def chineese(a,b,c,m1,m2,m3):
  inv1 = modinv(m2*m3,a)
  inv2 = modinv(m1*m3,b)
  inv3 = modinv(m1*m2,c)
  x1 = a*m2*m3*inv1
  x2 = b*m1*m3*inv2
  x3 = c*m1*m2*inv3
  print(x1,x2,x3)
  print(inv1,inv2,inv3)
  return (x1+x2+x3) %(m1*m2*m3)

print("returns ",chineese(a,b,c,m1,m2,m3))
