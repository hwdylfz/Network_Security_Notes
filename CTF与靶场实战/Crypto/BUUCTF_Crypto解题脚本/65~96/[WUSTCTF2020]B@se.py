import string
c = 'JASGBWcQPRXEFLbCDIlmnHUVKTYZdMovwipatNOefghq56rs****kxyz012789+/'
#for i in string.ascii_letters + string.digits:  # string.ascii_letters所有字母  string.digits所有数字
    #if(i not in c):
        #print(i,end='')
# ju34

import binascii
import itertools
cipher = 'MyLkTaP3FaA7KOWjTmKkVjWjVzKjdeNvTnAjoH9iZOIvTeHbvD' # 全排列组合
s = ['j','u','3','4']
for i in itertools.permutations(s,4): # 4就是把s列表里的字母4个为一组排列
    k = "JASGBWcQPRXEFLbCDIlmnHUVKTYZdMovwipatNOefghq56rs"+ "".join(i) + "kxyz012789+/"  # "".join(i)排列的结果（join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串）
    a = ""
    for j in cipher:
        a += bin(k.index(j))[2:].zfill(6)
    print(binascii.a2b_hex(hex(eval("0b"+a))[2:-1]))  # a2b_hex和binascii.unhexlify可以为16进制的 bytes 类型，也可以为十六进制 str 类型
                                                      # 举例：这里转为16进制后会出现0x471L，所以只有去掉0x和L就有了[2:-1]