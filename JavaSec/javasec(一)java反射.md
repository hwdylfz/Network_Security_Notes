---
title: javasec(一)java反射
tags:
  - java
  - websec
  - javasec
  - 反序列化
categories:
  - websec
  - javasec
  - 反序列化
cover: 'https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/1.jpeg'
feature: false
date: 2023-04-16 17:25:11

---

这篇文章介绍javasec基础知识--java反射。

<!--More-->

### 0x01 反射是什么？

[反射](https://so.csdn.net/so/search?q=反射&spm=1001.2101.3001.7020)是一种机制,利用反射机制动态的实例化对象、读写属性、调用方法、构造函数。

在**程序运行状态中**，**对于任意一个类或对象，都能够获取到这个类的所有属性和方法**（包括私有属性和方法），**这种动态获取信息以及动态调用对象方法的功能就称为反射机制**。简单来讲，通过反射，类对我们是完全透明的，想要获取任何东西都可以。

通过反射，我们可以在**程序运行时动态创建对象**，还能获取到类的所有信息，比如它的属性、构造器、方法、注解等（无法获取父类被projected修饰的东西）

### 0x02 铺垫知识

#### 1.java代码的三个阶段及class对象的由来

1. Source源代码阶段：.java被编译成*.class字节码文件。
2. Class类对象阶段：.class字节码文件被类加载器加载进内存，并将其封装成Class对象（用于在内存中描述字节码文件），**Class对象**将原字节码文件中的成员变量抽取出来封装成数组Field[],将原字节码文件中的构造函数抽取出来封装成数组Construction[]，将成员方法封装成数组Method[]。当然Class类内不止这三个，还封装了很多，我们常用的就这三个。(Class对象的由来:  将class文件读入内存，并为之创建一个Class对象)
3. RunTime运行时阶段：使用new创建对象的过程。
4. 示意图两张：

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304161725757.png)

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304161725931.png)

#### 2.获取class对象的3种方法

1）**Class.forName(类的全限定名/全路径名) -----常用**

通过类的全限定名获取该类的class对象，多用于**配置文件**，将类名定义在配置文件中，通过读取配置文件加载类。  

2）**类名.class**

通过类的属性class获取class对象。{所有数据类型（包括基本数据类型）都有的一个“静态的”class属性。} 多用于**参数的传递**

3）**对象.getClass()**

 此方法是定义在Objec类中的方法，因此所有的类都会继承此方法。多用于**对象获取字节码**的方式  

注意：**在运行期间，一个类，只有一个Class对象产生！**

先写一个Person类用于测试：

```java
package Reflect;
public class Person {
    public String name;
    public float high;
    protected int age;
    char sex;
    private String phoneNum;
    //无参构造方法
    public Person(){
        System.out.println("调用了公有、无参构造方法执行了。。。");
    }

    //有一个参数的构造方法
    public Person(String name){
        this.name = name;
        System.out.println("调用了一个参数的构造方法\n"+"姓名：" + name);
    }

    //有多个参数的构造方法
    public Person(String name ,int age){
        this.name = name;
        this.age = age;
        System.out.println("调用了两个参数的构造方法"+"姓名："+name+"年龄："+ age);//这的执行效率有问题，以后解决。
    }

    //受保护的构造方法
    protected Person(boolean n){
        System.out.println("调用受保护的构造方法 n = " + n);
    }

    //私有构造方法
    private Person(int age){
        System.out.println("私有的构造方法   年龄："+ age);
    }
}
package Reflect;

public class getClass {
    public static void main(String[] args) throws Exception {

        //方式一：Class.forName("全类名");
        Class class1 = Class.forName("Reflect.Person");   //Person自定义实体类
        System.out.println("class1 = " + class1);

        //方式二：类名.class
        Class class2 = Person.class;
        System.out.println("class2 = " + class2);

        //方式三：对象.getClass();
        Person person = new Person();
        Class class3 = person.getClass();
        System.out.println("class3 = " + class3);

        //比较三个对象
        System.out.println(class1 == class2);    //true
        System.out.println(class1 == class3);    //true
    }
}
```

执行结果：

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304161725673.png)

从执行比较结果看，**三种方法获取到的class对象都是同一个。**

