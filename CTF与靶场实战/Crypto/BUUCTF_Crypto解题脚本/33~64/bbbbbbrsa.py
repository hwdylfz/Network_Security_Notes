from base64 import b64encode as b32encode
from base64 import b64decode as b32decode
import gmpy2
from Crypto.Util.number import *
from binascii import a2b_hex,b2a_hex
import random

# flag = "******************************"

# nbit = 128

# p = getPrime(nbit)
# q = getPrime(nbit)
# n = p*q

# print p
# print n

# phi = (p-1)*(q-1)

# e = random.randint(50000,70000)

# while True:
# 	if gcd(e,phi) == 1:
# 		break;
# 	else:
# 		e -= 1;

# c = pow(int(b2a_hex(flag),16),e,n)

# print b32encode(str(c))[::-1]

# 2373740699529364991763589324200093466206785561836101840381622237225512234632
p = 177077389675257695042507998165006460849
n = 37421829509887796274897162249367329400988647145613325367337968063341372726061
q = n//p
phi = (p-1)*(q-1)
c = '==gMzYDNzIjMxUTNyIzNzIjMyYTM4MDM0gTMwEjNzgTM2UTN4cjNwIjN2QzM5ADMwIDNyMTO4UzM2cTM5kDN2MTOyUTO5YDM0czM3MjM'
c = str(c)[::-1]
print (b32decode(str(c)))
c = int(b32decode(str(c)))
e = random.randint(50000,70000)

for e in range (50000,70000):
	if gmpy2.gcd(e,phi) == 1:
	    d = gmpy2.invert(e,phi)
	    m = pow(c,d,n)
	    print(m)
	    if 'flag' in str(long_to_bytes(m)):
		    print(long_to_bytes(m))
		    break