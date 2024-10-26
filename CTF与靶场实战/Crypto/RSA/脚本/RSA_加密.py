from Crypto.Util.number import *
import gmpy2

msg = 'flag is :testflag'
hex_msg=int(hex(str2long(msg)),16)
print(hex_msg)
p=getPrime(100)
q=getPrime(100)
n=p*q
e=0x10001
phi=(p-1)*(q-1)
d=gmpy2.invert(e,phi)
print("d=",hex(d))
c=pow(hex_msg,e,n)
print("e=",hex(e))
print("n=",hex(n))
print("c=",hex(c))