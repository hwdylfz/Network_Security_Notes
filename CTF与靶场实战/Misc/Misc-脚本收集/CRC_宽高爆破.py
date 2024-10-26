import binascii
import struct
crcbp = open("fuck1.png", "rb").read()
for i in range(2000):
    for j in range(2000):
        data = crcbp[12:16] + struct.pack('>i', i)+struct.pack('>i', j)+crcbp[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if(crc32 == 0x9c7dab5b):#根据图片的CRC32值来修改
            print(i, j)
            print('hex:', hex(i), hex(j))