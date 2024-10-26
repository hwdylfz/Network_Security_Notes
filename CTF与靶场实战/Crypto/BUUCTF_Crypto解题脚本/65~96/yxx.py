key = open("C:\Learning\\2239\\Summer2023\CTF\Training\Crypto\\61~72\yxx\密文.txt", 'rb').read()
cipher = open("C:\Learning\\2239\\Summer2023\CTF\Training\Crypto\\61~72\yxx\明文.txt", "rb").read()

flag = []
result = ""
for i in range(len(key)):
    flag.append(key[i] ^ cipher[i])
    result += chr(flag[i])
print(flag)
print(result)