import libnum
e = 101
n = 52419317100235286358057114349639882093779997394202082664044401328860087685103
p = 184980129074643957218827272858529362113
q = 283378097758180413812138939650885549231
c = 0x459cc234f24a2fb115ff10e272130048d996f5b562964ee6138442a4429af847


R.<x> = Zmod(p)[]
f = x ^ e - c
f = f.monic()
res1 = f.roots()

R.<x> = Zmod(q)[]
f = x ^ e - c
f = f.monic()
res2 = f.roots()

for i in res1:
    for j in res2:
        # 普普通通中国剩余定理
        m = crt(int(i[0]),int(j[0]),p,q)
        flag = libnum.n2s(int(m))
        if b"vsctf" in flag:
            print(flag)