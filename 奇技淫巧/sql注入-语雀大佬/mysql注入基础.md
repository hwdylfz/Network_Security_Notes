# MySQL 数据合并方法

## 0x01 concat()

注意：返回结果为连接参数产生的字符串，如果有任何一个参数为null，则返回值为null

用途：连接一个或多个字符串

语法：concat(str1,str2…)

```plain
# 不带NULL的

mysql> select concat('123','456','aaa','789');
+---------------------------------+
| concat('123','456','aaa','789') |
+---------------------------------+
| 123456aaa789                    |
+---------------------------------+
# 带NULL的

mysql> select concat('123','456',NULL,'aaa','789');
+--------------------------------------+
| concat('123','456',NULL,'aaa','789') |
+--------------------------------------+
| NULL                                 |
+--------------------------------------+
1 row in set
```

## 0x02 concat_ws()

注意：如果 concat_ws 的参数有NULL会无视掉

用途：使用固定连接符连接一个或多个字符串

语法：concat_ws(separator,str1,str2…)

```plain
# 不带NULL的

mysql> select concat_ws('-','aa','bb','cc');
+------------------------+
| concat_ws('-','aa','bb','cc') |
+------------------------+
| aa-bb-cc               |
+------------------------+
1 row in set
# 带NULL的

mysql> select concat_ws('-','aa','bb',NULL,'cc');
+-----------------------------+
| concat_ws('-','aa','bb',NULL,'cc') |
+-----------------------------+
| aa-bb-cc                    |
+-----------------------------+
1 row in set
```

## 0x03 group_concat()

# MySQL 常见运算符

## 0x00 概述

运算符连接表达式中各个操作数，其作用是用来指明对操作数所进行的运算。常见的运算有数学计算、比较运算、位运算以及逻辑运算。运用运算符可以更加灵活地使用表中的数据，常见的运算符类型有：算术运算符，比较运算符，逻辑运算符，位运算符等。

## 0x01 运算符概述

运算符是告诉MySQL执行特殊算术或逻辑操作的符号。MySQL的内部运算符很丰富

主要有四大类：算术运算符、比较运算符、逻辑运算符、位操作运算符。

## 0x02 算术运算符

| 运算符 | 作用              |
| ------ | ----------------- |
| +      | 加法运算          |
| -      | 减法运算          |
| *      | 乘法运算          |
| /      | 除法运算          |
| %      | 求余运算,返回余数 |

## 0x03 比较运算符

一个比较运算符的结果总是1、0或者是NULL，比较运算符经常在SELECT的查询条件字句中使用，用来查询满足指定条件的记录

| 运算符  | 作用       |
| ------- | ---------- |
| =       | 等于       |
| <=>     | 安全的等于 |
| <> , != | 不等于     |
| <=      | 小于等于   |
| >=      | 大于等于   |
| >       | 大于       |
| <       | 小于       |

## 0x04 逻辑运算符

逻辑运算符的求值所得结果均为1(TRUE)、0(FALSE)

| 运算符      | 作用                               |
| ----------- | ---------------------------------- |
| NOT或者!    | 逻辑非                             |
| AND或者&&   | 逻辑与                             |
| OR或者`||`  | 逻辑或                             |
| XOR         | 逻辑异或                           |
| IS NULL     | 判断一个值是否为NULL               |
| IS NOT NULL | 判断一个值是否不为NULL             |
| LEAST       | 在有两个或多个参数时,返回最小值    |
| GREATEST    | 当有2或多个参数时，返回最大值      |
| BETWEEN AND | 判断一个值是否落在两个值之间       |
| IN          | 判断一个值是否落在两个值之间       |
| NOT IN      | 判断一个值不是IN列表中的任意一个值 |
| LIKE        | 通配符匹配                         |
| REGEXP      | 正则表达式匹配                     |
| RLIKE       | 正则表达式匹配                     |
| NOT RLIKE   | 就是 RLIKE 取反                    |
| NOT LIKE    | 就是 LIKE 取反                     |

# MySQL 字符串长度函数

## 0x00 概要

常用函数有char_length、length、bit_length，它们针对不同的字符编码处理方式不一样。

char_length 字符显示的个数

length 字符在当前编码下存储，所占的字节数

bit_length 字符在当前编码下存储，所占的bit，也就是length*8

## 0x01 GBK 编码

select char_length('中国');  -- 结果：2

select length('中国');  -- 结果：4

select length('china');  -- 结果：5

select bit_length('中国');  -- 结果：32

## 0x02 UTF-8 编码

select char_length('中国'); -- 结果：2

