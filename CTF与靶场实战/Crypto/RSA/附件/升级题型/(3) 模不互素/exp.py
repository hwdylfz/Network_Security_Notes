#!/usr/bin/python
#coding:utf-8
#@Author:醉清风

import gmpy2
from Crypto.Util.number import long_to_bytes

lines = open('tmp.txt','r').readlines()

c1 = int(lines[2],16)
c2 = int(lines[6],16)
n1 = int(lines[0])
n2 = int(lines[4])

p1 = gmpy2.gcd(n1, n2)
assert (p1 != 1)
p2 = n1 / p1
p3 = n2 / p1
e = 0x10001
d1 = gmpy2.invert(e, (p1 - 1) * (p2 - 1))
d2 = gmpy2.invert(e, (p1 - 1) * (p3 - 1))
m1 = pow(c1, d1, n1)
m2 = pow(c2, d2, n2)
print long_to_bytes(m1)+long_to_bytes(m2)
