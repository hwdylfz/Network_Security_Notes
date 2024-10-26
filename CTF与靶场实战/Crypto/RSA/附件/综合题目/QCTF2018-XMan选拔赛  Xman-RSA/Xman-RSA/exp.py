#!/usr/bin/python
#coding:utf-8

import base64
import libnum
import gmpy2
from Crypto.Util.number import long_to_bytes

lines = open('ciphertext','r').readlines()
msg1c1 = int(lines[0],16)
msg2c2 = int(lines[1],16)

lines = open('n2&n3','r').readlines()
n2 = int(base64.b64decode(lines[0]).encode('hex'),16)
n3 = int(base64.b64decode(lines[1]).encode('hex'),16)

lines=open('n1.encrypted','r').readlines()
n1c1 = int(lines[0],16)
n1c2 = int(lines[1],16)

e1 = 0x1001
e2 = 0x101

#使用共模攻击得到n1
_, r, s = gmpy2.gcdext(e1,e2)
n1 = pow(n1c1, r, n3) * pow(n1c2, s, n3) %n3


#n1,n2有一个共同的质因数p1
# n1 += n3  # 存在n3比n1小的可能，并且确实如此;貌似主办方中途改题，把n1改成小于n3了。
p1 = gmpy2.gcd(n1, n2)
assert (p1 != 1)
p2 = n1 / p1
p3 = n2 / p1
e = 0x1001
d1 = gmpy2.invert(e, (p1 - 1) * (p2 - 1))
d2 = gmpy2.invert(e, (p1 - 1) * (p3 - 1))
msg1 = pow(msg1c1, d1, n1)
msg2 = pow(msg2c2, d2, n2)
print long_to_bytes(msg1)+long_to_bytes(msg2)