select length('中国');  -- 结果：6

select length('china');  -- 结果：5

select bit_length('中国');  -- 结果：48

# MySQL 条件语句基本用法

## 0x00 基础数据

```plain
mysql> select user();
+---------------+
| user()         |
+---------------+
| root@localhost |
+---------------+
1 row in set
mysql> select * from test_table;
+----+-------+
| id | name |
+----+-------+
|  1 | bbb   |
|  2 | aaa   |
+----+-------+
2 rows in set
```

## 0x01 IF表达式

```plain
解释:  SELECT IF(表达式, 表达式成立时返回, 表达式不成立时返回)
```

### 0x01.1 IF表达式例子

```plain
mysql> select IF(1=1,1,0);
+-------------+
| IF(1=1,1,0) |
+-------------+
|           1 |
+-------------+
1 row in set (0.00 sec)
mysql> select IF(1=2,1,0);
+-------------+
| IF(1=2,1,0) |
+-------------+
|           0 |
+-------------+
1 row in set (0.00 sec)
```

### 0x02 CASE表达式

```plain
解释1: 
select case 表达式
when 判断条件 then 返回结果 
else 条件不成立时返回 end
解释2: 
case 后面紧跟要被作为判断的字段
when 后面跟判断条件
then 后面跟结果
else 相当于 default
end 是语句结束语
```

### 0x02.1 CASE表达式例子

```plain
mysql> select case 1
    -> when 1 then '成功'
    -> when 2 then '失败'
    -> else '其他' end;
----------------+
| 成功          |
+---------------+
1 row in set, 3 warnings (0.00 sec)
mysql> select case 2
    -> when 1 then '成功'
    -> when 2 then '失败'
    -> else '其他' end;
----------------+
| 失败          |
+---------------+
1 row in set, 3 warnings (0.00 sec)
mysql> select case 3
    -> when 1 then '成功'
    -> when 2 then '失败'
    -> else '其他' end;
----------------+
| 其他          |
+---------------+
1 row in set, 3 warnings (0.00 sec)
mysql> SELECT
    -> CASE
    -> WHEN 1 = 1
		-> THEN '真'
    -> ELSE '假'
    -> END;
+----------------------------------+
| 真                               |
+----------------------------------+
1 row in set



mysql> SELECT
    -> CASE
    -> WHEN 1 = 2
		-> THEN '真'
    -> ELSE '假'
    -> END;
+----------------------------------+
| 假                               |
+----------------------------------+
1 row in set
```

## 0x03 PERIOD_DIFF() 函数

```plain
PERIOD_DIFF(period1, period2)       返回两个时段之间的月份差值
```

### 0x03.1 例子

```plain
# user() 第一位数据转ascii

mysql> select ascii(substring(user(),1,1));
+------------------------+
| ascii(substring(user(),1,1)) |
+------------------------+
|                    114 |
+------------------------+
1 row in set
# user() 第二位数据转ascii

mysql> select ascii(substring(user(),2,1));
+------------------------+
| ascii(substring(user(),2,1)) |
+------------------------+
|                    111 |
+------------------------+
1 row in set
# 表示注入失败的时候

# 表示两个值相差1位
# ascii(substring(user(),1,1)) = 114
# 不为0就是表示True,那么页面就不会产生变化
mysql> select PERIOD_DIFF(ascii(substring(user(),1,1)), 113);
+----------------------------------------+
| PERIOD_DIFF(ascii(substring(user(),1,1)), 113) |
+----------------------------------------+
|                                      1 |
+----------------------------------------+
1 row in set



# 匹配失败的时候页面的数据会返回正常,不产生变化
mysql> SELECT * from test_table where id=1 and PERIOD_DIFF(ascii(substring(user(),1,1)), 113);
+----+-------+
| id | name |
+----+-------+
|  1 | bbb   |
+----+-------+
1 row in set
# 表示注入成功的时候

# 表示两个值相等
# ascii(substring(user(),1,1)) = 114
# 为0就是表示False
mysql> select PERIOD_DIFF(ascii(substring(user(),1,1)), 114);
+----------------------------------------+
| PERIOD_DIFF(ascii(substring(user(),1,1)), 114) |
+----------------------------------------+
|                                      0 |
+----------------------------------------+
1 row in set

# 匹配成功的时候,因为函数返回了0 0表示False,所以就不查询数据出来了
mysql> SELECT * from test_table where id=1 and PERIOD_DIFF(ascii(substring(user(),1,1)), 114);
Empty set
```

## 0x04 TIMEDIFF() 函数

