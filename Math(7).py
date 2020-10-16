#Polar Coordinates:
import cmath
x = complex(input())
c = cmath.polar(x)
print(c[0])
print(c[1])


#Find Angle MBC:
from math import *
AB = eval(input())
BC = eval(input())
t = AB/BC
teta = int(round(degrees(atan(t)), 0))
print(str(teta)+'°')


#Triangle Quest 2:
for i in range(1,int(input())+1):
    print(((10**i-1)//9)**2)


#Mod Divmod:
a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmod(a, b))


#Power - Mod Power:
a = int(input())
b = int(input())
m = int(input())
print(a**b)
print(pow(a, b, m))


#Integers Come In All Sizes:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print((a**b) + (c**d))


#Triangle Quest:
for i in range(1,int(input())):
    print((10**(i)//9)*i)

