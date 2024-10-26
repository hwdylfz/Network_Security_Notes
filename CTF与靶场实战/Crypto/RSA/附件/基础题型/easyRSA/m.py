#!/usr/bin/python
#coding:utf-8
#@Author:醉清风

#已知N,使用factor可计算出p和q
#还知道e以及密文c

import libnum
from Crypto.Util.number import long_to_bytes

c = 0xdc2eeeb2782c
n = 322831561921859
e = 23
q = 13574881
p = 23781539

d = libnum.invmod(e, (p - 1) * (q - 1))
m = pow(c, d, n)
print "m的值为:"
print long_to_bytes(m)