```plain
TIMEDIFF(time1, time2)    计算时间差值
```

### 0x04.1 例子

```plain
# user() 第一位数据转ascii

mysql> select ascii(substring(user(),1,1));
+------------------------+
| ascii(substring(user(),1,1)) |
+------------------------+
|                    114 |
+------------------------+
1 row in set
# user() 第二位数据转ascii

mysql> select ascii(substring(user(),2,1));
+------------------------+
| ascii(substring(user(),2,1)) |
+------------------------+
|                    111 |
+------------------------+
1 row in set
# 表示注入失败的时候

# 表示两个值相差1位
# ascii(substring(user(),1,1)) = 114
# 不为0就是表示True,那么页面就不会产生变化
mysql> SELECT TIMEDIFF(ascii(substring(user(),1,1)), 113);
+-------------------------------------+
| TIMEDIFF(ascii(substring(user(),1,1)), 113) |
+-------------------------------------+
| 00:00:01                             |
+-------------------------------------+
1 row in set



# 匹配失败的时候页面的数据会返回正常,不产生变化
mysql> SELECT * from test_table where id=1 and TIMEDIFF(ascii(substring(user(),1,1)), 113);
+----+-------+
| id | name |
+----+-------+
|  1 | bbb   |
+----+-------+
1 row in set
# 表示注入成功的时候

# 表示两个值相等
# ascii(substring(user(),1,1)) = 114
# 为0就是表示False
mysql> SELECT TIMEDIFF(ascii(substring(user(),1,1)), 114);
+-------------------------------------+
| TIMEDIFF(ascii(substring(user(),1,1)), 114) |
+-------------------------------------+
| 00:00:00                             |
+-------------------------------------+
1 row in set

# 匹配成功的时候,因为函数返回了0 0表示False,所以就不查询数据出来了
mysql> SELECT * from test_table where id=1 and TIMEDIFF(ascii(substring(user(),1,1)), 114);
Empty set
```

## 0x05 NULLIF(expr1, expr2)

```plain
NULLIF(expr1, expr2)	比较两个字符串，如果字符串 expr1 与 expr2 相等 返回 NULL，否则返回 expr1
```

### 0x05.1 例子

```plain
# user() 第一位数据转ascii

mysql> select ascii(substring(user(),1,1));
+------------------------+
| ascii(substring(user(),1,1)) |
+------------------------+
|                    114 |
+------------------------+
1 row in set
# user() 第二位数据转ascii

mysql> select ascii(substring(user(),2,1));
+------------------------+
| ascii(substring(user(),2,1)) |
+------------------------+
|                    111 |
+------------------------+
1 row in set
# 表示注入失败的时候

# 匹配不相等的话返回的是 NULLIF 第一个参数的结果值
mysql> SELECT * from test_table where id=1 and NULLIF(ascii(substring(user(),1,1)),111);
+----+-------+
| id | name |
+----+-------+
|  1 | bbb   |
+----+-------+
1 row in set
# 表示注入成功的时候

# 匹配相等会返回 NULL 所以sql不会返回数据
mysql> SELECT * from test_table where id=1 and NULLIF(ascii(substring(user(),1,1)),114);
Empty set
# 获取到的数据转成十进制

mysql> select concat(char('114'),char('111'));
+---------------------------+
| concat(char('114'),char('111')) |
+---------------------------+
| ro                        |
+---------------------------+
1 row in set
```

## 0x06 ELT

### 0x06.1 例子

```plain
ELT(N,str1,str2,str3,...)
如果N = 1,则返回str1
如果N = 2,则返回str2,依此类推
如果N小于1或大于参数个数,则返回NULL
ELT是FIELD的补充
// 基础教学

// 为true时
mysql> select ELT('a'='a', 1);
+-----------------+
| ELT('a'='a', 1) |
+-----------------+
| 1               |
+-----------------+
1 row in set


// 为false时
mysql> select ELT('a'='b', 1);
+-----------------+
| ELT('a'='b', 1) |
+-----------------+
| NULL            |
+-----------------+
1 row in set
# user()数据

mysql> select user();
+----------------+
| user()         |
+----------------+
| root@localhost |
+----------------+
1 row in set
# 注注入 user() 第二位的数据

# 为true时
mysql> select ELT(substring(user(),2,1)='o', 1);
+-----------------------------------+
| ELT(substring(user(),2,1)='o', 1) |
+-----------------------------------+
| 1                                 |
+-----------------------------------+
1 row in set

# 为false时
mysql> select ELT(substring(user(),2,1)='a', 1);
+-----------------------------------+
| ELT(substring(user(),2,1)='a', 1) |
+-----------------------------------+
| NULL                              |
+-----------------------------------+
1 row in set
```

