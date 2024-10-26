---
title: javasec(三)类加载机制
tags:
  - javasec
  - websec
  - java
categories:
  - javasec
cover: 'https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/1.jpeg'
feature: false
date: 2023-04-19 17:17:30
---

这篇文章介绍java的类加载机制。

<!--More-->

Java是一个依赖于JVM（Java虚拟机）实现的跨平台的开发语言。Java程序在运行前需要先编译成class文件，Java类初始化的时候会调用java.lang.ClassLoader加载类字节码，ClassLoader会调用JVM的native方法（defineClass0/1/2）来定义一个java.lang.Class实例。

## ClassLoader加载器

一切的Java类都必须经过JVM加载后才能运行，而ClassLoader的主要作用就是Java类文件的加载。
[![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304191718610.png)](https://img2022.cnblogs.com/blog/2670873/202205/2670873-20220509172303946-42180192.png)
在JVM类加载器中最顶层的是Bootstrap ClassLoader（引导类加载器）、Extension ClassLoader（扩展类加载器）、App ClassLoader（系统类加载器），AppClassLoader是默认的类加载器，如果类加载时我们不指定类加载器的情况下，默认会使用AppClassLoader加载类，ClassLoader.getSystemClassLoader()返回的系统类加载器也是AppClassLoader。

**ClassLoader**类有如下核心方法：

1. loadClass（加载指定的Java类）
2. findClass（查找指定的Java类）
3. findLoadedClass（查找JVM已经加载过的类）
4. defineClass（定义一个Java类）
5. resolveClass（链接指定的Java类）

## Java类动态加载方式

Java类加载方式分为显式和隐式,显式即我们通常使用Java反射或者ClassLoader来动态加载一个类对象，而隐式指的是类名.方法名()或new类实例。显式类加载方式也可以理解为类动态加载，我们可以自定义类加载器去加载任意的类。

```java
// 反射加载TestHelloWorld示例
Class.forName("com.test.classloader.TestHelloWorld");

// ClassLoader加载TestHelloWorld示例
this.getClass().getClassLoader().loadClass("com.test.classloader.TestHelloWorld");

/*
Class.forName("类名")默认会初始化被加载类的静态属性和方法，
如果不希望初始化类可以使用Class.forName("类名", 是否初始化类, 类加载器)，而ClassLoader.loadClass默认不会初始化类方法。
*/
//隐式
TestHelloWorld.get()
  
Class test = new TestHelloWorld()
```

**其他加载方式**：

URLClassLoader 任意类加载：file/http/jar

ClassLoader.defineClass 字节码加载任意类

Unsafe.defineClass 字节码加载

## ClassLoader类加载流程

ClassLoader加载com.test.classloader.TestHelloWorld类重要流程如下：

```vbnet
1.ClassLoader会调用public Class<?> loadClass(String name)方法加载com.test.classloader.TestHelloWorld类。
2.调用findLoadedClass方法检查TestHelloWorld类是否已经初始化，如果JVM已初始化过该类则直接返回类对象。
3.如果创建当前ClassLoader时传入了父类加载器（new ClassLoader(父类加载器)）就使用父类加载器加载TestHelloWorld类，否则使用JVM的Bootstrap ClassLoader加载。
4.如果上一步无法加载TestHelloWorld类，那么调用自身的findClass方法尝试加载TestHelloWorld类。
5.如果当前的ClassLoader没有重写了findClass方法，那么直接返回类加载失败异常。如果当前类重写了findClass方法并通过传入的com.test.classloader.TestHelloWorld类名找到了对应的类字节码，那么应该调用defineClass方法去JVM中注册该类。
6.如果调用loadClass的时候传入的resolve参数为true，那么还需要调用resolveClass方法链接类，默认为false。
7.返回一个被JVM加载后的java.lang.Class类对象。
```

## 自定义ClassLoader

java.lang.ClassLoader是所有的类加载器的父类，java.lang.ClassLoader有非常多的子类加载器，比如我们用于加载jar包的java.net.URLClassLoader其本身通过继承java.lang.ClassLoader类，重写了findClass方法从而实现了加载目录class文件甚至是远程资源文件。
![image-20230421143003401](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304211430502.png)
但是如果com.test.classloader.TestHelloWorld根本就不存在于我们的classpath，那么我们可以使用自定义类加载器重写findClass方法，然后在调用defineClass方法的时候传入TestHelloWorld类的字节码的方式来向JVM中定义一个TestHelloWorld类，最后通过反射机制就可以调用TestHelloWorld类的hello方法了。

```java
package com.test.classloader;

import java.lang.reflect.Method;

public class TestClassLoader extends ClassLoader {

    // TestHelloWorld类名
    private static String testClassName = "com.test.classloader.TestHelloWorld";

    // TestHelloWorld类字节码
    private static byte[] testClassBytes = new byte[]{
            -54, -2, -70, -66, 0, 0, 0, 51, 0, 17, 10, 0, 4, 0, 13, 8, 0, 14, 7, 0, 15, 7, 0,
            16, 1, 0, 6, 60, 105, 110, 105, 116, 62, 1, 0, 3, 40, 41, 86, 1, 0, 4, 67, 111, 100,
            101, 1, 0, 15, 76, 105, 110, 101, 78, 117, 109, 98, 101, 114, 84, 97, 98, 108, 101,
            1, 0, 5, 104, 101, 108, 108, 111, 1, 0, 20, 40, 41, 76, 106, 97, 118, 97, 47, 108,
            97, 110, 103, 47, 83, 116, 114, 105, 110, 103, 59, 1, 0, 10, 83, 111, 117, 114, 99,
            101, 70, 105, 108, 101, 1, 0, 19, 84, 101, 115, 116, 72, 101, 108, 108, 111, 87, 111,
            114, 108, 100, 46, 106, 97, 118, 97, 12, 0, 5, 0, 6, 1, 0, 12, 72, 101, 108, 108, 111,
            32, 87, 111, 114, 108, 100, 126, 1, 0, 40, 99, 111, 109, 47, 97, 110, 98, 97, 105, 47,
            115, 101, 99, 47, 99, 108, 97, 115, 115, 108, 111, 97, 100, 101, 114, 47, 84, 101, 115,
            116, 72, 101, 108, 108, 111, 87, 111, 114, 108, 100, 1, 0, 16, 106, 97, 118, 97, 47, 108,
            97, 110, 103, 47, 79, 98, 106, 101, 99, 116, 0, 33, 0, 3, 0, 4, 0, 0, 0, 0, 0, 2, 0, 1,
            0, 5, 0, 6, 0, 1, 0, 7, 0, 0, 0, 29, 0, 1, 0, 1, 0, 0, 0, 5, 42, -73, 0, 1, -79, 0, 0, 0,
            1, 0, 8, 0, 0, 0, 6, 0, 1, 0, 0, 0, 7, 0, 1, 0, 9, 0, 10, 0, 1, 0, 7, 0, 0, 0, 27, 0, 1,
            0, 1, 0, 0, 0, 3, 18, 2, -80, 0, 0, 0, 1, 0, 8, 0, 0, 0, 6, 0, 1, 0, 0, 0, 10, 0, 1, 0, 11,
            0, 0, 0, 2, 0, 12
    };

    @Override
    public Class<?> findClass(String name) throws ClassNotFoundException {
        // 只处理TestHelloWorld类
        if (name.equals(testClassName)) {
            // 调用JVM的native方法定义TestHelloWorld类
            return defineClass(testClassName, testClassBytes, 0, testClassBytes.length);
        }

        return super.findClass(name);
    }

    public static void main(String[] args) {
        // 创建自定义的类加载器
        TestClassLoader loader = new TestClassLoader();

        try {
            // 使用自定义的类加载器加载TestHelloWorld类
            Class testClass = loader.loadClass(testClassName);

            // 反射创建TestHelloWorld类，等价于 TestHelloWorld t = new TestHelloWorld();
            Object testInstance = testClass.newInstance();

            // 反射获取hello方法
            Method method = testInstance.getClass().getMethod("hello");

            // 反射调用hello方法,等价于 String str = t.hello();
            String str = (String) method.invoke(testInstance);

            System.out.println(str);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
```

## 双亲委派

当一个类加载器收到类加载请求的时候，它首先不会自己去加载这个类的信息，而是把该请求转发给父类加载器，依次向上。所以所有的类加载请求都会被传递到父类加载器中，只有当父类加载器中无法加载到所需的类，子类加载器才会自己尝试去加载该类。当当前类加载器和所有父类加载器都无法加载该类时，抛出ClassNotFindException异常。
这么做的目的是：

```cpp
1.防止重复加载同一个.class
2.保证核心.class不被篡改，提高系统安全性
```

## 类的卸载

1、 有JVM自带的三种类加载器Bootstrap ClassLoader（引导类加载器）、Extension ClassLoader（扩展类加载器）、App ClassLoader（系统类加载器）加载的类始终不会卸载。因为JVM始终引用这些类加载器，这些类加载器使用引用他们所加载的类，因此这些Class类对象始终是可到达的。
2、由用户自定义类加载器加载的类，是可以被卸载的。

```vbnet
JVM中的Class只有满足以下三个条件，才能被GC回收机制回收，也就是该Class被卸载（unload）：
1.该类所有的实例都已经被GC，也就是JVM中不存在该Class的任何实例
2.加载该类的ClassLoader已经被GC
3.该类的java.lang.Class 对象没有在任何地方被引用，如不能在任何地方通过反射访问该类的方法
```
