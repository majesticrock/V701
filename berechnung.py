import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *


a24 = ufloat(-9, 0.6) * 10**4
b24 = ufloat(2, 0.1) * 10**5
c24 = 1/2 * 67653

a42 = ufloat(-2.8, 0.2) * 10**4
b42 = ufloat(6.6, 0.4) * 10**4
c42 = 1/2 * 28410

rm1 = (c24 - b24)/a24
rm2 = (c42 - b42)/a42

m24 = ufloat(-1.09, 0.02)
n24 = ufloat(4.09, 0.02)

m42 = ufloat(-0.98, 0.04)
n42 = ufloat(4.01, 0.05)

E24 = m24 * rm1 + n24
E42 = m42 * rm2 + n42
ER24 = ( ( (rm1*10)  /  (3.1) )**2 )**(1/3)
ER42 = ( ( (rm2*10)  /  (3.1) )**2 )**(1/3)

print("--------------")
print(rm1)
print(E24)
print(ER24)

print("--------------")
print(rm2)
print(E42)
print(ER42)