# MySQL 字符串截取函数

## 0x01 left 函数

说明: 从左开始截取字符串

用法: left(str, length)，即: left(被截取字符串， 截取长度)

### 0x01.1 left 例子:

```plain
mysql> SELECT LEFT('hello world',8);
+-----------------------+
| LEFT('hello world',8) |
+-----------------------+
| hello wo              |
+-----------------------+
1 row in set (0.00 sec)
```

## 0x02 right 函数

从右开始截取字符串

用法: right(str, length)，即: right(被截取字符串， 截取长度)

### 0x02.1 right 例子:

```plain
mysql> SELECT RIGHT('hello world',8);
+------------------------+
| RIGHT('hello world',8) |
+------------------------+
| lo world               |
+------------------------+
1 row in set (0.00 sec)
```

## 0x03 substring 函数

截取特定长度的字符串

用法:

- substring(str, pos)，即: substring(被截取字符串， 从第几位开始截取)
  substring(str, pos, length)
- 即: substring(被截取字符串，从第几位开始截取，截取长度)

### 0x03.1 substring 例子一

从字符串的第9个字符开始读取直至结束

```plain
mysql> SELECT SUBSTRING('hello world', 9);
+-----------------------------+
| SUBSTRING('hello world', 9) |
+-----------------------------+
| rld                         |
+-----------------------------+
1 row in set (0.00 sec)
```

### 0x03.2 substring 例子二

从字符串的第2个字符开始，只取3个字符

```plain
mysql> SELECT SUBSTRING('hello world', 2, 3);
+--------------------------------+
| SUBSTRING('hello world', 2, 3) |
+--------------------------------+
| ell                            |
+--------------------------------+
1 row in set (0.00 sec)
```

### 0x03.3 substring 例子三

从字符串的倒数第6个字符开始读取直至结束

```plain
mysql> SELECT SUBSTRING('hello world', -6);
+------------------------------+
| SUBSTRING('hello world', -6) |
+------------------------------+
|  world                       |
+------------------------------+
1 row in set (0.00 sec)
```

### 0x03.4 substring 例子四

从字符串的倒数第4个字符开始读取，只取2个字

```plain
mysql> SELECT SUBSTRING('hello world', -4, 2);
+---------------------------------+
| SUBSTRING('hello world', -4, 2) |
+---------------------------------+
| or                              |
+---------------------------------+
1 row in set (0.00 sec)
```

## 0x04 substr 函数

截取特定长度的字符串

用法:

- substr(str, pos)，即: substr(被截取字符串， 从第几位开始截取)
  substr(str, pos, length)
- 即: substr(被截取字符串，从第几位开始截取，截取长度)

### 0x04.1 substr 例子一

从字符串的第1个字符开始读取直至结束

```plain
mysql> SELECT substr('hello world', 1);
+--------------------------+
| substr('hello world', 1) |
+--------------------------+
| hello world              |
+--------------------------+
1 row in set (0.00 sec)
```

## 0x05 mid 函数

得到一个字符串的一部分

用法:

- MID(str, start [, length])
- 即: MID(被截取字符串, 从第几位开始截取, 截取长度);
- 注: MID函数从1开始，而非0，length是可选项，如果没有提供，MID()函数将返回余下的字符串。

### 0x05.1 例子一

从第1个字符开始读取直至结束

```plain
mysql> SELECT mid('hello world', 1);
+--------------------------+
| mid('hello world', 1)    |
+--------------------------+
| hello world              |
+--------------------------+
1 row in set (0.00 sec)
```

### 0x05.2 例子一

从第2个字符开始读取3个字符

```plain
mysql> SELECT mid('hello world', 2, 3);
+--------------------------+
| mid('hello world', 2, 3) |
+--------------------------+
| ell                      |
+--------------------------+
1 row in set (0.00 sec)
```

# MySQL 注释符号

## 0x01 概述

MySql 注释符有三种

```
/**/
--
#
```

# MySQL 字符转码函数

## 0x01 ascii(str)

注意：ascii函数 只会返回字符串str的最左面第一个字符的ASCII代码值。

如果str是空字符串，返回0。如果str是NULL，返回NULL。

```plain
// 104是h的ASCII值
mysql> select ascii('hi');
+-------------+
| ascii('hi') |
+-------------+
|         104 |
+-------------+
1 row in set (0.00 sec)
```

## 0x02 ord(str)

注意：ord函数与ascii函数功能都是一样的

