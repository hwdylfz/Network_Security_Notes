with open('hex.txt', 'r') as h:     # hex.txt为要转换的文本文件
    val = h.read()
    h.close()

with open('result.txt', 'w') as re: # 转换完成后写入result.txt
    tem = ''
    for i in range(0, len(val), 2):
        tem = '0x' + val[i] + val[i+1]
        tem = int(tem, base=16)
        print(chr(tem), end="")
        re.write(chr(tem))
    re.close()