## 0x01 下载安装Ollama

1、访问Ollama官网（https://ollama.com/），下载ollama启动器，并点击安装

![标题: fig:](file:///C:/Users/yang/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)

2、安装完成后，Win+R，输入cmd，打开cmd命令行，输入ollama并回车，显示如下则表明安装成功

![标题: fig:](file:///C:/Users/yang/AppData/Local/Temp/msohtmlclip1/01/clip_image004.jpg)

3、配置环境变量，编辑系统环境变量Path，新建一行，输入Ollama安装位置

![标题: fig:](file:///C:/Users/yang/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png)



## 0x02 下载并配置大模型

1、修改环境变量，调整下载的大模型存储位置（比较大，默认存在C盘，很占位置）；新建系统环境变量：OLLAMA_MODELS,路径自定义到你想存放的地址即可，点击确认并保存

2、**重启****Ollama**，一定要重启，否则上述修改不生效。右下角点击ollama图标，quit退出，之后再重新打开cmd命令行，输入Ollama启动即可

3、下载需要的大模型：访问ollama官网的模型仓库（https://ollama.com/library），选择想安装的模型，比如阿里千问：qwen2.5，点击模型，选取版本（训练数据量不同）

![标题: fig:](file:///C:/Users/yang/AppData/Local/Temp/msohtmlclip1/01/clip_image008.png)

复制该命令，回到cmd命令行，键入该命令并回车，之后耐心等待下载完毕即可



## 0x03 简单使用

1、命令行输入命令：ollama run 模型名 以启动模型  示例：ollama run ollama run qwen2.5:7b
 2、ollama list 查看当前拥有的模型列表（不记得模型名时可以使用，方便启动）
 3、ollama -h  查看使用命令帮助

启动之后即可键入任意内容，开启对话