**也就是说：****在运行期间，一个类，只有一个Class对象产生**

### 0x03 代码中的利用

#### 1.获取属性/字段 用Field类

```java
获取成员变量并调用：
1.批量的
 		1).Field[] getFields():获取所有的"公有字段"
 		2).Field[] getDeclaredFields():获取所有字段，包括：私有、受保护、默认、公有；
2.获取单个的：
 		1).public Field getField(String fieldName):获取某个"公有的"字段；
 		2).public Field getDeclaredField(String fieldName):获取某个字段(可以是私有的)
获取字段值：Field --> get(对象)
设置字段的值：
 		Field --> public void set(对象,值): 					
参数说明：
1.obj:要设置的字段所在的对象；
2.value:要为字段设置的值；
package Reflect;
import java.lang.reflect.Field;

public class GetZd {
    public static void main(String[] args) throws Exception{
        //获取Person1类的Class对象
        Class Zd = Class.forName("Reflect.Person1");
        //获取public字段name：
        System.out.println("获取单个公有字段并调用"+Zd.getField("name")+"\n");
        //获取cn从父类Person继承的public字段who
        System.out.println("获取单个从父类继承的公有字段并调用"+Zd.getField("who")+"\n");
        //获取private字段phoneNum：
        System.out.println("获取单个私有字段并调用"+Zd.getDeclaredField("phoneNum")+"\n");
        //获取全部公有字段
        System.out.println("获取全部公有字段如下："+"\n");
        Field[] a = Zd.getFields();
        for(Field b : a){
           System.out.println(b);
        }
        //获取所有字段（包括公有、私有、受保护）
        System.out.println("获取全部字段如下："+"\n");
        Field[] c = Zd.getDeclaredFields();
        for(Field d : c){
            System.out.println(d);
        }
        //获取值与设置值
        Object xx = Zd.getConstructor().newInstance();
        Person1 x = (Person1)xx; //先通过反射得到的Class类对象Zd得到一个Person1类的对象
        //name.get()中的参数需要该类的对象，而不能是.class
        Field name = Zd.getField("name");
        System.out.println("直接输出name，无法获取值："+name+"\n");
        System.out.println("用name.get(对象)方法获得值为："+name.get(x)+"\n");
        //设置值
        //Field --> public void set(Object obj,Object value):
  		//参数说明：1.obj:要设置的字段所在的对象；2.value:要为字段设置的值；
        name.set(x,"uf9n1x3333");
        System.out.println("set后姓名为："+x.name+"\n");

        //获取并设置私有字段
        Field phonen = Zd.getDeclaredField("phoneNum");
        System.out.println();
        phonen.setAccessible(true);//暴力反射，解除私有限定
        phonen.set(x,"7777777");
        System.out.println("私有Set后phoneNum为："+x);//因为PhoneNum为私有权限，所以这里不能用x.PhoneNum输出它的值，所以就全输出出来看
    }
}
```

输出如下：

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304161725010.png)

#### 2. 获取方法   用Method类

Class类提供了以下几个方法来获取方法：

```java
 Method getMethod(name, Class...)：获取某个public的Method（包括父类）
 Method getDeclaredMethod(name, Class...)：获取当前类的某个Method（不包括父类）
 Method[] getMethods()：获取所有public的Method（包括父类）
 Method[] getDeclaredMethods()：获取当前类的所有Method（不包括父类）
```

**执行方法使用invoke()**

##### 2.1 通过反射来使用substring

```java
package Reflect;
import java.lang.reflect.Method;

public class Test {
    public static void main(String[] args) throws Exception{
        String name = "uf9n1x";
        Method substring1 = String.class.getMethod("substring", int.class);
        //Object a = substring1.invoke(name,3);
        //String aa = (String)a;
        //System.out.println(aa);
        System.out.println(substring1.invoke(name,3));
    }
}
```

**如果调用的方法是****静态方法****。那么invoke方法传入的第一个参数永远为null**

```java
// 获取Integer.parseInt(String)方法，参数为String: 
Method m = Integer.class.getMethod("parseInt", String.class); 
// 调用该静态方法并获取结果: 
Integer n = (Integer) m.invoke(null, "23333"); 
System.out.println(n);
```

