#标准当铺密码加密解密， 空格分割
code= "田由中人工大王夫井羊".decode('utf-8')
split = ""
def encode(s):
    S = s.decode('utf-8')
    buff = ""
    if len(s) > 0:
        for c in s:
            str1 = str(ord(c))
            for st in str1:
                buff += code[int(st)]
            buff += split
    return buff

def decode(s):
    s = s.decode( 'utf-8')
    buff = ""
    temp = ""
    if len(s) > 0:
        stringList = s.split(split)
        for s1 in stringList:
            for s2 in s1:
                index = code.find(s2)
                if index>-1:
                    temp += str(index)
            buff += chr(int(temp))
            temp = ''
    return buff