使用ord转汉字,如果数据库编码是“UTF-8”会有8位数

```plain
mysql> SELECT ORD('简明现代魔法');
+---------------------+
| ORD('简明现代魔法') |
+---------------------+
|            15183488 |
+---------------------+
1 row in set
mysql> SELECT ORD('简');
+-----------+
| ORD('简') |
+-----------+
|  15183488 |
+-----------+
1 row in set
```

## 0x03 conv(n,from_base,to_base)

对数字n进制转换,并转换为字串返回(任何参数为null时返回null,进制范围为2-36进制,当to_base是负数时n作为有符号数否则作无符号数,conv以64位点精度工作)

```plain
mysql> select conv("a",16,2); 
　　-> '1010'
mysql> select conv("6e",18,8); 
　　-> '172'
mysql> select conv(-17,10,-18); 
　　-> '-H'
mysql> select conv(10+"10"+'10'+0xa,10,10); 
　　-> '40'
```

## 0x04 bin(n)

把n转为二进制值并以字串返回(n是bigint数字,等价于conv(n,10,2))

```plain
mysql> select bin(12); 
　　-> '1100'
```

## 0x05 oct(n)

把n转为八进制值并以字串返回(n是bigint数字,等价于conv(n,10,8))

```plain
mysql> select oct(12); 
　　-> '14'
```

## 0x06 hex(n)

把n转为十六进制并以字串返回(n是bigint数字,等价于conv(n,10,16))

```plain
mysql> select hex(255); 
　　-> 'FF'
```

## 0x07 char(n,…)

返回由参数n,…对应的ascii代码字符组成的一个字串(参数是n,…是数字序列,null值被跳过)

```plain
mysql> select char(77,121,83,81,'76'); 
　　-> 'MySQL'
mysql> select char(77,77.3,'77.3'); 
　　-> 'MMM'
```

## 0x08 concat(str1,str2,…)

把参数连成一个长字符串并返回(任何参数是null时返回null)

```plain
mysql> select concat('my', 's', 'ql'); 
　　-> 'mysql'
mysql> select concat('my', null, 'ql'); 
　　-> null
mysql> select concat(14.3); 
　　-> '14.3'
```

## 0x09 UNHEX(n)

把16进制内容转为十进制内容

```plain
# 数据转为 16进制
mysql> select hex('test');
+-------------+
| hex('test') |
+-------------+
| 74657374    |
+-------------+
1 row in set (0.00 sec)
# 数据16进制转为10进制
mysql> select UNHEX(74657374);
+-----------------+
| UNHEX(74657374) |
+-----------------+
| test            |
+-----------------+
1 row in set (0.00 sec)
```

# MySQL 基本数据查询

## 0x00 查询MySql安装路径

select @@basedir;

```plain
mysql> select @@basedir;
+--------------------------------+
| @@basedir                      |
+--------------------------------+
| D:/phpStudy/PHPTutorial/MySQL/ |
+--------------------------------+
1 row in set (0.00 sec)
```

## 0x01 查询当前连接数据库

select database();

```plain
mysql> select database();
+------------+
| database() |
+------------+
| test       |
+------------+
1 row in set (0.00 sec)
```

## 0x02 查询用户

select user();

```plain
mysql> select user();
+----------------+
| user()         |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)
```

select current_user;

```plain
mysql> select current_user;
+----------------+
| current_user   |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)
```

select current_user();

```plain
mysql> select current_user();
+----------------+
| current_user() |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)
```

select system_user();

```plain
mysql> select system_user();
+----------------+
| system_user()  |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)
```

select SESSION_USER();

```plain
mysql> select SESSION_USER();
+----------------+
| system_user()  |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)
```

## 0x03 查询当前连接的数据库版本

select version();

```plain
mysql> select version();
+-----------+
| version() |
+-----------+
| 5.5.53    |
+-----------+
1 row in set (0.00 sec)
```

select @@version;

```plain
mysql> select @@version;
+-----------+
| @@version |
+-----------+
| 5.5.53    |
+-----------+
1 row in set (0.00 sec)
```

## 0x04 文件读取最大值

select @@max_allowed_packet;

```plain
mysql> select @@max_allowed_packet;
+----------------------+
| @@max_allowed_packet |
+----------------------+
|              1048576 |
+----------------------+
1 row in set (0.00 sec)
```

# MySQL 查询每个表数据量的语句

```shell
SELECT table_name, table_rows, TABLE_SCHEMA FROM INFORMATION_SCHEMA.TABLES ORDER BY table_rows desc;
```