##### 2.2 暴力反射成员方法

```java
m = stuClass.getDeclaredMethod("show4", int.class);//调用制定方法（所有包括私有的），需要传入两个参数，第一个是调用的方法名称，第二个是方法的形参类型，切记是类型。
System.out.println(m);
m.setAccessible(true);//解除私有限定
Object result = m.invoke(obj, 20);//需要两个参数，一个是要调用的对象（获取有反射），一个是实参
System.out.println("返回值：" + result);
```

#### 3. 获取构造方法 用Constructor类

通过Class实例获取Constructor的方法如下：

```java
Constructor-->getConstructor(Class...)：获取某个public的Constructor；
Constructor-->getDeclaredConstructor(Class...)：获取某个Constructor；
Constructor-->getConstructors()：获取所有public的Constructor；
Constructor-->getDeclaredConstructors()：获取所有Constructor。

eg:
//先获取Person的Class对象
Class Gz = Person1.class;
//获取有参的构造函数public Person(String name, Integer age) 参数类型顺序要与构造函数内一致，且参数类型为字节码文件类型
Constructor c2 = Gz.getConstructor(String.class,Integer.class);
//使用获取到的有参构造函数创建对象
Object person2 = constructor2.newInstance("zhangsan", 22);   //获取的是有参的构造方法，就必须要指定参数
System.out.println(person2);
```

**调用非public的Constructor时，必须首先通过setAccessible(true)设置允许访问。setAccessible(true)可能会失败。**

##### **3.1 反射执行命令**

```java
 Class.forName("java.lang.Runtime").getMethod("exec", String.class).invoke(Class.forName("java.lang.Runtime").getMethod("getRuntime").invoke(Class.forName("java.lang.Runtime")),"calc");
拆开来：
Object a = Class.forName("java.lang.Runtime").getMethod("getRuntime").invoke(Class.forName("java.lang.Runtime"));
Class.forName("java.lang.Runtime").getMethod("exec", String.class).invoke(a,"calc");
```

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304161725824.png)**exec.invoke(a,"calc");相当于就是a.exec("calc");**

**而a是什么，a是通过getRuntime()方法获取到的Runtime类的实例对象。**



因为Runtime类没有构造器可用，所以不能创建Runtime类的实例。

Runtime类有一个静态方法：getRuntime()，这个方法可以返回一个Runtime类的实例。这也是我们唯一获取Runtime类实例的办法。

Runtime r = Runtime.getRuntime();

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304161725053.png)![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304161725629.png)

#### **4.反射main()方法**

```java
package fanshe.main;
 
import java.lang.reflect.Method;
 
/**
 * 获取Student类的main方法、不要与当前的main方法搞混了
 */
public class Main {
	
	public static void main(String[] args) {
		try {
			//1、获取Student对象的字节码
			Class clazz = Class.forName("fanshe.main.Student");
			
			//2、获取main方法
			 Method methodMain = clazz.getMethod("main", String[].class);//第一个参数：方法名称，第二个参数：方法形参的类型，
			//3、调用main方法
			// methodMain.invoke(null, new String[]{"a","b","c"});
			 //第一个参数，对象类型，因为方法是static静态的，所以为null可以，第二个参数是String数组，这里要注意在jdk1.4时是数组，jdk1.5之后是可变参数
			 //这里拆的时候将  new String[]{"a","b","c"} 拆成3个对象。。。所以需要将它强转。
			 methodMain.invoke(null, (Object)new String[]{"a","b","c"});//方式一
			// methodMain.invoke(null, new Object[]{new String[]{"a","b","c"}});//方式二
			
		} catch (Exception e) {
			e.printStackTrace();
		}	
	}
}
```

#### 5.修改被final、static关键字修饰的成员变量

##### 5.1 修改final修饰的非String类型变量（直接反射修改即可）

声明一个final修饰的name如下. 接下来使用反射来对它进行修改. 目的也就是使name指向一个新的StringBuilder对象.

```java
public class Pojo2 {
private final StringBuilder name = new StringBuilder("default");
public void printName() {
System.out.println(name);
}
}
```

咱们看看反射的威力吧, **它能修改final的字段的指向.也就是让name字段指向一个新的地址.**

