# 0x01 docker常用命令

```bash
#系统命令
systemctl start docker				#启动docker
systemctl stop docker				#停止docker
systemctl restart docker			#重启docker
systemctl enable docker				#设置docker开机自启
 
#基本命令
docker version						#查看docker版本
docker info							#查看docker详细信息
docker --help						#查看docker命令
 
#镜像命令
docker images						#查看docker镜像列表
docker images -a					#列出本地所有镜像
docker images --digests				#显示镜像的摘要信息
docker search redis					#从Docker Hub上查找redis镜像
docker pull redis					#从Docker Hub上下载redis镜像
docker rmi 373f0984b070				#删除IMAGE ID 为373f0984b070的镜像
 
#运行命令
#-p 6379:6379	端口映射：前表示主机部分,后表示容器部分
#-d	在后台运行容器（不进入终端）并打印容器ID/容器名
#--name myredis表示自定义容器名为myredis
docker run -d -p 6379:6379 --name myredis redis:latest		#根据镜像创建并运行容器
 
#容器命令
docker container ls 或 docker ps				#查看正在运行的容器
docker container ls -a 或 docker ps -a			#列出所有容器
docker container start 容器ID 或 容器名称		#启动容器
docker start 容器ID 或 容器名称					#启动容器
docker container stop 容器ID 或 容器名称			#停止容器
docker stop 容器ID 或 容器名称					#停止容器
docker container rm 容器ID 或 容器名称			#删除容器
docker rm 容器ID 或 容器名称						#删除容器
docker container logs -f 容器ID 或 容器名称		#查看容器日志
docker exec -it name /bin/bash 					#进入name（容器名/id）中开启交互式的终端，exit退出
```

# 0x02 docker --help中文译解

```bash
Usage:
docker [OPTIONS] COMMAND [arg...]
       docker daemon [ --help | ... ]
       docker [ --help | -v | --version ]
A
self-sufficient runtime for containers.

Options:
  --config=~/.docker              Location of client config files  #客户端配置文件的位置
  -D, --debug=false               Enable debug mode  #启用Debug调试模式
  -H, --host=[]                   Daemon socket(s) to connect to  #守护进程的套接字（Socket）连接
  -h, --help=false                Print usage  #打印使用
  -l, --log-level=info            Set the logging level  #设置日志级别
  --tls=false                     Use TLS; implied by--tlsverify  #
  --tlscacert=~/.docker/ca.pem    Trust certs signed only by this CA  #信任证书签名CA
  --tlscert=~/.docker/cert.pem    Path to TLS certificate file  #TLS证书文件路径
  --tlskey=~/.docker/key.pem      Path to TLS key file  #TLS密钥文件路径
  --tlsverify=false               Use TLS and verify the remote  #使用TLS验证远程
  -v, --version=false             Print version information and quit  #打印版本信息并退出

Commands:
    attach    Attach to a running container  #当前shell下attach连接指定运行镜像
    build     Build an image from a Dockerfile  #通过Dockerfile定制镜像
    commit    Create a new image from a container's changes  #提交当前容器为新的镜像
    cp    	  Copy files/folders from a container to a HOSTDIR or to STDOUT  #从容器中拷贝指定文件或者目录到宿主机中
    create    Create a new container  #创建一个新的容器，同run 但不启动容器
    diff      Inspect changes on a container's filesystem  #查看docker容器变化
    events    Get real time events from the server#从docker服务获取容器实时事件
    exec      Run a command in a running container#在已存在的容器上运行命令
    export    Export a container's filesystem as a tar archive  #导出容器的内容流作为一个tar归档文件(对应import)
    history   Show the history of an image  #展示一个镜像形成历史
    images    List images  #列出系统当前镜像
    import    Import the contents from a tarball to create a filesystem image  #从tar包中的内容创建一个新的文件系统映像(对应export)
    info      Display system-wide information  #显示系统相关信息
    inspect   Return low-level information on a container or image  #查看容器详细信息
    kill      Kill a running container  #kill指定docker容器
    load      Load an image from a tar archive or STDIN  #从一个tar包中加载一个镜像(对应save)
    login     Register or log in to a Docker registry#注册或者登陆一个docker源服务器
    logout    Log out from a Docker registry  #从当前Docker registry退出
    logs   	  Fetch the logs of a container  #输出当前容器日志信息
    pause     Pause all processes within a container#暂停容器
    port      List port mappings or a specific mapping for the CONTAINER  #查看映射端口对应的容器内部源端口
    ps    	  List containers  #列出容器列表
    pull      Pull an image or a repository from a registry  #从docker镜像源服务器拉取指定镜像或者库镜像
    push      Push an image or a repository to a registry  #推送指定镜像或者库镜像至docker源服务器
    rename    Rename a container  #重命名容器
    restart   Restart a running container  #重启运行的容器
    rm    	  Remove one or more containers  #移除一个或者多个容器
    rmi    	  Remove one or more images  #移除一个或多个镜像(无容器使用该镜像才可以删除，否则需要删除相关容器才可以继续或者-f强制删除)
    run   	  Run a command in a new container  #创建一个新的容器并运行一个命令
    save      Save an image(s) to a tar archive#保存一个镜像为一个tar包(对应load)
    search    Search the Docker Hub for images  #在docker
hub中搜索镜像
    start     Start one or more stopped containers#启动容器
    stats     Display a live stream of container(s) resource usage statistics  #统计容器使用资源
    stop      Stop a running container  #停止容器
    tag       Tag an image into a repository  #给源中镜像打标签
    top       Display the running processes of a container #查看容器中运行的进程信息
    unpause   Unpause all processes within a container  #取消暂停容器
    version   Show the Docker version information#查看容器版本号

​    wait      Block until a container stops, then print its exit code  #截取容器停止时的退出状态值
```

