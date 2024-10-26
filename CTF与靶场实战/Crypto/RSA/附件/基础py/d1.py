#!/usr/bin/python
#coding:utf-8
#@Author:醉清风

import gmpy2
p = 3487583947589437589237958723892346254777
q = 8767867843568934765983476584376578389
e = 65537
phi = (p-1)*(q-1)
d = gmpy2.invert(e,phi) #e模phi的逆为d,   ( e * d ) % phi == 1 
print d