```java
//获取一个对象
Pojo2 p = new Pojo2();
// 查看被修改之前的值
p.printName();
// 反射获取字段, name成员变量
Field nameField = p.getClass().getDeclaredField("name");
// 由于name成员变量是private, 所以需要进行访问权限设定
nameField.setAccessible(true);
// 使用反射进行赋值
nameField.set(p, new StringBuilder("111"));
// 打印查看被修改后的值
p.printName();
```

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304161725183.png)

##### 5.2 修改final修饰的String类型变量（使其运行后才能得值）

把上面的例子修改一下：

```java
public class Pojo {
private final String name = "defult";
public void printName() {
System.out.println(name);
}
}
```

还是用上面的方法去修改：

```java
//获取一个对象
Pojo p = new Pojo();
// 查看被修改之前的值
p.printName();
// 反射获取字段, name成员变量
Field nameField = p.getClass().getDeclaredField("name");
// 由于name成员变量是private, 所以需要进行访问权限设定
nameField.setAccessible(true);
// 使用反射进行赋值
nameField.set(p, "111");
// 打印查看被修改后的值
p.printName();
```

发现修改失败了：

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304161725845.png)

因为JVM在编译时期, 就把final类型的String进行了优化, 在编译时期就会把String处理成常量, 所以 Pojo里的printName()方法, 就相当于:

```java
public void printName() {
System.out.println("default");
}
```

其实name的值是赋值成功了, 只是printName()方法在JVM优化后就被写死了, 所以无论name是否被正确修改为其他的值, printName始终都会打印"default3".

 final修饰的String在JVM编译时就被处理为常量, 怎么样防止这种现象呢?  

其实**只需要使用一些手段让final String类型的name的初始值经过一次运行才能得到**, 那么就不会在编译时期就被处理为常量了  

```java
public class Pojo {
// 防止JVM编译时就把"default4"作为常量处理
private final String name = (null == null ? "default" : "");

public void printName() {
System.out.println(name);
}
}
```

此时，再来测试修改：

```java
Pojo p = new Pojo();
p.printName();
Field nameField = p.getClass().getDeclaredField("name");
nameField.setAccessible(true);
nameField.set(p, "111");
p.printName();
```

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304161725212.png)

发现可以修改成功。

##### 5.3 （重点）修改 final + static修饰符的变量 

```java
public class Pojo {
private final static String name = "default";
public void printName() {
System.out.println(name);
}
}
```

此时如果还是用上面的方法去修改：

```java
Pojo p = new Pojo();
p.printName();
Field nameField = p.getClass().getDeclaredField("name");
nameField.setAccessible(true);
nameField.set(p, "111");
p.printName();
```

 执行之后会报出如下异常, 因为**反射无法修改同时被static final修饰的变量**:  

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304161725060.png)那该怎么修改呢？

思路是这样的, **先通过反射把name字段的final修饰符去掉**看如下代码:

先把name字段通过反射取出来, 这个和之前的步骤都一样, 反射出来的字段类型(Field)命名为'nameField'

```java
Field nameField = p.getClass().getDeclaredField("name");
nameField.setAccessible(true);
```

接下来再通过反射, 把nameField的final修饰符去掉:

```java
Field modifiers = nameField.getClass().getDeclaredField("modifiers");
modifiers.setAccessible(true);
modifiers.setInt(nameField, nameField.getModifiers() & ~Modifier.FINAL);//去除final修饰符
```

然后就可以正常对name字段进行值的修改了.

```java
nameField.set(p, new StringBuilder("111"));
```

最后别忘了再把final修饰符加回来:

```java
modifiers.setInt(nameField, nameField.getModifiers() & ~Modifier.FINAL);
```

本例子中反射部分完整的代码如下:

```java
Pojo p = new Pojo();
p.printName();
Field nameField = p.getClass().getDeclaredField("name");
nameField.setAccessible(true);
Field modifiers = nameField.getClass().getDeclaredField("modifiers");
modifiers.setAccessible(true);
modifiers.setInt(nameField, nameField.getModifiers() & ~Modifier.FINAL);//去除Final
nameField.set(p, "111");
modifiers.setInt(nameField, nameField.getModifiers() & ~Modifier.FINAL);//补回final
p.printName();
```

