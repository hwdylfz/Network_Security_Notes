from gmpy2 import invert
from base64 import b64encode

c = "welcylk"
a = 11
b = 6
n = 26

in_a = invert(a, n)#求a mod n的逆元
print(in_a)
# in_a = 19

m = []
for i in c:
    modified_c = ord(i)-97
    m.append((modified_c-b)*in_a % 26)
flag = ""
for mi in m:
    flag += chr(mi+97)

print(flag)
print(b64encode(flag.encode()))