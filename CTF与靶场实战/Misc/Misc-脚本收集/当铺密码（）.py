s ='田由中人工大王夫井羊'
code=input("请输入当铺密码：")
code = code.split(" ")
w = ''
for i in code:
    k=""
    for j in i:
       k+=str(s.index(j))
    w+=chr(int(k))
print(w)
