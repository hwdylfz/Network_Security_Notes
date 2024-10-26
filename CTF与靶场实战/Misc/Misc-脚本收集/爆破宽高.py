import struct
import binascii
import os
 
m = open("flag.png","rb").read()
print(m[20:29])
for i in range(5000):
    for j in range(5000):
        c = m[12:16] + struct.pack('>i', i) + struct.pack('>i', j)+m[24:29]
        crc = binascii.crc32(c) & 0xffffffff
        if crc == 0xd9f88e3f:
            print(c)
            print(i,j)
            break
