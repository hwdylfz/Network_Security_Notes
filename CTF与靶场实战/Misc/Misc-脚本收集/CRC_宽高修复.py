import zlib
import struct

# 读文件
file = 'fuck1.png'  # 图片要和脚本在同一个文件夹下
fr = open(file, 'rb').read()
data = bytearray(fr[12:29])# 生成字节数组
crc32key = eval(str(fr[29:33]).replace('\\x', '').replace("b'", '0x').replace("'", '')) # 格式化
n = 4095  # 理论上0xffffffff,但考虑到屏幕实际，0x0fff就差不多了
for w in range(n):  # 高和宽一起爆破
    width = bytearray(struct.pack('>i', w))  # q为8字节; i为4字节; h为2字节
    for h in range(n):
        height = bytearray(struct.pack('>i', h))
        for x in range(4):
            data[x + 4] = width[x]
            data[x + 8] = height[x]
            # print(data)
        crc32result = zlib.crc32(data) # CRC校验和
        if crc32result == crc32key:
            print(width, height)
            # 写文件
            newpic = bytearray(fr)
            for x in range(4):
                newpic[x + 16] = width[x]
                newpic[x + 20] = height[x]
            fw = open(file + '.png', 'wb')  # 保存副本
            fw.write(newpic)
            fw.close