---
title: javasec(六)RMI
tags:
  - java
  - javasec
  - websec
categories:
  - java
  - javasec
cover: 'https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/10.jpeg'
feature: false
date: 2023-04-18 16:03:15

---

这篇文章介绍java-RMI远程方法调用机制。

<!--More-->

RMI全称是Remote Method Invocation，远程⽅法调⽤。是让某个Java虚拟机上的对象调⽤另⼀个Java虚拟机中对象上的⽅法，只不过RMI是**Java独有**的⼀种**RPC**方法。看这篇之前可以先去看看RPC：https://www.bilibili.com/video/BV1zE41147Zq?from=search&seid=13740626242455157002

## RMI流程

**RMI远程⽅法调⽤的流程：**
[![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304191720474.png)](https://img2022.cnblogs.com/blog/2670873/202205/2670873-20220512130620792-184181070.png)
先介绍各个部分的功能作用：

- **Stub：**客户端调用一个被称为 Stub （存根）的客户端代理对象。该代理对象负责对客户端隐藏网络通讯的细节。Stub 写着如何通过网络套接字（Socket）发送调用，包括如何将调用参数转换为适当的形式以便传输等。简单理解就是封装了一层网络传输的细节，直接传入参数调用就行。
- **Skeleton：**在服务端中该代理对象负责对分布式对象隐藏网络通讯的细节。Skeleton 知道如何从网络套接字（Socket）中接受调用，包括如何将调用参数从网络传输形式转换为 Java 形式等。
- **Registry：**注册中心，服务端在注册中心注册服务时，需要提供一个key以及一个value，这个value是一个远程对象，Registry会对这个远程对象进行封装，使其转为一个远程代理对象，它本身不会执行方法。在低版本的JDK中，Server与Registry是可以不在一台服务器上的，而在**高版本的JDK中，Server与Registry只能在一台服务器上，否则无法注册成功**。
- **注：**

1. **Java对远程访问RMI Registry做了限制，只有来源地址是localhost的时候，才能调用rebind、bind、unbind等方法。**
2. 不过list和lookup方法可以远程调用。
3. list方法可以列出目标上所有绑定的对象；lookup作用就是获得某个远程对象。

那么，只要目标服务器上存在一些危险方法，我们通过RMI就可以对其进行调用。

利用工具：https://github.com/NickstaDB/BaRMIe

**建立RMI的流程如下**：

1. 通过分析需求定义远程接口(客户端和服务器端公用的)，此接口**必须扩展java.rmi.Remote**，且**远程方法必须声明抛出 java.rmi.RemoteException 异常，或者该异常的超类（Superclass）**。
2. 服务器端实现远程接口，为了不手动生成stub需要继承UnicastRemoteObject类，并调用其构造器；
3. 服务器端注册服务并启动；
4. 客户端查询服务并调用远程方法；

**代码实现**

分别建立三个项目：服务器端(RMIDemoServer)、客户端(RMIDemoClient)和远程接口(DemoRMI.RmoteInterface)

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304191720388.png)

**DemoRMI.RmoteInterface**

```java
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HelloRMI extends Remote {

    String sayHello(String name) throws RemoteException;
}
//继承了 java.rmi.Remote 的接⼝，其中定义我们要远程调⽤的函数，⽐如这⾥的  sayHello(String name)
```

**RMIDemoServer**

```java
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

@SuppressWarnings("serial")
public class RMIHelloImpl extends UnicastRemoteObject implements HelloRMI {

    protected RMIHelloImpl() throws RemoteException {
        super();
    }

    public String sayHello(String name) {
        return "Hello,"+name;
    }
}

//实现了接⼝的类 这里输出Hello 传入的值
import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;

public class SerApp
{
    public static void main( String[] args ) throws RemoteException, MalformedURLException
    {
        HelloRMI hello= (HelloRMI) new RMIHelloImpl();

        LocateRegistry.createRegistry(1099);
        Naming.rebind("rmi://127.0.0.1/hello", hello);
        System.out.println("Server ok");
    }
}

//创建Registry，并将实现类实例化后绑定到⼀个地址。这两部分就是我们所谓的Server
```

**RMIDemoClient**

```java
import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

public class ClientApp {
    public static void main( String[] args ) throws MalformedURLException, RemoteException, NotBoundException
    {
        HelloRMI hello=(HelloRMI) Naming.lookup("rmi://127.0.0.1/hello");
        System.out.println( hello.sayHello("Roderick RMI"));
    }
}

//客户端就简单多了，使⽤ Naming.lookup 在Registry中寻找到名字是hello的对象，调用hello.sayHello
```

简单说一下这个流程：首先定义公共的接口HelloRMI，然后服务端创建实现类RMIHelloImpl,同时创建Registry并将实现类实例化后绑定到⼀个地址。这样RMI的Server就算完成了，再直接启动SerApp。客户端直接用Naming.lookup去访问Registry获取对象，然后像使用本地方法一样使用RMI来的方法即可方法。启动ClientApp可以看到完成了RMI整个调用过程。

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304191720493.png)借用p牛的解说：

“过程进行了了两次TCP握手，也就是我们实际建立了两次TCP连接。第⼀一次建立TCP连接是连接远端的1099端口，这也是我们在代码⾥里里看到的端口，⼆二者进行沟通后，我向远端发送了一个“Call”消息，远端回复了一个“ReturnData”消息，然后我新建了一个TCP连接，连到远端的33769端口。所以捋一捋这整个过程，首先客户端连接Registry，并在其中寻找Name是Hello的对象，这个对应数据流中的Call消息；然后Registry返回一个序列化的数据，这个就是找到的Name=hello的对象，这个对应数据流中的ReturnData消息；客户端反序列化该对象，发现该对象是一个远程对象，地址在x.x.x.x:端口，于是再与这个地址建⽴立TCP连接；在这个新的连接中，才执行真正远程方法调⽤用，也就是hello()。”

借用下图来说明这些元素间的关系：

![img](https://blog-1313934826.cos.ap-chengdu.myqcloud.com/blog-images/202304191720429.png)RMI Registry就像一个网关，他自己是不不会执行远程方法的，但RMI Server可以在上⾯面注册一个Name到对象的绑定关系；RMI Client通过Name向RMI Registry查询，得到这个绑定关系，然后再连接RMIServer；最后，远程方法实际上在RMI Server上调用。

一个枚举和攻击 Java RMI（远程方法调用）服务的工具：https://github.com/NickstaDB/BaRMIe
