https://oceansec.blog.csdn.net/article/details/121023558?spm=1001.2101.3001.6650.12&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-12-121023558-blog-132787790.235%5Ev38%5Epc_relevant_default_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-12-121023558-blog-132787790.235%5Ev38%5Epc_relevant_default_base&utm_relevant_index=13

# rsa基本认识

```python
N：大整数N，我们称之为模数（modulus）
p 和 q ：大整数N的两个因子（factor）
e 和 d：互为模反数的两个指数（exponent）
c 和 m：分别是密文和明文

{N,e}称为公钥,{N,d}称为私钥
```

```python
加密过程：
c=m^e mod n
c=pow(m,e,n)

解密过程：
m=c^d mod n
m=pow(c,d,n)

求解私钥d：
d = gmpy2.invert(e, (p-1)*(q-1))
```

一般来说，n，e是公开的，但是由于n一般是两个大素数的乘积，所以我们很难求解出d，所以RSA加密就是利用现代无法快速实现大素数的分解，所存在的一种安全的非对称加密

# 应用流程

```python
1.选取两个较大的互不相等的质数p和q，计算n = p * q 。
2.计算phi = (p-1) * (q-1) 。
3.选取任意e，使得e满足 1<e<phi 且 gcd(e , phi) == 1 。
4.计算e关于 phi 的模逆元d， 即d满足(e * d)% phi ==1 。
5.加解密：c = (m ^ e) % n ， m = (c ^ d) % n 。其中m为明文，c为密文，(n,e)为公钥对，d为私钥，要求 0 <= m < n
```
# 相关工具

## 0x01 [CTF-RSA-tool](https://github.com/3summer/CTF-RSA-tool)（装在kali了）

```python
安装之前必须先安装这四个库(PyCrypto,GMPY2,SymPy,requests)

git clone https://github.com/Ganapati/RsaCtfTool.git 
cd RsaCtfTool  //进入这个目录
安装python第三方库
pip install -r requirements.txt
```

用法：

用法一：已知公钥(自动求私钥) –publickey，密文 —-uncipherfile。
将文件解压复制到RsaCtfTool里

    python RsaCtfTool.py --publickey 公钥文件 --uncipherfile 加密的文件

用法二：已知公钥求私钥

    python RsaCtfTool.py --publickey 公钥文件 --private

用法三：密钥格式转换——把PEM格式的公钥转换为n，e

    python RsaCtfTool.py --dumpkey --key 公钥文件

用法四：密钥格式转换——把n,e转换为PEM格式

```python
python RsaCtfTool.py --createpub -n 782837482376192871287312987398172312837182 -e 65537
```

## 0x02 rsatool

```shell
git clone https://github.com/ius/rsatool.git
cd rsatool  //进入这个目录
python setup.py install
```

提供模数和私有指数，PEM输出到key.pem：

```shell
python rsatool.py -f PEM -o key.pem -n 13826123222358393307 -d 9793706120266356337
```

提供两个素数，DER输出到key.der：

```shell
python rsatool.py -f DER -o key.der -p 4184799299 -q 3303891593
```

项目地址:https://github.com/ius/rsatool

## 0x03 openssl

1. 生成PKCS#1私钥

    openssl genrsa -out rsa_prikey.pem 1024
    -out 指定生成文件，此文件包含公钥和私钥两部分，所以即可以加密，也可以解密
    1024 生成密钥的长度(生成私钥为PKCS#1)

2.把RSA私钥转换成PKCS8格式

    openssl pkcs8 -topk8 -inform PEM -in rsa_prikey.pem -outform PEM -nocrypt -out prikey.pem 

3. 根据私钥生成公钥

    openssl rsa -in rsa_prikey.pem -pubout -out pubkey.pem
    -in 指定输入的密钥文件
    -out 指定提取生成公钥的文件(PEM公钥格式)

4. 提取PEM RSAPublicKey格式公钥

    openssl rsa -in key.pem -RSAPublicKey_out -out pubkey.pem
    -in 指定输入的密钥文件
    -out 指定提取生成公钥的文件(PEM RSAPublicKey格式)

5. 公钥加密文件

    openssl rsautl -encrypt -in input.file -inkey pubkey.pem -pubin -out output.file
    -in 指定被加密的文件
    -inkey 指定加密公钥文件
    -pubin 表面是用纯公钥文件加密
    -out 指定加密后的文件

6. 私钥解密文件

    openssl rsautl -decrypt -in input.file -inkey key.pem -out output.file
    -in 指定需要解密的文件
    -inkey 指定私钥文件
    -out 指定解密后的文件

ras 的用法如下：

```
openssl rsa [-inform PEM|NET|DER] [-outform PEM|NET|DER] [-in filename] [-passin arg] [-out filename] [-passout arg]
       [-sgckey] [-des] [-des3] [-idea] [-text] [-noout] [-modulus] [-check] [-pubin] [-pubout] [-engine id]</pre>

常用选项：

-in filename：指明私钥文件
-out filename：指明将提取出的公钥保存至指定文件中 
-pubin:根据公钥提取出私钥
-pubout：根据私钥提取出公钥 
```

## 0x04 sagemath

下载地址：https://mirrors.tuna.tsinghua.edu.cn/sagemath/linux/64bit/index.html

安装

```
tar xvf sage-8.0-Ubuntu_16.04-x86_64.tar.bz2
cd SageMath
```

## 0x05 分离整数(yafu)

yafu：q、p差值太大或者太小，p+1/p-1光滑，适用Fermat或Pollard rho法分解

# 相关攻击

## 0x00 基础的RSA加密脚本

```python
from Crypto.Util.number import *
import gmpy2

msg = 'flag is :testflag'
hex_msg=int(msg.encode("hex"),16)
print(hex_msg)
p=getPrime(100)
q=getPrime(100)
n=p*q
e=0x10001
phi=(p-1)*(q-1)
d=gmpy2.invert(e,phi)
print("d=",hex(d))
c=pow(hex_msg,e,n)
print("e=",hex(e))
print("n=",hex(n))
print("c=",hex(c))
```



## 0x01 基础RSA解密脚本

```python
# -*- coding:utf-8 -*-
import binascii
import gmpy2
n=0x80b32f2ce68da974f25310a23144977d76732fa78fa29fdcbf
#这边我用yafu分解了n
p=780900790334269659443297956843
q=1034526559407993507734818408829
e=0x10001
c=0x534280240c65bb1104ce3000bc8181363806e7173418d15762


phi=(p-1)*(q-1)
d=gmpy2.invert(e,phi)
m=pow(c,d,n)
print(hex(m))
print(binascii.unhexlify(hex(m)[2:].strip("L")))
```

