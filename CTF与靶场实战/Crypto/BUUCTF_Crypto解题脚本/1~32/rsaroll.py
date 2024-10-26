import gmpy2
n=920139713
e=19
p=18443
q=49891
#pq就是分解质因数n来的
d=gmpy2.invert(e,(p-1)*(q-1))
result=[]

with open("C:\Learning\Summer2023\CTF\Training\\25~36\\RsaRoll\\data.txt","r") as f:
    for line in f.readlines():
        line=line.strip('\n')
        result.append(chr(pow(int(line),d,n)))

for i in result:
    print(i,end='')